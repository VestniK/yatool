#include "module_builder.h"

#include "args_converter.h"
#include "builtin_macro_consts.h"
#include "makefile_loader.h"
#include "macro_string.h"
#include "out.h"
#include "add_dep_adaptor_inline.h"
#include "parser_manager.h"
#include "prop_names.h"

#include <devtools/ymake/lang/plugin_facade.h>
#include <devtools/ymake/lang/eval_context.h>

#include <devtools/ymake/compact_graph/query.h>

#include <devtools/ymake/common/npath.h>

#include <devtools/ymake/diag/trace.h>
#include <devtools/ymake/diag/dbg.h>
#include <devtools/ymake/diag/diag.h>
#include <devtools/ymake/diag/manager.h>

#include <devtools/libs/yaplatform/platform_map.h>

#include <util/generic/array_ref.h>
#include <util/generic/hash.h>
#include <util/folder/path.h>
#include <util/string/cast.h>
#include <util/string/split.h>
#include <util/string/subst.h>
#include <util/string/vector.h>

namespace {
    EMakeNodeType NodeTypeForVar(const TVarStr& var) {
        return var.NotFound ? EMNT_MissingFile : (var.IsOutputFile ? EMNT_NonParsedFile : EMNT_File);
    }

    EMakeNodeType NodeTypeForVarEx(const TVarStr& var) {
        return var.IsMacro ? EMNT_UnknownCommand : NodeTypeForVar(var);
    }

    bool ValidateForOwnDir(const TStringBuf& dir, const TModule& module, const TStringBuf& macroName) {
        if (dir == module.GetDir()) {
            TString what = TString::Join(module.GetName().GetTargetStr(), " has ", macroName, " to its own dir");
            YConfErr(BadDir) << what << Endl;
            TRACE(S, NEvent::TMakeSyntaxError(what, TString(module.GetMakefile().GetTargetStr())));
            return false;
        }
        return true;
    };

    bool ValidateNotRelative(TStringBuf dir, TStringBuf macroName) {
        auto rel = NPath::CutType(dir);
        if (rel == "." || rel.StartsWith("./") || rel.StartsWith("..")) {
             YConfErr(BadDir) << "Relative path [[imp]]" << NPath::CutType(dir) << "[[rst]] is not allowed in [[alt1]]" << macroName << "[[rst]]" << Endl;
             return false;

        }
        return true;
    }

    constexpr TStringBuf STRIP_PREFIX = "STRIP_PREFIX"sv;
}

void TModuleBuilder::SetProperty(TStringBuf propName, TStringBuf value) {
    Node.AddDepIface(EDT_Property, EMNT_Property, FormatProperty(propName, value));
}

void TModuleBuilder::AddDart(TStringBuf dartName, TStringBuf dartValue, const TVector<TStringBuf>& vars) {
    ui32 propId = Graph.Names().AddName(EMNT_Property, FormatProperty(dartName, dartValue));
    auto& groupVars = DartIdToGroupVars[propId];
    groupVars.insert(groupVars.begin(), vars.begin(), vars.end());
}

void TModuleBuilder::RecursiveAddInputs() {
    bool lastTryMode = false;
    const TCommandInfo* firstFail = nullptr;
    while (!CmdAddQueue.empty()) {
        TAutoPtr<TCommandInfo> cmdInfo = CmdAddQueue.front();
        CmdAddQueue.pop_front();

        if (firstFail == cmdInfo.Get()) {
            if (lastTryMode) { // didn't help, leaving as is :(
                break;
            }
            lastTryMode = true;
        }

        TCommandInfo::ECmdInfoState state = cmdInfo->CheckInputs(*this, Node, lastTryMode);
        if (state == TCommandInfo::SKIPPED) {
            TStringBuf cmd, cmdName;
            ui64 id;
            ParseLegacyCommandOrSubst(Get1(&cmdInfo->Cmd), id, cmdName, cmd);
            YConfErr(BadInput) << Module.GetDir() << ": skip processing macro " << cmdName << cmd << " due to unallowed input." << Endl;
            continue;
        }
        if (state == TCommandInfo::FAILED) {
            if (!firstFail) {
                firstFail = cmdInfo.Get();
            }
            // Command was not successful, Inputs will not be accessible
            // unless we attach it to module via Search
            CmdAddQueue.push_back(cmdInfo);
            continue;
        }
        firstFail = nullptr;
        if (!cmdInfo->Process(*this, Node, false)) {
            continue;
        }
        TCommandInfo& info = *cmdInfo;
        if (const auto* mainOut = cmdInfo->GetMainOutput()) {
            AddOutput(mainOut->ElemId, EMNT_NonParsedFile, false).GetAction().GetModuleData().CmdInfo = cmdInfo;
        }
        QueueCommandOutputs(info);
    }

    if (Module.IsInputsComplete()) {
        return;
    }

    // 2. add remaining CheckIfUsed as EDT_Search
    for (auto id : Module.GetOwnEntries()) {
        TModAddData* modInfo = UpdIter.GetAddedModuleInfo(MakeDepFileCacheId(id));
        // note that !modInfo means that the node has already been visited by AddIter, no need to worry
        if (modInfo && modInfo->CheckIfUsed && !modInfo->UsedAsInput) {
            //Node.AddDep(EDT_Search, i->second.AddCtx->NodeType, i->second.AddCtx->ElemId); <- this data might not be available yet
            if (!modInfo->AdditionalOutput) {
                if (modInfo->BadCmdInput) {
                    const auto& name = Graph.GetFileName(id);
                    YConfWarn(BadSrc) << "can't build anything from " << name << Endl;
                } else {
                    Node.AddUniqueDep(EDT_Search, EMNT_NonParsedFile, id);
                }
            }
        }
    }

    // 3. post-processing
    if (!HasBuildFrom && ::IsTrue(GetCmdValue(Vars.Get1("NEED_ADD_FAKE_SRC"))) ||
        ::IsTrue(GetCmdValue(Vars.Get1("_FAKE_MODULE")))) {
        if (!Module.IsCompleteTarget()) {
            Module.MarkFake();
            YDIAG(V) << "Module marked fake: " << Module.GetName() << Endl;
        } else {
            YConfErr(Misconfiguration) << "final target module shouldn't have NEED_ADD_FAKE_SRC enabled, ignored" << Endl;
        }
    }

    // 4. finalize

    AddFileGroupVars();
    AddDartsVars();

    Node.AddDeps(IncludeOnly);
    AddGlobalDep();
    AddLinkDep(Module.GetName(), GetModuleConf().Cmd, Node);

    for (auto& inducedDeps: DelayedInducedDeps) {
        Node.AddParsedIncls(inducedDeps.Type, inducedDeps.Files);
    }
    DelayedInducedDeps.clear();

    if (ShouldAddAllSrcs()) {
        AllSrcs.InitializeNode(*this);
    }

    Module.SetInputsComplete();
    Module.SetDirsComplete();
    return;
}

