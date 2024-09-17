import os

import exts.windows

import devtools.ya.test.const
import devtools.ya.test.util.tools
import devtools.ya.test.common as test_common
from devtools.ya.test.system import process
from devtools.ya.test.test_types import common as common_types


BOOST_TEST_TYPE = "boost_test"


class BoostTestSuite(common_types.AbstractTestSuite):
    def get_run_cmd(self, opts, retry=None, for_dist_build=True):
        test_work_dir = test_common.get_test_suite_work_dir(
            '$(BUILD_ROOT)',
            self.project_path,
            self.name,
            retry,
            target_platform_descriptor=self.target_platform_descriptor,
            multi_target_platform_run=self.multi_target_platform_run,
            remove_tos=opts.remove_tos,
        )
        cmd = devtools.ya.test.util.tools.get_test_tool_cmd(
            opts, 'run_boost_test', self.global_resources, wrapper=True, run_on_target_platform=False
        ) + [
            '--binary',
            self.binary_path('$(BUILD_ROOT)'),
            '--tracefile',
            os.path.join(test_work_dir, devtools.ya.test.const.TRACE_FILE_NAME),
            '--output-dir',
            os.path.join(test_work_dir, devtools.ya.test.const.TESTING_OUT_DIR_NAME),
            '--project-path',
            self.project_path,
            '--verbose',
        ]
        if opts and hasattr(opts, "tests_filters") and opts.tests_filters:
            for flt in opts.tests_filters:
                cmd += ['--test-filter', flt]
        for flt in self._additional_filters:
            cmd += ['--test-filter', flt]
        if opts.gdb:
            cmd += ["--gdb-debug"]
        if not exts.windows.on_win():
            cmd += ["--gdb-path", os.path.join("$(GDB)", "gdb", "bin", "gdb")]

        return cmd

    def get_type(self):
        return BOOST_TEST_TYPE

    @property
    def class_type(self):
        return devtools.ya.test.const.SuiteClassType.REGULAR

    def get_list_cmd(self, arc_root, build_root, opts):
        return self.get_run_cmd(opts) + ['--test-list']

    @classmethod
    def list(cls, cmd, cwd):
        return cls._get_subtests_info(process.execute(cmd, check_exit_code=False, cwd=cwd))

    @classmethod
    def _get_subtests_info(cls, list_cmd_result):
        result = []
        if list_cmd_result.exit_code == 0:
            for x in list_cmd_result.std_err.split():
                if devtools.ya.test.const.TEST_SUBTEST_SEPARATOR in x:
                    testname, subtest = x.split(devtools.ya.test.const.TEST_SUBTEST_SEPARATOR, 1)
                    result.append(test_common.SubtestInfo(testname, subtest))
            return result
        raise Exception(list_cmd_result.std_err)

    @property
    def supports_canonization(self):
        return False

    @property
    def supports_coverage(self):
        return True

    @property
    def smooth_shutdown_signals(self):
        return ["SIGUSR2"]

    def support_retries(self):
        return True
