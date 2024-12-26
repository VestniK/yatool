from __future__ import absolute_import
import os.path

import six

import core.yarg
import devtools.ya.core.config
import devtools.ya.core.common_opts

import build.build_opts
import build.compilation_database as bcd

import devtools.ya.ide.ide_common
import devtools.ya.ide.clion2016
import devtools.ya.ide.idea
import devtools.ya.ide.qt
import devtools.ya.ide.remote_ide_qt
import devtools.ya.ide.goland
import devtools.ya.ide.pycharm
import devtools.ya.ide.venv
import devtools.ya.ide.vscode_all
import devtools.ya.ide.vscode_clangd
import devtools.ya.ide.vscode_go
import devtools.ya.ide.vscode_py
import devtools.ya.ide.vscode_ts
import devtools.ya.ide.vscode.opts

import yalibrary.platform_matcher as pm

import devtools.ya.app
import app_config

if app_config.in_house:
    import devtools.ya.ide.fsnotifier

from core.yarg.help_level import HelpLevel

if six.PY3:
    import devtools.ya.ide.gradle


class TidyOptions(core.yarg.Options):
    def __init__(self):
        self.setup_tidy = False

    @staticmethod
    def consumer():
        return [
            core.yarg.ArgConsumer(
                ['--setup-tidy'],
                help="Setup default arcadia's clang-tidy config in a project",
                hook=core.yarg.SetConstValueHook('setup_tidy', True),
                group=core.yarg.BULLET_PROOF_OPT_GROUP,
            ),
            core.yarg.ConfigConsumer('setup_tidy'),
        ]


class CLionOptions(core.yarg.Options):
    CLION_OPT_GROUP = core.yarg.Group('CLion project options', 0)

    def __init__(self):
        self.filters = []
        self.lite_mode = False
        self.remote_toolchain = None
        self.remote_deploy_config = None
        self.remote_repo_path = None
        self.remote_build_path = None
        self.remote_deploy_host = None
        self.use_sync_server = False
        self.content_root = None
        self.strip_non_final_targets = False
        self.full_targets = False
        self.add_py_targets = False

    @staticmethod
    def consumer():
        return [
            core.yarg.ArgConsumer(
                ['--filter', '-f'],
                help='Only consider filtered content',
                hook=core.yarg.SetAppendHook('filters'),
                group=CLionOptions.CLION_OPT_GROUP,
            ),
            core.yarg.ArgConsumer(
                ['--mini', '-m'],
                help='Lite mode for solution (fast open, without build)',
                hook=core.yarg.SetConstValueHook('lite_mode', True),
                group=CLionOptions.CLION_OPT_GROUP,
            ),
            core.yarg.ArgConsumer(
                ['--remote-toolchain'],
                help='Generate configurations for remote toolchain with this name',
                hook=core.yarg.SetValueHook('remote_toolchain'),
                group=CLionOptions.CLION_OPT_GROUP,
            ),
            core.yarg.ArgConsumer(
                ['--remote-deploy-config'],
                help='Name of the remote server configuration tied to the remote toolchain',
                hook=core.yarg.SetValueHook('remote_deploy_config'),
                group=CLionOptions.CLION_OPT_GROUP,
            ),
            core.yarg.ArgConsumer(
                ['--remote-repo-path'],
                help='Path to the arc repository at the remote host',
                hook=core.yarg.SetValueHook('remote_repo_path'),
                group=CLionOptions.CLION_OPT_GROUP,
            ),
            core.yarg.ArgConsumer(
                ['--remote-build-path'],
                help='Path to the directory for CMake output at the remote host',
                hook=core.yarg.SetValueHook('remote_build_path'),
                group=CLionOptions.CLION_OPT_GROUP,
            ),
            core.yarg.ArgConsumer(
                ['--remote-host'],
                help='Hostname associated with remote server configuration',
                hook=core.yarg.SetValueHook('remote_deploy_host'),
                group=CLionOptions.CLION_OPT_GROUP,
            ),
            core.yarg.ArgConsumer(
                ['--use-sync-server'],
                help='Deploy local files via sync server instead of file watchers',
                hook=core.yarg.SetConstValueHook('use_sync_server', True),
                group=CLionOptions.CLION_OPT_GROUP,
            ),
            core.yarg.ArgConsumer(
                ['--project-root', '-r'],
                help='Root directory for a CLion project',
                hook=core.yarg.SetValueHook('content_root'),
                group=CLionOptions.CLION_OPT_GROUP,
            ),
            core.yarg.ArgConsumer(
                ['--strip-non-final-targets'],
                hook=core.yarg.SetConstValueHook('strip_non_final_targets', True),
                help='Do not create target for non-final nodes',
                group=CLionOptions.CLION_OPT_GROUP,
            ),
            core.yarg.ArgConsumer(
                ['--full-targets'],
                hook=core.yarg.SetConstValueHook('full_targets', True),
                help='Old Mode: Enable full targets graph generation for project.',
                group=CLionOptions.CLION_OPT_GROUP,
            ),
            core.yarg.ArgConsumer(
                ['--add-py3-targets'],
                hook=core.yarg.SetConstValueHook('add_py_targets', True),
                help='Add Python 3 targets to project',
                group=CLionOptions.CLION_OPT_GROUP,
            ),
            core.yarg.ConfigConsumer('filters'),
            core.yarg.ConfigConsumer('lite_mode'),
            core.yarg.ConfigConsumer('remote_toolchain'),
            core.yarg.ConfigConsumer('remote_deploy_config'),
            core.yarg.ConfigConsumer('remote_repo_path'),
            core.yarg.ConfigConsumer('remote_build_path'),
            core.yarg.ConfigConsumer('remote_deploy_host'),
            core.yarg.ConfigConsumer('use_sync_server'),
            core.yarg.ConfigConsumer('content_root'),
            core.yarg.ConfigConsumer('strip_non_executable_target'),
            core.yarg.ConfigConsumer('full_targets'),
            core.yarg.ConfigConsumer('add_py_targets'),
        ]

    def postprocess2(self, params):
        if ' ' in params.project_title:
            raise core.yarg.ArgsValidatingException('Clion project title should not contain space symbol')
        if params.add_py_targets and params.full_targets:
            raise core.yarg.ArgsValidatingException('--add-py-targets must be used without --full-targets')