void TModuleBuilder::SaveInputResolution(const TVarStrEx& input, TStringBuf origInput, TFileView curDir) {
    if (origInput == input.Name) {
        return;
    }
    if (NPath::IsTypedPathEx(origInput)) {
        switch (NPath::GetType(origInput))
        {
        case NPath::Link:
            if (!NPath::IsType(NPath::GetTargetFromLink(origInput), NPath::Unset)) {
                return;
            }
            [[fallthrough]];
        case NPath::Unset:
            break;
        case NPath::Source:
        case NPath::Build:
            return;
        }
    } else {
        TString dummyRes;
        if (Resolver().ResolveAsKnownWithoutCheck(origInput, curDir, dummyRes)) {
            return;
        }
    }

    Module.ResolveResults.insert({
        Graph.Names().AddName(
            EMNT_MissingFile,
            NPath::IsTypedPathEx(origInput) ? origInput : NPath::ConstructPath(origInput,  NPath::Unset)
        ),
        curDir.IsValid() ? curDir.GetElemId() : TResolveResult::EmptyPath,
        static_cast<ui32>(input.ElemId)
    });
}

bool TModuleBuilder::AddByExt(const TStringBuf& sectionName, TVarStrEx& src, const TVector<TStringBuf>* args) {
    YDIAG(V) << "AddByExt: " << src.Name << Endl;
    src.ForIncludeOnly = Conf.IsIncludeOnly(src.Name);
    // AddByExt called in one place only and there ResolveAsKnown is called without presence check
    // Hence ElemId should always be 0 here
    Y_ASSERT(!src.ElemId);
    // src.IsPathResolved however may be true and thus next line may leave ElemId as 0
    ResolveSourcePath(src, Module.GetDir(), TModuleResolver::Default);
    // Eventually if Resolving above succeeded (and IsPathResoved was false) the src.ElemId becomes != 0
    if (Y_UNLIKELY(src.IsDir)) {
        YConfErr(BadInput) << "try to process by extension in " << sectionName << " a directory: " << src.Name << ". Won't be processed!" << Endl;
        return false;
    }
    if (src.IsPathResolved && src.ForIncludeOnly) { // avoid creating TCommandInfo without much need
        EMakeNodeType nType = NodeTypeForVar(src);
        ui32 elemId = src.ElemId ?: Graph.Names().AddName(nType, src.Name);
        IncludeOnly.AddUnique(EDT_Search, nType, elemId);
        return true;
    }
    return AddSource(sectionName, src, args);
}

bool TModuleBuilder::AddSource(const TStringBuf& sname, TVarStrEx& src, const TVector<TStringBuf>* args) {
    YDIAG(V) << "Current filename: " << src.Name << " " << src.ElemId << Endl;
    if (!src.IsMacro && ModuleDef && ModuleDef->IsInput(sname, src.Name)) {
        if (src.IsPathResolved && !src.ElemId) { // if src is direct module input: like .o in repo
            src.ElemId = Graph.Names().AddName(EMNT_File, src.Name);
        }
        ui64 groupId = Graph.Names().AddName(EMNT_Property, NStaticConf::MODULE_INPUTS_MARKER);
        if (Module.GetAttrs().UseGlobalCmd && src.IsGlobal && ModuleDef->IsGlobalInput(src.Name)) {
            if (!GlobalNode) {
                GlobalNodeElemId = Module.GetGlobalFileName().GetElemId();
                GlobalNode = &Node.AddOutput(GlobalNodeElemId, EMNT_NonParsedFile);
            }
            AddDep(src, *GlobalNode, true, groupId);
        } else {
            AddDep(src, Node, true, groupId);
        }
        return true;
    }
    TAutoPtr<TCommandInfo> cmdInfo = new TCommandInfo(&Conf, &Graph, &UpdIter, &Module);
    cmdInfo->SetCommandSink(&Commands);
    if (!src.IsMacro && src.ElemId && src.OutputInThisModule) {
        TAddDepAdaptor& node = AddOutput(src.ElemId, NodeTypeForVar(src));
        node.GetModuleData().CheckIfUsed = true;
    }
    if (src.NoAutoSrc) {
        return false;
    }
    if (!cmdInfo->Init(sname, src, args, *this)) {
        // cmdInfo will be discarded
        return false;
    }
    CmdAddQueue.push_back(cmdInfo);
    return false;
}

void TModuleBuilder::AddPluginCustomCmd(TMacroCmd& macroCmd) {
    TAutoPtr<TCommandInfo> cmdInfo = new TCommandInfo(&Conf, &Graph, &UpdIter, &Module);
    cmdInfo->GetCommandInfoFromPluginCmd(macroCmd, Vars, Module);
    CmdAddQueue.push_back(cmdInfo);
}

void TModuleBuilder::AddDep(TVarStrEx& curSrc, TAddDepAdaptor& inputNode, bool isInput, ui64 groupId) {
    YDIAG(DG) << "SRCS dep for module: " << curSrc.Name << " " << curSrc.ElemId << Endl;
    EMakeNodeType nType = NodeTypeForVarEx(curSrc);
    if (!curSrc.IsPathResolved) {
        YConfWarn(Dev) << "path was not resolved before TModuleBuilder::AddDep: " << curSrc.Name << Endl;
        ResolveSourcePath(curSrc, {}, TModuleResolver::LastTry);
        if (Y_UNLIKELY(curSrc.IsDir)) {
            YConfErr(BadInput) << "try to add to " << Module.GetName() << " directory as input dependency: " << curSrc.Name << ". Won't be processed." << Endl;
            return;
        }
        nType = NodeTypeForVarEx(curSrc);
        Y_ASSERT(curSrc.ElemId); // resolving with LastTry mode must fill ElemId
    }
    bool builtInThisMod = !curSrc.IsGlobal || !GetModuleConf().Globals.contains("SRCS");
    HasBuildFrom |= isInput && builtInThisMod;
    ui64* currentGroupId = &CurrentInputGroup;
    if (inputNode.ElemId == GlobalNodeElemId) {
        currentGroupId = &CurrentGlobalInputGroup;
    }
    else {
        Y_ASSERT(inputNode.ElemId == ModuleNodeElemId);
    }
    if (isInput) {
        if (*currentGroupId != groupId) {
            inputNode.AddDepIface(EDT_Group, EMNT_Property, groupId);
            *currentGroupId = groupId;
        }
    }
    if (builtInThisMod) {
        if (isInput) {
            inputNode.AddDepIface(EDT_BuildFrom, nType, curSrc.ElemId);
        } else if (!curSrc.AddToModOutputs) {
            inputNode.AddUniqueDep(EDT_Search, nType, curSrc.ElemId);
        }
    }
    if (curSrc.IsGlobal) {
        if (isInput) {
            if (Module.GetAttrs().UseGlobalCmd && ModuleDef->IsGlobalInput(curSrc.Name)) {
                Y_ASSERT(inputNode.ElemId == GlobalNodeElemId);
                if (*currentGroupId != groupId) {
                    inputNode.AddDepIface(EDT_Group, EMNT_Property, groupId);
                    *currentGroupId = groupId;
                }
                inputNode.AddDepIface(EDT_BuildFrom, nType, curSrc.ElemId);
                GlobalSrcsAreAdded = true;
            } else {
                inputNode.AddUniqueDep(EDT_Search2, nType, curSrc.ElemId);
            }
        } else {
            YConfWarn(DG) << curSrc.Name << " is GLOBAL but this module type does not use it" << Endl;
        }
    }
}

