*Do not edit, this file is generated from comments to macros definitions using `ya dump conf-docs`.*

# ya.make commands

General info: [How to write ya.make files](https://wiki.yandex-team.ru/yatool/HowToWriteYaMakeFiles)

## Table of contents

   * [Multimodules](#multimodules)
       - Multimodule [DLL_JAVA](#multimodule_DLL_JAVA)
       - Multimodule [DOCS](#multimodule_DOCS)
       - Multimodule [FBS_LIBRARY](#multimodule_FBS_LIBRARY)
       - Multimodule [JAVA_CONTRIB_PROGRAM](#multimodule_JAVA_CONTRIB_PROGRAM)
       - Multimodule [JAVA_PROGRAM](#multimodule_JAVA_PROGRAM)
       - Multimodule [JTEST](#multimodule_JTEST)
       - Multimodule [JTEST_FOR](#multimodule_JTEST_FOR)
       - Multimodule [JUNIT5](#multimodule_JUNIT5)
       - Multimodule [PACKAGE](#multimodule_PACKAGE)
       - Multimodule [PROTO_LIBRARY](#multimodule_PROTO_LIBRARY)
       - Multimodule [PY23_LIBRARY](#multimodule_PY23_LIBRARY)
       - Multimodule [PY23_NATIVE_LIBRARY](#multimodule_PY23_NATIVE_LIBRARY)
       - Multimodule [PY23_TEST](#multimodule_PY23_TEST)
       - Multimodule [PY3TEST](#multimodule_PY3TEST)
       - Multimodule [PY3_PROGRAM](#multimodule_PY3_PROGRAM)
       - Multimodule [TS_NEXT](#multimodule_TS_NEXT)
       - Multimodule [TS_PACKAGE](#multimodule_TS_PACKAGE)
       - Multimodule [TS_TSC](#multimodule_TS_TSC)
       - Multimodule [TS_VITE](#multimodule_TS_VITE)
       - Multimodule [TS_WEBPACK](#multimodule_TS_WEBPACK)
       - Multimodule [YQL_UDF](#multimodule_YQL_UDF)
       - Multimodule [YQL_UDF_CONTRIB](#multimodule_YQL_UDF_CONTRIB)
       - Multimodule [YQL_UDF_YDB](#multimodule_YQL_UDF_YDB)
   * [Modules](#modules)
       - Module [BOOSTTEST](#module_BOOSTTEST)
       - Module [BOOSTTEST_WITH_MAIN](#module_BOOSTTEST_WITH_MAIN)
       - Module [CI_GROUP](#module_CI_GROUP)
       - Module [CPP_STYLE_TEST_16](#module_CPP_STYLE_TEST_16)
       - Module [DEFAULT_IOS_INTERFACE](#module_DEFAULT_IOS_INTERFACE)
       - Module [DLL](#module_DLL)
       - Module [DLL_TOOL](#module_DLL_TOOL)
       - Module [DOCS_LIBRARY](#module_DOCS_LIBRARY)
       - Module [EXECTEST](#module_EXECTEST)
       - Module [FAT_OBJECT](#module_FAT_OBJECT)
       - Module [FUZZ](#module_FUZZ)
       - Module [GEN_LIBRARY](#module_GEN_LIBRARY)
       - Module [GO_DLL](#module_GO_DLL)
       - Module [GO_LIBRARY](#module_GO_LIBRARY)
       - Module [GO_PROGRAM](#module_GO_PROGRAM)
       - Module [GO_TEST](#module_GO_TEST)
       - Module [GTEST](#module_GTEST)
       - Module [G_BENCHMARK](#module_G_BENCHMARK)
       - Module [IOS_INTERFACE](#module_IOS_INTERFACE)
       - Module [JAVA_CONTRIB](#module_JAVA_CONTRIB)
       - Module [JAVA_CONTRIB_PROXY](#module_JAVA_CONTRIB_PROXY)
       - Module [JAVA_LIBRARY](#module_JAVA_LIBRARY)
       - Module [LIBRARY](#module_LIBRARY)
       - Module [PROGRAM](#module_PROGRAM)
       - Module [PROTO_DESCRIPTIONS](#module_PROTO_DESCRIPTIONS)
       - Module [PROTO_REGISTRY](#module_PROTO_REGISTRY)
       - Module [PY2MODULE](#module_PY2MODULE)
       - Module [PY2TEST](#module_PY2TEST)
       - Module [PY2_LIBRARY](#module_PY2_LIBRARY)
       - Module [PY2_PROGRAM](#module_PY2_PROGRAM)
       - Module [PY3MODULE](#module_PY3MODULE)
       - Module [PY3TEST_BIN](#module_PY3TEST_BIN)
       - Module [PY3_LIBRARY](#module_PY3_LIBRARY)
       - Module [PY3_PROGRAM_BIN](#module_PY3_PROGRAM_BIN)
       - Module [PYTEST_BIN](#module_PYTEST_BIN)
       - Module [PY_ANY_MODULE](#module_PY_ANY_MODULE)
       - Module [RECURSIVE_LIBRARY](#module_RECURSIVE_LIBRARY)
       - Module [RESOURCES_LIBRARY](#module_RESOURCES_LIBRARY)
       - Module [R_MODULE](#module_R_MODULE)
       - Module [SO_PROGRAM](#module_SO_PROGRAM)
       - Module [TS_TEST_HERMIONE_FOR](#module_TS_TEST_HERMIONE_FOR)
       - Module [TS_TEST_JEST_FOR](#module_TS_TEST_JEST_FOR)
       - Module [TS_TEST_PLAYWRIGHT_FOR](#module_TS_TEST_PLAYWRIGHT_FOR)
       - Module [UNION](#module_UNION)
       - Module [UNITTEST](#module_UNITTEST)
       - Module [UNITTEST_FOR](#module_UNITTEST_FOR)
       - Module [UNITTEST_WITH_CUSTOM_ENTRY_POINT](#module_UNITTEST_WITH_CUSTOM_ENTRY_POINT)
       - Module [YQL_PYTHON3_UDF](#module_YQL_PYTHON3_UDF)
       - Module [YQL_PYTHON3_UDF_TEST](#module_YQL_PYTHON3_UDF_TEST)
       - Module [YQL_PYTHON_UDF](#module_YQL_PYTHON_UDF)
       - Module [YQL_PYTHON_UDF_PROGRAM](#module_YQL_PYTHON_UDF_PROGRAM)
       - Module [YQL_PYTHON_UDF_TEST](#module_YQL_PYTHON_UDF_TEST)
       - Module [YQL_UDF_MODULE](#module_YQL_UDF_MODULE)
       - Module [YQL_UDF_MODULE_CONTRIB](#module_YQL_UDF_MODULE_CONTRIB)
       - Module [YQL_UDF_TEST](#module_YQL_UDF_TEST)
       - Module [YQL_UDF_TEST_CONTRIB](#module_YQL_UDF_TEST_CONTRIB)
       - Module [YQL_UDF_YDB_MODULE](#module_YQL_UDF_YDB_MODULE)
       - Module [YQL_UDF_YDB_TEST](#module_YQL_UDF_YDB_TEST)
       - Module [YT_UNITTEST](#module_YT_UNITTEST)
       - Module [Y_BENCHMARK](#module_Y_BENCHMARK)
   * [Macros](#macros)
       - Macros [ACCELEO](#macro_ACCELEO) .. [ADD_LINTER_CHECK](#macro_ADD_LINTER_CHECK)
       - Macros [ADD_PYTEST_BIN](#macro_ADD_PYTEST_BIN) .. [ANNOTATION_PROCESSOR](#macro_ANNOTATION_PROCESSOR)
       - Macros [ARCHIVE](#macro_ARCHIVE) .. [BISON_HEADER](#macro_BISON_HEADER)
       - Macros [BISON_NO_HEADER](#macro_BISON_NO_HEADER) .. [BUNDLE](#macro_BUNDLE)
       - Macros [CFLAGS](#macro_CFLAGS) .. [CLANG_EMIT_AST_CXX_RUN_TOOL](#macro_CLANG_EMIT_AST_CXX_RUN_TOOL)
       - Macros [CLEAN_TEXTREL](#macro_CLEAN_TEXTREL) .. [COMPILE_SWIFT_MODULE](#macro_COMPILE_SWIFT_MODULE)
       - Macros [CONFIGURE_FILE](#macro_CONFIGURE_FILE) .. [CPP_PROTO_PLUGIN](#macro_CPP_PROTO_PLUGIN)
       - Macros [CPP_PROTO_PLUGIN0](#macro_CPP_PROTO_PLUGIN0) .. [CXXFLAGS](#macro_CXXFLAGS)
       - Macros [CYTHON_FLAGS](#macro_CYTHON_FLAGS) .. [DECLARE_EXTERNAL_HOST_RESOURCES_PACK](#macro_DECLARE_EXTERNAL_HOST_RESOURCES_PACK)
       - Macros [DECLARE_EXTERNAL_RESOURCE](#macro_DECLARE_EXTERNAL_RESOURCE) .. [DIRECT_DEPS_ONLY](#macro_DIRECT_DEPS_ONLY)
       - Macros [DISABLE](#macro_DISABLE) .. [ELSE](#macro_ELSE)
       - Macros [ELSEIF](#macro_ELSEIF) .. [EXCLUDE_TAGS](#macro_EXCLUDE_TAGS)
       - Macros [EXPLICIT_DATA](#macro_EXPLICIT_DATA) .. [FBS_NAMESPACE](#macro_FBS_NAMESPACE)
       - Macros [FBS_TO_PY2SRC](#macro_FBS_TO_PY2SRC) .. [FORK_TEST_FILES](#macro_FORK_TEST_FILES)
       - Macros [FROM_ARCHIVE](#macro_FROM_ARCHIVE) .. [GENERATE_SCRIPT](#macro_GENERATE_SCRIPT)
       - Macros [GENERATE_YT_RECORD](#macro_GENERATE_YT_RECORD) .. [GO_COMPILE_FLAGS](#macro_GO_COMPILE_FLAGS)
       - Macros [GO_EMBED_BINDIR](#macro_GO_EMBED_BINDIR) .. [GO_GRPC_GATEWAY_V2_SRCS](#macro_GO_GRPC_GATEWAY_V2_SRCS)
       - Macros [GO_LDFLAGS](#macro_GO_LDFLAGS) .. [GO_PROTO_USE_V2](#macro_GO_PROTO_USE_V2)
       - Macros [GO_SKIP_TESTS](#macro_GO_SKIP_TESTS) .. [GRPC_WITH_GMOCK](#macro_GRPC_WITH_GMOCK)
       - Macros [HEADERS](#macro_HEADERS) .. [IOS_APP_ASSETS_FLAGS](#macro_IOS_APP_ASSETS_FLAGS)
       - Macros [IOS_APP_COMMON_FLAGS](#macro_IOS_APP_COMMON_FLAGS) .. [JAVA_DEPENDENCIES_CONFIGURATION](#macro_JAVA_DEPENDENCIES_CONFIGURATION)
       - Macros [JAVA_EXTERNAL_DEPENDENCIES](#macro_JAVA_EXTERNAL_DEPENDENCIES) .. [JOIN_SRCS](#macro_JOIN_SRCS)
       - Macros [JOIN_SRCS_GLOBAL](#macro_JOIN_SRCS_GLOBAL) .. [LDFLAGS](#macro_LDFLAGS)
       - Macros [LICENSE](#macro_LICENSE) .. [LJ_21_ARCHIVE](#macro_LJ_21_ARCHIVE)
       - Macros [LJ_ARCHIVE](#macro_LJ_ARCHIVE) .. [LOCAL_SOURCES_JAR](#macro_LOCAL_SOURCES_JAR)
       - Macros [MACROS_WITH_ERROR](#macro_MACROS_WITH_ERROR) .. [NGINX_MODULES](#macro_NGINX_MODULES)
       - Macros [NO_BUILD_IF](#macro_NO_BUILD_IF) .. [NO_DOCTESTS](#macro_NO_DOCTESTS)
       - Macros [NO_EXPORT_DYNAMIC_SYMBOLS](#macro_NO_EXPORT_DYNAMIC_SYMBOLS) .. [NO_OPTIMIZE](#macro_NO_OPTIMIZE)
       - Macros [NO_OPTIMIZE_PY_PROTOS](#macro_NO_OPTIMIZE_PY_PROTOS) .. [NO_TS_TYPECHECK](#macro_NO_TS_TYPECHECK)
       - Macros [NO_UTIL](#macro_NO_UTIL) .. [OWNER](#macro_OWNER)
       - Macros [PACK](#macro_PACK) .. [POPULATE_CPP_COVERAGE_FLAGS](#macro_POPULATE_CPP_COVERAGE_FLAGS)
       - Macros [PREPARE_INDUCED_DEPS](#macro_PREPARE_INDUCED_DEPS) .. [PYTHON2_ADDINCL](#macro_PYTHON2_ADDINCL)
       - Macros [PYTHON2_MODULE](#macro_PYTHON2_MODULE) .. [PY_MAIN](#macro_PY_MAIN)
       - Macros [PY_NAMESPACE](#macro_PY_NAMESPACE) .. [RECURSE](#macro_RECURSE)
       - Macros [RECURSE_FOR_TESTS](#macro_RECURSE_FOR_TESTS) .. [RESTRICT_PATH](#macro_RESTRICT_PATH)
       - Macros [RUN](#macro_RUN) .. [RUN_PROGRAM](#macro_RUN_PROGRAM)
       - Macros [RUN_PYTHON3](#macro_RUN_PYTHON3) .. [SET_APPEND_WITH_GLOBAL](#macro_SET_APPEND_WITH_GLOBAL)
       - Macros [SET_COMPILE_OUTPUTS_MODIFIERS](#macro_SET_COMPILE_OUTPUTS_MODIFIERS) .. [SPLIT_FACTOR](#macro_SPLIT_FACTOR)
       - Macros [SRC](#macro_SRC) .. [SRC_C_PIC](#macro_SRC_C_PIC)
       - Macros [SRC_C_SSE2](#macro_SRC_C_SSE2) .. [STYLE_CPP](#macro_STYLE_CPP)
       - Macros [STYLE_PYTHON](#macro_STYLE_PYTHON) .. [TASKLET_REG_EXT](#macro_TASKLET_REG_EXT)
       - Macros [TEST_CWD](#macro_TEST_CWD) .. [TS_ESLINT_CONFIG](#macro_TS_ESLINT_CONFIG)
       - Macros [TS_EXCLUDE_FILES_GLOB](#macro_TS_EXCLUDE_FILES_GLOB) .. [TS_TEST_DEPENDS_ON_BUILD](#macro_TS_TEST_DEPENDS_ON_BUILD)
       - Macros [TS_TEST_FOR](#macro_TS_TEST_FOR) .. [UBERJAR_HIDE_EXCLUDE_PATTERN](#macro_UBERJAR_HIDE_EXCLUDE_PATTERN)
       - Macros [UBERJAR_HIDE_INCLUDE_PATTERN](#macro_UBERJAR_HIDE_INCLUDE_PATTERN) .. [USE_COMMON_GOOGLE_APIS](#macro_USE_COMMON_GOOGLE_APIS)
       - Macros [USE_CXX](#macro_USE_CXX) .. [USE_MODERN_FLEX_WITH_HEADER](#macro_USE_MODERN_FLEX_WITH_HEADER)
       - Macros [USE_NASM](#macro_USE_NASM) .. [VALIDATE_DATA_RESTART](#macro_VALIDATE_DATA_RESTART)
       - Macros [VALIDATE_IN_DIRS](#macro_VALIDATE_IN_DIRS) .. [WITHOUT_LICENSE_TEXTS](#macro_WITHOUT_LICENSE_TEXTS)
       - Macros [WITH_DYNAMIC_LIBS](#macro_WITH_DYNAMIC_LIBS) .. [WITH_KOTLIN_GRPC](#macro_WITH_KOTLIN_GRPC)
       - Macros [WITH_YA_1931](#macro_WITH_YA_1931) .. [YT_ORM_PROTO_YSON](#macro_YT_ORM_PROTO_YSON)
       - Macros [YT_SPEC](#macro_YT_SPEC) .. [YT_SPEC](#macro_YT_SPEC)
## Multimodules <a name="multimodules"></a>

###### Multimodule [DLL\_JAVA][]() <a name="multimodule_DLL_JAVA"></a>
DLL built using swig for Java. Produces dynamic library and a .jar.
Dynamic library is treated the same as in the case of PEERDIR from Java to DLL.
.jar goes on the classpath.

Documentation: https://wiki.yandex-team.ru/yatool/java/#integracijascpp/pythonsborkojj

###### Multimodule [DOCS][]() <a name="multimodule_DOCS"></a>
Documentation project multimodule.

When built directly, via RECURSE, DEPENDS or BUNDLE the output artifact is docs.tar.gz with statically generated site.
When PEERDIRed from other DOCS() module behaves like a UNION (supplying own content and dependencies to build target).
Peerdirs from modules other than DOCS are not accepted.
Most usual macros are not accepted, only used with the macros DOCS\_DIR(), DOCS\_CONFIG(), DOCS\_VARS().

@see: [DOCS\_DIR()](#macro\_DOCS\_DIR), [DOCS\_CONFIG()](#macro\_DOCS\_CONFIG), [DOCS\_VARS()](#macro\_DOCS\_VARS).

###### Multimodule [FBS\_LIBRARY][]() <a name="multimodule_FBS_LIBRARY"></a>
Build some variant of Flatbuffers library.

The particular variant is selected based on where PEERDIR to FBS\_LIBRARY
comes from.

Now supported 5 variants: C++, Java, Python 2.x, Python 3.x and Go.
When PEERDIR comes from module for particular language appropriate variant
is selected.

Notes: FBS\_NAMESPACE must be specified in all dependent FBS\_LIBRARY modules
       if build of Go code is requested.

###### Multimodule [JAVA\_CONTRIB\_PROGRAM][] <a name="multimodule_JAVA_CONTRIB_PROGRAM"></a>
Not documented yet.

###### Multimodule [JAVA\_PROGRAM][]() <a name="multimodule_JAVA_PROGRAM"></a>
The module describing java programs build.
Output artifacts: .jar and directory with all the jar to the classpath of the formation.

Documentation: https://wiki.yandex-team.ru/yatool/java/

###### Multimodule [JTEST][] <a name="multimodule_JTEST"></a>
Not documented yet.

###### Multimodule [JTEST\_FOR][] <a name="multimodule_JTEST_FOR"></a>
Not documented yet.

###### Multimodule [JUNIT5][] <a name="multimodule_JUNIT5"></a>
Not documented yet.

###### Multimodule [PACKAGE][](name) <a name="multimodule_PACKAGE"></a>
Module collects what is described directly inside it, builds and collects all its transitively available PEERDIRs.
As a result, build directory of the project gets the structure of the accessible part of Arcadia, where the build result of each PEERDIR is placed to relevant Arcadia subpath.
The data can be optionally packed if macro PACK() is used.

Is only used together with the macros FILES(), PEERDIR(), COPY(), FROM\_SANDBOX(), RUN\_PROGRAM or BUNDLE(). Don't use SRCS inside a PACKAGE.

Documentation: https://wiki.yandex-team.ru/yatool/large-data/

@see: [PACK()](#macro\_PACK)

###### Multimodule [PROTO\_LIBRARY][]() <a name="multimodule_PROTO_LIBRARY"></a>
Build some varian of protocol buffers library.

The particular variant is selected based on where PEERDIR to PROTO\_LIBRARY comes from.

Now supported 5 variants: C++, Java, Python 2.x, Python 3.x and Go.
When PEERDIR comes from module for particular language appropriate variant is selected.
PROTO\_LIBRARY also supports emission of GRPC code if GRPC() macro is specified.
Notes:
- Python versions emit C++ code in addition to Python as optimization.
- In some PROTO\_LIBRARY-es Java or Python versions are excluded via EXCLUDE\_TAGS macros due to incompatibilities.
- Use from DEPENDS or BUNDLE is not allowed

Documentation: https://wiki.yandex-team.ru/yatool/proto\_library/

See: [GRPC()](#macro\_GRPC), [OPTIMIZE\_PY\_PROTOS()](#macro\_OPTIMIZE\_PY\_PROTOS), [INCLUDE\_TAGS()](#macro\_INCLUDE\_TAGS), [EXCLUDE\_TAGS()](#macro\_EXCLUDE\_TAGS)

###### Multimodule [PY23\_LIBRARY][]([name]) <a name="multimodule_PY23_LIBRARY"></a>
Build PY2\_LIBRARY or PY3\_LIBRARY depending on incoming PEERDIR.
Direct build or build by RECURSE creates both variants.
This multimodule doesn't define any final targets, so use from DEPENDS or BUNDLE is not allowed.

Documentation: https://wiki.yandex-team.ru/arcadia/python/pysrcs

###### Multimodule [PY23\_NATIVE\_LIBRARY][]([name]) <a name="multimodule_PY23_NATIVE_LIBRARY"></a>
Build LIBRARY compatible with either Python 2.x or Python 3.x depending on incoming PEERDIR.

This multimodule doesn't depend on Arcadia Python binary build. It is intended only for C++ code and cannot contain PY\_SRCS and USE\_PYTHON2 macros.
Use these multimodule instead of PY23\_LIBRARY if the C++ extension defined in it will be used in PY2MODULE.
While it doesn't bring Arcadia Python dependency itself, it is still compatible with Arcadia Python build and can be PEERDIR-ed from PY2\_LIBRARY and alikes.
Proper version will be selected according to Python version of the module PEERDIR comes from.

This mulrtimodule doesn't define any final targets so cannot be used from DEPENDS or BUNDLE macros.

For more information read https://wiki.yandex-team.ru/arcadia/python/pysrcs/#pysrcssrcsipy23nativelibrary

@see [LIBRARY()](#module\_LIBRARY), [PY2MODULE()](#module\_PY2MODULE)

###### Multimodule [PY23\_TEST][] <a name="multimodule_PY23_TEST"></a>
Not documented yet.

###### Multimodule [PY3TEST][]([name]) <a name="multimodule_PY3TEST"></a>
The test module for Python 3.x based on py.test

This module is compatible only with PYTHON3-tagged modules and selects peers from multimodules accordingly.
This module is only compatible with Arcadia Python build (to avoid tests duplication from Python2/3-tests). For non-Arcadia python use PYTEST.

Documentation: https://wiki.yandex-team.ru/yatool/test/#testynapytest
Documentation about the Arcadia test system: https://wiki.yandex-team.ru/yatool/test/

###### Multimodule [PY3\_PROGRAM][]([progname]) <a name="multimodule_PY3_PROGRAM"></a>
Python 3.x binary program. Links all Python 3.x libraries and Python 3.x interpreter into itself to form regular executable.
If name is not specified it will be generated from the name of the containing project directory.
This only compatible with PYTHON3-tagged modules and selects those from multimodules.

Documentation: https://wiki.yandex-team.ru/devtools/commandsandvars/py\_srcs/

###### Multimodule [TS\_NEXT][]([name]) <a name="multimodule_TS_NEXT"></a>
NextJS app, built with `next build`. Requires sources to be under /src folder.
/pages and /app on the root level ar not supported.
Build results are output.tar.

Documentation: https://docs.yandex-team.ru/frontend-in-arcadia/references/TS\_NEXT

@example

    TS_NEXT()
    END()

###### Multimodule [TS\_PACKAGE][]() <a name="multimodule_TS_PACKAGE"></a>
The TypeScript/JavaScript library module, that does not need any compilation,
and is just a set of files and NPM dependencies. List required files in TS\_FILES macro.
`package.json` is included by default.

Documentation: https://docs.yandex-team.ru/frontend-in-arcadia/references/TS\_PACKAGE

@example

    TS_PACKAGE()
        TS_FILES(
            eslint.config.json
            prettierrc.json
        )
    END()

###### Multimodule [TS\_TSC][]([name]) <a name="multimodule_TS_TSC"></a>
The TypeScript/JavaScript library module, compiles TypeScript sources to JavaScript using tsc.
Build results are JavaScript files, typings and source mappings (depending on local tsconfig.json settings).

Documentation: https://docs.yandex-team.ru/frontend-in-arcadia/references/TS\_TSC

@example

    TS_TSC()

    END()

###### Multimodule [TS\_VITE][]([name]) <a name="multimodule_TS_VITE"></a>
The Vite bundle, bundles JavaScript code.
Build results are packed as `output.tar`.

Documentation: https://docs.yandex-team.ru/frontend-in-arcadia/references/TS\_VITE

@example

    TS_VITE()
    END()

###### Multimodule [TS\_WEBPACK][]([name]) <a name="multimodule_TS_WEBPACK"></a>
The Webpack bundle, bundles JavaScript code.
Build results are packed as `output.tar`.

Documentation: https://docs.yandex-team.ru/frontend-in-arcadia/references/TS\_WEBPACK

@example

    TS_WEBPACK()
    END()

###### Multimodule [YQL\_UDF][](name) <a name="multimodule_YQL_UDF"></a>
User-defined function for YQL

Multimodule which is YQL\_UDF\_MODULE when built directly or referred by BUNDLE and DEPENDS macros.
If used by PEERDIRs it is usual static LIBRARY with default YQL dependencies, allowing code reuse between UDFs.

@see: [YQL\_UDF\_MODULE()](#module\_YQL\_UDF\_MODULE)

###### Multimodule [YQL\_UDF\_CONTRIB][] <a name="multimodule_YQL_UDF_CONTRIB"></a>
Not documented yet.

###### Multimodule [YQL\_UDF\_YDB][] <a name="multimodule_YQL_UDF_YDB"></a>
Not documented yet.

## Modules <a name="modules"></a>

###### Module [BOOSTTEST][]([name]) _#deprecated_ <a name="module_BOOSTTEST"></a>
Test module based on boost/test/unit\_test.hpp.
As with entire boost library usage of this technology is deprecated in Arcadia and restricted with configuration error in most of projects.
No new module of this type should be introduced unless it is explicitly approved by C++ committee.

###### Module [BOOSTTEST\_WITH\_MAIN][]([name]) _#deprecated_ <a name="module_BOOSTTEST_WITH_MAIN"></a>
Same as BOOSTTEST (see above), but comes with builtin int main(argc, argv) implementation

###### Module [CI\_GROUP][]() <a name="module_CI_GROUP"></a>
Module collects what is described directly inside it transitively by PEERDIRs.
No particular layout of built artifacts is implied. This module is needed primarily for CI dependency analysis and may not trigger builds at all.

Is only used together with the macro PEERDIR() and FILES(). Don't use SRCS inside CI\_GROUP().

###### Module [CPP\_STYLE\_TEST\_16][]: PY3TEST\_BIN <a name="module_CPP_STYLE_TEST_16"></a>
Not documented yet.

###### Module [DEFAULT\_IOS\_INTERFACE][]: IOS\_INTERFACE <a name="module_DEFAULT_IOS_INTERFACE"></a>
Not documented yet.

###### Module [DLL][](name major\_ver [minor\_ver] [EXPORTS symlist\_file] [PREFIX prefix]) <a name="module_DLL"></a>
Dynamic library module definition.
1. major\_ver and minor\_ver must be integers.
2. EXPORTS allows you to explicitly specify the list of exported functions. This accepts 2 kind of files: .exports with <lang symbol> pairs and JSON-line .symlist files
3. PREFIX allows you to change the prefix of the output file (default DLL has the prefix "lib").

DLL cannot participate in linking to programs but can be used from Java or as final artifact (packaged and deployed).

###### Module [DLL\_TOOL][] <a name="module_DLL_TOOL"></a>
DLL\_TOOL is a DLL that can be used as a LD\_PRELOAD tool.

###### Module [DOCS\_LIBRARY][]: \_DOCS\_BARE\_UNIT <a name="module_DOCS_LIBRARY"></a>
Not documented yet.

###### Module [EXECTEST][]() <a name="module_EXECTEST"></a>
Module definition of generic test that executes a binary.
Use macro RUN to specify binary to run.

@example:

    EXECTEST()
        OWNER(g:yatool)

        RUN(
            cat input.txt
        )
        DATA(
            arcadia/devtools/ya/test/tests/exectest/data
        )
        DEPENDS(
            devtools/dummy_arcadia/cat
        )
        TEST_CWD(devtools/ya/test/tests/exectest/data)
    END()

More examples: https://wiki.yandex-team.ru/yatool/test/#exec-testy

@see: [RUN()](#macro\_RUN)

###### Module [FAT\_OBJECT][]() <a name="module_FAT_OBJECT"></a>
The "fat" object module. It will contain all its transitive dependencies reachable by PEERDIRs:
static libraries, local (from own SRCS) and global (from peers') object files.

Designed for use in XCode projects for iOS.

###### Module [FUZZ][]() <a name="module_FUZZ"></a>
In order to start using Fuzzing in Arcadia, you need to create a FUZZ module with the implementation of the function LLVMFuzzerTestOneInput().
This module should be reachable by RECURSE from /autocheck project in order for the corpus to be regularly updated.
AFL and Libfuzzer are supported in Arcadia via a single interface, but the automatic fuzzing still works only through Libfuzzer.

Example: https://github.com/yandex/yatool/tree/main/contrib/libs/re2/re2/fuzzing/re2\_fuzzer.cc?rev=2919463#L58

Documentation: https://wiki.yandex-team.ru/yatool/fuzzing/

###### Module [GEN\_LIBRARY][]() <a name="module_GEN_LIBRARY"></a>
Definition of a module that brings generated artefacts. This module can PEERDIRed
from any module. The resulted module is empty and cleaned up during construction
of the build graph.

NOTE! SRCS macro is not supported for this library.

###### Module [GO\_DLL][](name major\_ver [minor\_ver] [PREFIX prefix]) <a name="module_GO_DLL"></a>
Go ishared object module definition.
Compile and link Go module to a shared object.
Will select Go implementation on PEERDIR to PROTO\_LIBRARY.

###### Module [GO\_LIBRARY][]([name]) <a name="module_GO_LIBRARY"></a>
Go library module definition.
Compile Go module as a library suitable for PEERDIR from other Go modules.
Will select Go implementation on PEERDIR to PROTO\_LIBRARY.

###### Module [GO\_PROGRAM][]([name]) <a name="module_GO_PROGRAM"></a>
Go program module definition.
Compile and link Go module to an executable program.
Will select Go implementation on PEERDIR to PROTO\_LIBRARY.

###### Module [GO\_TEST][]([name]) <a name="module_GO_TEST"></a>
Go test module definition.
Compile and link Go module as a test suitable for running with Arcadia testing support.
All usual testing support macros like DATA, DEPENDS, SIZE, REQUIREMENTS etc. are supported.
Will select Go implementation on PEERDIR to PROTO\_LIBRARY.

###### Module [GTEST][]([name]) <a name="module_GTEST"></a>
Unit test module based on library/cpp/testing/gtest.
It is recommended not to specify the name.

Documentation: https://docs.yandex-team.ru/arcadia-cpp/docs/build/manual/tests/cpp#gtest

###### Module [G\_BENCHMARK][]([benchmarkname]) <a name="module_G_BENCHMARK"></a>
Benchmark test based on the google benchmark.

For more details see: https://github.com/yandex/yatool/tree/main/contrib/libs/benchmark/README.md

###### Module [IOS\_INTERFACE][]() <a name="module_IOS_INTERFACE"></a>
iOS GUI module definition

###### Module [JAVA\_CONTRIB][]: \_JAR\_BASE <a name="module_JAVA_CONTRIB"></a>
Not documented yet.

###### Module [JAVA\_CONTRIB\_PROXY][]: \_JAR\_BASE <a name="module_JAVA_CONTRIB_PROXY"></a>
Not documented yet.

###### Module [JAVA\_LIBRARY][]() <a name="module_JAVA_LIBRARY"></a>
The module describing java library build.

Documentation: https://wiki.yandex-team.ru/yatool/java/

###### Module [LIBRARY][]() <a name="module_LIBRARY"></a>
The regular static library module.

The LIBRARY() is intermediate module, so when built directly it won't build its dependencies.
It transitively provides its PEERDIRs to ultimate final target, where all LIBRARY() modules are built and linked together.

This is C++ library, and it selects peers from multimodules accordingly.

It makes little sense to mention LIBRARY in DEPENDS or BUNDLE, package and deploy it since it is not a standalone entity.
In order to use library in tests PEERDIR it to link into tests.
If you think you need to distribute static library please contact devtools@ for assistance.

###### Module [PROGRAM][]([progname]) <a name="module_PROGRAM"></a>
Regular program module.
If name is not specified it will be generated from the name of the containing project directory.

###### Module [PROTO\_DESCRIPTIONS][]: \_BARE\_UNIT <a name="module_PROTO_DESCRIPTIONS"></a>
Not documented yet.

###### Module [PROTO\_REGISTRY][]: PROTO\_DESCRIPTIONS <a name="module_PROTO_REGISTRY"></a>
Not documented yet.

###### Module [PY2MODULE][](name major\_ver [minor\_ver] [EXPORTS symlist\_file] [PREFIX prefix]) <a name="module_PY2MODULE"></a>
The Python external module for Python2 and any system Python
1. major\_ver and minor\_ver must be integers.
2. The resulting .so will have the prefix "lib".
3. Processing EXPORTS and PREFIX is the same as for DLL module
This is native DLL, so it will select C++ version from PROTO\_LIBRARY.

Note: this module will always PEERDIR Python2 version of PY23\_NATIVE\_LIBRARY.
Do not PEERDIR PY2\_LIBRARY or PY23\_LIBRARY: this will link Python in and render artifact unusable as Python module.

Documentation: https://wiki.yandex-team.ru/devtools/commandsandvars/py\_srcs/

###### Module [PY2TEST][]([name]) <a name="module_PY2TEST"></a>
The test module for Python 2.x based on py.test

This module is compatible only with PYTHON2-tagged modules and selects peers from multimodules accordingly.
This module is compatible with non-Arcadia Python builds.

Documentation: https://wiki.yandex-team.ru/yatool/test/#python
Documentation about the Arcadia test system: https://wiki.yandex-team.ru/yatool/test/

###### Module [PY2\_LIBRARY][]() _# deprecated_ <a name="module_PY2_LIBRARY"></a>
Deprecated. Use PY23\_LIBRARY or PY3\_LIBRARY instead.
Python 2.x binary built library. Builds sources from PY\_SRCS to data suitable for PY2\_PROGRAM.
Adds dependencies to Python 2.x runtime library from Arcadia.
This module is only compatible with PYTHON2-tagged modules and selects those from multimodules.
This module is only compatible with Arcadia Python build.

Documentation: https://wiki.yandex-team.ru/devtools/commandsandvars/py\_srcs/

###### Module [PY2\_PROGRAM][]([progname]) _# deprecated_ <a name="module_PY2_PROGRAM"></a>
Deprecated. Use PY3\_PROGRAM instead.
Python 2.x binary program. Links all Python 2.x libraries and Python 2.x interpreter into itself to form regular executable.
If name is not specified it will be generated from the name of the containing project directory.
This only compatible with PYTHON2-tagged modules and selects those from multimodules.

Documentation: https://wiki.yandex-team.ru/devtools/commandsandvars/py\_srcs/

###### Module [PY3MODULE][](name major\_ver [minor\_ver] [EXPORTS symlist\_file] [PREFIX prefix]) <a name="module_PY3MODULE"></a>
The Python external module for Python3 and any system Python
1. major\_ver and minor\_ver must be integers.
2. The resulting .so will have the prefix "lib".
3. Processing EXPORTS and PREFIX is the same as for DLL module
This is native DLL, so it will select C++ version from PROTO\_LIBRARY.

Note: this module will always PEERDIR Python3 version of PY23\_NATIVE\_LIBRARY.
Do not PEERDIR PY3\_LIBRARY or PY23\_LIBRARY: this will link Python in and render artifact unusable as Python module.

Documentation: https://wiki.yandex-team.ru/devtools/commandsandvars/py\_srcs/

###### Module [PY3TEST\_BIN][]() _#deprecated_ <a name="module_PY3TEST_BIN"></a>
Same as PY3TEST. Don't use this, use PY3TEST instead.

###### Module [PY3\_LIBRARY][]() <a name="module_PY3_LIBRARY"></a>
Python 3.x binary library. Builds sources from PY\_SRCS to data suitable for PY2\_PROGRAM
Adds dependencies to Python 2.x runtime library from Arcadia.
This module is only compatible with PYTHON3-tagged modules and selects those from multimodules.
This module is only compatible with Arcadia Python build.

Documentation: https://wiki.yandex-team.ru/devtools/commandsandvars/py\_srcs/

###### Module [PY3\_PROGRAM\_BIN][]([progname]) <a name="module_PY3_PROGRAM_BIN"></a>
Use instead of PY3\_PROGRAM only if ya.make with PY3\_PROGRAM() included in another ya.make
In all other cases use PY3\_PROGRAM

###### Module [PYTEST\_BIN][]() _#deprecated_ <a name="module_PYTEST_BIN"></a>
Same as PY2TEST. Don't use this, use PY2TEST instead.

###### Module [PY\_ANY\_MODULE][](name major\_ver [minor\_ver] [EXPORTS symlist\_file] [PREFIX prefix]) <a name="module_PY_ANY_MODULE"></a>
The Python external module for any versio of Arcadia or system Python.
1. major\_ver and minor\_ver must be integers.
2. The resulting .so will have the prefix "lib".
3. Processing EXPORTS and PREFIX is the same as for DLL module
This is native DLL, so it will select C++ version from PROTO\_LIBRARY.

Note: Use PYTHON2\_MODULE()/PYTHON3\_MODULE() in order to PEERDIR proper version of PY23\_NATIVE\_LIBRARY.
Do not PEERDIR any PY\*\_LIBRARY: this will link Python in and render artifact unusable as Python module.

Documentation: https://wiki.yandex-team.ru/devtools/commandsandvars/py\_srcs/

###### Module [RECURSIVE\_LIBRARY][]() <a name="module_RECURSIVE_LIBRARY"></a>
The recursive ("fat") library module. It will contain all its transitive dependencies reachable by PEERDIRs:
from static libraries, local (from own SRCS) and global (from peers') object files.

Designed for use in XCode projects for iOS.

###### Module [RESOURCES\_LIBRARY][]() <a name="module_RESOURCES_LIBRARY"></a>
Definition of a module that brings its content from external source (Sandbox) via DECLARE\_EXTERNAL\_RESOURCE macro.
This can participate in PEERDIRs of others as library but it cannot have own sources and PEERDIRs.

@see: [DECLARE\_EXTERNAL\_RESOURCE()](#macro\_DECLARE\_EXTERNAL\_RESOURCE)

###### Module [R\_MODULE][](name major\_ver [minor\_ver] [EXPORTS symlist\_file] [PREFIX prefix]) <a name="module_R_MODULE"></a>
The external module for R language.
1. major\_ver and minor\_ver must be integers.
2. The resulting .so will have the prefix "lib".
3. Processing EXPORTS and PREFIX is the same as for DLL module
This is native DLL, so it will select C++ version from PROTO\_LIBRARY.

###### Module [SO\_PROGRAM][](name major\_ver [minor\_ver] [EXPORTS symlist\_file] [PREFIX prefix]) <a name="module_SO_PROGRAM"></a>
Executable dynamic library module definition.
1. major\_ver and minor\_ver must be integers.
2. EXPORTS allows you to explicitly specify the list of exported functions. This accepts 2 kind of files: .exports with <lang symbol> pairs and JSON-line .symlist files
3. PREFIX allows you to change the prefix of the output file.

###### Module [TS\_TEST\_HERMIONE\_FOR][](Path) <a name="module_TS_TEST_HERMIONE_FOR"></a>
Defines testing module with hermione test runner.

Documentation: https://docs.yandex-team.ru/frontend-in-arcadia/references/TS\_TEST\_HERMIONE\_FOR

@example

    TS_TEST_HERMIONE_FOR(path/to/module)
        TS_TEST_SRCS(../src)
        TS_TEST_CONFIG(../hermione.conf.js)
    END()

###### Module [TS\_TEST\_JEST\_FOR][](Path) <a name="module_TS_TEST_JEST_FOR"></a>
Defines testing module with jest test runner.

Documentation: https://docs.yandex-team.ru/frontend-in-arcadia/references/TS\_TEST\_JEST\_FOR

@example

    TS_TEST_JEST_FOR(path/to/module)
        TS_TEST_SRCS(../src)
        TS_TEST_CONFIG(../jest.config.js)
    END()

###### Module [TS\_TEST\_PLAYWRIGHT\_FOR][](Path) <a name="module_TS_TEST_PLAYWRIGHT_FOR"></a>
Defines testing module with playwright test runner.

Documentation: https://docs.yandex-team.ru/frontend-in-arcadia/references/TS\_TEST\_PLAYWRIGHT\_FOR

@example

    TS_TEST_PLAYWRIGHT_FOR(path/to/module)
        TS_TEST_SRCS(../src)
        TS_TEST_CONFIG(../playwright.config.js)
    END()

###### Module [UNION][](name) <a name="module_UNION"></a>
Collection of PEERDIR dependencies, files and artifacts.
UNION doesn't build its peers, just provides those to modules depending on it.
When specified in DEPENDS() macro the UNION is transitively closed, building all its peers and providing those by own paths (without adding this module path like PACKAGE does).

Is only used together with the macros like FILES(), PEERDIR(), COPY(), FROM\_SANDBOX(), RUN\_PROGRAM or BUNDLE(). Don't use SRCS inside a UNION.

Documentation: https://wiki.yandex-team.ru/yatool/large-data/

###### Module [UNITTEST][]([name]) <a name="module_UNITTEST"></a>
Unit test module based on library/cpp/testing/unittest.
It is recommended not to specify the name.

Documentation: https://wiki.yandex-team.ru/yatool/test/#opisanievya.make1

###### Module [UNITTEST\_FOR][](path/to/lib) <a name="module_UNITTEST_FOR"></a>
Convenience extension of UNITTEST module.
The UNINTTEST module with additional SRCDIR + ADDINCL + PEERDIR on path/to/lib.
path/to/lib is the path to the directory with the LIBRARY project.

Documentation about the Arcadia test system: https://wiki.yandex-team.ru/yatool/test/

###### Module [UNITTEST\_WITH\_CUSTOM\_ENTRY\_POINT][]([name]) <a name="module_UNITTEST_WITH_CUSTOM_ENTRY_POINT"></a>
Generic unit test module.

###### Module [YQL\_PYTHON3\_UDF][](name) <a name="module_YQL_PYTHON3_UDF"></a>
The extension module for YQL with Python 3.x UDF (User Defined Function for YQL).
Unlike YQL\_UDF this is plain DLL module, so PEERDIRs to it are not allowed.

Documentation: https://yql.yandex-team.ru/docs/yt/udf/python/

###### Module [YQL\_PYTHON3\_UDF\_TEST][](name) <a name="module_YQL_PYTHON3_UDF_TEST"></a>
The Python test for Python 3.x YQL UDF (User Defined Function for YQL). The code should be a proper YQL\_PYTHON3\_UDF.

This module will basically build itself as UDF and run as test using yql/tools/run\_python\_udf/run\_python\_udf tool.

Documentation: https://yql.yandex-team.ru/docs/yt/udf/python/

@see: [YQL\_PYTHON3\_UDF()](#module\_YQL\_PYTHON3\_UDF)

###### Module [YQL\_PYTHON\_UDF][](name) <a name="module_YQL_PYTHON_UDF"></a>
Definition of the extension module for YQL with Python 2.x UDF (User Defined Function for YQL).
Unlike YQL\_UDF this is plain DLL module, so PEERDIRs to it are not allowed.

https://yql.yandex-team.ru/docs/yt/udf/python/

###### Module [YQL\_PYTHON\_UDF\_PROGRAM][](name) <a name="module_YQL_PYTHON_UDF_PROGRAM"></a>
Definition of the extension module for YQL with Python 2.x UDF (User Defined Function for YQL).
Unlike YQL\_UDF this is plain DLL module, so PEERDIRs to it are not allowed.

https://yql.yandex-team.ru/docs/yt/udf/python/

###### Module [YQL\_PYTHON\_UDF\_TEST][](name) <a name="module_YQL_PYTHON_UDF_TEST"></a>
The Python test for Python YQL UDF (Python User Defined Function for YQL). The code should be a proper YQL\_PYTHON\_UDF.

This module will basically build itself as UDF and run as test using yql/tools/run\_python\_udf/run\_python\_udf tool.

Documentation: https://yql.yandex-team.ru/docs/yt/udf/python/

@example: https://github.com/yandex/yatool/tree/main/yql/udfs/test/simple/ya.make

@see: [YQL\_PYTHON\_UDF()](#module\_YQL\_PYTHON\_UDF)

###### Module [YQL\_UDF\_MODULE][](name) <a name="module_YQL_UDF_MODULE"></a>
The extension module for YQL with C++ UDF (User Defined Function YQL)

https://yql.yandex-team.ru/docs/yt/udf/cpp/

###### Module [YQL\_UDF\_MODULE\_CONTRIB][]: UDF\_BASE <a name="module_YQL_UDF_MODULE_CONTRIB"></a>
Not documented yet.

###### Module [YQL\_UDF\_TEST][]([name]) <a name="module_YQL_UDF_TEST"></a>
The module to test YQL C++ UDF.

Documentation: https://yql.yandex-team.ru/docs/yt/libraries/testing/
Documentation about the Arcadia test system: https://wiki.yandex-team.ru/yatool/test/

###### Module [YQL\_UDF\_TEST\_CONTRIB][]: PY3TEST\_BIN <a name="module_YQL_UDF_TEST_CONTRIB"></a>
Not documented yet.

###### Module [YQL\_UDF\_YDB\_MODULE][]: UDF\_BASE <a name="module_YQL_UDF_YDB_MODULE"></a>
Not documented yet.

###### Module [YQL\_UDF\_YDB\_TEST][]: PY3TEST\_BIN <a name="module_YQL_UDF_YDB_TEST"></a>
Not documented yet.

###### Module [YT\_UNITTEST][]([name]) <a name="module_YT_UNITTEST"></a>
YT Unit test module based on library/cpp/testing/unittest with NYT::Initialize hook

###### Module [Y\_BENCHMARK][]([benchmarkname]) <a name="module_Y_BENCHMARK"></a>
Benchmark test based on the library/cpp/testing/benchmark.

For more details see: https://wiki.yandex-team.ru/yatool/test/#zapuskbenchmark

## Macros <a name="macros"></a>

###### Macro [ACCELEO][](XSD{input}[], MTL{input}[], MTL\_ROOT="${MODDIR}", LANG{input}[], OUT{output}[], OUT\_NOAUTO{output}[], OUTPUT\_INCLUDES[], DEBUG?"stdout2stderr":"stderr2stdout") <a name="macro_ACCELEO"></a>
Not documented yet.

###### Macro [ADDINCL][]([FOR <lang>][GLOBAL dir]\* dirlist)  _# builtin_ <a name="macro_ADDINCL"></a>
The macro adds the directories to include/import search path to compilation flags of the current project.
By default settings apply to C/C++ compilation namely sets -I<library path> flag, use FOR argument to change target command.
@params:
`FOR <lang>` - adds inclues/import serach path for othe language. E.g. `FOR proto` adds import search path for .proto files processing.
`GLOBAL` - extends the search for headers (-I) on the dependent projects.

###### Macro [ADDINCLSELF][]() <a name="macro_ADDINCLSELF"></a>
The macro adds the -I<project source path> flag to the source compilation flags of the current project.

###### Macro [ADD\_CHECK][] <a name="macro_ADD_CHECK"></a>
Not documented yet.

###### Macro [ADD\_CHECK\_PY\_IMPORTS][] <a name="macro_ADD_CHECK_PY_IMPORTS"></a>
Not documented yet.

###### Macro [ADD\_CLANG\_TIDY][]() <a name="macro_ADD_CLANG_TIDY"></a>
Not documented yet.

###### Macro [ADD\_COMPILABLE\_TRANSLATE][](Dict Name Options...) <a name="macro_ADD_COMPILABLE_TRANSLATE"></a>
Generate translation dictionary code to transdict.LOWER(Name).cpp that will than be compiled into library

###### Macro [ADD\_COMPILABLE\_TRANSLIT][](TranslitTable NGrams Name Options...) <a name="macro_ADD_COMPILABLE_TRANSLIT"></a>
Generate transliteration dictionary code
This will emit both translit, untranslit and ngrams table codes those will be than further compiled into library

###### Macro [ADD\_DLLS\_TO\_JAR][]() <a name="macro_ADD_DLLS_TO_JAR"></a>
Not documented yet.

###### Macro [ADD\_LINTER\_CHECK][](CheckName, Linter, DEPENDS[], EXCLUDE[], FILES[], CONFIGS[]) <a name="macro_ADD_LINTER_CHECK"></a>
Not documented yet.

###### Macro [ADD\_PYTEST\_BIN][] <a name="macro_ADD_PYTEST_BIN"></a>
Not documented yet.

###### Macro [ADD\_YTEST][] <a name="macro_ADD_YTEST"></a>
Not documented yet.

###### Macro [ALLOCATOR][](Alloc)  _# Default: LF_ <a name="macro_ALLOCATOR"></a>
Set memory allocator implementation for the PROGRAM()/DLL() module.
This may only be specified for programs and dlls, use in other modules leads to configuration errors.

Available allocators are: "LF", "LF\_YT", "LF\_DBG", "YT", "J", "B", "BM", "C", "TCMALLOC", "GOOGLE", "LOCKLESS", "SYSTEM", "FAKE", "MIM", "MIM\_SDC", "HU", "PROFILED\_HU", "THREAD\_PROFILED\_HU".
  - LF - lfalloc (https://github.com/yandex/yatool/tree/main/library/cpp/lfalloc)
  - LF\_YT -  Allocator selection for YT (https://github.com/yandex/yatool/tree/main/library/cpp/lfalloc/yt/ya.make)
  - LF\_DBG -  Debug allocator selection (https://github.com/yandex/yatool/tree/main/library/cpp/lfalloc/dbg/ya.make)
  - YT - The YTAlloc allocator (https://github.com/yandex/yatool/tree/main/library/cpp/ytalloc/impl/ya.make)
  - J - The JEMalloc allocator (https://github.com/yandex/yatool/tree/main/library/malloc/jemalloc)
  - B - The balloc allocator named Pyotr Popov and Anton Samokhvalov
      - Discussion: https://ironpeter.at.yandex-team.ru/replies.xml?item\_no=126
      - Code: https://github.com/yandex/yatool/tree/main/library/cpp/balloc
  - BM - The balloc for market (agri@ commits from july 2018 till November 2018 saved)
  - C - Like B, but can be disabled for each thread to LF or SYSTEM one (B can be disabled only to SYSTEM)
  - MIM -  Microsoft's mimalloc (actual version) (https://github.com/yandex/yatool/tree/main/library/malloc/mimalloc)
  - MIM\_SDC - Microsoft's mimalloc patched by SDC (https://github.com/yandex/yatool/tree/main/library/malloc/mimalloc\_sdc)
  - TCMALLOC -  Google TCMalloc (actual version) (https://github.com/yandex/yatool/tree/main/library/malloc/tcmalloc)
  - GOOGLE -  Google TCMalloc (https://github.com/yandex/yatool/tree/main/library/malloc/galloc)
  - LOCKLESS - Allocator based upon lockless queues (https://github.com/yandex/yatool/tree/main/library/malloc/lockless)
  - SYSTEM - Use target system allocator
  - FAKE - Don't link with any allocator
  - HU - Huge page allocator by @gulin.
  - PROFILED\_HU - patched HU. It is a bit slower but has metrics of memory consumption.
  - THREAD\_PROFILED\_HU - patched (special for market) HU. It is a bit slower but has metrics of memory consumption.

More about allocators in Arcadia: https://wiki.yandex-team.ru/arcadia/allocators/

###### Macro [ALLOCATOR\_IMPL][]() <a name="macro_ALLOCATOR_IMPL"></a>
Not documented yet.

###### Macro [ALL\_PYTEST\_SRCS][]([RECURSIVE] [Dirs...]) <a name="macro_ALL_PYTEST_SRCS"></a>
Puts all .py-files from given Dirs (relative to projects') into TEST\_SRCS of the current module.
If Dirs is omitted project directory is used

`RECURSIVE` makes lookup recursive with respect to Dirs
`ONLY\_TEST\_FILES` includes only files `test\_\*.py` and `\*\_test.py`, others are normally subject to `PY\_SRCS`

Note: Only one such macro per module is allowed
Note: Macro is designed to reject any ya.make files in Dirs except current one

@see [TEST\_SRCS()](#macro\_TEST\_SRCS)

###### Macro [ALL\_PY\_SRCS][]([RECURSIVE] [NO\_TEST\_FILES] { | TOP\_LEVEL | NAMESPACE ns} [Dirs...]) <a name="macro_ALL_PY_SRCS"></a>
Puts all .py-files from given Dirs (relative to projects') into PY\_SRCS of the current module.
If Dirs is ommitted project directory is used

`RECURSIVE` makes lookup recursive with resprect to Dirs
`NO\_TEST\_FILES` excludes files `test\_\*.py` and `\*\_test.py` those are normally subject to `TEST\_SRCS`
`TOP\_LEVEL` and `NAMESPACE` are forwarded to `PY\_SRCS`

Note: Only one such macro per module is allowed
Note: Macro is designed to reject any ya.make files in Dirs except current one

@see [PY\_SRCS()](#macro\_PY\_SRCS)

###### Macro [ALL\_RESOURCE\_FILES][](Ext [PREFIX {prefix}] [STRIP {strip}] Dirs...) <a name="macro_ALL_RESOURCE_FILES"></a>
This macro collects all files with extension `Ext` and
Passes them to `RESOURCE\_FILES` macro as relative to current directory

`PREFIX` and `STRIP` have the same meaning as in `ROURCES\_FILES`, both are applied over moddir-relative paths

Note: This macro can be used multiple times per ya.make, but only once for each Ext value
Note: Wildcards are not allowed neither as Ext nor in Dirs

###### Macro [ALL\_RESOURCE\_FILES\_FROM\_DIRS][]([PREFIX {prefix}] [STRIP {strip}] Dirs...) <a name="macro_ALL_RESOURCE_FILES_FROM_DIRS"></a>
This macro collects all files non-recursively from listed Dirs and
Passes them to `RESOURCE\_FILES` macro as relative to current directory
The macro is usefull if literally all files are needed because `ALL\_RESOURCE\_FILES` requires extension to be specified

`PREFIX` and `STRIP` have the same meaning as in `ROURCES\_FILES`, both are applied over moddir-relative paths

Note: This macro can be used only once per ya.make
Note: Wildcards are not allowed neither as Ext nor in Dirs

###### Macro [ALL\_SRCS][]([GLOBAL] filenames...) <a name="macro_ALL_SRCS"></a>
Make all source files listed as GLOBAL or not depending on the keyword GLOBAL
Call to ALL\_SRCS macro is equivalent to call to GLOBAL\_SRCS macro when GLOBAL keyword is specified
as the first argument and is equivalent to call to SRCS macro otherwise.

@example:

    LIBRARY()
        SET(MAKE_IT_GLOBAL GLOBAL)
        ALL_SRCS(${MAKE_IT_GLOBAL} foo.cpp bar.cpp)
    END()

@see: [GLOBAL\_SRCS()](#macro\_GLOBAL\_SRCS), [SRCS()](#macro\_SRCS)

###### Macro [ANNOTATION\_PROCESSOR][](processors...) <a name="macro_ANNOTATION_PROCESSOR"></a>
The macro is in development.
Used to specify annotation processors to build JAVA\_PROGRAM() and JAVA\_LIBRARY().

###### Macro [ARCHIVE][](archive\_name [DONT\_COMPRESS] files...) <a name="macro_ARCHIVE"></a>
Add arbitrary data to a modules. Unlike RESOURCE macro the result should be futher processed by othet macros in the module.

Example: https://wiki.yandex-team.ru/yatool/howtowriteyamakefiles/#a1ispolzujjtekomanduarchive

###### Macro [ARCHIVE\_ASM][](NAME archive\_name files...) <a name="macro_ARCHIVE_ASM"></a>
Similar to the macro ARCHIVE, but:
1. works faster and it is better to use for large files.
2. Different syntax (see examples in codesearch or users/pg/tests/archive\_test)

###### Macro [ARCHIVE\_BY\_KEYS][](archive\_name key [DONT\_COMPRESS] files...) <a name="macro_ARCHIVE_BY_KEYS"></a>
Add arbitrary data to a module be accessible by specified key.
Unlike RESOURCE macro the result should be futher processed by othet macros in the module.

Example: https://wiki.yandex-team.ru/yatool/howtowriteyamakefiles/#a1ispolzujjtekomanduarchive

###### Macro [ASM\_PREINCLUDE][](AsmFiles...) <a name="macro_ASM_PREINCLUDE"></a>
Supply additional .asm files to all assembler calls within a module

###### Macro [ASSERT][] <a name="macro_ASSERT"></a>
Not documented yet.

###### Macro [BENCHMARK\_OPTS][](opt1 [opt2...]) <a name="macro_BENCHMARK_OPTS"></a>
Allows to specify extra args to benchmark binary.
Supported for G\_BENCHMARK and Y\_BENCHMARK

@example:
    BENCHMARK\_OPTS (
        --benchmark\_min\_time=0
    )

Documentation: https://docs.yandex-team.ru/ya-make/manual/tests/benchmark

###### Macro [BISON\_FLAGS][](<flags>) <a name="macro_BISON_FLAGS"></a>
Set flags for Bison tool invocations.

###### Macro [BISON\_GEN\_C][]() <a name="macro_BISON_GEN_C"></a>
Generate C from Bison grammar. The C++ is generated by default.

###### Macro [BISON\_GEN\_CPP][]() <a name="macro_BISON_GEN_CPP"></a>
Generate C++ from Bison grammar. This is current default.

###### Macro [BISON\_HEADER][](<header\_suffix>) <a name="macro_BISON_HEADER"></a>
Use SUFF (including extension) to name Bison defines header file. The default is just `.h`.

###### Macro [BISON\_NO\_HEADER][]() <a name="macro_BISON_NO_HEADER"></a>
Don't emit Bison defines header file.

###### Macro [BPF][](Input Output Opts...) <a name="macro_BPF"></a>
Emit eBPF bytecode from .c file.
Note: Output name is used as is, no extension added.

###### Macro [BPF\_STATIC][](Input Output Opts...) <a name="macro_BPF_STATIC"></a>
Emit eBPF bytecode from .c file.
Note: Output name is used as is, no extension added.

###### Macro [BUILDWITH\_CYTHON\_C][](Src Options...) <a name="macro_BUILDWITH_CYTHON_C"></a>
Generates .c file from .pyx.

###### Macro [BUILDWITH\_CYTHON\_CPP][](Src Options...) <a name="macro_BUILDWITH_CYTHON_CPP"></a>
Generates .cpp file from .pyx.

###### Macro [BUILDWITH\_RAGEL6][](Src Options...) <a name="macro_BUILDWITH_RAGEL6"></a>
Compile .rl file using Ragel6.

###### Macro [BUILD\_CATBOOST][](cbmodel cbname) <a name="macro_BUILD_CATBOOST"></a>
Generate catboost model and access code.
cbmodel - CatBoost model file name (\*.cmb).
cbname - name for a variable (of NCatboostCalcer::TCatboostCalcer type) to be available in CPP code.
CatBoost specific macro.

###### Macro [BUILD\_ONLY\_IF][]([FATAL\_ERROR|STRICT] variables)  _# builtin_ <a name="macro_BUILD_ONLY_IF"></a>
Print warning if all variables are false. For example, BUILD\_ONLY\_IF(LINUX WIN32)
In STRICT mode disables build of all modules and RECURSES of the ya.make.
FATAL\_ERROR issues configure error and enables STRICT mode

###### Macro [BUILD\_YDL\_DESC][](Input Symbol Output) <a name="macro_BUILD_YDL_DESC"></a>
Generate a descriptor for a Symbol located in a ydl module Input, and put it to the file Output.

@example:

    PACKAGE()
        BUILD_YDL_DESC(../types.ydl Event Event.ydld)
    END()

This will parse file ../types.ydl, generate a descriptor for a symbol Event defined in the said file, and put the descriptor to the Event.ydld.

###### Macro [BUNDLE][](<Dir [NAME Name]>...) <a name="macro_BUNDLE"></a>
Brings build artefact from module Dir under optional Name to the current module (e.g. UNION)
If NAME is not specified, the name of the Dir's build artefact will be preserved
It makes little sense to specify BUNDLE on non-final targets and so this may stop working without prior notice.
Bundle on multimodule will select final target among multimodule variants and will fail if there are none or more than one.

###### Macro [CFLAGS][]([GLOBAL compiler\_flag]\* compiler\_flags) <a name="macro_CFLAGS"></a>
Add the specified flags to the compilation command of C and C++ files.
@params: GLOBAL - Propagates these flags to dependent projects
Note: remember about the incompatibility flags for clang and cl (to set flags specifically for cl.exe use MSVC\_FLAGS).

###### Macro [CGO\_CFLAGS][](Flags...) <a name="macro_CGO_CFLAGS"></a>
Compiler flags specific to CGO compilation

###### Macro [CGO\_LDFLAGS][](Files...) <a name="macro_CGO_LDFLAGS"></a>
Linker flags specific to CGO linking

###### Macro [CGO\_SRCS][](Files...) <a name="macro_CGO_SRCS"></a>
.go sources to be built with CGO

###### Macro [CHECK\_ALLOWED\_PATH][] <a name="macro_CHECK_ALLOWED_PATH"></a>
Not documented yet.

###### Macro [CHECK\_CONTRIB\_CREDITS][] <a name="macro_CHECK_CONTRIB_CREDITS"></a>
Not documented yet.

###### Macro [CHECK\_DEPENDENT\_DIRS][](DENY|ALLOW\_ONLY ([ALL|PEERDIRS|GLOB] dir)...) <a name="macro_CHECK_DEPENDENT_DIRS"></a>
Specify project transitive dependencies constraints.

@params:
 1. DENY: current module can not depend on module from any specified directory neither directly nor transitively.
 2. ALLOW\_ONLY: current module can not depend on module from a dir not specified in the directory list neither directly nor transitively.
 3. ALL: directory constraints following after this modifier are applied to both transitive PEERDIR dependencies and tool dependencies.
 4. PEERDIRS: directory constraints following after this modifier are applied to transitive PEERDIR dependencies only.
 5. GLOB: next directory constraint is an ANT glob pattern.
 6. EXCEPT: next constraint is an exception for the rest of other rules.

Directory constraints added before either ALL or PEERDIRS modifier is used are treated as ALL directory constraints.

Note: Can be used multiple times on the same module all specified constraints will be checked.
All macro invocation for the same module must use same constraints type (DENY or ALLOW\_ONLY)

###### Macro [CHECK\_JAVA\_DEPS][](<yes|no|strict>) <a name="macro_CHECK_JAVA_DEPS"></a>
Check for different classes with duplicate name in classpath.

Documentation: https://wiki.yandex-team.ru/yatool/test/

###### Macro [CLANG\_EMIT\_AST\_CXX][](Input Output Opts...) <a name="macro_CLANG_EMIT_AST_CXX"></a>
Emit Clang AST from .cpp file. CXXFLAGS and LLVM\_OPTS are passed in, while CFLAGS and C\_FLAGS\_PLATFORM are not.
Note: Output name is used as is, no extension added.

###### Macro [CLANG\_EMIT\_AST\_CXX\_RUN\_TOOL][](Tool Args... [SOURCES ...] [OPTS ...] [IN ...] [IN\_NOPARSE ...] [TOOL ...] [OUTPUT\_INCLUDES ...] [INDUCED\_DEPS ...] [IN\_DEPS ...] [STDOUT out-file-name] [STDOUT\_NOAUTO out-file-name] [CWD cwd]) <a name="macro_CLANG_EMIT_AST_CXX_RUN_TOOL"></a>
Emit Clang ASTs from .cpp files listed in SOURCES parameter (CXXFLAGS and LLVM\_OPTS are passed in, while CFLAGS and C\_FLAGS\_PLATFORM are not) and run tool Tool with Args... .
OPTS[] parameter is used to pass additional flags to clang. Parameters other than OPTS[] and SOURCES[] are used for runnig a generator (Tool):
- Tool - path to the directory of the tool
- Args... - Tool's arguments
- IN[] - input files required for running the Tool
- IN\_NOPARSE[] - input files required for running the Tool, but these files are not parsed for dependencies
- TOOL[] - list of directories of axiliary tools used by Tool
- OUTPUT\_INCLUDES[] - includes of the output files which are needed to "build" them
- STDOUT - redirect stdout of the Tool to the output file
- STDOUT\_NOAUTO - redirect stdout of the Tool to the output file, but do not chain this file automatically to the processing queue
- CWD - path to the working directory of the Tool
Note: Generated AST files generated into BINDIR according to corresponding .cpp file names listed in SOURCES parameter.

###### Macro [CLEAN\_TEXTREL][]() <a name="macro_CLEAN_TEXTREL"></a>
Not documented yet.

###### Macro [CMAKE\_EXPORTED\_TARGET\_NAME][](Name) <a name="macro_CMAKE_EXPORTED_TARGET_NAME"></a>
Forces to use the name given as cmake target name without changing the name of output artefact.
This macro should be used to resolve target name conflicts in  exported cmake project when
changing module name is not applicable. For example both CUDA and non-CUDA py modules for
catboost should have same name lib\_catboost.so and both of them are defined as PY\_ANY\_MODULE(\_catboost).
adding CMAKE\_EXPORTED\_TARGET\_NAME(\_catboost\_non\_cuda) to the non CUDA module ya.make file
changes exported cmake target name but preserve generated artefact file name.

###### Macro [COLLECT\_FRONTEND\_FILES][](Varname, Dir) <a name="macro_COLLECT_FRONTEND_FILES"></a>
Recursively collect files with typical frontend extensions from Dir and save the result into variable Varname

###### Macro [COLLECT\_GO\_SWAGGER\_FILES][](Varname, Dir) <a name="macro_COLLECT_GO_SWAGGER_FILES"></a>
Recursively collect files for swagger config creation

###### Macro [COLLECT\_JINJA\_TEMPLATES][](varname path) <a name="macro_COLLECT_JINJA_TEMPLATES"></a>
This macro collects all jinja and yaml files in the directory specified by second argument and
stores result in the variable with mane specified by first parameter.

###### Macro [COMPILE\_C\_AS\_CXX][]() <a name="macro_COMPILE_C_AS_CXX"></a>
Compile .c files as .cpp ones within a module.

###### Macro [COMPILE\_LUA][](Src, [NAME <import\_name>]) <a name="macro_COMPILE_LUA"></a>
Compile LUA source file to object code using LUA 2.0
Optionally override import name which is by default reflects Src name

###### Macro [COMPILE\_LUA\_21][](Src, [NAME <import\_name>]) <a name="macro_COMPILE_LUA_21"></a>
Compile LUA source file to object code using LUA 2.1
Optionally override import name which is by default reflects Src name

###### Macro [COMPILE\_LUA\_OPENRESTY][](Src, [NAME <import\_name>]) <a name="macro_COMPILE_LUA_OPENRESTY"></a>
Compile LUA source file to object code using OpenResty LUA 2.1
Optionally override import name which is by default reflects Src name

###### Macro [COMPILE\_SWIFT\_MODULE][](SRCS{input}[], BRIDGE\_HEADER{input}="", Flags...) <a name="macro_COMPILE_SWIFT_MODULE"></a>
Not documented yet.

###### Macro [CONFIGURE\_FILE][](from to) <a name="macro_CONFIGURE_FILE"></a>
Copy file with the replacement of configuration variables in form of @ANY\_CONF\_VAR@ with their values.
The values are collected during configure stage, while replacement itself happens during build stage.
Used implicitly for .in-files processing.

###### Macro [CONFTEST\_LOAD\_POLICY\_LOCAL][]() <a name="macro_CONFTEST_LOAD_POLICY_LOCAL"></a>
Loads conftest.py files in a way that pytest does it

###### Macro [CONLYFLAGS][]([GLOBAL compiler\_flag]\* compiler\_flags) <a name="macro_CONLYFLAGS"></a>
Add the specified flags to the compilation command of .c (but not .cpp) files.
@params: GLOBAL - Distributes these flags on dependent projects

###### Macro [COPY][] <a name="macro_COPY"></a>
Not documented yet.

###### Macro [COPY\_FILE][](File Destination [AUTO] [OUTPUT\_INCLUDES Deps...]) <a name="macro_COPY_FILE"></a>
Copy file to build root. It is possible to change both location and the name.

Parameters:
- File - Source file name.
- Destination - Output file name.
- AUTO - Consider copied file for further processing automatically.
- OUTPUT\_INCLUDES output\_includes... - Output file dependencies.
- INDUCED\_DEPS $VARs... - Dependencies for generated files. Unlike `OUTPUT\_INCLUDES` these may target files further in processing chain.
                          In order to do so VAR should be filled by PREPARE\_INDUCED\_DEPS macro, stating target files (by type)
                          and set of dependencies

The file will be just copied if AUTO boolean parameter is not specified. You should explicitly
mention it in SRCS under new name (or specify AUTO boolean parameter) for further processing.

###### Macro [COPY\_FILE\_WITH\_CONTEXT][](FILE DEST [AUTO] [OUTPUT\_INCLUDES DEPS...]) <a name="macro_COPY_FILE_WITH_CONTEXT"></a>
Copy file to build root the same way as it is done for COPY\_FILE, but also
propagates the context of the source file.

###### Macro [CPP\_ADDINCL][](Dirs...) <a name="macro_CPP_ADDINCL"></a>
Not documented yet.

###### Macro [CPP\_ENUMS\_SERIALIZATION][] <a name="macro_CPP_ENUMS_SERIALIZATION"></a>
Not documented yet.

###### Macro [CPP\_PROTOLIBS\_DEBUG\_INFO][]() <a name="macro_CPP_PROTOLIBS_DEBUG_INFO"></a>
Eqvivalent to NO\_DEBUG\_INFO() macro if the flag CPP\_PROTO\_NO\_DBGINFO=yes

###### Macro [CPP\_PROTO\_PLUGIN][](Name Tool Suf [DEPS <Dependencies>] [EXTRA\_OUT\_FLAG <ExtraOutFlag>]) <a name="macro_CPP_PROTO_PLUGIN"></a>
Define protoc plugin for C++ with given Name that emits code into 1 extra output
using Tool. Extra dependencies are passed via DEPS.

###### Macro [CPP\_PROTO\_PLUGIN0][](Name Tool [DEPS <Dependencies>] [EXTRA\_OUT\_FLAG <ExtraOutFlag>]) <a name="macro_CPP_PROTO_PLUGIN0"></a>
Define protoc plugin for C++ with given Name that emits code into regular outputs
using Tool. Extra dependencies are passed via DEPS.

###### Macro [CPP\_PROTO\_PLUGIN2][](Name Tool Suf1 Suf2 [DEPS <Dependencies>] [EXTRA\_OUT\_FLAG <ExtraOutFlag>]) <a name="macro_CPP_PROTO_PLUGIN2"></a>
Define protoc plugin for C++ with given Name that emits code into 2 extra outputs
using Tool. Extra dependencies are passed via DEPS.

###### Macro [CREATE\_BUILDINFO\_FOR][](GenHdr) <a name="macro_CREATE_BUILDINFO_FOR"></a>
Creates header file to access some information about build specified via configuration variables.
Unlike CREATE\_SVNVERSION\_FOR() it doesn't take revion information from VCS, it uses revision and SandboxTaskId passed via -D options to ya make

###### Macro [CREATE\_INIT\_PY\_STRUCTURE][] <a name="macro_CREATE_INIT_PY_STRUCTURE"></a>
Not documented yet.

###### Macro [CREDITS\_DISCLAIMER][] <a name="macro_CREDITS_DISCLAIMER"></a>
Not documented yet.

###### Macro [CTEMPLATE\_VARNAMES][](File) <a name="macro_CTEMPLATE_VARNAMES"></a>
Generate File.varnames.h using contrib/libs/ctemplate/make\_tpl\_varnames\_h

Documentation: https://github.com/yandex/yatool/tree/main/contrib/libs/ctemplate/README.md

###### Macro [CUDA\_NVCC\_FLAGS][](compiler flags) <a name="macro_CUDA_NVCC_FLAGS"></a>
Add the specified flags to the compile line .cu-files.

###### Macro [CUSTOM\_CONTRIB\_TYPESCRIPT][](P) <a name="macro_CUSTOM_CONTRIB_TYPESCRIPT"></a>
Not documented yet.

###### Macro [CUSTOM\_LINK\_STEP\_SCRIPT][](name) <a name="macro_CUSTOM_LINK_STEP_SCRIPT"></a>
Specifies name of a script for custom link step. The scripts
should be placed in the build/scripts directory and are subject to
review by devtools@.

###### Macro [CXXFLAGS][](compiler\_flags) <a name="macro_CXXFLAGS"></a>
Add the specified flags to the compilation command of .cpp (but not .c) files.

###### Macro [CYTHON\_FLAGS][](compiler\_flags) <a name="macro_CYTHON_FLAGS"></a>
Add the specified flags to the compilation command of .pyx files.

###### Macro [DARWIN\_SIGNED\_RESOURCE][](Resource, Relpath) <a name="macro_DARWIN_SIGNED_RESOURCE"></a>
Not documented yet.

###### Macro [DARWIN\_STRINGS\_RESOURCE][](Resource, Relpath) <a name="macro_DARWIN_STRINGS_RESOURCE"></a>
Not documented yet.

###### Macro [DATA][]([path...]) <a name="macro_DATA"></a>
Specifies the path to the data necessary test.
Valid values are: arcadia/<path> , arcadia\_tests\_data/<path> and sbr://<resource\_id>.
In the latter case resource will be brought to the working directory of the test before it is started

Used only inside TEST modules.

Documentation: https://wiki.yandex-team.ru/yatool/test/#dannyeizrepozitorija

###### Macro [DATA\_FILES][]([path...]) <a name="macro_DATA_FILES"></a>
Specifies the path to the arcadia source data necessary test.
Used only inside TEST modules.

Documentation: https://wiki.yandex-team.ru/yatool/test/#dannyeizrepozitorija

###### Macro [DEB\_VERSION][](File) <a name="macro_DEB_VERSION"></a>
Creates a header file DebianVersion.h define the DEBIAN\_VERSION taken from the File.

###### Macro [DECIMAL\_MD5\_LOWER\_32\_BITS][](<fileName> [FUNCNAME funcName] [inputs...]) <a name="macro_DECIMAL_MD5_LOWER_32_BITS"></a>
Generates .cpp file <fileName> with one defined function 'const char\* <funcName>() { return "<calculated\_md5\_hash>"; }'.
<calculated\_md5\_hash> will be md5 hash for all inputs passed to this macro.

###### Macro [DECLARE\_EXTERNAL\_HOST\_RESOURCES\_BUNDLE][](name sbr:id FOR platform1 sbr:id FOR platform2...)  _#builtin_ <a name="macro_DECLARE_EXTERNAL_HOST_RESOURCES_BUNDLE"></a>
Associate name with sbr-id on platform.

Ask devtools@yandex-team.ru if you need more information

###### Macro [DECLARE\_EXTERNAL\_HOST\_RESOURCES\_BUNDLE\_BY\_JSON][](VarName, FileName [, FriendlyResourceName]) <a name="macro_DECLARE_EXTERNAL_HOST_RESOURCES_BUNDLE_BY_JSON"></a>
Associate 'Name' with a platform to resource uri mapping
File 'FileName' contains json with a 'canonized platform -> resource uri' mapping.
'FriendlyResourceName', if specified, is used in configuration error messages instead of VarName.
The mapping file format see in SET\_RESOURCE\_URI\_FROM\_JSON description.

###### Macro [DECLARE\_EXTERNAL\_HOST\_RESOURCES\_PACK][](RESOURCE\_NAME name sbr:id FOR platform1 sbr:id FOR platform2... RESOURCE\_NAME name1 sbr:id1 FOR platform1...)  _#builtin_ <a name="macro_DECLARE_EXTERNAL_HOST_RESOURCES_PACK"></a>
Associate name with sbr-id on platform.

Ask devtools@yandex-team.ru if you need more information

###### Macro [DECLARE\_EXTERNAL\_RESOURCE][](name sbr:id name1 sbr:id1...)  _#builtin_ <a name="macro_DECLARE_EXTERNAL_RESOURCE"></a>
Associate name with sbr-id.

Ask devtools@yandex-team.ru if you need more information

###### Macro [DECLARE\_EXTERNAL\_RESOURCE\_BY\_JSON][](VarName, FileName [, FriendlyResourceName]) <a name="macro_DECLARE_EXTERNAL_RESOURCE_BY_JSON"></a>
Associate 'Name' with a resource for the current target platform
File 'FileName' contains json with a 'canonized platform -> resource uri' mapping.
'FriendlyResourceName', if specified, is used in configuration error messages instead of VarName.
The mapping file format see in SET\_RESOURCE\_URI\_FROM\_JSON description.

###### Macro DECLARE\_IN\_DIR(var\_prefix files\_mask DIRS dirs [RECURSIVE] [EXCLUDES excludes] [SRCDIR srcdir]) <a name="macro_DECLARE_IN_DIRS"></a>
This macro allow passing content of directories to macros like `RUN\_PROGRAM` and `RUN\_PYTHON3` as IN parameter.

The content is matched by following rules:
- The files are looked in <srcdir>. The srcdir is relative to module directory and defaulted to module directory.
- Inside <srcdir> files are looked in all <dirs>, recursively or not depending on RECURSIVE parameter.
- Files are matched by file\_mask which may contain \* or ?.
- <excludes> are then applied over matched files. Excludes are regular globs including recursive parts support.

Taking `var\_prefix` macro declared 4 variables:
- <var\_prefix>\_FILES - the file list matched by the macro using rules above. This variable can be passed to `IN` parameter of `RUN\_PROGRAM` and alikes.
                       Also it may be passed escaped as argument to tool/script. See example below.
- <var\_prefix>\_PATTERNS - the glob patterns used for match.
- <var\_prefix>\_EXCLUDES - exclude patterns from EXCLUDES argument and ones to exclude ya.make and a.yaml
- <var\_prefix>\_SRCDIR - value of SRCDIR argument

Parameters:
- var\_prefix - Mandatory prefix of variables the macro declares
- file\_mask - Mandatory glob-like mask for files
  file\_mask should not conatain '\*\*'
- DIRS dirs - Mandatory list of dirs relative to srcdir or current one in which files should be looked
  Dirs cannot contain ${ARCADIA\_ROOT} (and other similar vars), '..', '\*' or '?'.
- RECURSIVE - Optional request to lookup dirs recursively. Default is non-recursive lookup
- EXCLUDES excludes - Optional list of globs to exclude from match.
- SRCDIR srcdir - Optional directory (relative to current one) to apply globs. Default is the current dir.
  We strongly discourage this, but srcdir may contain '..' or start from ${ARCADIA\_ROOT} for root-relative addressing.
  scrdir cannot contain any of '\*' or '?'

Examples:
```
DECLARE_IN_DIRS(TXT *.txt DIRS . EXCLUDE .*.txt **/.*.txt)
# file list requires escaping as argument
RUN_PYTHON3(concat.py \${TXT_FILES} IN ${TXT_FILES} STDOUT concatenated.txt)
```

```
DECLARE_IN_DIRS(ALL_TXT *.txt SRCDIR txt RECURSIVE DIRS design rules EXCLUDE all.txt)
RUN_PYTHON3(concat_all.py --dirs ${MODDIR}/${ALL_TXT_SRCDIR} --pattern ${ALL_TXT_PATTERNS} --exclude ${ALL_TXT_EXCLUDES} IN ${ALL_TXT_FILES} STDOUT concatenated.txt)
```

```
DECLARE_IN_DIRS(D_TXT *.txt SRCDIR txt/design EXCLUDE all.txt DIRS .)
DECLARE_IN_DIRS(R_TXT *.txt SRCDIR txt/rules DIRS .)
RUN_PYTHON3(concat_all.py --dirs ${MODDIR}/${D_TXT_SRCDIR} ${MODDIR}/${R_TXT_SRCDIR} --patterns ${D_TXT_PATTERNS} ${R_TXT_PATTERNS} --exclude ${D_TXT_EXCLUDES} IN ${D_TXT_FILES} ${R_TXT_FILES} STDOUT concatenated.txt)
```

Notes:
1. All 'ya.make' and 'a.yaml' files are excluded from match.
2. Matched files are never parsed for dependencies even though they shall be passed to IN, not to IN\_NOPARSE.
3. The list of files expanded late and will not work in macros like SRCS. This macro only meant for use with generating macros like RUN\_PROGRAM processing entire matching list with one command.
4. We support extended file mask syntax for multiple masks like "(\*.cpp|\*.h)". However, this will be preserved in <var\_prefix>\_PATTERNS variable and so tool/script either should support such syntax or
   or should not rely on value of the variable for actual matching.
5. There is known issue with empty match and escaped substitution like `concat.py \${TXT\_FILES}`. It may result in weird errors and can be workarounded by extra argument like `concat.py - \${TXT\_FILES}`
6. EXCLUDES work differently with SRCDIR is specified. Use discriminating tail of SRCDIR in order to match exact files non-recursively.
   E.g. if SRCDIR is a/b/zz and EXCLUDE is \*.x the exclude will work recursively on all matches including zz's child dierctories. To limit match to zz's level use EXCLUDE zz/\*.x instead.
6. Parameters of macro are somewhat validated and we may add extra checks in the fulture including protection over too broad match.

###### Macro [DEFAULT][](varname value)  _#builtin_ <a name="macro_DEFAULT"></a>
Sets varname to value if value is not set yet

###### Macro [DEFAULT\_JAVA\_SRCS\_LAYOUT][]() <a name="macro_DEFAULT_JAVA_SRCS_LAYOUT"></a>
DEFAULT\_JAVA\_SRCS\_LAYOUT() declare all source files can be find at maven/gradle standard path src/main/java \*\*/\*.java
and all resources an be find at maven/gradle standard path src/main/resources \*\*/\*

###### Macro [DEFAULT\_JDK\_VERSION][](Version) <a name="macro_DEFAULT_JDK_VERSION"></a>
Specify JDK version for module, can be overridden by setting the JDK\_VERSION variable

###### Macro [DEFAULT\_JUNIT\_JAVA\_SRCS\_LAYOUT][]() <a name="macro_DEFAULT_JUNIT_JAVA_SRCS_LAYOUT"></a>
DEFAULT\_JUNIT\_JAVA\_SRCS\_LAYOUT() declare all test source files can be find at maven/gradle standard path src/test/java \*\*/\*.java
and all resources can be find at maven/gradle standard path src/test/resources \*\*/\*

###### Macro [DEPENDENCY\_MANAGEMENT][](path/to/lib1 path/to/lib2 ...) <a name="macro_DEPENDENCY_MANAGEMENT"></a>
Lock version of the library from the contrib/java at some point, so that all unversioned PEERDIRs to this library refer to the specified version.

For example, if the module has PEERDIR (contrib/java/junit/junit), and
  1. specifies DEPENDENCY\_MANAGEMENT(contrib/java/junit/junit/4.12),
     the PEERDIR is automatically replaced by contrib/java/junit/junit/4.12;
  2. doesn't specify DEPENDENCY\_MANAGEMENT, PEERDIR automatically replaced
     with the default from contrib/java/junit/junit/ya.make.
     These defaults are always there and are supported by maven-import, which puts
     there the maximum version available in contrib/java.

The property is transitive. That is, if module A PEERDIRs module B, and B has PEERDIR(contrib/java/junit/junit), and this junit was replaced by junit-4.12, then junit-4.12 will come to A through B.

If some module has both DEPENDENCY\_MANAGEMENT(contrib/java/junit/junit/4.12) and PERDIR(contrib/java/junit/junit/4.11), the PEERDIR wins.

Documentation: https://wiki.yandex-team.ru/yatool/java/

###### Macro [DEPENDS][](path1 [path2...]) _# builtin_ <a name="macro_DEPENDS"></a>
Buildable targets that should be brought to the test run. This dependency isonly used when tests run is requested. It will build the specified modules andbring them to the working directory of the test (in their Arcadia paths). Itis reasonable to specify only final targets her (like programs, DLLs orpackages). DEPENDS to UNION is the only exception: UNIONs aretransitively closed at DEPENDS bringing all dependencies to the test.

DEPENDS on multimodule will select and bring single final target. If more noneor more than one final target available in multimodule DEPENDS to it willproduce configuration error.

###### Macro [DIRECT\_DEPS\_ONLY][] <a name="macro_DIRECT_DEPS_ONLY"></a>
Add direct PEERDIR's only in java compile classpath

###### Macro [DISABLE][](varname)  _#builtin_ <a name="macro_DISABLE"></a>
Sets varname to 'no'

###### Macro [DISABLE\_DATA\_VALIDATION][]() <a name="macro_DISABLE_DATA_VALIDATION"></a>
Not documented yet.

###### Macro [DLL\_FOR][](path/to/lib [libname] [major\_ver [minor\_ver]] [EXPORTS symlist\_file])  _#builtin_ <a name="macro_DLL_FOR"></a>
DLL module definition based on specified LIBRARY

###### Macro [DOCS\_CONFIG][](path) <a name="macro_DOCS_CONFIG"></a>
Specify path to config file for DOCS multimodule if it differs from default path.
If used for [MKDOCS](#multimodule\_MKDOCS) multimodule the default path is "%%project\_directory%%/mkdocs.yml".
If used for [DOCS](#multimodule\_DOCS) multimodule the default path is "%%project\_directory%%/.yfm".
Path must be either Arcadia root relative.

@see: [DOCS](#multimodule\_DOCS)

###### Macro [DOCS\_COPY\_FILES][](FROM src\_dir [NAMESPCE dst\_dir] files...) <a name="macro_DOCS_COPY_FILES"></a>
Copy files from src\_dir to $BINDIR/dst\_dir

###### Macro [DOCS\_DIR][](path) <a name="macro_DOCS_DIR"></a>
Specify directory with source .md files for DOCS multimodule if it differs from project directory.
Path must be Arcadia root relative.

@see: [DOCS](#multimodule\_DOCS)

###### Macro [DOCS\_INCLUDE\_SOURCES][](path...) <a name="macro_DOCS_INCLUDE_SOURCES"></a>
Specify a list of paths to source code files which will be used as text includes in a documentation project.
Paths must be Arcadia root relative.

@see: [DOCS](#multimodule\_DOCS)

###### Macro [DOCS\_VARS][](variable1=value1 variable2=value2 ...) <a name="macro_DOCS_VARS"></a>
Specify a set of default values of template variables for DOCS multimodule.
There must be no spaces around "=". Values will be treated as strings.

@see: [DOCS](#multimodule\_DOCS)

###### Macro [DYNAMIC\_LIBRARY\_FROM][](Paths) <a name="macro_DYNAMIC_LIBRARY_FROM"></a>
Use specified libraries as sources of DLL

###### Macro IF(condition) .. [ELSE][]IF(other\_condition) .. ELSE() .. ENDIF()  _#builtin_ <a name="macro_ELSE"></a>
Apply macros if none of previous conditions hold

###### Macro IF(condition) .. [ELSEIF][](other\_condition) .. ELSE() .. ENDIF()  _#builtin_ <a name="macro_ELSEIF"></a>
Apply macros if other\_condition holds while none of previous conditions hold

###### Macro [EMBED\_JAVA\_VCS\_INFO][]() <a name="macro_EMBED_JAVA_VCS_INFO"></a>
Embed manifest with vcs info into `EXTERNAL\_JAVA\_LIBRARY`
By default this is disabled.

###### Macro [ENABLE][](varname)  _#builtin_ <a name="macro_ENABLE"></a>
Sets varname to 'yes'

###### Macro [ENABLE\_PREVIEW][]() <a name="macro_ENABLE_PREVIEW"></a>
Enable java preview features.

###### Macro [END][]()  _# builtin_ <a name="macro_END"></a>
The end of the module

###### Macro IF(condition) .. ELSEIF(other\_condition) .. ELSE() .. [ENDIF][]()  _#builtin_ <a name="macro_ENDIF"></a>
End of conditional construct

###### Macro [ENV][](key[=value]) <a name="macro_ENV"></a>
Sets env variable key to value (gets value from system env by default).

###### Macro [EVLOG\_CMD][](SRC) <a name="macro_EVLOG_CMD"></a>
Not documented yet.

###### Macro [EXCLUDE][] <a name="macro_EXCLUDE"></a>
EXCLUDE(prefixes)

Specifies which libraries should be excluded from the classpath.

###### Macro [EXCLUDE\_TAGS][](tags...)  _# builtin_ <a name="macro_EXCLUDE_TAGS"></a>
Instantiate from multimodule all variants except ones with tags listed

###### Macro [EXPLICIT\_DATA][]() <a name="macro_EXPLICIT_DATA"></a>
Not documented yet.

###### Macro [EXPLICIT\_OUTPUTS][](Files...) <a name="macro_EXPLICIT_OUTPUTS"></a>
Let UNION has only explicitly specified outputs listed in this macro
The list of files shall contain results of commands in this UNION.
Only these files will be outputs of the UNION. This allows to eliminate
intermediate files being result of the UNION

###### Macro [EXPORTS\_SCRIPT][](exports\_file) <a name="macro_EXPORTS_SCRIPT"></a>
Specify exports script within PROGRAM, DLL and DLL-derived modules.
This accepts 2 kind of files: .exports with <lang symbol> pairs and JSON-line .symlist files.
The other option use EXPORTS parameter of the DLL module itself.

@see: [DLL](#module\_DLL)

###### Macro [EXPORT\_ALL\_DYNAMIC\_SYMBOLS][]() <a name="macro_EXPORT_ALL_DYNAMIC_SYMBOLS"></a>
Export all non-hidden symbols as dynamic when linking a PROGRAM.

###### Macro [EXTERNAL\_JAR][] <a name="macro_EXTERNAL_JAR"></a>
Not documented yet.

###### Macro [EXTERNAL\_RESOURCE][](...)  _#builtin, deprecated_ <a name="macro_EXTERNAL_RESOURCE"></a>
Don't use this. Use RESOURCE\_LIBRARY or FROM\_SANDBOX instead

###### Macro [EXTRADIR][](...)  _#builtin, deprecated_ <a name="macro_EXTRADIR"></a>
Ignored

###### Macro [EXTRALIBS\_STATIC][](Libs...) <a name="macro_EXTRALIBS_STATIC"></a>
Add the specified external static libraries to the program link

###### Macro [FBS\_CMD][](SRC, SRCFLAGS...) <a name="macro_FBS_CMD"></a>
Not documented yet.

###### Macro [FBS\_NAMESPACE][](NAMESPACE, PATH...) <a name="macro_FBS_NAMESPACE"></a>
Not documented yet.

###### Macro [FBS\_TO\_PY2SRC][](OUT\_NAME, IN\_FBS\_FILES...) <a name="macro_FBS_TO_PY2SRC"></a>
Not documented yet.

###### Macro [FILES][] <a name="macro_FILES"></a>
Not documented yet.

###### Macro [FLATC\_FLAGS][](flags...) <a name="macro_FLATC_FLAGS"></a>
Add flags to flatc command line

###### Macro [FLAT\_JOIN\_SRCS\_GLOBAL][](Out Src...) <a name="macro_FLAT_JOIN_SRCS_GLOBAL"></a>
Join set of sources into single file named Out and send it for further processing as if it were listed as SRCS(GLOBAL Out).
This macro places all files into single file, so will work with any sources.
You should specify file name with the extension as Out. Further processing will be done according to this extension.

###### Macro [FLEX\_FLAGS][](<flags>) <a name="macro_FLEX_FLAGS"></a>
Set flags for Lex tool (flex) invocations.

###### Macro [FLEX\_GEN\_C][]() <a name="macro_FLEX_GEN_C"></a>
Generate C from Lex grammar. The C++ is generated by default.

###### Macro [FLEX\_GEN\_CPP][]() <a name="macro_FLEX_GEN_CPP"></a>
Generate C++ from Lex grammar. This is current default.

###### Macro [FORK\_SUBTESTS][]() <a name="macro_FORK_SUBTESTS"></a>
Splits the test run in chunks on subtests.
The number of chunks can be overridden using the macro SPLIT\_FACTOR.

Allows to run tests in parallel. Supported in UNITTEST, JTEST/JUNIT5 and PY2TEST/PY3TEST modules.

Documentation about the system test: https://wiki.yandex-team.ru/yatool/test/

###### Macro [FORK\_TESTS][]() <a name="macro_FORK_TESTS"></a>
Splits a test run on chunks by test classes.
The number of chunks can be overridden using the macro SPLIT\_FACTOR.

Allows to run tests in parallel. Supported in UNITTEST, JTEST/JUNIT5 and PY2TEST/PY3TEST modules.

Documentation about the system test: https://wiki.yandex-team.ru/yatool/test/

###### Macro [FORK\_TEST\_FILES][]() <a name="macro_FORK_TEST_FILES"></a>
Only for PY2TEST and PY3TEST: splits a file executable with the tests on chunks in the files listed in TEST\_SRCS
Compatible with FORK\_(SUB)TESTS.

Documentation about the system test: https://wiki.yandex-team.ru/yatool/test/

###### Macro [FROM\_ARCHIVE][](Src [RENAME <resource files>] OUT\_[NOAUTO] <output files> [EXECUTABLE] [OUTPUT\_INCLUDES <include files>] [INDUCED\_DEPS $VARs...]) <a name="macro_FROM_ARCHIVE"></a>
Process file archive as [FROM\_SANDBOX()](#macro\_FROM\_SANDBOX).

###### Macro [FROM\_SANDBOX][]([FILE] resource\_id [AUTOUPDATED script] [RENAME <resource files>] OUT\_[NOAUTO] <output files> [EXECUTABLE] [OUTPUT\_INCLUDES <include files>] [INDUCED\_DEPS $VARs...]) <a name="macro_FROM_SANDBOX"></a>
Download the resource from the Sandbox, unpack (if not explicitly specified word FILE) and add OUT files to the build. EXECUTABLE makes them executable.
You may specify extra dependencies that output files bring using OUTPUT\_INCLUDES or INDUCED\_DEPS. The change of these may e.g. lead to recompilation of .cpp files extracted from resource.
If there is no default processing for OUT files or you need process them specially use OUT\_NOAUTO instead of OUT.

It is disallowed to specify directory as OUT/OUT\_NOAUTO since all outputs of commands shall be known to build system.

RENAME renames files to the corresponding OUT and OUT\_NOAUTO outputs:
FROM\_SANDBOX(resource\_id RENAME in\_file1 in\_file2 OUT out\_file1 out\_file2 out\_file3)
FROM\_SANDBOX(resource\_id RENAME in\_file1 OUT out\_file1 RENAME in\_file2 OUT out\_file2)
FROM\_SANDBOX(FILE resource\_id RENAME resource\_file OUT out\_name)

RENAME RESOURCE allows to rename the resource without specifying its file name.

OUTPUT\_INCLUDES output\_includes... - Includes of the output files that are needed to build them.
INDUCED\_DEPS $VARs... - Dependencies for generated files. Unlike `OUTPUT\_INCLUDES` these may target files further in processing chain.
                        In order to do so VAR should be filled by PREPARE\_INDUCED\_DEPS macro, stating target files (by type) and set of dependencies

If AUTOUPDATED is specified than macro will be regularly updated according to autoupdate script. The dedicated Sandbox task scans the arcadia and
changes resource\_ids in such macros if newer resource of specified type is available. Note that the task seeks AUTOUPDATED in specific position,
so you shall place it immediately after resource\_id.

###### Macro [FULL\_JAVA\_SRCS][] <a name="macro_FULL_JAVA_SRCS"></a>
Fill JAVA\_SRCS to value for ya ide idea and real apply for late globs

###### Macro [FUNCTION\_ORDERING\_FILE][](VAR\_NAME) <a name="macro_FUNCTION_ORDERING_FILE"></a>
Select file for function reordering. Works only with lld linker.
VAR\_NAME should be the same value that was passed into DECLARE\_EXTERNAL\_HOST\_RESOURCES\_BUNDLE library.

###### Macro [FUZZ\_DICTS][](path1 [path2...]) <a name="macro_FUZZ_DICTS"></a>
Allows you to specify dictionaries, relative to the root of Arcadia, which will be used in Fuzzing.
Libfuzzer and AFL use a single syntax for dictionary descriptions.
Should only be used in FUZZ modules.

Documentation: https://wiki.yandex-team.ru/yatool/fuzzing/

###### Macro [FUZZ\_OPTS][](opt1 [Opt2...]) <a name="macro_FUZZ_OPTS"></a>
Overrides or adds options to the corpus mining and fuzzer run.
Currently supported only Libfuzzer, so you should use the options for it.
Should only be used in FUZZ modules.

@example:

    FUZZ_OPTS (
        -max_len=1024
        -rss_limit_mb=8192
    )

Documentation: https://wiki.yandex-team.ru/yatool/fuzzing/

###### Macro [GENERATE\_ENUM\_SERIALIZATION][](File.h) <a name="macro_GENERATE_ENUM_SERIALIZATION"></a>
Create serialization support for enumeration members defined in the header (String <-> Enum conversions) and compile it into the module.

Documentation: https://wiki.yandex-team.ru/yatool/HowToWriteYaMakeFiles/

###### Macro [GENERATE\_ENUM\_SERIALIZATION\_WITH\_HEADER][](File.h) <a name="macro_GENERATE_ENUM_SERIALIZATION_WITH_HEADER"></a>
Create serialization support for enumeration members defined in the header (String <-> Enum conversions) and compile it into the module
Provide access to serialization functions via generated header File\_serialized.h

Documentation: https://wiki.yandex-team.ru/yatool/HowToWriteYaMakeFiles/

###### Macro [GENERATE\_PY\_PROTOS][](ProtoFiles...) _# deprecated_ <a name="macro_GENERATE_PY_PROTOS"></a>
Generate python bindings for protobuf files.
Macro is obsolete and not recommended for use!

###### Macro [GENERATE\_SCRIPT][] <a name="macro_GENERATE_SCRIPT"></a>
heretic@ promised to make tutorial here
Don't forget
Feel free to remind

###### Macro [GENERATE\_YT\_RECORD][](Yaml, OUTPUT\_INCLUDES[]) <a name="macro_GENERATE_YT_RECORD"></a>
Not documented yet.

###### Macro [GEN\_SCHEEME2][](scheeme\_name from\_file dependent\_files...) <a name="macro_GEN_SCHEEME2"></a>
Generates a C++ description for structure(contains the field RecordSig) in the specified file (and connected).

1. ${scheeme\_name}.inc - the name of the generated file.
2. Use an environment variable - DATAWORK\_SCHEEME\_EXPORT\_FLAGS that allows to specify flags to tools/structparser

@example:

    SET(DATAWORK_SCHEEME_EXPORT_FLAGS --final_only -m "::")

all options are passed to structparser (in this example --final\_only - do not export heirs with public base that contains the required field,,- m "::" only from the root namespace)
sets in extra option

@example:

    SET(EXTRACT_STRUCT_INFO_FLAGS -f \"const static ui32 RecordSig\"
        -u \"RecordSig\" -n${scheeme_name}SchemeInfo ----gcc44_no_typename no_complex_overloaded_func_export
        ${DATAWORK_SCHEEME_EXPORT_FLAGS})

for compatibility with C++ compiler and the external environment.
See tools/structparser for more details.

###### Macro [GLOBAL\_CFLAGS][](compiler\_flags) <a name="macro_GLOBAL_CFLAGS"></a>
Add the specified flags to the compilation command of C and C++ files and propagate these flags to dependent projects

###### Macro [GLOBAL\_SRCS][](filenames...) <a name="macro_GLOBAL_SRCS"></a>
Make all source files listed as GLOBAL.
Call to GLOBAL\_SRCS macro is equivalent to call to SRCS macro when each source file is marked with GLOBAL keyword.
Arcadia root relative or project dir relative paths are supported for filenames arguments. GLOBAL keyword is not
recognized for GLOBAL\_SRCS in contrast to SRCS macro.

@example:
Consider the file to ya.make:

    LIBRARY()
        GLOBAL_SRCS(foo.cpp bar.cpp)
    END()

@see: [SRCS()](#macro\_SRCS)

###### Macro [GOLANG\_VERSION][](Arg) <a name="macro_GOLANG_VERSION"></a>
Not documented yet.

###### Macro [GO\_ASM\_FLAGS][](flags) <a name="macro_GO_ASM_FLAGS"></a>
Add the specified flags to the go asm compile command line.

###### Macro [GO\_BENCH\_TIMEOUT][](x) <a name="macro_GO_BENCH_TIMEOUT"></a>
Sets timeout in seconds for 1 Benchmark in go benchmark suite

Documentation about the system test: https://wiki.yandex-team.ru/yatool/test/

###### Macro [GO\_CGO1\_FLAGS][](flags) <a name="macro_GO_CGO1_FLAGS"></a>
Add the specified flags to the go cgo compile command line.

###### Macro [GO\_CGO2\_FLAGS][](flags) <a name="macro_GO_CGO2_FLAGS"></a>
Add the specified flags to the go cgo compile command line.

###### Macro [GO\_COMPILE\_FLAGS][](flags) <a name="macro_GO_COMPILE_FLAGS"></a>
Add the specified flags to the go compile command line.

###### Macro [GO\_EMBED\_BINDIR][](DIR) <a name="macro_GO_EMBED_BINDIR"></a>
Define an embed directory DIR for files from ARCADIA\_BUILD\_ROOT

###### Macro [GO\_EMBED\_DIR][](DIR) <a name="macro_GO_EMBED_DIR"></a>
Define an embed directory DIR.

###### Macro [GO\_EMBED\_PATTERN][](PATTERN) <a name="macro_GO_EMBED_PATTERN"></a>
Define an embed pattern.

###### Macro [GO\_EMBED\_TEST\_DIR][](DIR) <a name="macro_GO_EMBED_TEST_DIR"></a>
Define an embed directory DIR for internal go tests.

###### Macro [GO\_EMBED\_XTEST\_DIR][](DIR) <a name="macro_GO_EMBED_XTEST_DIR"></a>
Define an embed directory DIR for external go tests.

###### Macro [GO\_FAKE\_OUTPUT][](go-src-files...) <a name="macro_GO_FAKE_OUTPUT"></a>
Not documented yet.

###### Macro [GO\_GRPC\_GATEWAY\_SRCS][]() <a name="macro_GO_GRPC_GATEWAY_SRCS"></a>
Use of grpc-gateway plugin (Supported for Go only).

###### Macro [GO\_GRPC\_GATEWAY\_SWAGGER\_SRCS][]() <a name="macro_GO_GRPC_GATEWAY_SWAGGER_SRCS"></a>
Use of grpc-gateway plugin w/ swagger emission (Supported for Go only).

###### Macro [GO\_GRPC\_GATEWAY\_V2\_OPENAPI\_SRCS][](Files...) <a name="macro_GO_GRPC_GATEWAY_V2_OPENAPI_SRCS"></a>
Use of grpc-gateway plugin w/ openapi v2 emission (Supported for Go only).

###### Macro [GO\_GRPC\_GATEWAY\_V2\_SRCS][]() <a name="macro_GO_GRPC_GATEWAY_V2_SRCS"></a>
Use of grpc-gateway plugin (Supported for Go only).

###### Macro [GO\_LDFLAGS][](Flags...) <a name="macro_GO_LDFLAGS"></a>
Link flags for GO\_PROGRAM linking from .go sources

###### Macro [GO\_LINK\_FLAGS][](flags) <a name="macro_GO_LINK_FLAGS"></a>
Add the specified flags to the go link command line.

###### Macro [GO\_MOCKGEN\_CONTRIB\_FROM][](Path) <a name="macro_GO_MOCKGEN_CONTRIB_FROM"></a>
Not documented yet.

###### Macro [GO\_MOCKGEN\_FROM][](Path) <a name="macro_GO_MOCKGEN_FROM"></a>
Not documented yet.

###### Macro [GO\_MOCKGEN\_MOCKS][]() <a name="macro_GO_MOCKGEN_MOCKS"></a>
Not documented yet.

###### Macro [GO\_MOCKGEN\_REFLECT][]() <a name="macro_GO_MOCKGEN_REFLECT"></a>
Not documented yet.

###### Macro [GO\_MOCKGEN\_TYPES][](Types...) <a name="macro_GO_MOCKGEN_TYPES"></a>
Not documented yet.

###### Macro [GO\_PACKAGE\_NAME][](Name) <a name="macro_GO_PACKAGE_NAME"></a>
Override name of a Go package.

###### Macro [GO\_PROTO\_PLUGIN][](Name Ext Tool [DEPS dependencies...]) <a name="macro_GO_PROTO_PLUGIN"></a>
Define protoc plugin for GO with given Name that emits extra output with provided extension
Ext using Tool. Extra dependencies are passed via DEPS.

###### Macro [GO\_PROTO\_USE\_V2][]() <a name="macro_GO_PROTO_USE_V2"></a>
Not documented yet.

###### Macro [GO\_SKIP\_TESTS][](TestNames...) <a name="macro_GO_SKIP_TESTS"></a>
Define a set of tests that should not be run.
NB! Subtests are not taken into account!

###### Macro [GO\_TEST\_EMBED\_BINDIR][](DIR) <a name="macro_GO_TEST_EMBED_BINDIR"></a>
Define an embed directory DIR for files from ARCADIA\_BUILD\_ROOT for internal go tests

###### Macro [GO\_TEST\_EMBED\_PATTERN][](PATTERN) <a name="macro_GO_TEST_EMBED_PATTERN"></a>
Define an embed pattern for internal go tests.

###### Macro [GO\_TEST\_FOR][](path/to/module)  _#builtin_ <a name="macro_GO_TEST_FOR"></a>
Produces go test for specified module

###### Macro [GO\_TEST\_SRCS][](Files...) <a name="macro_GO_TEST_SRCS"></a>
.go sources for internal tests of a module

###### Macro [GO\_XTEST\_EMBED\_BINDIR][](DIR, FILES...) <a name="macro_GO_XTEST_EMBED_BINDIR"></a>
Define an embed directory DIR for files from ARCADIA\_BUILD\_ROOT for external go tests

###### Macro [GO\_XTEST\_EMBED\_PATTERN][](PATTERN) <a name="macro_GO_XTEST_EMBED_PATTERN"></a>
Define an embed pattern for external go tests.

###### Macro [GO\_XTEST\_SRCS][](Files...) <a name="macro_GO_XTEST_SRCS"></a>
.go sources for external tests of a module

###### Macro [GRPC][]() <a name="macro_GRPC"></a>
Emit GRPC code for all .proto files in a PROTO\_LIBRARY.
This works for all available PROTO\_LIBRARY versions (C++, Python 2.x, Python 3.x, Java and Go).

###### Macro WITH\_GMOCK() <a name="macro_GRPC_WITH_GMOCK"></a>
Enable generating \*\_mock.grpc.pb.cc/h files

###### Macro [HEADERS][]([Dir1 Dir2 ...]) <a name="macro_HEADERS"></a>
Add all C/C++ header files (h|H|hh|hpp|hxx|ipp) in given directories to SRCS

###### Macro [IDEA\_EXCLUDE\_DIRS][](<excluded dirs>) <a name="macro_IDEA_EXCLUDE_DIRS"></a>
Exclude specified directories from an idea project generated by ya ide idea
Have no effect on regular build.

###### Macro [IDEA\_MODULE\_NAME][](module\_name) <a name="macro_IDEA_MODULE_NAME"></a>
Set module name in an idea project generated by ya ide idea
Have no effect on regular build.

###### Macro [IDEA\_RESOURCE\_DIRS][](<additional dirs>) <a name="macro_IDEA_RESOURCE_DIRS"></a>
Set specified resource directories in an idea project generated by ya ide idea
Have no effect on regular build.

###### Macro [IF][](condition) .. ELSEIF(other\_condition) .. ELSE() .. ENDIF()  _#builtin_ <a name="macro_IF"></a>
Apply macros if condition holds

###### Macro [INCLUDE][](filename)  _#builtin_ <a name="macro_INCLUDE"></a>
Include file textually and process it as a part of the ya.make

###### Macro [INCLUDE\_ONCE][]([yes|no])  _#builtin_ <a name="macro_INCLUDE_ONCE"></a>
Control how file is is processed if it is included into one base ya.make by multiple paths.
if `yes` passed or argument omitted, process it just once. Process each time if `no` is passed (current default)
Note: for includes from multimodules the file is processed once from each submodule (like if INCLUDEs were preprocessed into multimodule body)

###### Macro [INCLUDE\_TAGS][](tags...)  _# builtin_ <a name="macro_INCLUDE_TAGS"></a>
Additionally instantiate from multimodule all variants with tags listed (overrides default)

###### Macro [INDUCED\_DEPS][](Extension Path...)  _#builtin_ <a name="macro_INDUCED_DEPS"></a>
States that files wih the Extension generated by the PROGRAM will depend on files in Path.
This only useful in PROGRAM and similar modules. It will be applied if the PROGRAM is used in RUN\_PROGRAM macro.
All Paths specified must be absolute arcadia paths i.e. start with ${ARCADIA\_ROOT} ${ARCADIA\_BUILD\_ROOT}, ${CURDIR} or ${BINDIR}.

###### Macro [IOS\_APP\_ASSETS\_FLAGS][](Flags...) <a name="macro_IOS_APP_ASSETS_FLAGS"></a>
Not documented yet.

###### Macro [IOS\_APP\_COMMON\_FLAGS][](Flags...) <a name="macro_IOS_APP_COMMON_FLAGS"></a>
Not documented yet.

###### Macro [IOS\_APP\_SETTINGS][] <a name="macro_IOS_APP_SETTINGS"></a>
Not documented yet.

###### Macro [IOS\_ASSETS][] <a name="macro_IOS_ASSETS"></a>
Not documented yet.

###### Macro [JAR\_ANNOTATION\_PROCESSOR][](Classes...) <a name="macro_JAR_ANNOTATION_PROCESSOR"></a>
Not documented yet.

###### Macro [JAR\_EXCLUDE][](Filters...) <a name="macro_JAR_EXCLUDE"></a>
Filter .jar file content: remove matched files
\* and \*\* patterns are supported (like JAVA\_SRCS)

###### Macro [JAR\_INCLUDE][](Filters...) <a name="macro_JAR_INCLUDE"></a>
Filter .jar file content: keep only matched files
\* and \*\* patterns are supported (like JAVA\_SRCS)

###### Macro [JAR\_MAIN\_CLASS][](Class) <a name="macro_JAR_MAIN_CLASS"></a>
Not documented yet.

###### Macro [JAR\_RESOURCE][](Id) <a name="macro_JAR_RESOURCE"></a>
Not documented yet.

###### Macro [JAVAC\_FLAGS][](Args...) <a name="macro_JAVAC_FLAGS"></a>
Set additional Java compilation flags.

###### Macro [JAVA\_DEPENDENCIES\_CONFIGURATION][](Vetos...) <a name="macro_JAVA_DEPENDENCIES_CONFIGURATION"></a>
Validate contrib/java dependencies
Valid arguments
FORBID\_DIRECT\_PEERDIRS - fail when module have direct PEERDIR (with version) (non-transitive)
FORBID\_CONFLICT - fail when module have resolved without DEPENDENCY\_MANAGEMENT version conflict (transitive)
FORBID\_CONFLICT\_DM - fail when module have resolved with DEPENDENCY\_MANAGEMENT version conflict (transitive)
FORBID\_CONFLICT\_DM\_RECENT - like FORBID\_CONFLICT\_DM but fail only when dependency have more recent version than specified in DEPENDENCY\_MANAGEMENT
REQUIRE\_DM - all dependencies must be specified in DEPENDENCY\_MANAGEMENT (transitive)

###### Macro [JAVA\_EXTERNAL\_DEPENDENCIES][](file1 file2 ...) <a name="macro_JAVA_EXTERNAL_DEPENDENCIES"></a>
Add non-source java external build dependency (like lombok config file)

###### Macro [JAVA\_IGNORE\_CLASSPATH\_CLASH\_FOR][]([classes]) <a name="macro_JAVA_IGNORE_CLASSPATH_CLASH_FOR"></a>
Ignore classpath clash test fails for classes

###### Macro [JAVA\_MODULE][] <a name="macro_JAVA_MODULE"></a>
Not documented yet.

###### Macro [JAVA\_PROTO\_PLUGIN][](Name Tool DEPS <Dependencies>) <a name="macro_JAVA_PROTO_PLUGIN"></a>
Define protoc plugin for Java with given Name that emits extra outputs
using Tool. Extra dependencies are passed via DEPS

###### Macro [JAVA\_RESOURCE][](JAR, SOURCES="") <a name="macro_JAVA_RESOURCE"></a>
Not documented yet.

###### Macro [JAVA\_SRCS][](srcs) <a name="macro_JAVA_SRCS"></a>
Specify java source files and resources. A macro can be contained in any of four java modules.
Keywords:
1. SRCDIR x - specify the directory x is performed relatively to search the source code for these patterns. If there is no SRCDIR, the source will be searched relative to the module directory.
2. PACKAGE\_PREFIX x - use if source paths relative to the SRCDIR does not coincide with the full class names. For example, if all sources of module are in the same package, you can create a directory package/name , and just put the source code in the SRCDIR and specify PACKAGE\_PREFIX package.name.

@example:
 - example/ya.make

       JAVA_PROGRAM()
           JAVA_SRCS(SRCDIR src/main/java **/*)
       END()

 - example/src/main/java/ru/yandex/example/HelloWorld.java

       package ru.yandex.example;
       public class HelloWorld {
            public static void main(String[] args) {
                System.out.println("Hello, World!");
            }
       }

Documentation: https://wiki.yandex-team.ru/yatool/java/#javasrcs

###### Macro [JAVA\_TEST][] <a name="macro_JAVA_TEST"></a>
Not documented yet.

###### Macro [JAVA\_TEST\_DEPS][] <a name="macro_JAVA_TEST_DEPS"></a>
Not documented yet.

###### Macro [JDK\_VERSION][](Version) <a name="macro_JDK_VERSION"></a>
Specify JDK version for module

###### Macro [JOIN\_SRCS][](Out Src...) <a name="macro_JOIN_SRCS"></a>
Join set of sources into single file named Out and send it for further processing.
This macro doesn't place all file into Out, it emits #include<Src>... Use the for C++ source files only.
You should specify file name with the extension as Out. Further processing will be done according this extension.

###### Macro [JOIN\_SRCS\_GLOBAL][](Out Src...) <a name="macro_JOIN_SRCS_GLOBAL"></a>
Join set of sources into single file named Out and send it for further processing as if it were listed as SRCS(GLOBAL Out).
This macro doesn't place all file into Out, it emits #include<Src>... Use the for C++ source files only.
You should specify file name with the extension as Out. Further processing will be done according to this extension.

###### Macro [JUNIT\_TESTS\_JAR][] <a name="macro_JUNIT_TESTS_JAR"></a>
Usage JUNIT\_TESTS\_JAR(path/to/some/peer realname.jar)

Specifies jar to search test suites and test cases. By default tests are
searched in the jar compild by JTEST or JUNIT5 module sources. This macro
allows to specify diferent jar to search tests.

Only one jar file is used to search tests. If this macro invoked multiple
times (which is not reccomended practice) only the last invocation will
have effect.

If this macro is used no test from the module build by current ya.make
will be searched and executed.

###### Macro [JVM\_ARGS][](Args...) <a name="macro_JVM_ARGS"></a>
Arguments to run Java programs in tests.

Documentation: https://wiki.yandex-team.ru/yatool/test/

###### Macro [KAPT\_ANNOTATION\_PROCESSOR][](processors...) <a name="macro_KAPT_ANNOTATION_PROCESSOR"></a>
Used to specify annotation processor qualified class names.
If specified multiple times, only last specification is used.

###### Macro [KAPT\_ANNOTATION\_PROCESSOR\_CLASSPATH][](jars...) <a name="macro_KAPT_ANNOTATION_PROCESSOR_CLASSPATH"></a>
Used to specify classpath for annotation processors.
If specified multiple times, all specifications are used.

###### Macro [KAPT\_OPTS][](opts...) <a name="macro_KAPT_OPTS"></a>
Used to specify annotation processor qualified class names.
If specified multiple times, only last specification is used.

###### Macro [KOTLINC\_FLAGS][](-flags) <a name="macro_KOTLINC_FLAGS"></a>
Set additional Kotlin compilation flags.

###### Macro _#deprecated [KTLINT\_BASELINE\_FILE][](ktlint-baseline.xml "https://st.yandex-team.ru/REMOVE-BASELINE-1")_ <a name="macro_KTLINT_BASELINE_FILE"></a>
Path to baseline file for ktlint test and ticket to fix all ktlint warnings in file and then remove it

###### Macro [LARGE\_FILES][]([AUTOUPDATED]  Files...) <a name="macro_LARGE_FILES"></a>
Use large file ether from working copy or from remote storage via placeholder <File>.external
If <File> is present locally (and not a symlink!) it will be copied to build directory.
Otherwise macro will try to locate <File>.external, parse it retrieve ot during build phase.

###### Macro [LDFLAGS][](LinkerFlags...) <a name="macro_LDFLAGS"></a>
Add flags to the link command line of executable or shared library/dll.
Note: LDFLAGS are always global. When set in the LIBRARY module they will affect all programs/dlls/tests the library is linked into.
Note: remember about the incompatibility of flags for gcc and cl.

###### Macro [LICENSE][](licenses...) <a name="macro_LICENSE"></a>
Specify the licenses of the module, separated by spaces. Specifying multiple licenses interpreted as permission to use this
library satisfying all conditions of any of the listed licenses.

A license must be prescribed for contribs

###### Macro [LICENSE\_RESTRICTION][](ALLOW\_ONLY|DENY LicenseProperty...) <a name="macro_LICENSE_RESTRICTION"></a>
Restrict licenses of direct and indirect module dependencies.

ALLOW\_ONLY restriction type requires dependent module to have at least one license without properties not listed in restrictions list.

DENY restriction type forbids dependency on module with no license without any listed property from the list.

Note: Can be used multiple times on the same module all specified constraints will be checked.
All macro invocation for the same module must use same constraints type (DENY or ALLOW\_ONLY)

###### Macro [LICENSE\_RESTRICTION\_EXCEPTIONS][](Module...) <a name="macro_LICENSE_RESTRICTION_EXCEPTIONS"></a>
List of modules for exception from LICENSE\_RESTRICTION and MODULEWISE\_LICENSE\_RESTRICTION logic.

###### Macro [LICENSE\_TEXTS][](File) <a name="macro_LICENSE_TEXTS"></a>
This macro specifies the filename with all library licenses texts

###### Macro [LINKER\_SCRIPT][](Files...) <a name="macro_LINKER_SCRIPT"></a>
Specify files to be used as a linker script

###### Macro [LINK\_EXEC\_DYN\_LIB\_IMPL][] <a name="macro_LINK_EXEC_DYN_LIB_IMPL"></a>
$usage: LINK\_EXEC\_DYN\_LIB\_IMPL(peers...) # internal

###### Macro [LINK\_EXE\_IMPL][] <a name="macro_LINK_EXE_IMPL"></a>
$usage: LINK\_EXE\_IMPL(peers...) # internal

###### Macro [LINT][](<none|base|strict|extended>) <a name="macro_LINT"></a>
Set linting level for sources of the module

###### Macro [LIST\_PROTO][]([TO list.proto] Files...)  _# deprecated_ <a name="macro_LIST_PROTO"></a>
Create list of .proto files in a list-file (should be .proto, files.proto by default)
with original .proto-files as list's dependencies.

This allows to process files listed, passing list as an argument to the processor

TODO: proper implementation needed

###### Macro [LJ\_21\_ARCHIVE][](NAME Name LuaFiles...) _# deprecated_ <a name="macro_LJ_21_ARCHIVE"></a>
Precompile .lua files using LuaJIT 2.1 and archive both sources and results using sources names as keys

###### Macro [LJ\_ARCHIVE][](NAME Name LuaFiles...) <a name="macro_LJ_ARCHIVE"></a>
Precompile .lua files using LuaJIT and archive both sources and results using sources names as keys

###### Macro [LLVM\_BC][] <a name="macro_LLVM_BC"></a>
Not documented yet.

###### Macro [LLVM\_COMPILE\_C][](Input Output Opts...) <a name="macro_LLVM_COMPILE_C"></a>
Emit LLVM bytecode from .c file. BC\_CFLAGS, LLVM\_OPTS and C\_FLAGS\_PLATFORM are passed in, while CFLAGS are not.
Note: Output name is used as is, no extension added.

###### Macro [LLVM\_COMPILE\_CXX][](Input Output Opts...) <a name="macro_LLVM_COMPILE_CXX"></a>
Emit LLVM bytecode from .cpp file. BC\_CXXFLAGS, LLVM\_OPTS and C\_FLAGS\_PLATFORM are passed in, while CFLAGS are not.
Note: Output name is used as is, no extension added.

###### Macro [LLVM\_COMPILE\_LL][](Input Output Opts...) <a name="macro_LLVM_COMPILE_LL"></a>
Compile LLVM bytecode to object representation.
Note: Output name is used as is, no extension added.

###### Macro [LLVM\_LINK][](Output Inputs...) <a name="macro_LLVM_LINK"></a>
Call llvm-link on set of Inputs to produce Output.
Note: Unlike many other macros output argument goes first. Output name is used as is, no extension added.

###### Macro [LLVM\_LLC][](Src Opts...) <a name="macro_LLVM_LLC"></a>
Call llvm-llc with set of Opts on Src to produce object file.

Note: Output name is calculated as concatenation of Src name and platform specific object file extension.

###### Macro [LLVM\_OPT][](Input Output Opts...) <a name="macro_LLVM_OPT"></a>
Call llvm-opt with set of Opts on Input to produce Output.
Note: Output name is used as is, no extension added.

###### Macro [LOCAL\_JAR][](File) <a name="macro_LOCAL_JAR"></a>
Not documented yet.

###### Macro [LOCAL\_SOURCES\_JAR][](File) <a name="macro_LOCAL_SOURCES_JAR"></a>
Not documented yet.

###### Macro [MACROS\_WITH\_ERROR][] <a name="macro_MACROS_WITH_ERROR"></a>
Not documented yet.

###### Macro [MANUAL\_GENERATION][](Outs...) <a name="macro_MANUAL_GENERATION"></a>
Not documented yet.

###### Macro [MASMFLAGS][](compiler flags) <a name="macro_MASMFLAGS"></a>
Add the specified flags to the compilation command of .masm files.

###### Macro [MAVEN\_GROUP\_ID][](group\_id\_for\_maven\_export) <a name="macro_MAVEN_GROUP_ID"></a>
Set maven export group id for JAVA\_PROGRAM() and JAVA\_LIBRARY().
Have no effect on regular build.

###### Macro [MESSAGE][]([severity] message)  _# builtin_ <a name="macro_MESSAGE"></a>
Print message with given severity level (STATUS, FATAL\_ERROR)

###### Macro [MODULEWISE\_LICENSE\_RESTRICTION][](ALLOW\_ONLY|DENY LicenseProperty...) <a name="macro_MODULEWISE_LICENSE_RESTRICTION"></a>
Restrict licenses per module only, without it peers.

ALLOW\_ONLY restriction type requires module to have at least one license without properties not listed in restrictions list.

DENY restriction type forbids module with no license without any listed property from the list.

Note: Can be used multiple times on the same module all specified constraints will be checked.
All macro invocation for the same module must use same constraints type (DENY or ALLOW\_ONLY)

###### Macro [MSVC\_FLAGS][]([GLOBAL compiler\_flag]\* compiler\_flags) <a name="macro_MSVC_FLAGS"></a>
Add the specified flags to the compilation line of C/C++files.
Flags apply only if the compiler used is MSVC (cl.exe)

###### Macro [NEED\_CHECK][]() <a name="macro_NEED_CHECK"></a>
Commits to the project marked with this macro will be blocked by pre-commit check and then will be
automatically merged to trunk only if there is no new broken build targets in check results.
The use of this macro is disabled by default.

###### Macro [NEED\_REVIEW][]() _# deprecated_ <a name="macro_NEED_REVIEW"></a>
Mark the project as needing review.
Reviewers are listed in the macro OWNER. The use of this macro is disabled by default.
Details can be found here: https://clubs.at.yandex-team.ru/arcadia/6104

###### Macro [NGINX\_MODULES][](Modules...) <a name="macro_NGINX_MODULES"></a>
Not documented yet.

###### Macro [NO\_BUILD\_IF][]([FATAL\_ERROR|STRICT] variables)  _# builtin_ <a name="macro_NO_BUILD_IF"></a>
Print warning or error if some variable is true.
In STRICT mode disables build of all modules and RECURSES of the ya.make.
FATAL\_ERROR issues configure error and enables STRICT mode.

###### Macro [NO\_CHECK\_IMPORTS][]([patterns]) <a name="macro_NO_CHECK_IMPORTS"></a>
Do not run checks on imports of Python modules.
Optional parameter mask patterns describes the names of the modules that do not need to check.

###### Macro [NO\_CLANG\_COVERAGE][]() <a name="macro_NO_CLANG_COVERAGE"></a>
Disable heavyweight clang coverage for the module. Clang coverage instrumentation is enabled by the --clang-coverage option.

###### Macro [NO\_CLANG\_TIDY][]() <a name="macro_NO_CLANG_TIDY"></a>
Not documented yet.

###### Macro [NO\_COMPILER\_WARNINGS][]() <a name="macro_NO_COMPILER_WARNINGS"></a>
Disable all compiler warnings in the module.
Priorities: NO\_COMPILER\_WARNINGS > NO\_WERROR > WERROR\_MODE > WERROR.

###### Macro [NO\_CONTRIB\_TYPESCRIPT][]() <a name="macro_NO_CONTRIB_TYPESCRIPT"></a>
Not documented yet.

###### Macro [NO\_CPU\_CHECK][]() <a name="macro_NO_CPU_CHECK"></a>
Compile module without startup CPU features check

###### Macro [NO\_CYTHON\_COVERAGE][]() <a name="macro_NO_CYTHON_COVERAGE"></a>
Disable cython and cythonized python coverage (CYTHONIZE\_PY)
Implies NO\_CLANG\_COVERAGE() - right now, we can't disable instrumentation for .py.cpp files, but enable for .cpp

###### Macro [NO\_DEBUG\_INFO][]() <a name="macro_NO_DEBUG_INFO"></a>
Compile files without debug info collection.

###### Macro [NO\_DOCTESTS][]() <a name="macro_NO_DOCTESTS"></a>
Disable doctests in PY[|3|23\_]TEST

###### Macro [NO\_EXPORT\_DYNAMIC\_SYMBOLS][]() <a name="macro_NO_EXPORT_DYNAMIC_SYMBOLS"></a>
Disable exporting all non-hidden symbols as dynamic when linking a PROGRAM.

###### Macro [NO\_EXTENDED\_SOURCE\_SEARCH][]() <a name="macro_NO_EXTENDED_SOURCE_SEARCH"></a>
Prevent module using in extended python source search.
Use the macro if module contains python2-only files (or other python sources which shouldn't be imported by python3 interpreter)
which resides in the same directories with python 3 useful code. contrib/python/future is a example.
Anyway, preferred way is to move such files into separate dir and don't use this macro at all.

Also see: https://docs.yandex-team.ru/ya-make/manual/python/vars#y\_python\_extended\_source\_search for details

###### Macro [NO\_IMPORT\_TRACING][]() <a name="macro_NO_IMPORT_TRACING"></a>
Disable python coverage for module

###### Macro [NO\_JOIN\_SRC][]() _# deprecated, does-nothing_ <a name="macro_NO_JOIN_SRC"></a>
This macro currently does nothing. This is default behavior which cannot be overridden at module level.

###### Macro [NO\_LIBC][]() <a name="macro_NO_LIBC"></a>
Exclude dependencies on C++ and C runtimes (including util, musl and libeatmydata).
Note: use this with care. libc most likely will be linked into executable anyway,
so using libc headers/functions may not be detected at build time and may lead to unpredictable behavors at configure time.

###### Macro [NO\_LINT][]([ktlint]) <a name="macro_NO_LINT"></a>
Do not check for style files included in PY\_SRCS, TEST\_SRCS, JAVA\_SRCS.
Ktlint can be disabled using NO\_LINT(ktlint) explicitly.

###### Macro [NO\_LTO][]() <a name="macro_NO_LTO"></a>
Disable any lto (link-time optimizations) for the module.
This will compile module source files as usual (without LTO) but will not prevent lto-enabled
linking of entire program if global settings say so.

###### Macro [NO\_MYPY][]() <a name="macro_NO_MYPY"></a>
Not documented yet.

###### Macro [NO\_NEED\_CHECK][]() <a name="macro_NO_NEED_CHECK"></a>
Commits to the project marked with this macro will not be affected by higher-level NEED\_CHECK macro.

###### Macro [NO\_OPTIMIZE][]() <a name="macro_NO_OPTIMIZE"></a>
Build code without any optimizations (-O0 mode).

###### Macro [NO\_OPTIMIZE\_PY\_PROTOS][]() <a name="macro_NO_OPTIMIZE_PY_PROTOS"></a>
Disable Python proto optimization using embedding corresponding C++ code into binary.
Python protobuf runtime will use C++ implementation instead of Python one if former is available.
This is default mode only for some system libraries.

###### Macro [NO\_PLATFORM][]() <a name="macro_NO_PLATFORM"></a>
Exclude dependencies on C++ and C runtimes (including util, musl and libeatmydata) and set NO\_PLATFORM variable for special processing.
Note: use this with care. libc most likely will be linked into executable anyway,
so using libc headers/functions may not be detected at build time and may lead to unpredictable behavors at configure time.

###### Macro [NO\_PROFILE\_RUNTIME][]() <a name="macro_NO_PROFILE_RUNTIME"></a>
Never link this target with profile runtime. Only should be used for very basic build tools

###### Macro [NO\_PYTHON\_COVERAGE][]() <a name="macro_NO_PYTHON_COVERAGE"></a>
Disable python coverage for module

###### Macro [NO\_RUNTIME][]() <a name="macro_NO_RUNTIME"></a>
This macro:
1. Sets the ENABLE(NOUTIL) + DISABLE(USE\_INTERNAL\_STL);
2. If the project that contains the macro NO\_RUNTIME(), peerdir-it project does not contain NO\_RUNTIME() => Warning.
Note: use this with care. Arcadia STL most likely will be linked into executable anyway, so using STL headers/functions/classes
may not be detected at build time and may lead to unpredictable behavors at configure time.

###### Macro [NO\_SANITIZE][]() <a name="macro_NO_SANITIZE"></a>
Disable all sanitizers for the module.

###### Macro [NO\_SANITIZE\_COVERAGE][]() <a name="macro_NO_SANITIZE_COVERAGE"></a>
Disable lightweight coverage (-fsanitize-coverage) for the module.
Sanitize coverage is commonly used with fuzzing.
It might be useful to disable it for libraries that should never
be the main targets for fuzzing, like libfuzzer library itself.
Sanitize coverage instrumentation is enabled by the --sanitize-coverage option.

###### Macro [NO\_SPLIT\_DWARF][]() <a name="macro_NO_SPLIT_DWARF"></a>
Do NOT emit debug info for the PROGRAM/DLL as a separate file.
On macOS this also means do NOT generate dSym files (faster linkage)

###### Macro [NO\_SSE4][]() <a name="macro_NO_SSE4"></a>
Compile module without SSE4

###### Macro [NO\_TS\_TYPECHECK][]() <a name="macro_NO_TS_TYPECHECK"></a>
Not documented yet.

###### Macro [NO\_UTIL][]() <a name="macro_NO_UTIL"></a>
Build module without dependency on util.
Note: use this with care. Util most likely will be linked into executable anyway,
so using util headers/functions/classes may not be detected at build time and may lead to unpredictable behavors at configure time.

###### Macro [NO\_WERROR][]() <a name="macro_NO_WERROR"></a>
Override WERROR() behavior
Priorities: NO\_COMPILER\_WARNINGS > NO\_WERROR > WERROR\_MODE > WERROR.

###### Macro [NO\_WSHADOW][]() <a name="macro_NO_WSHADOW"></a>
Disable C++ shadowing warnings.

###### Macro [NO\_YMAKE\_PYTHON3][]() <a name="macro_NO_YMAKE_PYTHON3"></a>
Not documented yet.

###### Macro [NVCC\_DEVICE\_LINK][](file.cu...) <a name="macro_NVCC_DEVICE_LINK"></a>
Run nvcc --device-link on objects compiled from srcs with --device-c.
This generates a stub object devlink.o that supplies missing pieces for the
host linker to link relocatable device objects into the final executable.

###### Macro [ONLY\_TAGS][](tags...)  _# builtin_ <a name="macro_ONLY_TAGS"></a>
Instantiate from multimodule only variants with tags listed

###### Macro [OPENSOURCE\_EXPORT\_REPLACEMENT][](CMAKE PkgName CMAKE\_COMPONENT OptCmakePkgComponent CMAKE\_TARGET PkgName::PkgTarget CONAN ConanRequire CONAN ConanOptions CONAN\_ADDITIONAL\_SEMS ConanAdditionalSems) <a name="macro_OPENSOURCE_EXPORT_REPLACEMENT"></a>
Use specified conan/system package when exporting cmake build scripts for arcadia C++ project for opensource publication.

###### Macro [OPENSOURCE\_EXPORT\_REPLACEMENT\_BY\_OS][](OS Os CMAKE PkgName CMAKE\_COMPONENT OptCmakePkgComponent CMAKE\_TARGET PkgName::PkgTarget CONAN ConanRequire CONAN ConanOptions CONAN\_ADDITIONAL\_SEMS ConanAdditionalSems) <a name="macro_OPENSOURCE_EXPORT_REPLACEMENT_BY_OS"></a>
Use specified conan/system package when exporting cmake build scripts for arcadia C++ project for opensource publication.

###### Macro [ORIGINAL\_SOURCE][](Source) <a name="macro_ORIGINAL_SOURCE"></a>
This macro specifies the source repository for contrib
Does nothing now (just a placeholder for future functionality)
See https://st.yandex-team.ru/DTCC-316

###### Macro [OWNER][](owners...)  _# builtin_ <a name="macro_OWNER"></a>
Add reviewers/responsibles of the code.
In the OWNER macro you can use:
1. login-s from staff.yandex-team.ru
2. Review group (to specify the Code-review group need to use the prefix g:)

Ask devtools@yandex-team.ru if you need more information

###### Macro [PACK][](archive\_type) <a name="macro_PACK"></a>
When placed inside the PACKAGE module, packs the build results tree to the archive with specified extension. Currently supported extensions are `tar` and `tar.gz`

Is not allowed other module types than PACKAGE().

@see: [PACKAGE()](#module\_PACKAGE)

###### Macro [PACKAGE\_STRICT][]() <a name="macro_PACKAGE_STRICT"></a>
Not documented yet.

###### Macro [PACK\_GLOBALS\_IN\_LIBRARY][]() <a name="macro_PACK_GLOBALS_IN_LIBRARY"></a>
Not documented yet.

###### Macro [PARTITIONED\_RECURSE][]([BALANCING\_CONFIG config] dirs...)  _# builtin_ <a name="macro_PARTITIONED_RECURSE"></a>
Add directories to the build
All projects must be reachable from the root chain RECURSE() for monorepo continuous integration functionality.
Arguments are processed in chunks

###### Macro [PARTITIONED\_RECURSE\_FOR\_TESTS][]([BALANCING\_CONFIG config] dirs...)  _# builtin_ <a name="macro_PARTITIONED_RECURSE_FOR_TESTS"></a>
Add directories to the build if tests are demanded.
Arguments are processed in chunks

###### Macro [PARTITIONED\_RECURSE\_ROOT\_RELATIVE][]([BALANCING\_CONFIG config] dirlist)  _# builtin_ <a name="macro_PARTITIONED_RECURSE_ROOT_RELATIVE"></a>
In comparison with RECURSE(), in dirlist there must be a directory relative to the root (${ARCADIA\_ROOT}).
Arguments are processed in chunks

###### Macro [PEERDIR][](dirs...)  _# builtin_ <a name="macro_PEERDIR"></a>
Specify project dependencies
Indicates that the project depends on all of the projects from the list of dirs.
Libraries from these directories will be collected and linked to the current target if the target is executable or sharedlib/dll.
If the current target is a static library, the specified directories will not be built, but they will be linked to any executable target that will link the current library.
@params:
1. As arguments PEERDIR you can only use the LIBRARY directory (the directory with the PROGRAM/DLL and derived from them are prohibited to use as arguments PEERDIR).
2. ADDINCL Keyword ADDINCL (written before the specified directory), adds the flag -I<path to library> the flags to compile the source code of the current project.
Perhaps it may be removed in the future (in favor of a dedicated ADDINCL)

###### Macro [PIRE\_INLINE][](FILES...) <a name="macro_PIRE_INLINE"></a>
Not documented yet.

###### Macro [PIRE\_INLINE\_CMD][](SRC) <a name="macro_PIRE_INLINE_CMD"></a>
Not documented yet.

###### Macro [POPULATE\_CPP\_COVERAGE\_FLAGS][]() <a name="macro_POPULATE_CPP_COVERAGE_FLAGS"></a>
Not documented yet.

###### Macro [PREPARE\_INDUCED\_DEPS][](VAR Type Files...) <a name="macro_PREPARE_INDUCED_DEPS"></a>
Format value for `INDUCED\_DEPS` param in certain macros and assign to `VAR`
This tells that files of Type resulted from code generation macros (not neccessarily directly,
but in processing chain of generated files) should have extra dependencies from list of Files...

Prominent example here is Cython: one can generate .pyx file that may depend on .pxd and have cimpot from
certain .h. The former is dependency for .pyx itself, while the latter is dependency for .pyx.cpp
resulted from Cython-processing of generated pyx. The code ganeration will look like:
```
PREPARE_INDUCED_DEPS(PYX_DEPS pyx imported.pxd)
PREPARE_INDUCED_DEPS(CPP_DEPS cpp cdefed.h)
RUN_PYTHON3(generate_pyx.py genereted.pyx OUT generated.pyx INDUCED_DEPS $PYX_DEPS $CPP_DEPS)
```

The VAR will basically contain pair of `Type:[Files...]` in a form suitable for passing
as an element of array parameter. This is needed because language of ya.make doesn't support
Dict params right now and so it is impossible to directly pass something
like `{Type1:[Files2...], Type2:[Files2...]}`

###### Macro [PROCESS\_DOCS][] <a name="macro_PROCESS_DOCS"></a>
Not documented yet.

###### Macro [PROCESS\_MKDOCS][] <a name="macro_PROCESS_MKDOCS"></a>
Not documented yet.

###### Macro [PROTO2FBS][](InputProto) <a name="macro_PROTO2FBS"></a>
Produce flatbuf schema out of protobuf description.

###### Macro [PROTOC\_FATAL\_WARNINGS][]() <a name="macro_PROTOC_FATAL_WARNINGS"></a>
Treat protoc warnings as fatal errors that break the build, for example, unused imports
Adds `--fatal\_warnings` argument to protoc

###### Macro [PROTO\_ADDINCL][]([GLOBAL] [WITH\_GEN] Path) <a name="macro_PROTO_ADDINCL"></a>
This macro introduces proper ADDINCLs for .proto-files found in sources and
.cpp/.h generated files, supplying them to appropriate commands and allowing
proper dependency resolution at configure-time.

Note: you normally shouldn't use this macro. ADDINCLs should be sent to user
from dependency via PROTO\_NAMESPACE macro

###### Macro [PROTO\_CMD][](SRC) <a name="macro_PROTO_CMD"></a>
Not documented yet.

###### Macro [PROTO\_NAMESPACE][]([WITH\_GEN] Namespace) <a name="macro_PROTO_NAMESPACE"></a>
Defines protobuf namespace (import/export path prefix) which should be used for imports and
which defines output path for .proto generation.

For proper importing and configure-time dependency management it sets ADDINCLs
for both .cpp headers includes and .proto imports. If .proto expected to be used outside of the
processing module use GLOBAL to send proper ADDINCLs to all (transitive) users. PEERDIR to
PROTO\_LIBRARY with PROTO\_NAMESPACE() is enough at user side to correctly use the library.
If generated .proto files are going to be used for building a module than use of WITH\_GEN
parameter will add appropriate dir from the build root for .proto files search.

###### Macro [PROVIDES][](Name...) <a name="macro_PROVIDES"></a>
Specifies provided features. The names must be correct C identifiers.
This prevents different libraries providing the same features to be linked into one program.

###### Macro [PYTHON2\_ADDINCL][]() <a name="macro_PYTHON2_ADDINCL"></a>
This macro adds include path for Python headers (Python 2.x variant) without PEERDIR.
This should be used in 2 cases only:
- In PY2MODULE since it compiles into .so and uses external Python runtime;
- In system Python libraries themselves since proper PEERDIR there may create a loop;
In all other cases use USE\_PYTHON2 macro instead.

Never use this macro in PY2\_PROGRAM, PY2\_LIBRARY and PY23\_LIBRARY: they have everything needed by default.

Documentation: https://wiki.yandex-team.ru/devtools/commandsandvars/py\_srcs

###### Macro [PYTHON2\_MODULE][]() <a name="macro_PYTHON2_MODULE"></a>
Use in PY\_ANY\_MODULE to set it up for Python 2.x.

###### Macro [PYTHON3\_ADDINCL][]() <a name="macro_PYTHON3_ADDINCL"></a>
This macro adds include path for Python headers (Python 3.x variant).
This should be used in 2 cases only:
- In PY2MODULE since it compiles into .so and uses external Python runtime;
- In system Python libraries themselves since peerdir there may create a loop;
In all other cases use USE\_PYTHON3() macro instead.

Never use this macro in PY3\_PROGRAM and PY3\_LIBRARY and PY23\_LIBRARY: they have everything by default.

Documentation: https://wiki.yandex-team.ru/devtools/commandsandvars/py\_srcs

###### Macro [PYTHON3\_MODULE][]() <a name="macro_PYTHON3_MODULE"></a>
Use in PY\_ANY\_MODULE to set it up for Python 3.x.

###### Macro [PYTHON\_PATH][](Path) <a name="macro_PYTHON_PATH"></a>
Set path to Python that will be used to runs scripts in tests

###### Macro [PY\_CONSTRUCTOR][](package.module[:func]) <a name="macro_PY_CONSTRUCTOR"></a>
Specifies the module or function which will be started before python's main()
init() is expected in the target module if no function is specified
Can be considered as \_\_attribute\_\_((constructor)) for python

###### Macro [PY\_DOCTESTS][](Packages...) <a name="macro_PY_DOCTESTS"></a>
Add to the test doctests for specified Python packages
The packages should be part of a test (listed as sources of the test or its PEERDIRs).

###### Macro [PY\_ENUMS\_SERIALIZATION][] <a name="macro_PY_ENUMS_SERIALIZATION"></a>
Not documented yet.

###### Macro EXTRALIBS(liblist) <a name="macro_PY_EXTRALIBS"></a>
Add external dynamic libraries during program linkage stage" }

###### Macro [PY\_EXTRA\_LINT\_FILES][](files...) <a name="macro_PY_EXTRA_LINT_FILES"></a>
Add extra Python files for linting. This macro allows adding
Python files which has no .py extension.

###### Macro [PY\_MAIN][](package.module[:func]) <a name="macro_PY_MAIN"></a>
Specifies the module or function from which to start executing a python program

Documentation: https://wiki.yandex-team.ru/arcadia/python/pysrcs/#modulipyprogrampy3programimakrospymain

###### Macro [PY\_NAMESPACE][](prefix) <a name="macro_PY_NAMESPACE"></a>
Sets default Python namespace for all python sources in the module.
Especially suitable in PROTO\_LIBRARY where Python sources are generated and there is no PY\_SRCS to place NAMESPACE parameter.

###### Macro [PY\_PROTOS\_FOR][](path/to/module)  _#builtin, deprecated_ <a name="macro_PY_PROTOS_FOR"></a>
Use PROTO\_LIBRARY() in order to have .proto compiled into Python.
Generates pb2.py files out of .proto files and saves those into PACKAGE module

###### Macro [PY\_PROTO\_PLUGIN][](Name Ext Tool DEPS <Dependencies>) <a name="macro_PY_PROTO_PLUGIN"></a>
Define protoc plugin for python with given Name that emits extra output with provided Extension
using Tool. Extra dependencies are passed via DEPS

###### Macro [PY\_PROTO\_PLUGIN2][](Name Ext1 Ext2 Tool DEPS <Dependencies>) <a name="macro_PY_PROTO_PLUGIN2"></a>
Define protoc plugin for python with given Name that emits 2 extra outputs with provided Extensions
using Tool. Extra dependencies are passed via DEPS

###### Macro [PY\_REGISTER][]([package.]module\_name) <a name="macro_PY_REGISTER"></a>
Python knows about which built-ins can be imported, due to their registration in the Assembly or at the start of the interpreter.
All modules from the sources listed in PY\_SRCS() are registered automatically.
To register the modules from the sources in the SRCS(), you need to use PY\_REGISTER().

PY\_REGISTER(module\_name) initializes module globally via call to initmodule\_name()
PY\_REGISTER(package.module\_name) initializes module in the specified package
It renames its init function with CFLAGS(-Dinitmodule\_name=init7package11module\_name)
or CFLAGS(-DPyInit\_module\_name=PyInit\_7package11module\_name)

Documentation: https://wiki.yandex-team.ru/arcadia/python/pysrcs/#makrospyregister

###### Macro [PY\_SRCS][]({| CYTHON\_C} { | TOP\_LEVEL | NAMESPACE ns} Files...) <a name="macro_PY_SRCS"></a>
Build specified Python sources according to Arcadia binary Python build. Basically creates precompiled and source resources keyed with module paths.
The resources eventually are linked into final program and can be accessed as regular Python modules.
This custom loader linked into the program will add them to sys.meta\_path.

PY\_SRCS also support .proto, .ev, .pyx and .swg files. The .proto and .ev are compiled to .py-code by protoc and than handled as usual .py files.
.pyx and .swg lead to C/C++ Python extensions generation, that are automatically registered in Python as built-in modules.

By default .pyx files are built as C++-extensions. Use CYTHON\_C to build them as C (similar to BUILDWITH\_CYTHON\_C, but with the ability to specify namespace).

\_\_init\_\_.py never required, but if present (and specified in PY\_SRCS), it will be imported when you import package modules with \_\_init\_\_.py Oh.

@example

    PY2_LIBRARY(mymodule)
        PY_SRCS(a.py sub/dir/b.py e.proto sub/dir/f.proto c.pyx sub/dir/d.pyx g.swg sub/dir/h.swg)
    END()

PY\_SRCS honors Python2 and Python3 differences and adjusts itself to Python version of a current module.
PY\_SRCS can be used in any Arcadia Python build modules like PY\*\_LIBRARY, PY\*\_PROGRAM, PY\*TEST.
PY\_SRCS in LIBRARY or PROGRAM effectively converts these into PY2\_LIBRARY and PY2\_PROGRAM respectively.
It is strongly advised to make this conversion explicit. Never use PY\_SRCS in a LIBRARY if you plan to use it from external Python extension module.

Documentation: https://wiki.yandex-team.ru/arcadia/python/pysrcs/#modulipylibrarypy3libraryimakrospysrcs

###### Macro [REAL\_LINK\_DYN\_LIB\_IMPL][] <a name="macro_REAL_LINK_DYN_LIB_IMPL"></a>
$usage: REAL\_LINK\_DYN\_LIB\_IMPL(peers...) # internal

###### Macro [REAL\_LINK\_EXEC\_DYN\_LIB\_IMPL][] <a name="macro_REAL_LINK_EXEC_DYN_LIB_IMPL"></a>
$usage: REAL\_LINK\_EXEC\_DYN\_LIB\_IMPL(peers...) # internal

###### Macro [REAL\_LINK\_EXE\_IMPL][] <a name="macro_REAL_LINK_EXE_IMPL"></a>
$usage: REAL\_LINK\_EXE\_IMPL(peers...) # internal

###### Macro [RECURSE][](dirs...)  _# builtin_ <a name="macro_RECURSE"></a>
Add directories to the build
All projects must be reachable from the root chain RECURSE() for monorepo continuous integration functionality

###### Macro [RECURSE\_FOR\_TESTS][](dirs...)  _# builtin_ <a name="macro_RECURSE_FOR_TESTS"></a>
Add directories to the build if tests are demanded.
Use --force-build-depends flag if you want to build testing modules without tests running

###### Macro [RECURSE\_ROOT\_RELATIVE][](dirlist)  _# builtin_ <a name="macro_RECURSE_ROOT_RELATIVE"></a>
In comparison with RECURSE(), in dirlist there must be a directory relative to the root (${ARCADIA\_ROOT})

###### Macro [REGISTER\_SANDBOX\_IMPORT][] <a name="macro_REGISTER_SANDBOX_IMPORT"></a>
Not documented yet.

###### Macro [REGISTER\_YQL\_PYTHON\_UDF][] <a name="macro_REGISTER_YQL_PYTHON_UDF"></a>
Not documented yet.

###### Macro [REQUIREMENTS][]([cpu:<count>] [disk\_usage:<size>] [ram:<size>] [ram\_disk:<size>] [container:<id>] [network:<restricted|full>] [dns:dns64]) <a name="macro_REQUIREMENTS"></a>
Allows you to specify the requirements of the test.

Documentation about the Arcadia test system: https://wiki.yandex-team.ru/yatool/test/

###### Macro [REQUIRES][](dirs...) <a name="macro_REQUIRES"></a>
Specify list of dirs which this module must depend on indirectly.

This macro can be used if module depends on the directories specified but they can't be listed
as direct PEERDIR dependencies (due to public include order or link order issues).

###### Macro [RESOLVE\_PROTO][]() <a name="macro_RESOLVE_PROTO"></a>
Enable include resolving within UNIONs and let system .proto being resolved
among .proto/.gztproto imports

Note: it is currently impossible to enable resolving only for .proto, so resolving is enabled for all supported files
also we only add ADDINCL for stock protobuf. So use this macro with care: it may cause resolving problems those are
to be addressed by either ADDINCLs or marking them as TEXT. Please contact devtools for details.

###### Macro [RESOURCE][]([FORCE\_TEXT ][Src Key]\* [- Key=Value]\*) _# built-in_ <a name="macro_RESOURCE"></a>
Add data (resources, random files, strings) to the program)
The common usage is to place Src file into binary. The Key is used to access it using library/cpp/resource or library/python/resource.
Alternative syntax with '- Key=Value' allows placing Value string as resource data into binary and make it accessible by Key.

This is a simpler but less flexible option than ARCHIVE(), because in the case of ARCHIVE(), you have to use the data explicitly,
and in the case of RESOURCE(), the data will fall through SRCS() or SRCS(GLOBAL) to binary linking.

Use the FORCE\_TEXT parameter to explicitly mark all Src files as text files: they will not be parsed unless used elsewhere.

@example: https://wiki.yandex-team.ru/yatool/howtowriteyamakefiles/#a2ispolzujjtekomanduresource

@example:

    LIBRARY()
        OWNER(user1)

        RESOURCE(
            path/to/file1 /key/in/program/1
            path/to/file2 /key2
        )
    END()

###### Macro [RESOURCE\_FILES][]([PREFIX {prefix}] [STRIP prefix\_to\_strip] {path}) <a name="macro_RESOURCE_FILES"></a>
This macro expands into
RESOURCE(DONT\_PARSE {path} resfs/file/{prefix}{path}
    - resfs/src/resfs/file/{prefix}{remove\_prefix(path, prefix\_to\_strip)}={rootrel\_arc\_src(path)}
)

resfs/src/{key} stores a source root (or build root) relative path of the
source of the value of the {key} resource.

resfs/file/{key} stores any value whose source was a file on a filesystem.
resfs/src/resfs/file/{key} must store its path.

DONT\_PARSE disables parsing for source code files (determined by extension)
           Please don't abuse: use separate DONT\_PARSE macro call only for files subject to parsing

This form is for use from other plugins:
RESOURCE\_FILES([DEST {dest}] {path}) expands into RESOURCE({path} resfs/file/{dest})

@see: https://wiki.yandex-team.ru/devtools/commandsandvars/resourcefiles/

###### Macro [RESTRICT\_PATH][] <a name="macro_RESTRICT_PATH"></a>
Not documented yet.

###### Macro [RUN][] <a name="macro_RUN"></a>
Not documented yet.

###### Macro [RUN\_ANTLR][](Args...) <a name="macro_RUN_ANTLR"></a>
Macro to invoke ANTLR3 generator (general case)

###### Macro [RUN\_ANTLR4][](Args...) <a name="macro_RUN_ANTLR4"></a>
Macro to invoke ANTLR4 generator (general case)

###### Macro [RUN\_ANTLR4\_CPP][](GRAMMAR, OUTPUT\_INCLUDES, LISTENER, VISITOR, Args...) <a name="macro_RUN_ANTLR4_CPP"></a>
Macro to invoke ANTLR4 generator for combined lexer+parser grammars (Cpp)

###### Macro [RUN\_ANTLR4\_CPP\_SPLIT][](LEXER, PARSER, OUTPUT\_INCLUDES, LISTENER, VISITOR, Args...) <a name="macro_RUN_ANTLR4_CPP_SPLIT"></a>
Macro to invoke ANTLR4 generator for separate lexer and parser grammars (Cpp)

###### Macro [RUN\_ANTLR4\_GO][](GRAMMAR, DEPS <extra\_go\_deps>, LISTENER, VISITOR, Args...) <a name="macro_RUN_ANTLR4_GO"></a>
Macro to invoke ANTLR4 generator (Go)

###### Macro [RUN\_ANTLR4\_PYTHON][](Grammar [LISTENER] [VISITOR] [SUBDIR] [EXTRA\_OUTS Outs...] Args...) <a name="macro_RUN_ANTLR4_PYTHON"></a>
`LISTENER` - emit grammar listener
`VISITOR` -  emit grammar visitor
`SUBDIR` - place generated files to specified subdirectory of BINDIR
`EXTRA\_OUTS` - list extra outputs produced by Antlr (e.g. .interp and .token files) if they are needed. If `SUBDIR` is specied it will affect these as well. Use file names only.

Macro to invoke ANTLR4 generator (Python). The Python3 will be used for PY3\_LIBRARY/PY3\_PROGRAM/PY3TEST, Python2 will be used in all other cases.

###### Macro [RUN\_JAVA\_PROGRAM][](Args...) <a name="macro_RUN_JAVA_PROGRAM"></a>
Not documented yet.

###### Macro [RUN\_LUA][](script\_path args... [CWD dir] [ENV key=value...] [TOOL tools...] [IN[\_NOPARSE] inputs...] [OUT[\_NOAUTO] outputs...] [STDOUT[\_NOAUTO] output] [OUTPUT\_INCLUDES output\_includes...] [INDUCED\_DEPS $VARs...]) <a name="macro_RUN_LUA"></a>
Run a lua script.
These macros are similar: RUN\_PROGRAM, RUN\_LUA, PYTHON.

Parameters:
- script\_path - Path to the script.3
- args... - Program arguments. Relative paths listed in TOOL, IN, OUT, STDOUT become absolute.
- CWD dir - Absolute path of the working directory.
- ENV key=value... - Environment variables.
- TOOL tools... - Auxiliary tool directories.
- IN[\_NOPARSE] inputs... - Input files. NOPARSE inputs are treated as textual and not parsed for dependencies regardless of file extensions.
- OUT[\_NOAUTO] outputs... - Output files. NOAUTO outputs are not automatically added to the build process.
- STDOUT[\_NOAUTO] output - Redirect the standard output to the output file.
- OUTPUT\_INCLUDES output\_includes... - Includes of the output files that are needed to build them.
- INDUCED\_DEPS $VARs... - Dependencies for generated files. Unlike `OUTPUT\_INCLUDES` these may target files further in processing chain.
                          In order to do so VAR should be filled by PREPARE\_INDUCED\_DEPS macro, stating target files (by type) and set of dependencies

For absolute paths use ${ARCADIA\_ROOT} and ${ARCADIA\_BUILD\_ROOT}, or
${CURDIR} and ${BINDIR} which are expanded where the outputs are used.

###### Macro [RUN\_PROGRAM][](tool\_path args... [CWD dir] [ENV key=value...] [TOOL tools...] [IN[\_NOPARSE] inputs...] [OUT[\_NOAUTO] outputs...] [STDOUT[\_NOAUTO] output] [OUTPUT\_INCLUDES output\_includes...] [INDUCED\_DEPS $VARs...]) <a name="macro_RUN_PROGRAM"></a>
Run a program from arcadia.
These macros are similar: RUN\_PROGRAM, RUN\_LUA, PYTHON.

Parameters:
- tool\_path - Path to the directory of the tool.
- args... - Program arguments. Relative paths listed in TOOL, IN, OUT, STDOUT become absolute.
- CWD dir - Absolute path of the working directory.
- ENV key=value... - Environment variables.
- TOOL tools... - Auxiliary tool directories.
- IN[\_NOPARSE] inputs... - Input files. NOPARSE inputs are treated as textual and not parsed for dependencies regardless of file extensions.
- OUT[\_NOAUTO] outputs... - Output files. NOAUTO outputs are not automatically added to the build process.
- STDOUT[\_NOAUTO] output - Redirect the standard output to the output file.
- OUTPUT\_INCLUDES output\_includes... - Includes of the output files that are needed to build them.
- INDUCED\_DEPS $VARs... - Dependencies for generated files. Unlike `OUTPUT\_INCLUDES` these may target files further in processing chain.
                          In order to do so VAR should be filled by PREPARE\_INDUCED\_DEPS macro, stating target files (by type) and set of dependencies

For absolute paths use ${ARCADIA\_ROOT} and ${ARCADIA\_BUILD\_ROOT}, or
${CURDIR} and ${BINDIR} which are expanded where the outputs are used.
Note that Tool is always built for the host platform, so be careful to provide that tool can be built for all Arcadia major host platforms (Linux, MacOS and Windows).

###### Macro [RUN\_PYTHON3][](script\_path args... [CWD dir] [ENV key=value...] [TOOL tools...] [IN[\_NOPARSE] inputs...] [OUT[\_NOAUTO] outputs...] [STDOUT[\_NOAUTO] output] [OUTPUT\_INCLUDES output\_includes...] [INDUCED\_DEPS $VARs...]) <a name="macro_RUN_PYTHON3"></a>
Run a python script with prebuilt python3 interpretor built from devtools/huge\_python3.
These macros are similar: RUN\_PROGRAM, RUN\_LUA, PYTHON.

Parameters:
- script\_path - Path to the script.
- args... - Program arguments. Relative paths listed in TOOL, IN, OUT, STDOUT become absolute.
- CWD dir - Absolute path of the working directory.
- ENV key=value... - Environment variables.
- TOOL tools... - Auxiliary tool directories.
- IN[\_NOPARSE] inputs... - Input files. NOPARSE inputs are treated as textual and not parsed for dependencies regardless of file extensions.
- OUT[\_NOAUTO] outputs... - Output files. NOAUTO outputs are not automatically added to the build process.
- STDOUT[\_NOAUTO] output - Redirect the standard output to the output file.
- OUTPUT\_INCLUDES output\_includes... - Includes of the output files that are needed to build them.
- INDUCED\_DEPS $VARs... - Dependencies for generated files. Unlike `OUTPUT\_INCLUDES` these may target files further in processing chain.
                          In order to do so VAR should be filled by PREPARE\_INDUCED\_DEPS macro, stating target files (by type) and set of dependencies

For absolute paths use ${ARCADIA\_ROOT} and ${ARCADIA\_BUILD\_ROOT}, or
${CURDIR} and ${BINDIR} which are expanded where the outputs are used.

###### Macro [SDBUS\_CPP\_ADAPTOR][](File) <a name="macro_SDBUS_CPP_ADAPTOR"></a>
Not documented yet.

###### Macro [SDBUS\_CPP\_PROXY][](File) <a name="macro_SDBUS_CPP_PROXY"></a>
Not documented yet.

###### Macro [SELECT\_CLANG\_SA\_CONFIG][](static\_analyzer.yaml) <a name="macro_SELECT_CLANG_SA_CONFIG"></a>
Select config file for clang static analyzer.
The file should be called static\_analyzer.yaml.

###### Macro [SET][](varname value)  _#builtin_ <a name="macro_SET"></a>
Sets varname to value

###### Macro [SETUP\_EXECTEST][] <a name="macro_SETUP_EXECTEST"></a>
Not documented yet.

###### Macro [SETUP\_PYTEST\_BIN][] <a name="macro_SETUP_PYTEST_BIN"></a>
Not documented yet.

###### Macro [SETUP\_RUN\_PYTHON][] <a name="macro_SETUP_RUN_PYTHON"></a>
Not documented yet.

###### Macro [SET\_APPEND][](varname appendvalue)  _#builtin_ <a name="macro_SET_APPEND"></a>
Appends appendvalue to varname's value using space as a separator

###### Macro [SET\_APPEND\_WITH\_GLOBAL][](varname appendvalue)  _#builtin_ <a name="macro_SET_APPEND_WITH_GLOBAL"></a>
Appends appendvalue to varname's value using space as a separator.
New value is propagated to dependants

###### Macro [SET\_COMPILE\_OUTPUTS\_MODIFIERS][](NOREL?"norel;output":"output") <a name="macro_SET_COMPILE_OUTPUTS_MODIFIERS"></a>
Not documented yet.

###### Macro [SET\_CPP\_COVERAGE\_FLAGS][] <a name="macro_SET_CPP_COVERAGE_FLAGS"></a>
Not documented yet.

###### Macro [SET\_RESOURCE\_MAP\_FROM\_JSON][](VarName, FileName) <a name="macro_SET_RESOURCE_MAP_FROM_JSON"></a>
Loads the platform to resource uri mapping from the json file FileName and assign it to the variable VarName.
'VarName' value format is the same as an input of the DECLARE\_EXTERNAL\_HOST\_RESOURCES\_BUNDLE macro and can be passed to this macro as is.
File 'FileName' contains json with a 'canonized platform -> resource uri' mapping.
The mapping file format see in SET\_RESOURCE\_URI\_FROM\_JSON description.

###### Macro [SET\_RESOURCE\_URI\_FROM\_JSON][](VarName, FileName) <a name="macro_SET_RESOURCE_URI_FROM_JSON"></a>
Assigns a resource uri matched with a current target platform to the variable VarName.
The 'platform to resource uri' mapping is loaded from json file 'FileName'. File content example:
{
    "by\_platform": {
        "linux": {
            "uri": "sbr:12345"
        },
        "darwin": {
            "uri": "sbr:54321"
        }
    }
}

###### Macro [SIZE][](SMALL/MEDIUM/LARGE) <a name="macro_SIZE"></a>
Set the 'size' for the test. Each 'size' has own set of resrtictions, SMALL bein the most restricted and LARGE being the list.
See documentation on test system for more details.

Documentation about the system test: https://wiki.yandex-team.ru/yatool/test/

###### Macro [SKIP\_TEST][](Reason) <a name="macro_SKIP_TEST"></a>
Skip the suite defined by test module. Provide a reason to be output in test execution report.

###### Macro [SOURCE\_GROUP][](...)  _#builtin, deprecated_ <a name="macro_SOURCE_GROUP"></a>
Ignored

###### Macro [SPLIT\_CODEGEN][](tool prefix opts... [OUT\_NUM num] [OUTPUT\_INCLUDES output\_includes...]) <a name="macro_SPLIT_CODEGEN"></a>
Generator of a certain number of parts of the .cpp file + one header .h file from .in

Supports keywords:
1. OUT\_NUM <the number of generated Prefix.N.cpp default 25 (N varies from 0 to 24)>
2. OUTPUT\_INCLUDES <path to files that will be included in generalnyj of macro files>

###### Macro [SPLIT\_DWARF][]() <a name="macro_SPLIT_DWARF"></a>
Emit debug info for the PROGRAM/DLL as a separate file <module\_name>.debug.
NB: It does not help you to save process RSS but can add problems (see e.g. BEGEMOT-2147).

###### Macro [SPLIT\_FACTOR][](x) <a name="macro_SPLIT_FACTOR"></a>
Sets the number of chunks for parallel run tests when used in test module with FORK\_TESTS() or FORK\_SUBTESTS().
If none of those is specified this macro implies FORK\_TESTS().

Supports C++ ut and PyTest.

Documentation about the system test: https://wiki.yandex-team.ru/yatool/test/

###### Macro [SRC][](File Flags...) <a name="macro_SRC"></a>
Compile single file with extra Flags.
Compilation is driven by the last extension of the File and Flags are specific to corresponding compilation command

###### Macro [SRCDIR][](dirlist)  _# builtin_ <a name="macro_SRCDIR"></a>
Add the specified directories to the list of those in which the source files will be searched
Available only for arcadia/contrib

###### Macro [SRCS][](<[GLOBAL] File> ...) <a name="macro_SRCS"></a>
Source files of the project. Files are built according to their extension and put int module output or fed to ultimate PROGRAM/DLL depending on GLOBAL presence.
Arcadia Paths from the root and is relative to the project's LIST are supported

GLOBAL marks next file as direct input to link phase of the program/shared library project built into. This prevents symbols of the file to be excluded by linker as unused.
The scope of the GLOBAL keyword is the following file (that is, in the case of SRCS(GLOBAL foo.cpp bar.cpp) global will be only foo.cpp)

@example:

    LIBRARY(test_global)
        SRCS(GLOBAL foo.cpp)
    END()

This will produce foo.o and feed it to any PROGRAM/DLL module transitively depending on test\_global library. The library itself will be empty and won't produce .a file.

###### Macro [SRC\_C\_AMX][] <a name="macro_SRC_C_AMX"></a>
@uasge SRC\_C\_AVX512(File Flags...)

Compile a single C/C++ file with AVX512 and additional Flags

###### Macro [SRC\_C\_AVX][] <a name="macro_SRC_C_AVX"></a>
@uasge SRC\_C\_AVX(File Flags...)

Compile a single C/C++ file with AVX and additional Flags

###### Macro [SRC\_C\_AVX2][] <a name="macro_SRC_C_AVX2"></a>
@uasge SRC\_C\_AVX2(File Flags...)

Compile a single C/C++ file with AVX2 and additional Flags

###### Macro [SRC\_C\_AVX512][] <a name="macro_SRC_C_AVX512"></a>
@uasge SRC\_C\_AVX512(File Flags...)

Compile a single C/C++ file with AVX512 and additional Flags

###### Macro [SRC\_C\_NO\_LTO][] <a name="macro_SRC_C_NO_LTO"></a>
@uasge SRC\_C\_NO\_LTO(File Flags...)

Compile a single C/C++ file with link-time-optimization disabling and additional Flags

###### Macro [SRC\_C\_PCLMUL][] <a name="macro_SRC_C_PCLMUL"></a>
@uasge SRC\_C\_PCLMUL(File Flags...)

Compile a single C/C++ file with PCLMUL and additional Flags

###### Macro [SRC\_C\_PIC][] <a name="macro_SRC_C_PIC"></a>
@uasge SRC\_C\_PIC(File Flags...)

Compile a single C/C++ file with -fPIC and additional Flags

###### Macro [SRC\_C\_SSE2][] <a name="macro_SRC_C_SSE2"></a>
@uasge SRC\_C\_SSE2(File Flags...)

Compile a single C/C++ file with SSE2 and additional Flags

###### Macro [SRC\_C\_SSE3][] <a name="macro_SRC_C_SSE3"></a>
@uasge SRC\_C\_SSE3(File Flags...)

Compile a single C/C++ file with SSE3 and additional Flags

###### Macro [SRC\_C\_SSE4][] <a name="macro_SRC_C_SSE4"></a>
@uasge SRC\_C\_SSE4(File Flags...)

Compile a single C/C++ file with SSE4 and additional Flags

###### Macro [SRC\_C\_SSE41][] <a name="macro_SRC_C_SSE41"></a>
@uasge SRC\_C\_SSE41(File Flags...)

Compile a single C/C++ file with SSE4.1 and additional Flags

###### Macro [SRC\_C\_SSSE3][] <a name="macro_SRC_C_SSSE3"></a>
@uasge SRC\_C\_SSSE3(File Flags...)

Compile a single C/C++ file with SSSE3 and additional Flags

###### Macro [SRC\_C\_XOP][] <a name="macro_SRC_C_XOP"></a>
@uasge SRC\_C\_XOP(File Flags...)

Compile a single C/C++ file with (an AMD-specific instruction set,
see https://en.wikipedia.org/wiki/XOP\_instruction\_set) and additional Flags

###### Macro [SRC\_RESOURCE][](Id) <a name="macro_SRC_RESOURCE"></a>
Not documented yet.

###### Macro [STRIP][]() <a name="macro_STRIP"></a>
Strip debug info from a PROGRAM, DLL or TEST.
This macro doesn't work in LIBRARY's, UNION's and PACKAGE's.

###### Macro [STYLE][](Globs...) <a name="macro_STYLE"></a>
Not documented yet.

###### Macro [STYLE\_CPP][]() <a name="macro_STYLE_CPP"></a>
Run 'ya tool clang-format' test on all cpp sources and headers of the current module

###### Macro [STYLE\_PYTHON][]([pyproject]) <a name="macro_STYLE_PYTHON"></a>
Check python3 sources for style issues using black.

###### Macro [STYLE\_RUFF][]() <a name="macro_STYLE_RUFF"></a>
Check python3 sources for style issues using ruff.

###### Macro [SUBSCRIBER][](subscribers...)  _# builtin_ <a name="macro_SUBSCRIBER"></a>
Add observers of the code.
In the SUBSCRIBER macro you can use:
1. login-s from staff.yandex-team.ru
2. Review group (to specify the Code-review group need to use the prefix g:)

Note: current behavior of SUBSCRIBER is almost the same as OWNER. The are only 2 differences: SUBSCRIBER is not mandatory and it may be separately processed by external tools

Ask devtools@yandex-team.ru if you need more information

###### Macro [SUPPRESSIONS][] <a name="macro_SUPPRESSIONS"></a>
SUPPRESSIONS() - allows to specify files with suppression notation which will be used by
address, leak or thread sanitizer runtime by default.
Use asan.supp filename for address sanitizer, lsan.supp for leak sanitizer
and tsan.supp for thread sanitizer suppressions respectively.
See https://clang.llvm.org/docs/AddressSanitizer.html#suppressing-memory-leaks
for details.

###### Macro [SYMLINK][](from to) <a name="macro_SYMLINK"></a>
Add symlink

###### Macro [SYSTEM\_PROPERTIES][]([<Key Value>...] [<File Path>...]) <a name="macro_SYSTEM_PROPERTIES"></a>
List of Key,Value pairs that will be available to test via System.getProperty().
FILE means that parst should be read from file specifies as Path.

Documentation: https://wiki.yandex-team.ru/yatool/test/

###### Macro [TAG][] ([tag...]) <a name="macro_TAG"></a>
Each test can have one or more tags used to filter tests list for running.
There are also special tags affecting test behaviour, for example ya:external, sb:ssd.

Documentation: https://wiki.yandex-team.ru/yatool/test/#obshhieponjatija

###### Macro [TASKLET][]() <a name="macro_TASKLET"></a>
Not documented yet.

###### Macro [TASKLET\_REG][](Name, Lang, Impl, Includes...) <a name="macro_TASKLET_REG"></a>
Not documented yet.

###### Macro [TASKLET\_REG\_EXT][](Name, Lang, Impl, Wrapper, Includes...) <a name="macro_TASKLET_REG_EXT"></a>
Not documented yet.

###### Macro [TEST\_CWD][](path) <a name="macro_TEST_CWD"></a>
Defines working directory for test runs. Often used in conjunction with DATA() macro.
Is only used inside of the TEST modules.

Documentation: https://wiki.yandex-team.ru/yatool/test/

###### Macro [TEST\_DATA][] <a name="macro_TEST_DATA"></a>
Not documented yet.

###### Macro [TEST\_JAVA\_CLASSPATH\_CMD\_TYPE][](Type) <a name="macro_TEST_JAVA_CLASSPATH_CMD_TYPE"></a>
Available types: MANIFEST(default), COMMAND\_FILE, LIST
Method for passing a classpath value to a java command line
MANIFEST via empty jar file with manifest that contains Class-Path attribute
COMMAND\_FILE via @command\_file
LIST via flat args

###### Macro [TEST\_SRCS][](Files...) <a name="macro_TEST_SRCS"></a>
In PY2TEST, PY3TEST and PY\*\_LIBRARY modules used as PY\_SRCS macro and additionally used to mine test cases to be executed by testing framework.

Documentation: https://wiki.yandex-team.ru/yatool/test/#testynapytest

###### Macro [THINLTO\_CACHE][](file) <a name="macro_THINLTO_CACHE"></a>
Not documented yet.

###### Macro [TIMEOUT][](TIMEOUT) <a name="macro_TIMEOUT"></a>
Sets a timeout on test execution

Documentation about the system test: https://wiki.yandex-team.ru/yatool/test/

###### Macro [TOOLCHAIN][] <a name="macro_TOOLCHAIN"></a>
Specify that current module is used as toolchain. Allows to have contrib hooks for toolchain modules
defined in repo internal python plugins

###### Macro [TOUCH\_RANDOM\_FILE][] <a name="macro_TOUCH_RANDOM_FILE"></a>
Not documented yet.

###### Macro [TS\_CONFIG][](ConfigPath) <a name="macro_TS_CONFIG"></a>
Macro sets the path for "TypeScript Config".

- ConfigPath - config path (one at least)

Documentation: https://docs.yandex-team.ru/frontend-in-arcadia/references/macros#ts-config

###### Macro [TS\_ESLINT\_CONFIG][](ConfigPath) <a name="macro_TS_ESLINT_CONFIG"></a>
Macro sets the path for ESLint config file.

- ConfigPath - config path

Documentation: https://docs.yandex-team.ru/frontend-in-arcadia/references/macros#ts-eslint-config

###### Macro [TS\_EXCLUDE\_FILES\_GLOB][](GlobExpression) <a name="macro_TS_EXCLUDE_FILES_GLOB"></a>
Macro sets glob to mark some files to ignore while building.
These files won't be copied to BINDIR.

- GlobExpression - glob expression

Documentation: https://docs.yandex-team.ru/frontend-in-arcadia/references/macros#ts-exclude-files-glob

###### Macro [TS\_FILES][] <a name="macro_TS_FILES"></a>
TS\_FILES(Files...)

Adds files to output as is. Similar to FILES but works for TS build modules

###### Macro [TS\_FILES\_GLOB][] <a name="macro_TS_FILES_GLOB"></a>
TS\_FILES\_GLOB(Glob...)

Adds files to output by glob, e.g. TS\_FILES\_GLOB(\*\*/\*.css)

###### Macro [TS\_NEXT\_CONFIG][](ConfigPath) <a name="macro_TS_NEXT_CONFIG"></a>
Macro sets the config path for TS\_NEXT module.

- ConfigPath - config path. Default value: next.config.js

Documentation: https://docs.yandex-team.ru/frontend-in-arcadia/references/TS\_NEXT#ts-next-config

###### Macro [TS\_NEXT\_EXPERIMENTAL\_COMPILE][]() <a name="macro_TS_NEXT_EXPERIMENTAL_COMPILE"></a>
Not documented yet.

###### Macro [TS\_NEXT\_OUTPUT][](DirName) <a name="macro_TS_NEXT_OUTPUT"></a>
Macro sets the output directory name for TS\_NEXT module.

- DirName - output directory name. Default value: .next.

Documentation: https://docs.yandex-team.ru/frontend-in-arcadia/references/TS\_NEXT#ts-next-output

###### Macro [TS\_STYLELINT][](configFile) <a name="macro_TS_STYLELINT"></a>
For check CSS, SASS, LESS for StyleLint. Must be inside of Module (TS\_WEBPACK, TS\_VITE, TS\_NEXT, etc)

   - configFile - by default .stylelintrc.

Documentation: https://docs.yandex-team.ru/frontend-in-arcadia/references/macros#ts-stylelint

@example:

    TS_VITE()
        TS_STYLELINT(.stylelintrc)
    END()

###### Macro [TS\_TEST\_CONFIG][](Path) <a name="macro_TS_TEST_CONFIG"></a>
Macro sets the path to configuration file of the test runner.

- Path - path to the config file.

Documentation: https://docs.yandex-team.ru/frontend-in-arcadia/references/macros#ts-test-config

###### Macro [TS\_TEST\_DATA][]([RENAME] GLOBS...) <a name="macro_TS_TEST_DATA"></a>
Macro to add tests data (i.e. snapshots) used in testing to a bindir from curdir.
Creates symbolic links to directories of files found by the specified globs.

Parameters:
- RENAME - adds ability to rename paths for tests data from curdir to bindir.
           For example if your tested module located on "module" path and tests data in "module/tests\_data".
           Then you can be able to rename "tests\_data" folder to something else - `RENAME tests\_data:example`.
           As a result in your bindir will be created folder - "module/example" which is a symbolic link on "module/tests\_data" in curdir.
           It is possible to specify multiple renaming rules in the following format "dir1:dir2;dir3/foo:dir4/bar", where "dir1" and "dir3" folders in curdir.
- GLOBS... - globs to tests data files, symbolic links will be created to their folders. For example - "tests\_data/\*\*/\*".

###### Macro [TS\_TEST\_DEPENDS\_ON\_BUILD][]() <a name="macro_TS_TEST_DEPENDS_ON_BUILD"></a>
Macro enables build and results unpacking for the module test is targeting.
It is not required for most of the tests, but it might be needeed in some special cases.

###### Macro [TS\_TEST\_FOR][](path/to/module)  _#builtin_ <a name="macro_TS_TEST_FOR"></a>
Produces typescript test for specified module

###### Macro [TS\_TEST\_SRCS][](DIRS...) <a name="macro_TS_TEST_SRCS"></a>
Macro to define directories where the test source files should be located.

- DIRS... - directories.

Documentation: https://docs.yandex-team.ru/frontend-in-arcadia/references/macros#ts-test-srcs

###### Macro [TS\_TYPECHECK][](tsconfigFile) <a name="macro_TS_TYPECHECK"></a>
For check CSS, SASS, LESS for StyleLint. Must be inside of Module (TS\_WEBPACK, TS\_VITE, TS\_NEXT, etc)

   - tsconfigFile - by default tsconfig.json or value from TS\_CONFIG macros.

Documentation: https://docs.yandex-team.ru/frontend-in-arcadia/references/macros#ts-typecheck

@example:

    TS_VITE()
        TS_TYPECHECK()
    END()

###### Macro [TS\_VITE\_CONFIG][](ConfigPath) <a name="macro_TS_VITE_CONFIG"></a>
Macro sets the config path for TS\_VITE module.

- ConfigPath - config path

Documentation: https://docs.yandex-team.ru/frontend-in-arcadia/references/TS\_VITE#ts-vite-config

###### Macro [TS\_VITE\_OUTPUT][](DirName) <a name="macro_TS_VITE_OUTPUT"></a>
Macro sets the output directory name for TS\_VITE module.

- DirName - output directory name

Documentation: https://docs.yandex-team.ru/frontend-in-arcadia/references/TS\_VITE#ts-vite-output

###### Macro [TS\_WEBPACK\_CONFIG][](ConfigPath) <a name="macro_TS_WEBPACK_CONFIG"></a>
Macro sets the config path for TS\_WEBPACK module.

- ConfigPath - config path

Documentation: https://docs.yandex-team.ru/frontend-in-arcadia/references/TS\_WEBPACK#ts-webpack-config

###### Macro [TS\_WEBPACK\_OUTPUT][](FirstDirName DirNames) <a name="macro_TS_WEBPACK_OUTPUT"></a>
Macro sets the output directory names (one at least) for TS\_WEBPACK module.

- DirNames - output directory names (one at least)
Documentation: https://docs.yandex-team.ru/frontend-in-arcadia/references/TS\_WEBPACK#ts-webpack-output

###### Macro [UBERJAR][]() <a name="macro_UBERJAR"></a>
UBERJAR is a single all-in-one jar-archive that includes all its Java dependencies (reachable PEERDIR).
It also supports shading classes inside the archive by moving them to a different package (similar to the maven-shade-plugin).
Use UBERJAR inside JAVA\_PROGRAM module.

You can use the following macros to configure the archive:
1. UBERJAR\_HIDING\_PREFIX prefix for classes to shade (classes remain in their packages by default)
2. UBERJAR\_HIDE\_INCLUDE\_PATTERN include classes matching this patterns to shading, include LDC mapping
3. UBERJAR\_HIDE\_EXCLUDE\_PATTERN exclude classes matching this patterns from shading (if enabled).
4. UBERJAR\_PATH\_EXCLUDE\_PREFIX the prefix for classes that should not get into the jar archive (all classes are placed into the archive by default)
5. UBERJAR\_MANIFEST\_TRANSFORMER\_MAIN add ManifestResourceTransformer class to uberjar processing and specify main-class
6. UBERJAR\_MANIFEST\_TRANSFORMER\_ATTRIBUTE add ManifestResourceTransformer class to uberjar processing and specify some attribute
7. UBERJAR\_APPENDING\_TRANSFORMER add AppendingTransformer class to uberjar processing
8. UBERJAR\_SERVICES\_RESOURCE\_TRANSFORMER add ServicesResourceTransformer class to uberjar processing

Documentation: https://wiki.yandex-team.ru/yatool/java/

@see: [JAVA\_PROGRAM](#module\_JAVA\_PROGRAM), [UBERJAR\_HIDING\_PREFIX](#macro\_UBERJAR\_HIDING\_PREFIX), [UBERJAR\_HIDE\_INCLUDE\_PATTERN](#macro\_UBERJAR\_HIDE\_INCLUDE\_PATTERN) [UBERJAR\_HIDE\_EXCLUDE\_PATTERN](#macro\_UBERJAR\_HIDE\_EXCLUDE\_PATTERN), [UBERJAR\_PATH\_EXCLUDE\_PREFIX](#macro\_UBERJAR\_PATH\_EXCLUDE\_PREFIX)

###### Macro [UBERJAR\_APPENDING\_TRANSFORMER][](Resource) <a name="macro_UBERJAR_APPENDING_TRANSFORMER"></a>
Add AppendingTransformer for UBERJAR() java programs

Parameters:
- Resource - Resource name

@see: [UBERJAR](#macro\_UBERJAR)

###### Macro [UBERJAR\_HIDE\_EXCLUDE\_PATTERN][](Args...) <a name="macro_UBERJAR_HIDE_EXCLUDE_PATTERN"></a>
Exclude classes matching this patterns from shading (if enabled).
Pattern may contain '\*' and '\*\*' globs.
Shading is enabled for UBERJAR program using UBERJAR\_HIDING\_PREFIX macro. If this macro is not specified all classes are shaded.

@see: [UBERJAR](#macro\_UBERJAR), [UBERJAR\_HIDING\_PREFIX](#macro\_UBERJAR\_HIDING\_PREFIX)

###### Macro [UBERJAR\_HIDE\_INCLUDE\_PATTERN][](Args...) <a name="macro_UBERJAR_HIDE_INCLUDE_PATTERN"></a>
Include classes matching this patterns to shading, enabled LDC processing.
Pattern may contain '\*' and '\*\*' globs.
Shading is enabled for UBERJAR program using UBERJAR\_HIDING\_PREFIX macro. If this macro is not specified all classes are shaded.

@see: [UBERJAR](#macro\_UBERJAR), [UBERJAR\_HIDING\_PREFIX](#macro\_UBERJAR\_HIDING\_PREFIX)

###### Macro [UBERJAR\_HIDING\_PREFIX][](Arg) <a name="macro_UBERJAR_HIDING_PREFIX"></a>
Set prefix for classes to shade. All classes in UBERJAR will be moved into package prefixed with Arg.
Classes remain in their packages by default.

@see: [UBERJAR](#macro\_UBERJAR)

###### Macro [UBERJAR\_MANIFEST\_TRANSFORMER\_ATTRIBUTE][](Key, Value) <a name="macro_UBERJAR_MANIFEST_TRANSFORMER_ATTRIBUTE"></a>
Transform manifest.mf for UBERJAR() java programs, set attribute

@see: [UBERJAR](#macro\_UBERJAR)

###### Macro [UBERJAR\_MANIFEST\_TRANSFORMER\_MAIN][](Main) <a name="macro_UBERJAR_MANIFEST_TRANSFORMER_MAIN"></a>
Transform manifest.mf for UBERJAR() java programs, set main-class attribute

@see: [UBERJAR](#macro\_UBERJAR)

###### Macro [UBERJAR\_PATH\_EXCLUDE\_PREFIX][](Args...) <a name="macro_UBERJAR_PATH_EXCLUDE_PREFIX"></a>
Exclude classes matching this patterns from UBERJAR.
By default all dependencies of UBERJAR program will lend in a .jar archive.

@see: [UBERJAR](#macro\_UBERJAR)

###### Macro [UBERJAR\_SERVICES\_RESOURCE\_TRANSFORMER][]() <a name="macro_UBERJAR_SERVICES_RESOURCE_TRANSFORMER"></a>
Add ServicesResourceTransformer for UBERJAR() java programs

@see: [UBERJAR](#macro\_UBERJAR)

###### Macro [UDF\_NO\_PROBE][]() <a name="macro_UDF_NO_PROBE"></a>
Disable UDF import check at build stage

###### Macro [UPDATE\_VCS\_JAVA\_INFO\_NODEP][](Jar) <a name="macro_UPDATE_VCS_JAVA_INFO_NODEP"></a>
Not documented yet.

###### Macro [USE\_ANNOTATION\_PROCESSOR][](AnnotationProcessor) <a name="macro_USE_ANNOTATION_PROCESSOR"></a>
Used to specify annotation processor for building JAVA\_PROGRAM() and JAVA\_LIBRARY().

###### Macro [USE\_COMMON\_GOOGLE\_APIS][](APIS...) <a name="macro_USE_COMMON_GOOGLE_APIS"></a>
Not documented yet.

###### Macro [USE\_CXX][]() <a name="macro_USE_CXX"></a>
Add dependency on C++ runtime
Note: This macro is inteneded for use in \_GO\_BASE\_UNIT like module when the module is built without C++ runtime by default

###### Macro [USE\_DYNAMIC\_CUDA][]() <a name="macro_USE_DYNAMIC_CUDA"></a>
Enable linking of PROGRAM with dynamic CUDA. By default CUDA uses static linking

###### Macro [USE\_ERROR\_PRONE][]() <a name="macro_USE_ERROR_PRONE"></a>
Use errorprone instead of javac for .java compilation.

###### Macro [USE\_JAVALITE][]() <a name="macro_USE_JAVALITE"></a>
Use protobuf-javalite for Java

###### Macro [USE\_KTLINT\_OLD][]() <a name="macro_USE_KTLINT_OLD"></a>
Marks that need use the old version of ktlint

###### Macro [USE\_LINKER\_GOLD][]() <a name="macro_USE_LINKER_GOLD"></a>
Use gold linker for a program. This doesn't work in libraries

###### Macro [USE\_LLVM\_BC14][]() <a name="macro_USE_LLVM_BC14"></a>
Not documented yet.

###### Macro [USE\_LLVM\_BC16][]() <a name="macro_USE_LLVM_BC16"></a>
Not documented yet.

###### Macro [USE\_MODERN\_FLEX][]() <a name="macro_USE_MODERN_FLEX"></a>
Use `contrib/tools/flex` as flex tool. Default is `contrib/tools/flex-old`.
@note: by default no header is emitted. Use `USE\_MODERN\_FLEX\_WITH\_HEADER` to add header emission.

###### Macro [USE\_MODERN\_FLEX\_WITH\_HEADER][](<header\_suffix>) <a name="macro_USE_MODERN_FLEX_WITH_HEADER"></a>
Use `contrib/tools/flex` as flex tool. Default is `contrib/tools/flex-old`.
Additionally emit headers with suffix provided. Header suffix should include extension `.h`.

@example: USE\_MODERN\_FLEX\_WITH\_HEADER(\_lexer.h)

###### Macro [USE\_NASM][]() <a name="macro_USE_NASM"></a>
Build only .asm files with nasm toolchain instead of yasm
Add to ya.make file ADDINCL(asm ...) with all folders where .asm files include smth

###### Macro [USE\_OLD\_FLEX][]() <a name="macro_USE_OLD_FLEX"></a>
Use `contrib/tools/flex-old` as flex tool. This is current default.

###### Macro [USE\_PLANTUML][]() <a name="macro_USE_PLANTUML"></a>
Use PlantUML plug-in for yfm builder to render UML diagrams into documentation

###### Macro [USE\_PYTHON2][]() <a name="macro_USE_PYTHON2"></a>
This adds Python 2.x runtime library to your LIBRARY and makes it Python2-compatible.
Compatibility means proper PEERDIRs, ADDINCLs and variant selection on PEERDIRs to multimodules.

If you'd like to use #include <Python.h> with Python2 specify USE\_PYTHON2 or better make it PY2\_LIBRARY.
If you'd like to use #include <Python.h> with Python3 specify USE\_PYTHON3 or better make it PY3\_LIBRARY.
If you'd like to use #include <Python.h> with both Python2 and Python3 convert your LIBRARY to PY23\_LIBRARY.

@see: [PY2\_LIBRARY](#module\_PY2\_LIBRARY), [PY3\_LIBRARY](#module\_PY3\_LIBRARY), [PY23\_LIBRARY](#multimodule\_PY23\_LIBRARY)

###### Macro [USE\_PYTHON3][]() <a name="macro_USE_PYTHON3"></a>
This adds Python3 library to your LIBRARY and makes it Python3-compatible.
Compatibility means proper PEERDIRs, ADDINCLs and variant selection on PEERDIRs to multimodules.

If you'd like to use #include <Python.h> with Python3 specify USE\_PYTHON3 or better make it PY3\_LIBRARY.
If you'd like to use #include <Python.h> with Python2 specify USE\_PYTHON2 or better make it PY2\_LIBRARY.
If you'd like to use #include <Python.h> with both Python2 and Python3 convert your LIBRARY to PY23\_LIBRARY.

@see: [PY2\_LIBRARY](#module\_PY2\_LIBRARY), [PY3\_LIBRARY](#module\_PY3\_LIBRARY), [PY23\_LIBRARY](#multimodule\_PY23\_LIBRARY)

###### Macro [USE\_RECIPE][](path [arg1 arg2...]) <a name="macro_USE_RECIPE"></a>
Provides prepared environment via recipe for test.

Documentation: https://wiki.yandex-team.ru/yatool/test/recipes

###### Macro [USE\_SA\_PLUGINS][](FROM path/to/external/module1 NAME VAR\_NAME1 FROM path/to/external/module2 NAME VAR\_NAME2 ...) <a name="macro_USE_SA_PLUGINS"></a>
Select additional plugins for clang static analyzer, each path/to/external/module should declare target RESOURCES\_LIBRARY.
VAR\_NAME should be the same value that was passed into DECLARE\_EXTERNAL\_HOST\_RESOURCES\_BUNDLE as first argument.
See example in market/report/csa\_checks/static\_analyzer\_ymake.inc

###### Macro [USE\_SKIFF][]() _#wip, do not use_ <a name="macro_USE_SKIFF"></a>
Use mapreduce/yt/skiff\_proto/plugin for C++

###### Macro [USE\_UTIL][]() <a name="macro_USE_UTIL"></a>
Add dependency on util and C++ runtime
Note: This macro is intended for use in \_GO\_BASE\_UNIT like module when the module is build without util by default

###### Macro [VALIDATE\_DATA\_RESTART][](ext) <a name="macro_VALIDATE_DATA_RESTART"></a>
Change uid for resource validation tests. May be useful when sandbox resource ttl is changed, but test status is cached in CI.
You can change ext to change test's uid. For example VALIDATE\_DATA\_RESTART(X), where is X is current revision.

###### Macro [VALIDATE\_IN\_DIRS][] <a name="macro_VALIDATE_IN_DIRS"></a>
Not documented yet.

###### Macro [VCS\_INFO\_FILE][]([FILE out\_file]) <a name="macro_VCS_INFO_FILE"></a>
Enable saving vcs info as a json-file into PACKAGE

Info is saved to 'vcs\_info.json' by default.
Use FILE parameter if you want another name.

Note: macro can be used only once per module

###### Macro [VERSION][](Args...) <a name="macro_VERSION"></a>
Specify version of a module. Currently unused by build system, only informative.

###### Macro [VISIBILITY][](level) <a name="macro_VISIBILITY"></a>
This macro sets visibility level for symbols compiled for the current module. 'level'
may take only one of the following values: DEFAULT, HIDDEN.

###### Macro [VITE\_OUTPUT][](DirName) <a name="macro_VITE_OUTPUT"></a>
Not documented yet.

###### Macro [WEBPACK\_OUTPUT][](FirstDirName, DirNames...) <a name="macro_WEBPACK_OUTPUT"></a>
Not documented yet.

###### Macro [WERROR][]() <a name="macro_WERROR"></a>
Consider warnings as errors in the current module.
In the bright future will be removed, since WERROR is the default.
Priorities: NO\_COMPILER\_WARNINGS > NO\_WERROR > WERROR\_MODE > WERROR.

###### Macro [WINDOWS\_LONG\_PATH\_MANIFEST][]() <a name="macro_WINDOWS_LONG_PATH_MANIFEST"></a>
Not documented yet.

###### Macro [WINDOWS\_MANIFEST][](Manifest) <a name="macro_WINDOWS_MANIFEST"></a>
Not documented yet.

###### Macro [WITHOUT\_LICENSE\_TEXTS][]() <a name="macro_WITHOUT_LICENSE_TEXTS"></a>
This macro indicates that the module has no license text

###### Macro [WITH\_DYNAMIC\_LIBS][] <a name="macro_WITH_DYNAMIC_LIBS"></a>
$usage: WITH\_DYNAMIC\_LIBS() # restricted

Include dynamic libraries as extra PROGRAM/DLL outputs

###### Macro [WITH\_GROOVY][]() <a name="macro_WITH_GROOVY"></a>
Compile groovy source code in this java module

###### Macro [WITH\_JDK][]() <a name="macro_WITH_JDK"></a>
Add directory with JDK to JAVA\_PROGRAM output

###### Macro [WITH\_KAPT][]() <a name="macro_WITH_KAPT"></a>
Use kapt for as annotation processor

###### Macro [WITH\_KOTLIN][]() <a name="macro_WITH_KOTLIN"></a>
Compile kotlin source code in this java module

###### Macro [WITH\_KOTLINC\_ALLOPEN][](-flags) <a name="macro_WITH_KOTLINC_ALLOPEN"></a>
Enable allopen kotlin compiler plugin https://kotlinlang.org/docs/all-open-plugin.html

###### Macro [WITH\_KOTLINC\_LOMBOK][](-flags) <a name="macro_WITH_KOTLINC_LOMBOK"></a>
Enable lombok kotlin compiler plugin https://kotlinlang.org/docs/lombok.html

###### Macro [WITH\_KOTLINC\_NOARG][](-flags) <a name="macro_WITH_KOTLINC_NOARG"></a>
Enable noarg kotlin compiler plugin https://kotlinlang.org/docs/no-arg-plugin.html

###### Macro [WITH\_KOTLINC\_SERIALIZATION][]() <a name="macro_WITH_KOTLINC_SERIALIZATION"></a>
Enable serialization kotlin compiler plugin https://kotlinlang.org/docs/serialization.html

###### Macro [WITH\_KOTLIN\_GRPC][]() <a name="macro_WITH_KOTLIN_GRPC"></a>
Not documented yet.

###### Macro [WITH\_YA\_1931][]() <a name="macro_WITH_YA_1931"></a>
Interim macro to temporarily remove ALL\_SRCDIRS from being added to ktlint test sources.

###### Macro [XS\_PROTO][](InputProto Dir Outputs...) _# deprecated_ <a name="macro_XS_PROTO"></a>
Generate Perl code from protobuf.
In order to use this macro one should predict all outputs protoc will emit from input\_proto file and enlist those as outputs.

###### Macro [YABS\_GENERATE\_CONF][] <a name="macro_YABS_GENERATE_CONF"></a>
Not documented yet.

###### Macro [YABS\_GENERATE\_PHANTOM\_CONF\_PATCH][] <a name="macro_YABS_GENERATE_PHANTOM_CONF_PATCH"></a>
Not documented yet.

###### Macro [YABS\_GENERATE\_PHANTOM\_CONF\_TEST\_CHECK][] <a name="macro_YABS_GENERATE_PHANTOM_CONF_TEST_CHECK"></a>
Not documented yet.

###### Macro [YA\_CONF\_JSON][] <a name="macro_YA_CONF_JSON"></a>
Add passed ya.conf.json and all bottle's formula external files to resources
File MUST be arcadia root relative path (without "${ARCADIA\_ROOT}/" prefix).
NOTE:
  An external formula file referenced from ya.conf.json must be passed as an arcadia root relative path and
  should be located in any subdirectory of the ya.conf.json location ("build/" if we consider a production).
  The later restriction prevents problems in selectively checkouted arcadia.

###### Macro [YDL\_DESC\_USE\_BINARY][]() <a name="macro_YDL_DESC_USE_BINARY"></a>
Used in conjunction with BUILD\_YDL\_DESC. When enabled, all generated descriptors are binary.

@example:

    PACKAGE()
        YDL_DESC_USE_BINARY()
        BUILD_YDL_DESC(../types.ydl Event Event.ydld)
    END()

This will generate descriptor Event.ydld in a binary format.

###### Macro [YQL\_ABI\_VERSION][](major minor release)) <a name="macro_YQL_ABI_VERSION"></a>
Specifying the supported ABI for YQL\_UDF.

@see: [YQL\_UDF()](#multimodule\_YQL\_UDF)

###### Macro [YQL\_LAST\_ABI\_VERSION][]() <a name="macro_YQL_LAST_ABI_VERSION"></a>
Use the last ABI for YQL\_UDF

###### Macro [YT\_ORM\_PROTO\_YSON][](Files... OUT\_OPTS Opts...) <a name="macro_YT_ORM_PROTO_YSON"></a>
Generate .yson.go from .proto using yt/yt/orm/go/codegen/yson/internal/proto-yson-gen/cmd/proto-yson-gen

###### Macro [YT\_SPEC][](path1 [path2...]) <a name="macro_YT_SPEC"></a>
Allows you to specify json-files with YT task and operation specs,
which will be used to run test node in the YT.
Test must be marked with ya:yt tag.
Files must be relative to the root of Arcadia.

Documentation: https://wiki.yandex-team.ru/yatool/test/

 [DLL\_JAVA]: https://github.com/yandex/yatool/tree/main/build/conf/swig.conf?rev=14709839#L89
 [DOCS]: https://github.com/yandex/yatool/tree/main/build/conf/docs.conf?rev=14709839#L151
 [FBS\_LIBRARY]: https://github.com/yandex/yatool/tree/main/build/conf/fbs.conf?rev=14709839#L103
 [JAVA\_CONTRIB\_PROGRAM]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L244
 [JAVA\_PROGRAM]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L31
 [JTEST]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L153
 [JTEST\_FOR]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L207
 [JUNIT5]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L97
 [PACKAGE]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2377
 [PROTO\_LIBRARY]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L678
 [PY23\_LIBRARY]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L1020
 [PY23\_NATIVE\_LIBRARY]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L1047
 [PY23\_TEST]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L1072
 [PY3TEST]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L367
 [PY3\_PROGRAM]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L232
 [TS\_NEXT]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts_next.conf?rev=14709839#L59
 [TS\_PACKAGE]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts_package.conf?rev=14709839#L30
 [TS\_TSC]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts_tsc.conf?rev=14709839#L23
 [TS\_VITE]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts_vite.conf?rev=14709839#L60
 [TS\_WEBPACK]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts_webpack.conf?rev=14709839#L57
 [YQL\_UDF]: https://github.com/yandex/yatool/tree/main/build/conf/project_specific/yql_udf.conf?rev=14709839#L184
 [YQL\_UDF\_CONTRIB]: https://github.com/yandex/yatool/tree/main/build/conf/project_specific/yql_udf.conf?rev=14709839#L226
 [YQL\_UDF\_YDB]: https://github.com/yandex/yatool/tree/main/build/conf/project_specific/yql_udf.conf?rev=14709839#L205
 [BOOSTTEST]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1443
 [BOOSTTEST\_WITH\_MAIN]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1464
 [CI\_GROUP]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2419
 [CPP\_STYLE\_TEST\_16]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1655
 [DEFAULT\_IOS\_INTERFACE]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5590
 [DLL]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2186
 [DLL\_TOOL]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2203
 [DOCS\_LIBRARY]: https://github.com/yandex/yatool/tree/main/build/conf/docs.conf?rev=14709839#L84
 [EXECTEST]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1691
 [FAT\_OBJECT]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1996
 [FUZZ]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1399
 [GEN\_LIBRARY]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L563
 [GO\_DLL]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L932
 [GO\_LIBRARY]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L811
 [GO\_PROGRAM]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L828
 [GO\_TEST]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L952
 [GTEST]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1375
 [G\_BENCHMARK]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1729
 [IOS\_INTERFACE]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5579
 [JAVA\_CONTRIB]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L568
 [JAVA\_CONTRIB\_PROXY]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L518
 [JAVA\_LIBRARY]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L19
 [LIBRARY]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1879
 [PROGRAM]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1225
 [PROTO\_DESCRIPTIONS]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L845
 [PROTO\_REGISTRY]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L858
 [PY2MODULE]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L453
 [PY2TEST]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L317
 [PY2\_LIBRARY]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L544
 [PY2\_PROGRAM]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L200
 [PY3MODULE]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L472
 [PY3TEST\_BIN]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L339
 [PY3\_LIBRARY]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L585
 [PY3\_PROGRAM\_BIN]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L749
 [PYTEST\_BIN]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L300
 [PY\_ANY\_MODULE]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L395
 [RECURSIVE\_LIBRARY]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2052
 [RESOURCES\_LIBRARY]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1951
 [R\_MODULE]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2156
 [SO\_PROGRAM]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2215
 [TS\_TEST\_HERMIONE\_FOR]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts_test.conf?rev=14709839#L66
 [TS\_TEST\_JEST\_FOR]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts_test.conf?rev=14709839#L31
 [TS\_TEST\_PLAYWRIGHT\_FOR]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts_test.conf?rev=14709839#L100
 [UNION]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2441
 [UNITTEST]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1317
 [UNITTEST\_FOR]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1773
 [UNITTEST\_WITH\_CUSTOM\_ENTRY\_POINT]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1353
 [YQL\_PYTHON3\_UDF]: https://github.com/yandex/yatool/tree/main/build/conf/project_specific/yql_udf.conf?rev=14709839#L323
 [YQL\_PYTHON3\_UDF\_TEST]: https://github.com/yandex/yatool/tree/main/build/conf/project_specific/yql_udf.conf?rev=14709839#L372
 [YQL\_PYTHON\_UDF]: https://github.com/yandex/yatool/tree/main/build/conf/project_specific/yql_udf.conf?rev=14709839#L270
 [YQL\_PYTHON\_UDF\_PROGRAM]: https://github.com/yandex/yatool/tree/main/build/conf/project_specific/yql_udf.conf?rev=14709839#L297
 [YQL\_PYTHON\_UDF\_TEST]: https://github.com/yandex/yatool/tree/main/build/conf/project_specific/yql_udf.conf?rev=14709839#L358
 [YQL\_UDF\_MODULE]: https://github.com/yandex/yatool/tree/main/build/conf/project_specific/yql_udf.conf?rev=14709839#L151
 [YQL\_UDF\_MODULE\_CONTRIB]: https://github.com/yandex/yatool/tree/main/build/conf/project_specific/yql_udf.conf?rev=14709839#L163
 [YQL\_UDF\_TEST]: https://github.com/yandex/yatool/tree/main/build/conf/project_specific/yql_udf.conf?rev=14709839#L36
 [YQL\_UDF\_TEST\_CONTRIB]: https://github.com/yandex/yatool/tree/main/build/conf/project_specific/yql_udf.conf?rev=14709839#L65
 [YQL\_UDF\_YDB\_MODULE]: https://github.com/yandex/yatool/tree/main/build/conf/project_specific/yql_udf.conf?rev=14709839#L157
 [YQL\_UDF\_YDB\_TEST]: https://github.com/yandex/yatool/tree/main/build/conf/project_specific/yql_udf.conf?rev=14709839#L53
 [YT\_UNITTEST]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1343
 [Y\_BENCHMARK]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1709
 [ACCELEO]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L9
 [ADDINCL]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [ADDINCLSELF]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2957
 [ADD\_CHECK]: https://github.com/yandex/yatool/tree/main/build/plugins/ytest.py?rev=14709839#L696
 [ADD\_CHECK\_PY\_IMPORTS]: https://github.com/yandex/yatool/tree/main/build/plugins/_dart_fields.py?rev=14709839#L36
 [ADD\_CLANG\_TIDY]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1119
 [ADD\_COMPILABLE\_TRANSLATE]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2625
 [ADD\_COMPILABLE\_TRANSLIT]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2635
 [ADD\_DLLS\_TO\_JAR]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1737
 [ADD\_LINTER\_CHECK]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5823
 [ADD\_PYTEST\_BIN]: https://github.com/yandex/yatool/tree/main/build/plugins/_dart_fields.py?rev=14709839#L36
 [ADD\_YTEST]: https://github.com/yandex/yatool/tree/main/build/plugins/ytest.py?rev=14709839#L1380
 [ALLOCATOR]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2527
 [ALLOCATOR\_IMPL]: https://github.com/yandex/yatool/tree/main/build/conf/opensource.conf?rev=14709839#L100
 [ALL\_PYTEST\_SRCS]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L997
 [ALL\_PY\_SRCS]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L979
 [ALL\_RESOURCE\_FILES]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2696
 [ALL\_RESOURCE\_FILES\_FROM\_DIRS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2711
 [ALL\_SRCS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2331
 [ANNOTATION\_PROCESSOR]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1683
 [ARCHIVE]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3911
 [ARCHIVE\_ASM]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3889
 [ARCHIVE\_BY\_KEYS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3922
 [ASM\_PREINCLUDE]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4953
 [ASSERT]: https://github.com/yandex/yatool/tree/main/build/plugins/macros_with_error.py?rev=14709839#L28
 [BENCHMARK\_OPTS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1748
 [BISON\_FLAGS]: https://github.com/yandex/yatool/tree/main/build/conf/bison_lex.conf?rev=14709839#L56
 [BISON\_GEN\_C]: https://github.com/yandex/yatool/tree/main/build/conf/bison_lex.conf?rev=14709839#L63
 [BISON\_GEN\_CPP]: https://github.com/yandex/yatool/tree/main/build/conf/bison_lex.conf?rev=14709839#L71
 [BISON\_HEADER]: https://github.com/yandex/yatool/tree/main/build/conf/bison_lex.conf?rev=14709839#L93
 [BISON\_NO\_HEADER]: https://github.com/yandex/yatool/tree/main/build/conf/bison_lex.conf?rev=14709839#L103
 [BPF]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4742
 [BPF\_STATIC]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4756
 [BUILDWITH\_CYTHON\_C]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3795
 [BUILDWITH\_CYTHON\_CPP]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3764
 [BUILDWITH\_RAGEL6]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3833
 [BUILD\_CATBOOST]: https://github.com/yandex/yatool/tree/main/build/conf/project_specific/other.conf?rev=14709839#L9
 [BUILD\_ONLY\_IF]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [BUILD\_YDL\_DESC]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3491
 [BUNDLE]: https://github.com/yandex/yatool/tree/main/build/plugins/bundle.py?rev=14709839#L4
 [CFLAGS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4028
 [CGO\_CFLAGS]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L338
 [CGO\_LDFLAGS]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L347
 [CGO\_SRCS]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L321
 [CHECK\_ALLOWED\_PATH]: https://github.com/yandex/yatool/tree/main/build/internal/plugins/container_layers.py?rev=14709839#L4
 [CHECK\_CONTRIB\_CREDITS]: https://github.com/yandex/yatool/tree/main/build/plugins/credits.py?rev=14709839#L9
 [CHECK\_DEPENDENT\_DIRS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L459
 [CHECK\_JAVA\_DEPS]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1446
 [CLANG\_EMIT\_AST\_CXX]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4703
 [CLANG\_EMIT\_AST\_CXX\_RUN\_TOOL]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5873
 [CLEAN\_TEXTREL]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2071
 [CMAKE\_EXPORTED\_TARGET\_NAME]: https://github.com/yandex/yatool/tree/main/build/conf/opensource.conf?rev=14709839#L95
 [COLLECT\_FRONTEND\_FILES]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5627
 [COLLECT\_GO\_SWAGGER\_FILES]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L5
 [COLLECT\_JINJA\_TEMPLATES]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5157
 [COMPILE\_C\_AS\_CXX]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4666
 [COMPILE\_LUA]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3415
 [COMPILE\_LUA\_21]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3433
 [COMPILE\_LUA\_OPENRESTY]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3451
 [COMPILE\_SWIFT\_MODULE]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5635
 [CONFIGURE\_FILE]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4007
 [CONFTEST\_LOAD\_POLICY\_LOCAL]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1600
 [CONLYFLAGS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4051
 [COPY]: https://github.com/yandex/yatool/tree/main/build/plugins/cp.py?rev=14709839#L6
 [COPY\_FILE]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2669
 [COPY\_FILE\_WITH\_CONTEXT]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2678
 [CPP\_ADDINCL]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5017
 [CPP\_ENUMS\_SERIALIZATION]: https://github.com/yandex/yatool/tree/main/build/plugins/pybuild.py?rev=14709839#L820
 [CPP\_PROTOLIBS\_DEBUG\_INFO]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L71
 [CPP\_PROTO\_PLUGIN]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L241
 [CPP\_PROTO\_PLUGIN0]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L227
 [CPP\_PROTO\_PLUGIN2]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L252
 [CREATE\_BUILDINFO\_FOR]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3978
 [CREATE\_INIT\_PY\_STRUCTURE]: https://github.com/yandex/yatool/tree/main/build/plugins/create_init_py.py?rev=14709839#L4
 [CREDITS\_DISCLAIMER]: https://github.com/yandex/yatool/tree/main/build/plugins/credits.py?rev=14709839#L4
 [CTEMPLATE\_VARNAMES]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4682
 [CUDA\_NVCC\_FLAGS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4065
 [CUSTOM\_CONTRIB\_TYPESCRIPT]: https://github.com/yandex/yatool/tree/main/build/conf/ts/node_modules.conf?rev=14709839#L15
 [CUSTOM\_LINK\_STEP\_SCRIPT]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1273
 [CXXFLAGS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4058
 [CYTHON\_FLAGS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4082
 [DARWIN\_SIGNED\_RESOURCE]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5570
 [DARWIN\_STRINGS\_RESOURCE]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5566
 [DATA]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1539
 [DATA\_FILES]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1551
 [DEB\_VERSION]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4307
 [DECIMAL\_MD5\_LOWER\_32\_BITS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3990
 [DECLARE\_EXTERNAL\_HOST\_RESOURCES\_BUNDLE]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [DECLARE\_EXTERNAL\_HOST\_RESOURCES\_BUNDLE\_BY\_JSON]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [DECLARE\_EXTERNAL\_HOST\_RESOURCES\_PACK]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [DECLARE\_EXTERNAL\_RESOURCE]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [DECLARE\_EXTERNAL\_RESOURCE\_BY\_JSON]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [DECLARE\_IN\_DIRS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4518
 [DEFAULT]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [DEFAULT\_JAVA\_SRCS\_LAYOUT]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L381
 [DEFAULT\_JDK\_VERSION]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L2052
 [DEFAULT\_JUNIT\_JAVA\_SRCS\_LAYOUT]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L393
 [DEPENDENCY\_MANAGEMENT]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1774
 [DEPENDS]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [DIRECT\_DEPS\_ONLY]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1926
 [DISABLE]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [DISABLE\_DATA\_VALIDATION]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1524
 [DLL\_FOR]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [DOCS\_CONFIG]: https://github.com/yandex/yatool/tree/main/build/conf/docs.conf?rev=14709839#L285
 [DOCS\_COPY\_FILES]: https://github.com/yandex/yatool/tree/main/build/conf/docs.conf?rev=14709839#L13
 [DOCS\_DIR]: https://github.com/yandex/yatool/tree/main/build/conf/docs.conf?rev=14709839#L241
 [DOCS\_INCLUDE\_SOURCES]: https://github.com/yandex/yatool/tree/main/build/conf/docs.conf?rev=14709839#L309
 [DOCS\_VARS]: https://github.com/yandex/yatool/tree/main/build/conf/docs.conf?rev=14709839#L297
 [DYNAMIC\_LIBRARY\_FROM]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2173
 [ELSE]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [ELSEIF]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [EMBED\_JAVA\_VCS\_INFO]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L276
 [ENABLE]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [ENABLE\_PREVIEW]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1645
 [END]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [ENDIF]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [ENV]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1593
 [EVLOG\_CMD]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L863
 [EXCLUDE]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1691
 [EXCLUDE\_TAGS]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [EXPLICIT\_DATA]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1561
 [EXPLICIT\_OUTPUTS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4864
 [EXPORTS\_SCRIPT]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1241
 [EXPORT\_ALL\_DYNAMIC\_SYMBOLS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1255
 [EXTERNAL\_JAR]: https://github.com/yandex/yatool/tree/main/build/plugins/java.py?rev=14709839#L240
 [EXTERNAL\_RESOURCE]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [EXTRADIR]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [EXTRALIBS\_STATIC]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2618
 [FBS\_CMD]: https://github.com/yandex/yatool/tree/main/build/conf/fbs.conf?rev=14709839#L142
 [FBS\_NAMESPACE]: https://github.com/yandex/yatool/tree/main/build/conf/fbs.conf?rev=14709839#L85
 [FBS\_TO\_PY2SRC]: https://github.com/yandex/yatool/tree/main/build/conf/fbs.conf?rev=14709839#L28
 [FILES]: https://github.com/yandex/yatool/tree/main/build/plugins/files.py?rev=14709839#L1
 [FLATC\_FLAGS]: https://github.com/yandex/yatool/tree/main/build/conf/fbs.conf?rev=14709839#L10
 [FLAT\_JOIN\_SRCS\_GLOBAL]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2834
 [FLEX\_FLAGS]: https://github.com/yandex/yatool/tree/main/build/conf/bison_lex.conf?rev=14709839#L49
 [FLEX\_GEN\_C]: https://github.com/yandex/yatool/tree/main/build/conf/bison_lex.conf?rev=14709839#L79
 [FLEX\_GEN\_CPP]: https://github.com/yandex/yatool/tree/main/build/conf/bison_lex.conf?rev=14709839#L86
 [FORK\_SUBTESTS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2766
 [FORK\_TESTS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2752
 [FORK\_TEST\_FILES]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2792
 [FROM\_ARCHIVE]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4651
 [FROM\_SANDBOX]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4632
 [FULL\_JAVA\_SRCS]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L371
 [FUNCTION\_ORDERING\_FILE]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L139
 [FUZZ\_DICTS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1476
 [FUZZ\_OPTS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1495
 [GENERATE\_ENUM\_SERIALIZATION]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4286
 [GENERATE\_ENUM\_SERIALIZATION\_WITH\_HEADER]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4298
 [GENERATE\_PY\_PROTOS]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L608
 [GENERATE\_SCRIPT]: https://github.com/yandex/yatool/tree/main/build/plugins/java.py?rev=14709839#L41
 [GENERATE\_YT\_RECORD]: https://github.com/yandex/yatool/tree/main/build/conf/project_specific/yt.conf?rev=14709839#L1
 [GEN\_SCHEEME2]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4380
 [GLOBAL\_CFLAGS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4036
 [GLOBAL\_SRCS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2313
 [GOLANG\_VERSION]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L170
 [GO\_ASM\_FLAGS]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L132
 [GO\_BENCH\_TIMEOUT]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L941
 [GO\_CGO1\_FLAGS]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L140
 [GO\_CGO2\_FLAGS]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L148
 [GO\_COMPILE\_FLAGS]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L156
 [GO\_EMBED\_BINDIR]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L453
 [GO\_EMBED\_DIR]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L420
 [GO\_EMBED\_PATTERN]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L384
 [GO\_EMBED\_TEST\_DIR]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L428
 [GO\_EMBED\_XTEST\_DIR]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L436
 [GO\_FAKE\_OUTPUT]: https://github.com/yandex/yatool/tree/main/devtools/ymake/plugins/plugin_go_fake_output_handler.cpp?rev=14709839#L110
 [GO\_GRPC\_GATEWAY\_SRCS]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L518
 [GO\_GRPC\_GATEWAY\_SWAGGER\_SRCS]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L526
 [GO\_GRPC\_GATEWAY\_V2\_OPENAPI\_SRCS]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L573
 [GO\_GRPC\_GATEWAY\_V2\_SRCS]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L591
 [GO\_LDFLAGS]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L330
 [GO\_LINK\_FLAGS]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L164
 [GO\_MOCKGEN\_CONTRIB\_FROM]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L987
 [GO\_MOCKGEN\_FROM]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L981
 [GO\_MOCKGEN\_MOCKS]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L1018
 [GO\_MOCKGEN\_REFLECT]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L998
 [GO\_MOCKGEN\_TYPES]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L993
 [GO\_PACKAGE\_NAME]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L276
 [GO\_PROTO\_PLUGIN]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L355
 [GO\_PROTO\_USE\_V2]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L585
 [GO\_SKIP\_TESTS]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L358
 [GO\_TEST\_EMBED\_BINDIR]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L461
 [GO\_TEST\_EMBED\_PATTERN]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L392
 [GO\_TEST\_FOR]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [GO\_TEST\_SRCS]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L295
 [GO\_XTEST\_EMBED\_BINDIR]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L469
 [GO\_XTEST\_EMBED\_PATTERN]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L400
 [GO\_XTEST\_SRCS]: https://github.com/yandex/yatool/tree/main/build/conf/go.conf?rev=14709839#L306
 [GRPC]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L557
 [GRPC\_WITH\_GMOCK]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L578
 [HEADERS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5854
 [IDEA\_EXCLUDE\_DIRS]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1603
 [IDEA\_MODULE\_NAME]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1623
 [IDEA\_RESOURCE\_DIRS]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1613
 [IF]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [INCLUDE]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [INCLUDE\_ONCE]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [INCLUDE\_TAGS]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [INDUCED\_DEPS]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [IOS\_APP\_ASSETS\_FLAGS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5562
 [IOS\_APP\_COMMON\_FLAGS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5556
 [IOS\_APP\_SETTINGS]: https://github.com/yandex/yatool/tree/main/build/plugins/ios_app_settings.py?rev=14709839#L5
 [IOS\_ASSETS]: https://github.com/yandex/yatool/tree/main/build/plugins/ios_assets.py?rev=14709839#L6
 [JAR\_ANNOTATION\_PROCESSOR]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L457
 [JAR\_EXCLUDE]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1990
 [JAR\_INCLUDE]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1982
 [JAR\_MAIN\_CLASS]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L904
 [JAR\_RESOURCE]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L540
 [JAVAC\_FLAGS]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1633
 [JAVA\_DEPENDENCIES\_CONFIGURATION]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1966
 [JAVA\_EXTERNAL\_DEPENDENCIES]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1935
 [JAVA\_IGNORE\_CLASSPATH\_CLASH\_FOR]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5526
 [JAVA\_MODULE]: https://github.com/yandex/yatool/tree/main/build/plugins/java.py?rev=14709839#L57
 [JAVA\_PROTO\_PLUGIN]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L189
 [JAVA\_RESOURCE]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L799
 [JAVA\_SRCS]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1728
 [JAVA\_TEST]: https://github.com/yandex/yatool/tree/main/build/plugins/_dart_fields.py?rev=14709839#L36
 [JAVA\_TEST\_DEPS]: https://github.com/yandex/yatool/tree/main/build/plugins/_dart_fields.py?rev=14709839#L36
 [JDK\_VERSION]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L2042
 [JOIN\_SRCS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2813
 [JOIN\_SRCS\_GLOBAL]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2824
 [JUNIT\_TESTS\_JAR]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L89
 [JVM\_ARGS]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1435
 [KAPT\_ANNOTATION\_PROCESSOR]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L648
 [KAPT\_ANNOTATION\_PROCESSOR\_CLASSPATH]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L655
 [KAPT\_OPTS]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L641
 [KOTLINC\_FLAGS]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1831
 [KTLINT\_BASELINE\_FILE]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L2079
 [LARGE\_FILES]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4642
 [LDFLAGS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4018
 [LICENSE]: https://github.com/yandex/yatool/tree/main/build/conf/license.conf?rev=14709839#L26
 [LICENSE\_RESTRICTION]: https://github.com/yandex/yatool/tree/main/build/conf/license.conf?rev=14709839#L43
 [LICENSE\_RESTRICTION\_EXCEPTIONS]: https://github.com/yandex/yatool/tree/main/build/conf/license.conf?rev=14709839#L66
 [LICENSE\_TEXTS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5770
 [LINKER\_SCRIPT]: https://github.com/yandex/yatool/tree/main/build/plugins/linker_script.py?rev=14709839#L1
 [LINK\_EXEC\_DYN\_LIB\_IMPL]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1045
 [LINK\_EXE\_IMPL]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1039
 [LINT]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1650
 [LIST\_PROTO]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L636
 [LJ\_21\_ARCHIVE]: https://github.com/yandex/yatool/tree/main/build/plugins/lj_archive.py?rev=14709839#L25
 [LJ\_ARCHIVE]: https://github.com/yandex/yatool/tree/main/build/plugins/lj_archive.py?rev=14709839#L1
 [LLVM\_BC]: https://github.com/yandex/yatool/tree/main/build/plugins/llvm_bc.py?rev=14709839#L4
 [LLVM\_COMPILE\_C]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4727
 [LLVM\_COMPILE\_CXX]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4712
 [LLVM\_COMPILE\_LL]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4765
 [LLVM\_LINK]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4775
 [LLVM\_LLC]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4796
 [LLVM\_OPT]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4785
 [LOCAL\_JAR]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L550
 [LOCAL\_SOURCES\_JAR]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L555
 [MACROS\_WITH\_ERROR]: https://github.com/yandex/yatool/tree/main/build/plugins/macros_with_error.py?rev=14709839#L8
 [MANUAL\_GENERATION]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3142
 [MASMFLAGS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4043
 [MAVEN\_GROUP\_ID]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1671
 [MESSAGE]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [MODULEWISE\_LICENSE\_RESTRICTION]: https://github.com/yandex/yatool/tree/main/build/conf/license.conf?rev=14709839#L58
 [MSVC\_FLAGS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5805
 [NEED\_CHECK]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4316
 [NEED\_REVIEW]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4334
 [NGINX\_MODULES]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5747
 [NO\_BUILD\_IF]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [NO\_CHECK\_IMPORTS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4873
 [NO\_CLANG\_COVERAGE]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4247
 [NO\_CLANG\_TIDY]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4259
 [NO\_COMPILER\_WARNINGS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4105
 [NO\_CONTRIB\_TYPESCRIPT]: https://github.com/yandex/yatool/tree/main/build/conf/ts/node_modules.conf?rev=14709839#L19
 [NO\_CPU\_CHECK]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2950
 [NO\_CYTHON\_COVERAGE]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L922
 [NO\_DEBUG\_INFO]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4673
 [NO\_DOCTESTS]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L275
 [NO\_EXPORT\_DYNAMIC\_SYMBOLS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1248
 [NO\_EXTENDED\_SOURCE\_SEARCH]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L220
 [NO\_IMPORT\_TRACING]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L913
 [NO\_JOIN\_SRC]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4219
 [NO\_LIBC]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4173
 [NO\_LINT]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1643
 [NO\_LTO]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L373
 [NO\_MYPY]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L451
 [NO\_NEED\_CHECK]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4324
 [NO\_OPTIMIZE]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4095
 [NO\_OPTIMIZE\_PY\_PROTOS]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L139
 [NO\_PLATFORM]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4184
 [NO\_PROFILE\_RUNTIME]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4255
 [NO\_PYTHON\_COVERAGE]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L905
 [NO\_RUNTIME]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4162
 [NO\_SANITIZE]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4227
 [NO\_SANITIZE\_COVERAGE]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4239
 [NO\_SPLIT\_DWARF]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2602
 [NO\_SSE4]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2942
 [NO\_TS\_TYPECHECK]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts_test.conf?rev=14709839#L227
 [NO\_UTIL]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4151
 [NO\_WERROR]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4121
 [NO\_WSHADOW]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4127
 [NO\_YMAKE\_PYTHON3]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L178
 [NVCC\_DEVICE\_LINK]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4074
 [ONLY\_TAGS]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [OPENSOURCE\_EXPORT\_REPLACEMENT]: https://github.com/yandex/yatool/tree/main/build/conf/opensource.conf?rev=14709839#L70
 [OPENSOURCE\_EXPORT\_REPLACEMENT\_BY\_OS]: https://github.com/yandex/yatool/tree/main/build/conf/opensource.conf?rev=14709839#L79
 [ORIGINAL\_SOURCE]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5757
 [OWNER]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [PACK]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2357
 [PACKAGE\_STRICT]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2362
 [PACK\_GLOBALS\_IN\_LIBRARY]: https://github.com/yandex/yatool/tree/main/build/conf/linkers/ld.conf?rev=14709839#L367
 [PARTITIONED\_RECURSE]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [PARTITIONED\_RECURSE\_FOR\_TESTS]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [PARTITIONED\_RECURSE\_ROOT\_RELATIVE]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [PEERDIR]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [PIRE\_INLINE]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3900
 [PIRE\_INLINE\_CMD]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3895
 [POPULATE\_CPP\_COVERAGE\_FLAGS]: https://github.com/yandex/yatool/tree/main/build/conf/coverage_full_instrumentation.conf?rev=14709839#L3
 [PREPARE\_INDUCED\_DEPS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4444
 [PROCESS\_DOCS]: https://github.com/yandex/yatool/tree/main/build/plugins/docs.py?rev=14709839#L38
 [PROCESS\_MKDOCS]: https://github.com/yandex/yatool/tree/main/build/internal/plugins/mkdocs.py?rev=14709839#L38
 [PROTO2FBS]: https://github.com/yandex/yatool/tree/main/build/conf/fbs.conf?rev=14709839#L151
 [PROTOC\_FATAL\_WARNINGS]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L119
 [PROTO\_ADDINCL]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L92
 [PROTO\_CMD]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L868
 [PROTO\_NAMESPACE]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L109
 [PROVIDES]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [PYTHON2\_ADDINCL]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L777
 [PYTHON2\_MODULE]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L482
 [PYTHON3\_ADDINCL]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L825
 [PYTHON3\_MODULE]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L494
 [PYTHON\_PATH]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1623
 [PY\_CONSTRUCTOR]: https://github.com/yandex/yatool/tree/main/build/plugins/pybuild.py?rev=14709839#L788
 [PY\_DOCTESTS]: https://github.com/yandex/yatool/tree/main/build/plugins/pybuild.py?rev=14709839#L715
 [PY\_ENUMS\_SERIALIZATION]: https://github.com/yandex/yatool/tree/main/build/plugins/pybuild.py?rev=14709839#L803
 [PY\_EXTRALIBS]: https://github.com/yandex/yatool/tree/main/build/plugins/extralibs.py?rev=14709839#L1
 [PY\_EXTRA\_LINT\_FILES]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L1008
 [PY\_MAIN]: https://github.com/yandex/yatool/tree/main/build/plugins/pybuild.py?rev=14709839#L771
 [PY\_NAMESPACE]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L530
 [PY\_PROTOS\_FOR]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [PY\_PROTO\_PLUGIN]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L162
 [PY\_PROTO\_PLUGIN2]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L174
 [PY\_REGISTER]: https://github.com/yandex/yatool/tree/main/build/plugins/pybuild.py?rev=14709839#L733
 [PY\_SRCS]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L953
 [REAL\_LINK\_DYN\_LIB\_IMPL]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1033
 [REAL\_LINK\_EXEC\_DYN\_LIB\_IMPL]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1027
 [REAL\_LINK\_EXE\_IMPL]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1021
 [RECURSE]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [RECURSE\_FOR\_TESTS]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [RECURSE\_ROOT\_RELATIVE]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [REGISTER\_SANDBOX\_IMPORT]: https://github.com/yandex/yatool/tree/main/build/internal/plugins/sandbox_registry.py?rev=14709839#L6
 [REGISTER\_YQL\_PYTHON\_UDF]: https://github.com/yandex/yatool/tree/main/build/plugins/yql_python_udf.py?rev=14709839#L11
 [REQUIREMENTS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1584
 [REQUIRES]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L437
 [RESOLVE\_PROTO]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L598
 [RESOURCE]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L493
 [RESOURCE\_FILES]: https://github.com/yandex/yatool/tree/main/build/plugins/res.py?rev=14709839#L14
 [RESTRICT\_PATH]: https://github.com/yandex/yatool/tree/main/build/plugins/macros_with_error.py?rev=14709839#L13
 [RUN]: https://github.com/yandex/yatool/tree/main/build/plugins/ytest.py?rev=14709839#L902
 [RUN\_ANTLR]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4960
 [RUN\_ANTLR4]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4968
 [RUN\_ANTLR4\_CPP]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4990
 [RUN\_ANTLR4\_CPP\_SPLIT]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4982
 [RUN\_ANTLR4\_GO]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4998
 [RUN\_ANTLR4\_PYTHON]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5011
 [RUN\_JAVA\_PROGRAM]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L449
 [RUN\_LUA]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4574
 [RUN\_PROGRAM]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4548
 [RUN\_PYTHON3]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4599
 [SDBUS\_CPP\_ADAPTOR]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5726
 [SDBUS\_CPP\_PROXY]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5732
 [SELECT\_CLANG\_SA\_CONFIG]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L155
 [SET]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [SETUP\_EXECTEST]: https://github.com/yandex/yatool/tree/main/build/plugins/_dart_fields.py?rev=14709839#L36
 [SETUP\_PYTEST\_BIN]: https://github.com/yandex/yatool/tree/main/build/plugins/ytest.py?rev=14709839#L895
 [SETUP\_RUN\_PYTHON]: https://github.com/yandex/yatool/tree/main/build/plugins/ytest.py?rev=14709839#L945
 [SET\_APPEND]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [SET\_APPEND\_WITH\_GLOBAL]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [SET\_COMPILE\_OUTPUTS\_MODIFIERS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2970
 [SET\_CPP\_COVERAGE\_FLAGS]: https://github.com/yandex/yatool/tree/main/build/plugins/coverage.py?rev=14709839#L61
 [SET\_RESOURCE\_MAP\_FROM\_JSON]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [SET\_RESOURCE\_URI\_FROM\_JSON]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [SIZE]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2804
 [SKIP\_TEST]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1632
 [SOURCE\_GROUP]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [SPLIT\_CODEGEN]: https://github.com/yandex/yatool/tree/main/build/internal/plugins/split_codegen.py?rev=14709839#L9
 [SPLIT\_DWARF]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2594
 [SPLIT\_FACTOR]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2780
 [SRC]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3517
 [SRCDIR]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [SRCS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3536
 [SRC\_C\_AMX]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3673
 [SRC\_C\_AVX]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3649
 [SRC\_C\_AVX2]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3657
 [SRC\_C\_AVX512]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3665
 [SRC\_C\_NO\_LTO]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3755
 [SRC\_C\_PCLMUL]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3690
 [SRC\_C\_PIC]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3747
 [SRC\_C\_SSE2]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3609
 [SRC\_C\_SSE3]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3617
 [SRC\_C\_SSE4]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3633
 [SRC\_C\_SSE41]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3641
 [SRC\_C\_SSSE3]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3625
 [SRC\_C\_XOP]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3682
 [SRC\_RESOURCE]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L545
 [STRIP]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4089
 [STYLE]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1660
 [STYLE\_CPP]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5847
 [STYLE\_PYTHON]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L255
 [STYLE\_RUFF]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L266
 [SUBSCRIBER]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [SUPPRESSIONS]: https://github.com/yandex/yatool/tree/main/build/plugins/suppressions.py?rev=14709839#L1
 [SYMLINK]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4386
 [SYSTEM\_PROPERTIES]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1424
 [TAG]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1573
 [TASKLET]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5031
 [TASKLET\_REG]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5048
 [TASKLET\_REG\_EXT]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5063
 [TEST\_CWD]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2494
 [TEST\_DATA]: https://github.com/yandex/yatool/tree/main/build/plugins/ytest.py?rev=14709839#L105
 [TEST\_JAVA\_CLASSPATH\_CMD\_TYPE]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1949
 [TEST\_SRCS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1520
 [THINLTO\_CACHE]: https://github.com/yandex/yatool/tree/main/build/conf/linkers/ld.conf?rev=14709839#L408
 [TIMEOUT]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2725
 [TOOLCHAIN]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5886
 [TOUCH\_RANDOM\_FILE]: https://github.com/yandex/yatool/tree/main/build/internal/plugins/touch_random_file.py?rev=14709839#L16
 [TS\_CONFIG]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts.conf?rev=14709839#L22
 [TS\_ESLINT\_CONFIG]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts.conf?rev=14709839#L109
 [TS\_EXCLUDE\_FILES\_GLOB]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts.conf?rev=14709839#L67
 [TS\_FILES]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts.conf?rev=14709839#L175
 [TS\_FILES\_GLOB]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts.conf?rev=14709839#L182
 [TS\_NEXT\_CONFIG]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts_next.conf?rev=14709839#L11
 [TS\_NEXT\_EXPERIMENTAL\_COMPILE]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts_next.conf?rev=14709839#L29
 [TS\_NEXT\_OUTPUT]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts_next.conf?rev=14709839#L25
 [TS\_STYLELINT]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts_test.conf?rev=14709839#L267
 [TS\_TEST\_CONFIG]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts_test.conf?rev=14709839#L172
 [TS\_TEST\_DATA]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts_test.conf?rev=14709839#L209
 [TS\_TEST\_DEPENDS\_ON\_BUILD]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts_test.conf?rev=14709839#L218
 [TS\_TEST\_FOR]: https://github.com/yandex/yatool/tree/main/devtools/ymake/yndex/builtin.cpp?rev=14709839#L14
 [TS\_TEST\_SRCS]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts_test.conf?rev=14709839#L186
 [TS\_TYPECHECK]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts_test.conf?rev=14709839#L244
 [TS\_VITE\_CONFIG]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts_vite.conf?rev=14709839#L10
 [TS\_VITE\_OUTPUT]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts_vite.conf?rev=14709839#L24
 [TS\_WEBPACK\_CONFIG]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts_webpack.conf?rev=14709839#L10
 [TS\_WEBPACK\_OUTPUT]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts_webpack.conf?rev=14709839#L22
 [UBERJAR]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1479
 [UBERJAR\_APPENDING\_TRANSFORMER]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1579
 [UBERJAR\_HIDE\_EXCLUDE\_PATTERN]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1508
 [UBERJAR\_HIDE\_INCLUDE\_PATTERN]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1523
 [UBERJAR\_HIDING\_PREFIX]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1493
 [UBERJAR\_MANIFEST\_TRANSFORMER\_ATTRIBUTE]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1563
 [UBERJAR\_MANIFEST\_TRANSFORMER\_MAIN]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1550
 [UBERJAR\_PATH\_EXCLUDE\_PREFIX]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1537
 [UBERJAR\_SERVICES\_RESOURCE\_TRANSFORMER]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1592
 [UDF\_NO\_PROBE]: https://github.com/yandex/yatool/tree/main/build/conf/project_specific/yql_udf.conf?rev=14709839#L26
 [UPDATE\_VCS\_JAVA\_INFO\_NODEP]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3951
 [USE\_ANNOTATION\_PROCESSOR]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L477
 [USE\_COMMON\_GOOGLE\_APIS]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L312
 [USE\_CXX]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4194
 [USE\_DYNAMIC\_CUDA]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1263
 [USE\_ERROR\_PRONE]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1454
 [USE\_JAVALITE]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L476
 [USE\_KTLINT\_OLD]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L2069
 [USE\_LINKER\_GOLD]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L828
 [USE\_LLVM\_BC14]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4689
 [USE\_LLVM\_BC16]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4694
 [USE\_MODERN\_FLEX]: https://github.com/yandex/yatool/tree/main/build/conf/bison_lex.conf?rev=14709839#L111
 [USE\_MODERN\_FLEX\_WITH\_HEADER]: https://github.com/yandex/yatool/tree/main/build/conf/bison_lex.conf?rev=14709839#L122
 [USE\_NASM]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4211
 [USE\_OLD\_FLEX]: https://github.com/yandex/yatool/tree/main/build/conf/bison_lex.conf?rev=14709839#L131
 [USE\_PLANTUML]: https://github.com/yandex/yatool/tree/main/build/conf/docs.conf?rev=14709839#L228
 [USE\_PYTHON2]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L874
 [USE\_PYTHON3]: https://github.com/yandex/yatool/tree/main/build/conf/python.conf?rev=14709839#L891
 [USE\_RECIPE]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1611
 [USE\_SA\_PLUGINS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L164
 [USE\_SKIFF]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L263
 [USE\_UTIL]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4202
 [VALIDATE\_DATA\_RESTART]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L2735
 [VALIDATE\_IN\_DIRS]: https://github.com/yandex/yatool/tree/main/build/plugins/macros_with_error.py?rev=14709839#L35
 [VCS\_INFO\_FILE]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3965
 [VERSION]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4343
 [VISIBILITY]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5704
 [VITE\_OUTPUT]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts_vite.conf?rev=14709839#L30
 [WEBPACK\_OUTPUT]: https://github.com/yandex/yatool/tree/main/build/conf/ts/ts_webpack.conf?rev=14709839#L28
 [WERROR]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L4114
 [WINDOWS\_LONG\_PATH\_MANIFEST]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5689
 [WINDOWS\_MANIFEST]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5684
 [WITHOUT\_LICENSE\_TEXTS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5778
 [WITH\_DYNAMIC\_LIBS]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1015
 [WITH\_GROOVY]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1822
 [WITH\_JDK]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1784
 [WITH\_KAPT]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1813
 [WITH\_KOTLIN]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1802
 [WITH\_KOTLINC\_ALLOPEN]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1848
 [WITH\_KOTLINC\_LOMBOK]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1859
 [WITH\_KOTLINC\_NOARG]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1871
 [WITH\_KOTLINC\_SERIALIZATION]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L1883
 [WITH\_KOTLIN\_GRPC]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L200
 [WITH\_YA\_1931]: https://github.com/yandex/yatool/tree/main/build/conf/java.conf?rev=14709839#L2089
 [XS\_PROTO]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L514
 [YABS\_GENERATE\_CONF]: https://github.com/yandex/yatool/tree/main/build/internal/plugins/yabs_generate_conf.py?rev=14709839#L10
 [YABS\_GENERATE\_PHANTOM\_CONF\_PATCH]: https://github.com/yandex/yatool/tree/main/build/internal/plugins/yabs_generate_conf.py?rev=14709839#L41
 [YABS\_GENERATE\_PHANTOM\_CONF\_TEST\_CHECK]: https://github.com/yandex/yatool/tree/main/build/internal/plugins/yabs_generate_conf.py?rev=14709839#L51
 [YA\_CONF\_JSON]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L5816
 [YDL\_DESC\_USE\_BINARY]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L3508
 [YQL\_ABI\_VERSION]: https://github.com/yandex/yatool/tree/main/build/conf/project_specific/yql_udf.conf?rev=14709839#L250
 [YQL\_LAST\_ABI\_VERSION]: https://github.com/yandex/yatool/tree/main/build/conf/project_specific/yql_udf.conf?rev=14709839#L259
 [YT\_ORM\_PROTO\_YSON]: https://github.com/yandex/yatool/tree/main/build/conf/proto.conf?rev=14709839#L380
 [YT\_SPEC]: https://github.com/yandex/yatool/tree/main/build/ymake.core.conf?rev=14709839#L1509