class IdeaOptions(core.yarg.Options):
    IDEA_OPT_GROUP = core.yarg.Group('Idea project options', 0)
    IDE_PLUGIN_INTEGRATION_GROUP = core.yarg.Group('Integration with IDE plugin', 1)

    def __init__(self):
        self.idea_project_root = None
        self.local = False
        self.group_modules = None
        self.dry_run = False
        self.ymake_bin = None
        self.iml_in_project_root = False
        self.iml_keep_relative_paths = False
        self.idea_files_root = None
        self.omit_test_data = False
        self.with_content_root_modules = False
        self.external_content_root_modules = []
        self.generate_tests_run = False
        self.generate_tests_for_deps = False
        self.separate_tests_modules = False
        self.auto_exclude_symlinks = False
        self.exclude_dirs = []
        self.with_common_jvm_args_in_junit_template = False
        self.with_long_library_names = False
        self.copy_shared_index_config = False
        self.idea_jdk_version = None
        self.regenerate_with_project_update = False
        self.project_update_targets = []
        self.project_update_kind = None

    @staticmethod
    def consumer():
        return [
            core.yarg.ArgConsumer(
                ['-r', '--project-root'],
                help='IntelliJ IDEA project root path',
                hook=core.yarg.SetValueHook('idea_project_root'),
                group=IdeaOptions.IDEA_OPT_GROUP,
            ),
            core.yarg.ArgConsumer(
                ['-P', '--project-output'],
                help='IntelliJ IDEA project root path. Please, use instead of -r',
                hook=core.yarg.SetValueHook('idea_project_root'),
                group=IdeaOptions.IDEA_OPT_GROUP,
            ),
            core.yarg.ArgConsumer(
                ['-l', '--local'],
                help='Only recurse reachable projects are idea modules',
                hook=core.yarg.SetConstValueHook('local', True),
                group=IdeaOptions.IDEA_OPT_GROUP,
            ),
            core.yarg.ArgConsumer(
                ['--group-modules'],
                help='Group idea modules according to paths',
                hook=core.yarg.SetValueHook('group_modules', values=('tree', 'flat')),
                group=IdeaOptions.IDEA_OPT_GROUP,
            ),
            core.yarg.ArgConsumer(
                ['-n', '--dry-run'],
                help='Emulate create project, but do nothing',
                hook=core.yarg.SetConstValueHook('dry_run', True),
                group=IdeaOptions.IDEA_OPT_GROUP,
            ),
            core.yarg.ArgConsumer(
                ['--ymake-bin'], help='Path to ymake binary', hook=core.yarg.SetValueHook('ymake_bin'), visible=False
            ),
            core.yarg.ArgConsumer(
                ['--iml-in-project-root'],
                help='Store ".iml" files in project root tree(stores in source root tree by default)',
                hook=core.yarg.SetConstValueHook('iml_in_project_root', True),
            ),
            core.yarg.ArgConsumer(
                ['--iml-keep-relative-paths'],
                help='Keep relative paths in ".iml" files (works with --iml-in-project-root)',
                hook=core.yarg.SetConstValueHook('iml_keep_relative_paths', True),
            ),
            core.yarg.ArgConsumer(
                ['--idea-files-root'],
                help='Root for .ipr and .iws files',
                hook=core.yarg.SetValueHook('idea_files_root'),
            ),
            core.yarg.ArgConsumer(
                ['--omit-test-data'],
                help='Do not export test_data',
                hook=core.yarg.SetConstValueHook('omit_test_data', True),
            ),
            core.yarg.ArgConsumer(
                ['--with-content-root-modules'],
                help='Generate content root modules',
                hook=core.yarg.SetConstValueHook('with_content_root_modules', True),
            ),
            core.yarg.ArgConsumer(
                ['--external-content-root-module'],
                help='Add external content root modules',
                hook=core.yarg.SetAppendHook('external_content_root_modules'),
            ),
            core.yarg.ArgConsumer(
                ['--generate-junit-run-configurations'],
                help='Generate run configuration for junit tests',
                hook=core.yarg.SetConstValueHook('generate_tests_run', True),
            ),
            core.yarg.ArgConsumer(
                ['--generate-tests-for-dependencies'],
                help='Generate tests for PEERDIR dependencies',
                hook=core.yarg.SetConstValueHook('generate_tests_for_deps', True),
            ),
            core.yarg.ArgConsumer(
                ['--separate-tests-modules'],
                help='Do not merge tests modules with their own libraries',
                hook=core.yarg.SetConstValueHook('separate_tests_modules', True),
            ),
            core.yarg.ArgConsumer(
                ['--auto-exclude-symlinks'],
                help='Add all symlink-dirs in modules to exclude dirs',
                hook=core.yarg.SetConstValueHook('auto_exclude_symlinks', True),
            ),
            core.yarg.ArgConsumer(
                ['--exclude-dirs'],
                help='Exclude dirs with specific names from all modules',
                hook=core.yarg.SetAppendHook('exclude_dirs'),
            ),
            core.yarg.ArgConsumer(
                ['--with-common-jvm-args-in-junit-template'],
                help='Add common JVM_ARGS flags to default junit template',
                hook=core.yarg.SetConstValueHook('with_common_jvm_args_in_junit_template', True),
            ),
            core.yarg.ArgConsumer(
                ['--with-long-library-names'],
                help='Generate long library names',
                hook=core.yarg.SetConstValueHook('with_long_library_names', True),
            ),
            core.yarg.ArgConsumer(
                ['--copy-shared-index-config'],
                help='Copy project config for Shared Indexes if exist',
                hook=core.yarg.SetConstValueHook('copy_shared_index_config', True),
            ),
            core.yarg.ArgConsumer(
                ['--idea-jdk-version'],
                help='Project JDK version',
                hook=core.yarg.SetValueHook('idea_jdk_version'),
            ),
            core.yarg.ArgConsumer(
                ['-U', '--regenerate-with-project-update'],
                help='Run `ya project update` upon regeneration from Idea',
                group=IdeaOptions.IDE_PLUGIN_INTEGRATION_GROUP,
                hook=core.yarg.SetConstValueHook('regenerate_with_project_update', True),
            ),
            core.yarg.ArgConsumer(
                ['--project-update-targets'],
                help='Run `ya project update` for this dirs upon regeneration from Idea',
                hook=core.yarg.SetAppendHook('project_update_targets'),
                group=IdeaOptions.IDE_PLUGIN_INTEGRATION_GROUP,
                visible=HelpLevel.ADVANCED,
            ),
            core.yarg.ArgConsumer(
                ['--project-update-kind'],
                help='Type of a project to use in `ya project update` upon regernation from Idea',
                hook=core.yarg.SetValueHook('project_update_kind'),
                group=IdeaOptions.IDE_PLUGIN_INTEGRATION_GROUP,
                visible=HelpLevel.ADVANCED,
            ),
            core.yarg.ConfigConsumer('idea_project_root'),
            core.yarg.ConfigConsumer('local'),
            core.yarg.ConfigConsumer('group_modules'),
            core.yarg.ConfigConsumer('dry_run'),
            core.yarg.ConfigConsumer('iml_in_project_root'),
            core.yarg.ConfigConsumer('iml_keep_relative_paths'),
            core.yarg.ConfigConsumer('idea_files_root'),
            core.yarg.ConfigConsumer('omit_test_data'),
            core.yarg.ConfigConsumer('with_content_root_modules'),
            core.yarg.ConfigConsumer('external_content_root_modules'),
            core.yarg.ConfigConsumer('generate_tests_run'),
            core.yarg.ConfigConsumer('generate_tests_for_deps'),
            core.yarg.ConfigConsumer('separate_tests_modules'),
            core.yarg.ConfigConsumer('auto_exclude_symlinks'),
            core.yarg.ConfigConsumer('exclude_dirs'),
            core.yarg.ConfigConsumer('with_common_jvm_args_in_junit_template'),
            core.yarg.ConfigConsumer('with_long_library_names'),
            core.yarg.ConfigConsumer('copy_shared_index_config'),
            core.yarg.ConfigConsumer('idea_jdk_version'),
            core.yarg.ConfigConsumer('regenarate_with_project_update'),
            core.yarg.ConfigConsumer('project_update_targets'),
            core.yarg.ConfigConsumer('project_update_kind'),
        ]

    def postprocess(self):
        if self.idea_project_root is None:
            raise core.yarg.ArgsValidatingException('Idea project root(-r, --project-root) must be specified.')

        self.idea_project_root = os.path.abspath(self.idea_project_root)

        if self.iml_keep_relative_paths and not self.iml_in_project_root:
            raise core.yarg.ArgsValidatingException(
                '--iml-keep-relative-paths can be used only with --iml-in-project-root'
            )

        for p in self.exclude_dirs:
            if os.path.isabs(p):
                raise core.yarg.ArgsValidatingException('Absolute paths are not allowed in --exclude-dirs')