void TModuleBuilder::AddInputVarDep(TVarStrEx& input, TAddDepAdaptor& inputNode) {
    EMakeNodeType nType = NodeTypeForVarEx(input);
    if (!input.IsPathResolved) {
        YConfWarn(Dev) << "path was not resolved before TModuleBuilder::AddInputVarDep: " << input.Name << Endl;
        ResolveSourcePath(input, {}, TModuleBuilder::LastTry);
        if (Y_UNLIKELY(input.IsDir)) {
            YConfErr(BadInput) << "try to add directory as input dependency: " << input.Name << ". Won't be processed." << Endl;
            return;
        }
        nType = NodeTypeForVarEx(input);
        Y_ASSERT(input.ElemId); // resolving with LastTry mode must fill ElemId
    }
    inputNode.AddDepIface(EDT_BuildFrom, nType, input.ElemId);
}

void TModuleBuilder::AddGlobalVarDep(const TStringBuf& varName, TAddDepAdaptor& node, bool structCmd) {
    if (Vars.Get1(varName).size() && GetCmdValue(Vars.Get1(varName)).size()) {
        ui64 id;
        TStringBuf cmdName;
        TStringBuf cmdValue;
        ParseCommandLikeVariable(Vars.Get1(varName), id, cmdName, cmdValue);
        const TString res = [&]() {
            if (structCmd) {
                auto compiled = Commands.Compile(cmdValue, &Conf, Vars, Vars, false);
                // TODO: there's no point in allocating cmdElemId for expressions
                // that do _not_ have directly corresponding nodes
                // (and are linked as "0:VARNAME=S:123" instead)
                auto cmdElemId = Commands.Add(Graph, std::move(compiled.Expression));
                auto value = Graph.Names().CmdNameById(cmdElemId).GetStr();
                return FormatCmd(id, cmdName, value);
            } else {
                TCommandInfo cmd(&Conf, &Graph, &UpdIter);
                auto value = cmd.SubstVarDeeply(varName, Vars);
                return FormatCmd(id, cmdName, value);
            }
        }();
        if (TBuildConfiguration::Workaround_AddGlobalVarsToFileNodes) {
            // duplication comes from adding locally referenced vars
            // via TCommandInfo::GlobalVars, then the whole list through here
            node.AddUniqueDep(EDT_Include, EMNT_BuildCommand, res);
        } else {
            node.AddDepIface(EDT_Include, EMNT_BuildCommand, res);
        }
    }
}

void TModuleBuilder::AddGlobalVarDeps(TAddDepAdaptor& node, bool structCmd) {
    for (const auto& var : GetModuleConf().Globals) {
        const TString depName = TString::Join(var, "_GLOBAL");
        AddGlobalVarDep(depName, node, structCmd);
    }
    for (const auto& resource : Module.ExternalResources) {
        AddGlobalVarDep(resource, node, structCmd);
    }
}

