#include "ymake.h"

#include "mkcmd.h"
#include "blacklist_checker.h"

#include <devtools/ymake/compact_graph/dep_graph.h>
#include <devtools/ymake/compact_graph/query.h>

#include <devtools/ymake/common/npath.h>
#include <devtools/ymake/diag/dbg.h>
#include <devtools/ymake/diag/trace.h>
#include <devtools/ymake/compute_reachability.h>

namespace {
    enum class ESortPriority {
        Peers           = 1,
        DirectPeers     = 2,
        OutTogetherBack = 3,
        Default         = 4,
        IncludeFile     = 5,
        DirectTools     = 6
    };

    inline ESortPriority ComputeEdgePriority(EMakeNodeType fromType, EDepType depType, EMakeNodeType toType) {
        if (IsDirectPeerdirDep(fromType, depType, toType)) {
            return ESortPriority::DirectPeers;
        }
        if (IsPeerdirDep(fromType, depType, toType)) {
            return ESortPriority::Peers;
        }
        if (IsDirectToolDep(fromType, depType, toType)) {
            return ESortPriority::DirectTools;
        }
        if (IsIncludeFileDep(fromType, depType, toType) || IsPropertyFileDep(depType, toType)) {
            return ESortPriority::IncludeFile;
        }
        if (depType == EDT_OutTogetherBack) {
            return ESortPriority::OutTogetherBack;
        }
        return ESortPriority::Default;
    }
}

TNodeEdgesComparator::TNodeEdgesComparator(TConstDepNodeRef node):
    FromType{node->NodeType},
    Graph{TDepGraph::Graph(node)}
{}

bool TNodeEdgesComparator::operator() (const TDepGraph::TEdge& edge1, const TDepGraph::TEdge& edge2) const noexcept {
    auto node1 = edge1.IsValid() ? Graph[edge1.Id()] : Graph.GetInvalidNode();
    auto node2 = edge2.IsValid() ? Graph[edge2.Id()] : Graph.GetInvalidNode();
    if (!node1.IsValid() && node2.IsValid()) {
        return true;
    }
    if (!node1.IsValid() || !node2.IsValid()) {
        return false;
    }

    const ESortPriority priority1 = ComputeEdgePriority(FromType, edge1.Value(), node1->NodeType);
    const ESortPriority priority2 = ComputeEdgePriority(FromType, edge2.Value(), node2->NodeType);
    if (priority1 == ESortPriority::IncludeFile && priority2 == ESortPriority::IncludeFile) {
        return Graph.GetFileName(node1) < Graph.GetFileName(node2);
    }
    return static_cast<ui32>(priority1) < static_cast<ui32>(priority2);
}

void TYMake::SortAllEdges() {
    NYMake::TTraceStage stageTracer{"Sort edges"};
    for (auto node: Graph.Nodes()) {
        if (node.IsValid()) {
            node.SortEdges(TNodeEdgesComparator{node});
        }
    }
}

void TYMake::CheckBlacklist() {
    NYMake::TTraceStage stageTracer{"Check blacklist"};
    TRestoreContext restoreContext(Conf, Graph, Modules);
    TRestoreContext recurseRestoreContext(Conf, RecurseGraph, Modules);
    TBlacklistChecker blacklistChecker(restoreContext, StartTargets, recurseRestoreContext, RecurseStartTargets);
    blacklistChecker.CheckAll();
}

void TYMake::CheckIsolatedProjects() {
    NYMake::TTraceStage stageTracer{"Check isolated projects"};
    TRestoreContext restoreContext(Conf, Graph, Modules);
    TRestoreContext recurseRestoreContext(Conf, RecurseGraph, Modules);
    Conf.IsolatedProjects.CheckAll(restoreContext, StartTargets, recurseRestoreContext, RecurseStartTargets);
}

void TYMake::TransferStartDirs() {
    for (const auto& dir : Conf.StartDirs) {
        TString curDir = NPath::ConstructPath(NPath::FromLocal(dir), NPath::Source);
        CurStartDirs_.push_back(Names.AddName(EMNT_Directory, curDir));
    }
}

void TYMake::PostInit() {
    TransferStartDirs();
    IncParserManager.InitManager(Conf.ParserPlugins);
    LoadPatch();
    Names.FileConf.InitAfterCacheLoading();
    FSCacheMonEvent();
    DepsCacheMonEvent();
}

static void SafeRemove(const TFsPath& path) {
    try {
        if (path.IsDefined())
            path.DeleteIfExists();
    } catch(...) {
        // Ignore any errors
    }
}

TYMake::~TYMake() {
    SafeRemove(DepCacheTempFile);
    SafeRemove(UidsCacheTempFile);
}

TModuleResolveContext TYMake::GetModuleResolveContext(const TModule& mod) {
    Y_ASSERT(UpdIter != nullptr);
    return MakeModuleResolveContext(mod, Conf, Graph, *UpdIter, IncParserManager.Cache);
}

TRestoreContext TYMake::GetRestoreContext() {
    return {Conf, Graph, Modules};
}

TTraverseStartsContext TYMake::GetTraverseStartsContext() const noexcept {
    return {StartTargets, RecurseStartTargets, ModuleStartTargets};
}

TFileProcessContext TYMake::GetFileProcessContext(TModule* module, TAddDepAdaptor& node) {
    Y_ASSERT(module);
    Y_ASSERT(UpdIter);
    return {Conf, GetModuleResolveContext(*module), UpdIter->State, *module, node};
}

void TYMake::ReportGraphBuildStats() {
    Names.FileConf.ReportStats();
    IncParserManager.Stats.Report();
    Parser->ReportStats();
    Graph.ReportStats();
    UpdIter->Stats.Report();
    UpdIter->ResolveStats.Report();
}

void TYMake::ReportModulesStats() {
    Modules.ReportStats();
}

void TYMake::ReportMakeCommandStats() {
    TMakeCommand::ReportStats();
}

void TYMake::AddStartTarget(const TString& dir) {
    TString dirPath = NPath::ConstructPath(NPath::FromLocal(TStringBuf{dir}), NPath::Source);
    auto elemId = Names.AddName(EMNT_Directory, dirPath);
    auto nodeId = UpdIter->RecursiveAddStartTarget(EMNT_Directory, elemId, &Modules.GetRootModule());
    if (nodeId != TNodeId::Invalid) {
        StartTargets.push_back(nodeId);
    }
}

void TYMake::AddTarget(const TString& dir) {
    TString dirPath = NPath::ConstructPath(NPath::FromLocal(TStringBuf{dir}), NPath::Source);
    auto elemId = Names.AddName(EMNT_Directory, dirPath);
    UpdIter->RecursiveAddNode(EMNT_Directory, elemId, &Modules.GetRootModule());
}

void TYMake::ComputeReachableNodes() {
    if (DepsCacheLoaded_) {
        NYMake::TTraceStage scopeTracer{"Reset reachable nodes"};
        NComputeReachability::ResetReachableNodes(Graph);
    }

    NYMake::TTraceStage scopeTracer{"Set reachable nodes"};
    NComputeReachability::ComputeReachableNodes(Graph, StartTargets);
}