class GradleOptions(core.yarg.Options):
    YGRADLE_OPT_GROUP = core.yarg.Group('Yexport gradle project options', 0)

    OPT_GRADLE_NAME = '--gradle-name'
    OPT_SETTINGS_ROOT = '--settings-root'
    OPT_YEXPORT_BIN = '--yexport-bin'
    OPT_BUILD_CONTRIBS = '--build-contribs'
    OPT_DISABLE_ERRORPRONE = '--disable-errorprone'
    OPT_REMOVE = '--remove'

    def __init__(self):
        self.gradle_name = None
        self.settings_root = None
        self.yexport_bin = None
        self.build_contribs = False
        self.disable_errorprone = False
        self.yexport_debug_mode = None
        self.login = None
        self.bucket_token = None
        self.remove = None

    @staticmethod
    def consumer():
        return [
            core.yarg.ArgConsumer(
                [GradleOptions.OPT_GRADLE_NAME],
                help='Set project name manually',
                hook=core.yarg.SetValueHook('gradle_name'),
                group=GradleOptions.YGRADLE_OPT_GROUP,
            ),
            core.yarg.ArgConsumer(
                [GradleOptions.OPT_SETTINGS_ROOT],
                help='Directory in Arcadia to place Gradle project settings',
                hook=core.yarg.SetValueHook('settings_root'),
                group=GradleOptions.YGRADLE_OPT_GROUP,
            ),
            core.yarg.ArgConsumer(
                [GradleOptions.OPT_YEXPORT_BIN],
                help='Full path to yexport binary',
                hook=core.yarg.SetValueHook('yexport_bin'),
                group=GradleOptions.YGRADLE_OPT_GROUP,
            ),
            core.yarg.ArgConsumer(
                [GradleOptions.OPT_BUILD_CONTRIBS],
                help='Build all contribs from arcadia to jar files',
                hook=core.yarg.SetConstValueHook('build_contribs', True),
                group=GradleOptions.YGRADLE_OPT_GROUP,
            ),
            core.yarg.ArgConsumer(
                [GradleOptions.OPT_DISABLE_ERRORPRONE],
                help='Disable errorprone in Gradle project',
                hook=core.yarg.SetConstValueHook('disable_errorprone', True),
                group=GradleOptions.YGRADLE_OPT_GROUP,
            ),
            core.yarg.ArgConsumer(
                [GradleOptions.OPT_REMOVE],
                help='Remove gradle project files and all symlinks',
                hook=core.yarg.SetConstValueHook('remove', True),
                group=GradleOptions.YGRADLE_OPT_GROUP,
            ),
            core.yarg.ArgConsumer(
                ['--yexport-debug-mode'],
                help='Debug mode for yexport',
                hook=core.yarg.SetValueHook('yexport_debug_mode'),
                group=GradleOptions.YGRADLE_OPT_GROUP,
                visible=HelpLevel.INTERNAL,
            ),
        ]

    def postprocess(self):
        if self.yexport_bin is not None and not os.path.exists(self.yexport_bin):
            raise core.yarg.ArgsValidatingException(
                'Not found yexport binary({}) {}.'.format(GradleOptions.OPT_YEXPORT_BIN, self.yexport_bin)
            )
        if self.remove and (self.gradle_name or self.build_contribs):
            raise core.yarg.ArgsValidatingException(
                '{} and {} not applicable with {}'.format(
                    GradleOptions.OPT_GRADLE_NAME, GradleOptions.OPT_BUILD_CONTRIBS, GradleOptions.OPT_REMOVE
                )
            )