void TModuleBuilder::AddLinkDep(TFileView name, const TString& command, TAddDepAdaptor& node, EModuleCmdKind cmdKind) {
    YDIAG(Dev) << "Add LinkDep for: " << name << node.NodeType << Endl;

    Y_ASSERT(ModuleDef);
    if (ModuleDef->GetBuildConf().RenderSemantics) {
        if (cmdKind == EModuleCmdKind::Default && !GetModuleConf().HasSemantics) {
            YConfErr(NoSem) << "No semantics set for " << Module.GetUserType() << ". Module is not intended to be exported." << Endl;
        }
        if (cmdKind == EModuleCmdKind::Global && !GetModuleConf().HasSemanticsForGlobals) {
            YConfErr(NoSem) << "No semantics set for GLOBAL sources. Module " << Module.GetUserType() << " is not intended to be exportd when GLOBAL sources are used." << Endl;
        }
    }

    if (GetModuleConf().StructCmd && (cmdKind == EModuleCmdKind::Default || cmdKind == EModuleCmdKind::Global)) {
        auto compiled = [&]() {
            try {
                return Commands.Compile(command, &Conf, Vars, Vars, true, EOutputAccountingMode::Module);
            } catch (std::exception& e) {
                YConfErr(Details) << "Command processing error (module " << Module.GetUserType() << "): " << e.what() << Endl;
                return Commands.Compile("$FAIL_MODULE_CMD", &Conf, Vars, Vars, true, EOutputAccountingMode::Module);
            }
        }();
        const ui32 cmdElemId = Commands.Add(Graph, std::move(compiled.Expression));

        TAutoPtr<TCommandInfo> cmdInfo = new TCommandInfo(&Conf, &Graph, &UpdIter, &Module);
        cmdInfo->InitFromModule(Module);

        cmdInfo->GetCommandInfoFromStructCmd(Commands, cmdElemId, compiled.Inputs.Take(), compiled.Outputs.Take(), Vars);

        if (cmdInfo->CheckInputs(*this, node, /* lastTry */ true) == TCommandInfo::OK && cmdInfo->Process(*this, node, true)) {
            AddGlobalVarDeps(node, true);
            node.AddOutput(node.ElemId, EMNT_NonParsedFile, false).GetAction().GetModuleData().CmdInfo = cmdInfo;
        } else {
            YDIAG(Dev) << "Failed to add LinkDep for:" << name << node.NodeType << Endl;
            if (cmdKind == EModuleCmdKind::Default || cmdKind == EModuleCmdKind::Global) {
                YDIAG(Dev) << "... will try to add FAIL_MODULE_CMD" << Endl;
                AddLinkDep(name, command, node, EModuleCmdKind::Fail);
            }
        }

        return;
    }

    if (cmdKind == EModuleCmdKind::Default) {
        AddGlobalVarDeps(node, false);
    }

    TStringBuf cmdName;
    TVector<TStringBuf> modArgs;
    bool isMacroCall = false;

    if (cmdKind == EModuleCmdKind::Default || cmdKind == EModuleCmdKind::Global) {
        isMacroCall = ParseMacroCall(command, cmdName, modArgs);
        TStringBuf cmd = Vars.Get1(cmdName);
        if (cmd.empty()) {
            if (cmdKind == EModuleCmdKind::Global) {
                YConfErr(NoCmd) << "No valid command to link global srcs " << name << ", check your config for " << cmd << Endl;
            }
            else {
                YConfErr(NoCmd) << "No valid command to link " << name << ", check your config for " << cmd << Endl;
            }
            cmdKind = EModuleCmdKind::Fail;
        }
    }
    if (cmdKind == EModuleCmdKind::Fail) {
        // Add fake command instead of bad one (it will fail at link time)
        isMacroCall = ParseMacroCall(TStringBuf("FAIL_MODULE_CMD"), cmdName, modArgs);
    }

    TAutoPtr<TCommandInfo> cmdInfo = new TCommandInfo(&Conf, &Graph, &UpdIter, &Module);
    cmdInfo->InitFromModule(Module);

    // can not fail, we've checked `cmd' already
    cmdInfo->GetCommandInfoFromMacro(cmdName, isMacroCall ? EMT_MacroCall : EMT_Usual, modArgs, Vars, Module.GetId());
    cmdInfo->SetCmdType(TCommandInfo::MacroImplInp);

    if (cmdInfo->CheckInputs(*this, node, /* lastTry */ true) == TCommandInfo::OK && cmdInfo->Process(*this, node, true)) {
        node.AddOutput(node.ElemId, EMNT_NonParsedFile, false).GetAction().GetModuleData().CmdInfo = cmdInfo;
    } else {
        YDIAG(Dev) << "Failed to add LinkDep for:" << name << node.NodeType << Endl;
        if (cmdKind == EModuleCmdKind::Default || cmdKind == EModuleCmdKind::Global) {
            YDIAG(Dev) << "... will try to add FAIL_MODULE_CMD" << Endl;
            AddLinkDep(name, command, node, EModuleCmdKind::Fail);
        }
    }
}

void TModuleBuilder::AddGlobalDep() {
    if (!Module.GetAttrs().UseGlobalCmd || !GlobalSrcsAreAdded) {
        return;
    }
    Node.AddUniqueDep(EDT_Search2, EMNT_NonParsedFile, Module.GetGlobalFileName().GetElemId());
    if (GetModuleConf().GlobalCmd.empty()) {
        YConfErr(Misconfiguration) << "Global cmd is empty for " << Module.GetName() << " module but USE_GLOBAL_CMD is enabled" << Endl;
    }

    AddLinkDep(Module.GetGlobalFileName(), GetModuleConf().GlobalCmd, *GlobalNode, EModuleCmdKind::Global);
    Module.SetGlobalLibId(GlobalNode->ElemId);
}

void TModuleBuilder::AddFileGroupVars() {
    for (auto& [varId, cmdInfo] : FileGroupCmds) {
        Node.AddUniqueDep(EDT_Property, EMNT_BuildCommand, varId);
        auto& [id, entryStats] = *UpdIter.Nodes.Insert(MakeDepsCacheId(EMNT_BuildCommand, varId), &UpdIter.YMake, &Module);
        entryStats.OnceEntered = false;
        entryStats.SetReassemble(true);
        auto& cmdNode = entryStats.GetAddCtx(&Module, UpdIter.YMake);

        cmdInfo->CheckInputs(*this, cmdNode, true);
        cmdInfo->ProcessVar(*this, cmdNode);
    }
}

void TModuleBuilder::AddDartsVars() {
    for (const auto& [propId, vars] : DartIdToGroupVars) {
        Node.AddDepIface(EDT_Property, EMNT_Property, propId);
        auto& [id, entryStats] = *UpdIter.Nodes.Insert(MakeDepsCacheId(EMNT_Property, propId), &UpdIter.YMake, &Module);
        entryStats.OnceEntered = false;
        entryStats.SetReassemble(true);
        auto& propNode = entryStats.GetAddCtx(&Module, UpdIter.YMake);
        for (auto varName : vars) {
            const TYVar* varPtr = Vars.Lookup(varName);
            if (!varPtr) {
                YConfErr(Syntax) << "Cannot add to dart property not initialized variable " << varName << Endl;
                continue;
            }
            auto varCmd = FormatCmd(Module.GetId(), varName, "");
            TVarStrEx varStrEx = varCmd;
            varStrEx.IsMacro = true;
            AddInputVarDep(varStrEx, propNode);
        }
    }
}

void TModuleBuilder::TryProcessStatement(const TStringBuf& name, const TVector<TStringBuf>& args) {
    try {
        ProcessStatement(name, args);
    } catch (yexception& e) {
        TString what = TString::Join(name, "(", JoinStrings(args.begin(), args.end(), " "), ") was not processed properly: ", e.what());
        TRACE(S, NEvent::TMakeSyntaxError(what, TString(Module.GetMakefile().GetTargetStr())));
        YConfErr(Syntax) << what << ". Skip " << name << Endl;
    }
}

void TModuleBuilder::ProcessStatement(const TStringBuf& name, const TVector<TStringBuf>& args) {
    DirStatement(name, args) ||
    SrcStatement(name, args) ||
    RememberStatement(name, args) ||
    LateGlobStatement(name, args) ||
    MacroToVarStatement(name, args) ||
    GenStatement(name, args) ||
    BundleStatements(name, args) ||
    PluginStatement(name, args) ||
    SkipStatement(name, args);
    // Make directories immediately available after command processing
    ApplyVarAsMacro(NMacro::PEERDIR);
    ApplyVarAsMacro(NMacro::SRCDIR);
    ApplyVarAsMacro(NMacro::ADDINCL);
}

