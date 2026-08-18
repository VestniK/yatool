import os

import devtools.ya.test.const
import devtools.ya.test.util.tools
from devtools.ya.test import common as test_common
from devtools.ya.test.test_types import common as common_types

RUST_TEST_TYPE = "rust_test"
RUST_BENCH_TEST_TYPE = "rust_bench"


class RustTestSuite(common_types.AbstractTestSuite):
    """
    A libtest binary produced by RUST_TEST: `rustc --test` over src/lib.rs.
    The run_rust_test wrapper executes it and parses the stable text output
    (`test <name> ... ok`) into the trace file.
    """

    def support_splitting(self, opts=None):
        return False

    def support_list_node(self):
        return False

    def support_retries(self):
        return True

    @property
    def smooth_shutdown_signals(self):
        # Lets the wrapper convert an approaching timeout into a TIMEOUT
        # chunk error instead of being killed outright.
        return ["SIGUSR2"]

    def get_type(self):
        return RUST_TEST_TYPE

    @property
    def class_type(self):
        return devtools.ya.test.const.SuiteClassType.REGULAR

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
            opts, 'run_rust_test', self.global_resources, wrapper=True, run_on_target_platform=True
        ) + [
            '--binary',
            self.binary_path('$(BUILD_ROOT)'),
            '--test-work-dir',
            test_work_dir,
            '--tracefile',
            os.path.join(test_work_dir, devtools.ya.test.const.TRACE_FILE_NAME),
            '--output-dir',
            os.path.join(test_work_dir, devtools.ya.test.const.TESTING_OUT_DIR_NAME),
            '--project-path',
            self.project_path,
            '--timeout',
            str(self.timeout),
        ]

        for flt in getattr(opts, "tests_filters", None) or []:
            cmd += ['--test-filter', flt]
        for flt in self._additional_filters:
            cmd += ['--test-filter', flt]

        for additional_arg in getattr(opts, "test_binary_args", None) or []:
            cmd += ["--test-binary-args={}".format(additional_arg)]

        return cmd


class RustBenchSuite(RustTestSuite):
    """
    RUST_BENCH: the same libtest binary run with --bench; `#[bench]` results
    (ns/iter) are reported as test metrics, the way go.bench reports theirs.
    """

    def get_type(self):
        return RUST_BENCH_TEST_TYPE

    def get_run_cmd(self, opts, retry=None, for_dist_build=True):
        return super(RustBenchSuite, self).get_run_cmd(opts, retry, for_dist_build) + ["--bench-run"]
