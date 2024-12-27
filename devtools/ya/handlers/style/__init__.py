from __future__ import absolute_import

import devtools.ya.core.common_opts
import devtools.ya.core.yarg

from build.build_opts import CustomFetcherOptions, SandboxAuthOptions, ToolsOptions, BuildThreadsOptions
import devtools.ya.core.yarg.consumers

from .style import run_style
from .styler import StylerKind
from .target import STDIN_FILENAME

import devtools.ya.app


class StyleOptions(devtools.ya.core.yarg.Options):
    def __init__(self):
        self.targets: list[str] = []
        self.dry_run = False
        self.check = False
        self.full_output = False
        self.stdin_filename = STDIN_FILENAME
        self.py2 = False
        self.force = False
        self.use_ruff = False

    @staticmethod
    def consumer():
        return [
            devtools.ya.core.yarg.FreeArgConsumer(help='file or dir', hook=devtools.ya.core.yarg.ExtendHook(name='targets')),
            devtools.ya.core.yarg.ArgConsumer(
                ['--dry-run'],
                help='Print diff instead of overwriting files',
                hook=devtools.ya.core.yarg.SetConstValueHook('dry_run', True),
                group=devtools.ya.core.yarg.BULLET_PROOF_OPT_GROUP,
            ),
            devtools.ya.core.yarg.ArgConsumer(
                ['--check'],
                help="Don't format files but return code 3 if some files would be reformatted",
                hook=devtools.ya.core.yarg.SetConstValueHook('check', True),
                group=devtools.ya.core.yarg.BULLET_PROOF_OPT_GROUP,
            ),
            devtools.ya.core.yarg.ArgConsumer(
                ['--no-diff'],
                help="Print full file's content instead of diff. Can be used only with --dry-run",
                hook=devtools.ya.core.yarg.SetConstValueHook('full_output', True),
                group=devtools.ya.core.yarg.BULLET_PROOF_OPT_GROUP,
            ),
            devtools.ya.core.yarg.ArgConsumer(
                ['--stdin-filename'],
                help="File name for stdin input",
                hook=devtools.ya.core.yarg.SetValueHook('stdin_filename'),
                group=devtools.ya.core.yarg.BULLET_PROOF_OPT_GROUP,
            ),
            devtools.ya.core.yarg.ArgConsumer(
                ['--py2'],
                help='Use Black with Python 2 support',
                hook=devtools.ya.core.yarg.SetConstValueHook('py2', True),
                group=devtools.ya.core.yarg.BULLET_PROOF_OPT_GROUP,
            ),
            devtools.ya.core.yarg.ArgConsumer(
                ['-f', '--force'],
                help="Don't skip files",
                hook=devtools.ya.core.yarg.SetConstValueHook('force', True),
                group=devtools.ya.core.yarg.BULLET_PROOF_OPT_GROUP,
            ),
            devtools.ya.core.yarg.ArgConsumer(
                ['--ruff'],
                help="Use ruff format, instead black for python files",
                hook=devtools.ya.core.yarg.SetConstValueHook('use_ruff', True),
                group=devtools.ya.core.yarg.ADVANCED_OPT_GROUP,
            ),
        ]


class FilterOptions(devtools.ya.core.yarg.Options):
    def __init__(self):
        self.file_types: list[str] = []

    @staticmethod
    def consumer():
        checks = [kind for kind in StylerKind]

        return [
            devtools.ya.core.yarg.ArgConsumer(
                ['--{file_type}'.format(file_type=file_type)],
                help='Process only {filetype} files'.format(filetype=file_type),
                hook=devtools.ya.core.yarg.SetConstAppendHook('file_types', file_type),
                group=devtools.ya.core.yarg.FILTERS_OPT_GROUP,
            )
            for file_type in checks
        ] + [
            devtools.ya.core.yarg.ArgConsumer(
                ['--all'],
                help='Run all checks: {}'.format(', '.join(checks)),
                hook=devtools.ya.core.yarg.SetConstValueHook('file_types', checks),
                group=devtools.ya.core.yarg.FILTERS_OPT_GROUP,
            )
        ]


class ReportOptions(devtools.ya.core.yarg.Options):
    def __init__(self):
        self.quiet = False

    @staticmethod
    def consumer():
        return [
            devtools.ya.core.yarg.ArgConsumer(
                ['-q', '--quiet'],
                help="Skip warning messages",
                hook=devtools.ya.core.yarg.SetConstValueHook('quiet', True),
                group=devtools.ya.core.yarg.BULLET_PROOF_OPT_GROUP,
            ),
        ]


class StyleYaHandler(devtools.ya.core.yarg.OptsHandler):
    description = 'Run styler'

    def __init__(self):
        devtools.ya.core.yarg.OptsHandler.__init__(
            self,
            action=devtools.ya.app.execute(action=run_style, respawn=devtools.ya.app.RespawnType.OPTIONAL),
            description=self.description,
            opts=[
                StyleOptions(),
                ReportOptions(),
                devtools.ya.core.common_opts.ShowHelpOptions(),
                CustomFetcherOptions(),
                SandboxAuthOptions(),
                ToolsOptions(),
                BuildThreadsOptions(build_threads=None),
                FilterOptions(),
            ],
            examples=[
                devtools.ya.core.yarg.UsageExample('{prefix}', 'restyle text from <stdin>, write result to <stdout>'),
                devtools.ya.core.yarg.UsageExample('{prefix} .', 'restyle all files in current directory'),
                devtools.ya.core.yarg.UsageExample(
                    '{prefix} file.cpp',
                    'restyle file.cpp',
                ),
                devtools.ya.core.yarg.UsageExample('{prefix} folder/', 'restyle all files in subfolders recursively'),
            ],
            unknown_args_as_free=False,
        )