void TModuleBuilder::ApplyVarAsMacro(const TStringBuf& name, bool force) {
    if (const auto* var = Vars.Lookup(name)) {
        ui64 hash = THash<TStringBuf>()(Get1(var)); // Here come single-line VARs only
        if (!VarMacroApplied.insert(hash).second && !force) {
            return;
        }
        TVector<TStringBuf> args;
        TString value = TCommandInfo(&Conf, &Graph, &UpdIter).SubstVarDeeply(name, Vars);
        Split(GetCmdValue(value), " ", args);
        if (args.size()) {
            //YConfWarn(Dev) << "ApplyVarAsMacro: " << name << ": " << value << Endl;
            if (name == "OBJADDE") {
                YConfErr(Misconfiguration) << "Using OBJADDE var" << Endl;
            } else {
                DirStatement(name, args);
            }
        }
    }
}

bool TModuleBuilder::ProcessMakeFile() {
    AssertEx(ModuleDef != nullptr, "Makefile is not provided for processing");
    TScopedContext context(Module.GetName());
    if (const auto dllDirIt = OrigVars().find("DLL_FOR_DIR")) {
        const auto& dir_for = dllDirIt->second;
        AddSrcdir(dir_for);
        AddIncdir(dir_for, EIncDirScope::Local, false);
    } else if (const auto pyDirIt = OrigVars().find("PY_PROTOS_FOR_DIR")) {
        const auto& dir_for = pyDirIt->second;
        TVector<TStringBuf> callargs;
        ModuleDef->AddStatement("CREATE_INIT_PY_STRUCTURE", callargs);
        AddSrcdir(dir_for);
        AddIncdir(dir_for, EIncDirScope::Local, false);
    }

    ApplyVarAsMacro(NMacro::PEERDIR);
    ApplyVarAsMacro(NMacro::SRCDIR);
    ApplyVarAsMacro(NMacro::ADDINCL);

    for (const auto& statement : ModuleDef->GetMakeFileMap()) {
        const TStringBuf& name = statement.first.second;
        const TVector<TStringBuf>& args = statement.second;
        TryProcessStatement(name, args);
    }

    // These functions perform some macro substitution inside and it is not guaranteed that
    // values are known at the time of arrtival. Here we know all the VARs, so reapply forcefully just in case.
    // Internal de-duplication code ensures that directies are not added twice.
    ApplyVarAsMacro(NMacro::PEERDIR, true);
    ApplyVarAsMacro(NMacro::SRCDIR, true);
    ApplyVarAsMacro(NMacro::ADDINCL, true);

//  FIXME(spreis) Some Dirs are added with inputs, so call to AddDirsToProps() here
//                loses some dirs in props. On the other hand late call leaves GlIncDirs
//                unpopulated for re-entrants via PEERDIR+RECURSE loops. To make the latter
//                happy we should call AddDirsToProps() twice but this is currently impossible
//                due to missing property node update support.
//    AddDirsToProps();

    if (!Node.HasAnyDeps()) {
        RecursiveAddInputs();
    }

    return true;
}


bool TModuleBuilder::DirStatement(const TStringBuf& name, const TVector<TStringBuf>& args) {
    using namespace NPath;

    if (name == NMacro::PEERDIR || name == NMacro::_GHOST_PEERDIR) {
        enum { normal, include } next = normal;
        for (const auto& arg : args) {
            if (arg == NMacro::ADDINCL) {
                next = include;
            } else {
                TString dir = NPath::IsExternalPath(arg) ? TString{arg} : NPath::ConstructYDir(arg, {}, ConstrYDirDiag);
                if (dir.empty() || !ValidateForOwnDir(dir, Module, name) || !ValidateNotRelative(dir, name)) {
                    continue;
                }
                if (Conf.ExcludedPeerdirs.contains(dir)) {
                    continue;
                }

                const TFlags<EPeerOption> addPeerOpts{next == include ? EPeerOption::AddIncl : EPeerOption::NoOption};
                if (name == NMacro::_GHOST_PEERDIR) {
                    if (Graph.Names().FileConf.DirHasYaMakeFile(dir)) {
                        AddPeerdir(dir, addPeerOpts | EPeerOption::MaterialGhost);
                    } else {
                        AddPeerdir(dir, addPeerOpts | EPeerOption::VirtualGhost);
                    }
                } else {
                    AddPeerdir(dir, addPeerOpts);
                }
                next = normal;
            }
        }
    } else if (name == NMacro::SRCDIR) {
        for (const auto& arg : args) {
            TString dir = NPath::IsExternalPath(arg) ? TString{arg} : NPath::ConstructYDir(arg, {}, ConstrYDirDiag);
            if (dir.empty() || dir == Module.GetDir().GetTargetStr() || !ValidateNotRelative(dir, name)) {
                continue;
            }
            AddSrcdir(dir);
        }
    } else if (name == NMacro::ADDINCL) {
        TLangId nextLangId = TModuleIncDirs::BAD_LANG;
        EIncDirScope nextScope = EIncDirScope::Local;
        enum { normal, lang } next = normal;
        for (const auto& arg : args) {
            if (arg == TStringBuf("FOR")) {
                if (nextLangId != TModuleIncDirs::BAD_LANG) {
                    YConfErr(UserErr) << "Two different languages specified for [[alt1]]" << name << "[[rst]]: previous was \"" << NLanguages::GetLanguageName(nextLangId) << "\"" << Endl;
                }
                next = lang;
            } else if (next == lang) {
                nextLangId = NLanguages::GetLanguageId(arg);
                if (nextLangId == TModuleIncDirs::BAD_LANG) {
                    YConfErr(UserErr) << "Bad language argument in [[alt1]]" << name << "[[rst]]: \"" << arg << "\". Possible languages: " << NLanguages::DumpLanguagesList() << Endl;
                    nextLangId = TModuleIncDirs::BAD_LANG;
                }
                next = normal;
            } else if (arg == TStringBuf("GLOBAL")) {
                nextScope = EIncDirScope::Global;
            } else if (arg == TStringBuf("ONE_LEVEL")) {
                nextScope = EIncDirScope::User;
            } else if (arg == TStringBuf("LOCAL")) {
                // LOCAL is current default
                continue;
            } else {
                // The source root is valid argument here. We should accept, but ignore it
                bool srcRoot = false;
                const auto diagNoSrc = [&srcRoot](NPath::EDirConstructIssue issue, const TStringBuf& path) {
                    if (issue == NPath::EDirConstructIssue::SourceDir) {
                        srcRoot = true;
                    } else {
                        ConstrYDirDiag(issue, path);
                    }
                };

                TString dir;

                if (NLanguages::GetLanguageAddinclsAreNonPaths(nextLangId)) {
                    dir = NPath::ConstructPath(arg);
                } else {
                    dir = NPath::IsExternalPath(arg) ? TString{arg} : NPath::ConstructYDir(arg, {}, diagNoSrc);
                }

                if (!dir.empty() && ValidateNotRelative(dir, name)) {
                    if (nextLangId == TModuleIncDirs::BAD_LANG) {
                        nextLangId = TModuleIncDirs::C_LANG;
                    }
                    AddIncdir(dir, nextScope, true, nextLangId);
                } else if (!srcRoot) {
                    continue;
                }

                next = normal;
                nextScope = EIncDirScope::Local;
                nextLangId = TModuleIncDirs::BAD_LANG;
            }
        }
        if (nextScope != EIncDirScope::Local || next != normal || nextLangId != TModuleIncDirs::BAD_LANG) {
            YConfErr(UserErr) << "Tail arguments in [[alt1]]" << name << "[[rst]] without a dir to apply will be ignored" << Endl;
        }
    } else if (name == TStringBuf(NProps::DEPENDS)) {
        AddDepends(args);
    } else if (name == TStringBuf("PROVIDES")) {
        Module.Provides.reserve(args.size());
        Transform(args.begin(), args.end(), std::back_inserter(Module.Provides), [](TStringBuf in) {return TString{in};});
    } else if (name == TStringBuf("CHECK_PROVIDES")) {
        Module.SetCheckProvides(true);
    } else if (name == NMacro::_DATA_FILES) {
        for (auto arg : args) {
            arg.SkipPrefix("${ARCADIA_ROOT}/"sv);
            if (arg.StartsWith("${ARCADIA_BUILD_ROOT}"sv)) {
                YConfErr(Misconfiguration) << "Build path [[imp]]" << arg << "[[rst]] inside [[alt1]]" << name << "[[rst]] is prohibited. Only source paths accepted." << Endl;
            }
            if (Conf.CheckDataPaths && !TFsPath(Conf.RealPathEx(ArcPath(arg))).Exists()) {
                TRACE(S, NEvent::TInvalidDataDir(TString{arg}));
                YConfErr(Misconfiguration) << "Path [[imp]]" << arg << "[[rst]] inside [[alt1]]" << name << "[[rst]] section is missing." << Endl;
            }
            AddDataPath(arg);
        }
    } else {
        return false;
    }
    return true;
}