class PycharmOptions(core.yarg.Options):
    PYCHARM_OPT_GROUP = core.yarg.Group('Pycharm project options', 0)
    PYTHON_WRAPPER_NAME = 'pycharm_python_wrapper'

    def __init__(self):
        self.only_generate_wrapper = False
        self.wrapper_name = PycharmOptions.PYTHON_WRAPPER_NAME
        self.list_ide = False
        self.ide_version = None

    @staticmethod
    def consumer():
        return [
            core.yarg.ArgConsumer(
                ['--only-generate-wrapper'],
                help="Don not generate Pycharm project, only wrappers",
                hook=core.yarg.SetConstValueHook('only_generate_wrapper', True),
                group=PycharmOptions.PYCHARM_OPT_GROUP,
            ),
            core.yarg.ArgConsumer(
                ['--wrapper-name'],
                help='Name of generated python wrapper. Use `python` for manual adding wrapper as Python SDK.',
                hook=core.yarg.SetValueHook('wrapper_name'),
                group=PycharmOptions.PYCHARM_OPT_GROUP,
            ),
            core.yarg.ArgConsumer(
                ['--list-ide'],
                help='List available JB IDE for patching SDK list.',
                hook=core.yarg.SetConstValueHook('list_ide', True),
                group=PycharmOptions.PYCHARM_OPT_GROUP,
            ),
            core.yarg.ArgConsumer(
                ['--ide-version'],
                help='Change IDE version for patching SDK list. Available IDE: {}'.format(
                    ", ".join(devtools.ya.ide.pycharm.find_available_ide())
                ),
                hook=core.yarg.SetValueHook('ide_version'),
                group=PycharmOptions.PYCHARM_OPT_GROUP,
            ),
        ]

    def postprocess(self):
        if PycharmOptions.PYTHON_WRAPPER_NAME != self.wrapper_name and not self.only_generate_wrapper:
            raise core.yarg.ArgsValidatingException(
                "Custom wrapper name can be used with option --only-generate-wrapper"
            )