bool TModuleBuilder::BundleStatements(const TStringBuf& , const TVector<TStringBuf>& ) {
    return false;
}

bool TModuleBuilder::SrcStatement(const TStringBuf& name, const TVector<TStringBuf>& args) {
    const auto macroBlockData = Conf.BlockData.find(name);
    if (macroBlockData == Conf.BlockData.end() || !IsFileExtRule(&macroBlockData->second)) {
        return false;
    }

    const TBlockData& data = macroBlockData->second;
    size_t firstSimple = 0;
    if (HasNamedArgs(&data)) {
        firstSimple = ConvertArgsToPositionalArrays(*data.CmdProps, const_cast<TVector<TStringBuf>&>(args), *ModuleDef->GetMakeFileMap().Pool);
    }

    TVector<TStringBuf> srcArgs;
    srcArgs.resize(firstSimple + 1);
    if (firstSimple) {
        srcArgs.assign(args.begin(), args.begin() + firstSimple + 1);
    }

    bool globalNext = false;
    bool keepDirStruct = false;
    for (size_t i = firstSimple; i < args.size(); ++i) {
        if (args[i] == "KEEP_DIR_STRUCT") {
            if (i == 0) {
                keepDirStruct = true;
            }
            continue;
        } else // TODO: remove this hack
        if (args[i] == "RESULT" || args[i] == "DESTINATION") {
            i++;
            continue;
        } else if (args[i] == "GLOBAL") {
            globalNext = true;
        } else {
            TVarStrEx src(args[i]);
            ResolveAsKnownWithoutCheck(src);
            if (globalNext) {
                src.IsGlobal = true;
                globalNext = false;
            }
            if (keepDirStruct) {
                src.KeepDirStruct = true;
            }

            srcArgs[srcArgs.size() - 1] = NPath::Basename(src.Name);
            YDIAG(DG) << "Section element process:" << TVecDumpSb(srcArgs) << Endl;
            ProcessConfigMacroCalls(name, srcArgs);
            AddByExt(name, src, srcArgs.size() > 1 ? &srcArgs : nullptr);
        }
    }
    return true;
}

static void ProcessExternalResource(TStringBuf name, const NYa::TResourceDesc& resource, TModule& module, TAddDepAdaptor& node, TVars& vars, TOriginalVars& orig) {
    const TString variableName = TString::Join(name, NYMake::RESOURCE_GLOBAL_SUFFIX);
    const TString resourceName = NYa::ResourceVarName(name, resource);
    const TString value = TString::Join("$(", resourceName, ")");
    node.AddDepIface(EDT_Property, EMNT_Property, FormatProperty("EXT_RESOURCE", TString::Join(resourceName, " ", NYa::ResourceToJsonString(resourceName, resource))));
    vars.SetStoreOriginals(variableName, value, orig);
    module.ExternalResources.insert(variableName);
}

static void ProcessExternalHostResources(const TVector<TStringBuf>& args, TModule& module, TAddDepAdaptor& node, TVars& vars, TOriginalVars& orig, const TStringBuf& macro) {
    NYa::TTempPlatformMap resources;
    size_t sz = args.size();
    size_t n;
    for (n = 1; n + 2 < sz; n += 3) {
        TStringBuf uri = args[n];
        TStringBuf platform = args[n + 2];
        ui32 stripPrefix = 0;
        if (n + 4 < sz && args[n + 3] == STRIP_PREFIX) {
            if (!TryFromString<ui32>(args[n + 4], stripPrefix))
                YConfErr(UserErr) << "[[alt1]]STRIP_PREFIX[[rst]] must be integral in [[alt1]]" << macro << "[[rst]]: " << TVecDumpSb(args) << Endl;
            n += 2;
        }
        resources[platform] = NYa::TResourceDesc{TString{uri}, stripPrefix};
    }
    if (n != sz) {
        YConfErr(UserErr) << "Incorrect number or arguments in [[alt1]]" << macro << "[[rst]]: " << TVecDumpSb(args) << Endl;
        return;
    }
    // Process single 'any' platform as DECLARE_EXTERNAL_RESOURCE() macro
    if (resources.size() == 1 && resources.begin()->first == NYa::ANY_PLATFORM_UC) {
        ProcessExternalResource(args[0], resources.begin()->second, module, node, vars, orig);
        return;
    }
    const TString variableName = TString::Join(args[0], NYMake::RESOURCE_GLOBAL_SUFFIX);
    const TString resourceName = NYa::MappingVarName(args[0], resources);
    const TString value = TString::Join("$(", resourceName, ")");
    node.AddDepIface(EDT_Property, EMNT_Property, FormatProperty("EXT_HOST_RESOURCE", NYa::MappingPatternToJsonString(resourceName, resources)));
    vars.SetStoreOriginals(variableName, value, orig);
    module.ExternalResources.insert(variableName);
}

bool TModuleBuilder::RememberStatement(const TStringBuf& name, const TVector<TStringBuf>& args) {
    if (name == "INDUCED_DEPS") {
        CheckMinArgs(name, args, 2, ": src_type files...");
        TVector<TResolveFile> files;
        files.reserve(args.size() - 1);
        for (auto arg: TArrayRef<const TStringBuf>{args}.subspan(1)) {
            TString resolved;
            if (!ResolveAsKnownWithoutCheck(arg, resolved)) {
                YConfErr(Misconfiguration) << "Ambigous resolution for INDUCED_DEPS argument: " << arg << Endl;
                continue;
            }
            files.push_back(MakeUnresolved(resolved));
        }
        DelayedInducedDeps.push_back({TString{args[0]}, std::move(files)});
    } else if (name == "DECLARE_EXTERNAL_RESOURCE") {
        if (!args) {
            YConfErr(UserErr) << "Missed arguments in [[alt1]]DECLARE_EXTERNAL_RESOURCE[[rst]]" << Endl;
        }
        size_t sz = args.size();
        for(size_t n = 0; n < sz; n += 2) {
            if (n + 1 >= sz) {
                YConfErr(UserErr) << "Incorrect number or arguments in [[alt1]]DECLARE_EXTERNAL_RESOURCE[[rst]]: " << TVecDumpSb(args) << Endl;
                break;
            }
            TStringBuf name = args[n];
            TStringBuf uri = args[n + 1];
            ui32 stripPrefix = 0;
            if (n + 2 < sz && args[n + 2] == STRIP_PREFIX) {
                if (n + 3 < sz) {
                    if (!TryFromString(args[n + 3], stripPrefix)) {
                        YConfErr(UserErr) << "[[alt1]]STRIP_PREFIX[[rst]] must be integral in [[alt1]]DECLARE_EXTERNAL_RESOURCE[[rst]]: " << TVecDumpSb(args) << Endl;
                        break;
                    }
                } else {
                    YConfErr(UserErr) << "Missed argument after [[alt1]]STRIP_PREFIX[[rst]] in [[alt1]]DECLARE_EXTERNAL_RESOURCE[[rst]]: " << TVecDumpSb(args) << Endl;
                    break;
                }
                n += 2;
            }
            NYa::TResourceDesc resource{TString{uri}, stripPrefix};
            ProcessExternalResource(name, resource, Module, Node, Vars, OrigVars());
        }
    } else if (name == "DECLARE_EXTERNAL_HOST_RESOURCES_PACK") {
        if (args.empty() || args[0] != TStringBuf("RESOURCE_NAME")) {
            YConfErr(UserErr) << "Incorrect arguments in " << name << ": " << TVecDumpSb(args) << Endl;
        } else {
            TVector<TStringBuf> margs;
            margs.reserve(args.size());
            for (auto i = args.begin() + 1; i != args.end(); i++) {
                if (*i == TStringBuf("RESOURCE_NAME")) {
                    ProcessExternalHostResources(margs, Module, Node, Vars, OrigVars(), name);
                    margs.clear();
                } else {
                    margs.push_back(*i);
                }
            }
            ProcessExternalHostResources(margs, Module, Node, Vars, OrigVars(), name);
        }
    } else if (name == "DECLARE_EXTERNAL_HOST_RESOURCES_BUNDLE") {
        ProcessExternalHostResources(args, Module, Node, Vars, OrigVars(), name);
    } else {
        return false;
    }
    return true;
}

bool TModuleBuilder::MacroToVarStatement(const TStringBuf& name, const TVector<TStringBuf>& args) {
    auto i = Conf.BlockData.find(name);
    if (i && i->second.CmdProps && i->second.CmdProps->HasConditions) {
        ModuleDef->SetSpecServiceVars(TString::Join("env", name));
        return args.empty();
    }
    return false;
}

bool TModuleBuilder::GenStatement(const TStringBuf& name, const TVector<TStringBuf>& args) {
    auto i = Conf.BlockData.find(name);
    if (i && i->second.IsFileGroupMacro) {
        if (HasNamedArgs(&i->second)) {
            ConvertArgsToPositionalArrays(*i->second.CmdProps, const_cast<TVector<TStringBuf>&>(args), *ModuleDef->GetMakeFileMap().Pool);
        }
        Y_ASSERT(args.size() > 1);

        TStringBuf varName = args.front();
        auto varCmd = FormatCmd(Module.GetId(), varName, "");
        const auto varId = Graph.Names().AddName(EMNT_BuildCommand, varCmd);

        TYVar* groupVar = &Vars[varName];
        groupVar->IsReservedName = true;
        groupVar->push_back(varCmd);
        groupVar->back().IsMacro = true;

        TAutoPtr<TCommandInfo> cmdInfo = new TCommandInfo(&Conf, &Graph, &UpdIter, &Module);
        TVarStrEx cmd(name);
        cmd.IsMacro = true;
        cmdInfo->Init("SRCS", cmd, &args, *this);

        FileGroupCmds.emplace_back(varId, cmdInfo);
    } else if (i && i->second.IsUserMacro) {
        if (HasNamedArgs(&i->second)) {
            ConvertArgsToPositionalArrays(*i->second.CmdProps, const_cast<TVector<TStringBuf>&>(args), *ModuleDef->GetMakeFileMap().Pool);
        }
        TVarStrEx cmd(name);
        cmd.IsMacro = true;
        AddSource(/*for outputs*/ "SRCS", cmd, &args);
    } else {
        return false;
    }
    return true;
}

bool TModuleBuilder::PluginStatement(const TStringBuf& name, const TVector<TStringBuf>& args) {
    if (MacroFacade()->ContainsMacro(name)) {
        TVector<TSimpleSharedPtr<TMacroCmd>> cmds;
        MacroFacade()->InvokeMacro(*this, name, args, &cmds);
        for (size_t i = 0; i < cmds.size(); ++i) {
            AddPluginCustomCmd(*cmds[i]);
        }
        return true;
    }
    return false;
}