def get_description(text, ref_name):
    if app_config.in_house:
        ref = {
            "multi": "https://docs.yandex-team.ru/ya-make/usage/ya_ide/vscode#ya-ide-vscode",
            "typescript": "https://docs.yandex-team.ru/ya-make/usage/ya_ide/vscode#typescript",
        }[ref_name]
        return "{}\nDocs: [[c:dark-cyan]]{}[[rst]]".format(text, ref)
    else:
        return text


class IdeYaHandler(core.yarg.CompositeHandler):
    description = 'Generate project for IDE'

    def __init__(self):
        core.yarg.CompositeHandler.__init__(self, description=self.description)
        self['clion'] = core.yarg.OptsHandler(
            action=devtools.ya.app.execute(devtools.ya.ide.clion2016.do_clion),
            description='[[imp]]ya ide clion[[rst]] is deprecated, please use clangd-based tooling instead',
            opts=devtools.ya.ide.ide_common.ide_via_ya_make_opts()
            + [
                CLionOptions(),
                TidyOptions(),
                devtools.ya.core.common_opts.YaBin3Options(),
            ],
        )

        self['idea'] = core.yarg.OptsHandler(
            action=devtools.ya.app.execute(devtools.ya.ide.idea.do_idea),
            description='Generate stub for IntelliJ IDEA',
            opts=devtools.ya.ide.ide_common.ide_minimal_opts(targets_free=True)
            + [
                devtools.ya.ide.ide_common.IdeYaMakeOptions(),
                devtools.ya.ide.ide_common.YaExtraArgsOptions(),
                IdeaOptions(),
                devtools.ya.core.common_opts.OutputStyleOptions(),
                devtools.ya.core.common_opts.CrossCompilationOptions(),
                devtools.ya.core.common_opts.PrintStatisticsOptions(),
                build.build_opts.ContinueOnFailOptions(),
                build.build_opts.YMakeDebugOptions(),
                build.build_opts.BuildThreadsOptions(build_threads=None),
                build.build_opts.DistCacheOptions(),
                build.build_opts.FlagsOptions(),
                build.build_opts.IgnoreRecursesOptions(),
                build.build_opts.ContentUidsOptions(),
                build.build_opts.ExecutorOptions(),
                build.build_opts.CustomFetcherOptions(),
                build.build_opts.SandboxAuthOptions(),
                devtools.ya.core.common_opts.YaBin3Options(),
            ],
            unknown_args_as_free=True,
        )
        self['gradle'] = core.yarg.OptsHandler(
            action=devtools.ya.app.execute(devtools.ya.ide.gradle.do_gradle),
            description='Generate gradle for project with yexport',
            opts=devtools.ya.ide.ide_common.ide_minimal_opts(targets_free=True)
            + [
                devtools.ya.ide.ide_common.YaExtraArgsOptions(),
                GradleOptions(),
                build.build_opts.YMakeBinOptions(),
                build.build_opts.FlagsOptions(),
                build.build_opts.CustomFetcherOptions(),
                build.build_opts.SandboxAuthOptions(),
                devtools.ya.core.common_opts.CrossCompilationOptions(),
                build.build_opts.ToolsOptions(),
                build.build_opts.BuildTypeOptions('release'),
                build.build_opts.JavaSpecificOptions(),
            ],
            visible=False,
        )
        self['qt'] = core.yarg.OptsHandler(
            action=devtools.ya.app.execute(self._choose_qt_handler),
            description='[[imp]]ya ide qt[[rst]] is deprecated, please use clangd-based tooling instead',
            opts=devtools.ya.ide.qt.QT_OPTS + [devtools.ya.core.common_opts.YaBin3Options()],
        )
        self['goland'] = core.yarg.OptsHandler(
            action=devtools.ya.app.execute(devtools.ya.ide.goland.do_goland),
            description='Generate stub for Goland',
            opts=devtools.ya.ide.ide_common.ide_via_ya_make_opts()
            + [
                devtools.ya.ide.goland.GolandOptions(),
                devtools.ya.core.common_opts.YaBin3Options(),
            ],
        )
        self['pycharm'] = core.yarg.OptsHandler(
            action=devtools.ya.app.execute(devtools.ya.ide.pycharm.do_pycharm),
            description='Generate PyCharm project.',
            opts=devtools.ya.ide.ide_common.ide_minimal_opts(targets_free=True)
            + [
                PycharmOptions(),
                devtools.ya.ide.ide_common.IdeYaMakeOptions(),
                devtools.ya.ide.ide_common.YaExtraArgsOptions(),
                build.build_opts.DistCacheOptions(),
                devtools.ya.core.common_opts.YaBin3Options(),
            ],
            visible=(pm.my_platform() != 'win32'),
        )
        self['vscode-clangd'] = core.yarg.OptsHandler(
            action=devtools.ya.app.execute(devtools.ya.ide.vscode_clangd.gen_vscode_workspace),
            description="[[bad]]ya ide vscode-clangd[[rst]] is deprecated, please use [[good]]ya ide vscode --cpp[[rst]] instead",
            opts=devtools.ya.ide.ide_common.ide_minimal_opts(targets_free=True)
            + [
                devtools.ya.ide.vscode_clangd.VSCodeClangdOptions(),
                devtools.ya.ide.ide_common.YaExtraArgsOptions(),
                bcd.CompilationDatabaseOptions(),
                build.build_opts.FlagsOptions(),
                build.build_opts.OutputOptions(),
                build.build_opts.BuildThreadsOptions(build_threads=None),
                build.build_opts.ContentUidsOptions(),
                build.build_opts.ToolsOptions(),
                devtools.ya.core.common_opts.YaBin3Options(),
            ],
            visible=(pm.my_platform() != 'win32'),
        )
        self['vscode-go'] = core.yarg.OptsHandler(
            action=devtools.ya.app.execute(devtools.ya.ide.vscode_go.gen_vscode_workspace),
            description="[[bad]]ya ide vscode-go[[rst]] is deprecated, please use [[good]]ya ide vscode --go[[rst]] instead",
            opts=devtools.ya.ide.ide_common.ide_minimal_opts(targets_free=True)
            + [
                devtools.ya.ide.vscode_go.VSCodeGoOptions(),
                devtools.ya.ide.ide_common.YaExtraArgsOptions(),
                build.build_opts.FlagsOptions(),
                build.build_opts.BuildThreadsOptions(build_threads=None),
                build.build_opts.ContentUidsOptions(),
                build.build_opts.ToolsOptions(),
                devtools.ya.core.common_opts.YaBin3Options(),
            ],
        )
        self['vscode-py'] = core.yarg.OptsHandler(
            action=devtools.ya.app.execute(devtools.ya.ide.vscode_py.gen_vscode_workspace),
            description="[[bad]]ya ide vscode-py[[rst]] is deprecated, please use [[good]]ya ide vscode --py3[[rst]] instead",
            opts=devtools.ya.ide.ide_common.ide_minimal_opts(targets_free=True)
            + [
                devtools.ya.ide.vscode_py.VSCodePyOptions(),
                devtools.ya.ide.ide_common.YaExtraArgsOptions(),
                build.build_opts.FlagsOptions(),
                build.build_opts.BuildThreadsOptions(build_threads=None),
                build.build_opts.ContentUidsOptions(),
                build.build_opts.ToolsOptions(),
                devtools.ya.core.common_opts.YaBin3Options(),
            ],
            visible=(pm.my_platform() != 'win32'),
        )
        self['vscode-ts'] = core.yarg.OptsHandler(
            action=devtools.ya.app.execute(devtools.ya.ide.vscode_ts.gen_vscode_workspace),
            description=get_description('Generate VSCode TypeScript project.', ref_name='typescript'),
            opts=devtools.ya.ide.ide_common.ide_minimal_opts(targets_free=True)
            + [
                devtools.ya.ide.vscode_ts.VSCodeTypeScriptOptions(),
                devtools.ya.ide.ide_common.YaExtraArgsOptions(),
                build.build_opts.FlagsOptions(),
                build.build_opts.BuildThreadsOptions(build_threads=None),
                build.build_opts.ContentUidsOptions(),
                build.build_opts.ToolsOptions(),
                devtools.ya.core.common_opts.YaBin3Options(),
            ],
            visible=(pm.my_platform() != 'win32'),
        )
        self['vscode'] = core.yarg.OptsHandler(
            action=devtools.ya.app.execute(devtools.ya.ide.vscode_all.gen_vscode_workspace),
            description=get_description('Generate VSCode multi-language project.', ref_name='multi'),
            opts=devtools.ya.ide.ide_common.ide_minimal_opts(targets_free=True, prefetch=True)
            + [
                devtools.ya.ide.vscode.opts.VSCodeAllOptions(),
                devtools.ya.ide.ide_common.YaExtraArgsOptions(),
                bcd.CompilationDatabaseOptions(),
                build.build_opts.FlagsOptions(),
                build.build_opts.OutputOptions(),
                build.build_opts.BuildThreadsOptions(build_threads=None),
                build.build_opts.ContentUidsOptions(),
                build.build_opts.ToolsOptions(),
                devtools.ya.core.common_opts.YaBin3Options(),
            ],
        )
        self['venv'] = core.yarg.OptsHandler(
            action=devtools.ya.app.execute(devtools.ya.ide.venv.do_venv),
            description='Create or update python venv',
            opts=devtools.ya.ide.ide_common.ide_minimal_opts(targets_free=True)
            + [
                build.build_opts.BuildTypeOptions('release'),
                build.build_opts.BuildThreadsOptions(build_threads=None),
                build.build_opts.ExecutorOptions(),
                build.build_opts.FlagsOptions(),
                build.build_opts.IgnoreRecursesOptions(),
                build.build_opts.RebuildOptions(),
                devtools.ya.core.common_opts.BeVerboseOptions(),
                devtools.ya.core.common_opts.CrossCompilationOptions(),
                devtools.ya.ide.ide_common.YaExtraArgsOptions(),
                devtools.ya.ide.venv.VenvOptions(),
                devtools.ya.core.common_opts.YaBin3Options(),
            ],
            visible=(pm.my_platform() != 'win32'),
        )
        if app_config.in_house:
            self['fix-jb-fsnotifier'] = core.yarg.OptsHandler(
                action=devtools.ya.app.execute(devtools.ya.ide.fsnotifier.fix_fsnotifier),
                description='Replace fsnotifier for JB IDEs.',
                opts=[
                    devtools.ya.ide.fsnotifier.FixFsNotifierOptions(),
                    devtools.ya.core.common_opts.ShowHelpOptions(),
                    devtools.ya.core.common_opts.DumpDebugOptions(),
                    devtools.ya.core.common_opts.AuthOptions(),
                    devtools.ya.core.common_opts.YaBin3Options(),
                ],
            )

    @staticmethod
    def _choose_qt_handler(params):
        if params.run:
            devtools.ya.ide.qt.run_qtcreator(params)
        elif params.remote_host:
            devtools.ya.ide.remote_ide_qt.generate_remote_project(params)
        else:
            devtools.ya.ide.qt.gen_qt_project(params)