bool TModuleBuilder::LateGlobStatement(const TStringBuf& name, const TVector<TStringBuf>& args) {
    if (name != NMacro::_LATE_GLOB) {
        return false;
    }

    if (args.empty()) {
        YConfErr(Syntax) << "empty argument in [[alt1]]" << name << "[[rst]]" << Endl;
        return true;
    }

    TStringBuf varName = args.front();
    const auto [globs, excludes] = SplitBy(TArrayRef<const TStringBuf>{args}.subspan(1), NArgs::EXCLUDE);

    TUniqVector<ui32> excludeIds;
    TExcludeMatcher excludeMatcher;
    for (auto pattern: excludes) {
        if (pattern == NArgs::EXCLUDE) {
            continue;
        }
        if (excludeIds.Push(Graph.Names().AddName(EMNT_Property, FormatProperty(NProps::GLOB_EXCLUDE, pattern)))) {
            excludeMatcher.AddExcludePattern(Module.GetDir(), pattern);
        }
    }

    TYVar* lateExpansionVar = &Vars[varName];
    lateExpansionVar->IsReservedName = true;

    auto CreateGlobNode = [this, &lateExpansionVar](const TModuleGlobInfo& globInfo, const TString& globCmd) {
        Node.AddUniqueDep(EDT_Property, EMNT_BuildCommand, globInfo.GlobId);
        auto& [id, entryStats] = *UpdIter.Nodes.Insert(MakeDepsCacheId(EMNT_BuildCommand, globInfo.GlobId), &UpdIter.YMake, &Module);
        auto& globNode = entryStats.GetAddCtx(&Module, UpdIter.YMake);
        globNode.NodeType = EMNT_BuildCommand;
        globNode.ElemId = globInfo.GlobId;
        entryStats.OnceEntered = false;
        entryStats.SetReassemble(true);
        PopulateGlobNode(globNode, globInfo);
        Y_ASSERT(lateExpansionVar);
        lateExpansionVar->push_back(globCmd);
        lateExpansionVar->back().IsMacro = true;
    };
    for (auto globStr : globs) {
        try {
            TUniqVector<ui32> matches;
            TGlob glob(Graph.Names().FileConf, globStr, Module.GetDir());
            for (const auto& result : glob.Apply(excludeMatcher)) {
                matches.Push(Graph.Names().FileConf.ConstructLink(ELinkType::ELT_Text, result).GetElemId());
            }

            const TString globCmd = FormatCmd(Module.GetName().GetElemId(), NProps::LATE_GLOB, globStr);
            TModuleGlobInfo globInfo = {
                Graph.Names().AddName(EMNT_BuildCommand, globCmd),
                Graph.Names().AddName(EMNT_Property, FormatProperty(NProps::GLOB_HASH, glob.GetMatchesHash())),
                glob.GetWatchDirs().Data(),
                matches.Take(),
                excludeIds.Data(),
                Graph.Names().AddName(EMNT_Property, FormatProperty(NProps::REFERENCED_BY, varName))
            };
            CreateGlobNode(globInfo, globCmd);
        } catch (const yexception& error){
            YConfErr(Syntax) << "Invalid pattern in [[alt1]]" << name << "[[rst]]: " << error.what() << Endl;
        }
    }

    if (globs.empty()) {
        // Add fake glob property in order to be able to reference variable created with _LATE_GLOB
        // without patterns from command subgraph
        const TString globCmd = FormatCmd(Module.GetName().GetElemId(), NProps::LATE_GLOB, "");
        TModuleGlobInfo globInfo = {
            Graph.Names().AddName(EMNT_BuildCommand, globCmd),
            Graph.Names().AddName(EMNT_Property, FormatProperty(NProps::GLOB_HASH, "")),
            {},
            {},
            excludeIds.Data(),
            Graph.Names().AddName(EMNT_Property, FormatProperty(NProps::REFERENCED_BY, varName))
        };
        CreateGlobNode(globInfo, globCmd);
    }
    return true;
}

void TModuleBuilder::CallMacro(TStringBuf name, const TVector<TStringBuf>& args) {
    ProcessConfigMacroCalls(name, args);
    ProcessStatement(name, args);
}

bool TModuleBuilder::SkipStatement(const TStringBuf& name, const TVector<TStringBuf>& args) {
    auto i = Conf.BlockData.find(name);
    if (i && i->second.CmdProps && i->second.CmdProps->HasMacroCalls) {
        YDIAG(DG) << "Use composed only from macro calls: " << name << " statement\n";
        return true;
    }

    if (IsKnownGarbageStatement(name)) {
        YConfInfo(Garbage) << "ymake doesn't make use of " << name << " statement\n";
    } else if (name == NMacro::RECURSE || name == NMacro::RECURSE_FOR_TESTS) {
        TString what = TString::Join("[[alt1]]", name, "[[rst]] inside module ", Module.GetName().GetTargetStr(), "; ymake skip this.");
        TRACE(S, NEvent::TMakeSyntaxError(what, TString(Module.GetMakefile().GetTargetStr())));
        YConfErr(Syntax) << what << Endl;
    } else {
        YConfErr(UnkStatm) << "skip unknown statement: " << name << " " << TVecDumpSb(args) << Endl;
    }

    return false;
}

bool TModuleBuilder::QueueCommandOutputs(TCommandInfo& cmdInfo) {
    if (!cmdInfo.Cmd) {
        Y_ASSERT(cmdInfo.GetOutput().empty());
        for (auto& input : cmdInfo.GetInput()) {
            AddDep(input, Node, false);
            TModAddData& data = AddOutput(input.ElemId, NodeTypeForVar(input)).GetModuleData();
            data.CheckIfUsed = true;
            if (input.AddToModOutputs) {
                data.AdditionalOutput = true;
            } else if (input.ByExtFailed) {
                data.BadCmdInput = true;
            }
        }
        return !cmdInfo.GetInput().empty();
    }

    bool hasInput = false;
    for (auto& output : cmdInfo.GetOutput()) {
        if (!output.IsTmp) {
            output.IsOutputFile = true;
            hasInput |= AddSource(/*OutSecName*/ TStringBuf("SRCS"), output, nullptr);
        }
    }
    return hasInput;
}

bool IsForbiddenStatement(const TStringBuf& name) {
    if (name == NMacro::_GLOB || name == NMacro::_LATE_GLOB) {
        YConfErr(Syntax) << "[[alt1]]" << name << "[[rst]] macro can't be applied from here (it's too late). Skip it." << Endl;
        return true;
    }

    return false;
}
