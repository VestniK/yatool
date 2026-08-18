# coding: utf-8
"""
Runs a libtest binary produced by RUST_TEST / RUST_BENCH.

rustc's machine-readable output (--format json) is still nightly-only, so this
parses the stable text format instead:

    running 2 tests
    test tests::works ... ok
    test tests::fails ... FAILED

    failures:

    ---- tests::fails stdout ----
    thread 'tests::fails' panicked at src/lib.rs:12:9:
    ...

    test result: FAILED. 1 passed; 1 failed; ...; finished in 0.00s

and, under --bench (note the column padding libtest adds to bench names):

    test benches::short          ... bench:         123.45 ns/iter (+/- 6.78)
    test benches::the_longest_one ... bench:      1,234.56 ns/iter (+/- 8.90)
"""

import argparse
import io
import logging
import os
import re
import signal
import sys
import time
import warnings

import devtools.ya.test.filter as test_filter
from devtools.ya.test import const
from devtools.ya.test import facility
from devtools.ya.test.common import get_test_log_file_path
from devtools.ya.test.system import process
from devtools.ya.test.test_types.common import PerformedTestSuite
from devtools.ya.test.util import shared

logger = logging.getLogger(__name__)

# Bench names are column-padded by libtest, hence \s+ before the dots.
TEST_LINE = re.compile(r'^test (\S+)\s+\.\.\. (ok|FAILED|ignored)(?:,.*)?$')
BENCH_LINE = re.compile(r'^test (\S+)\s+\.\.\. bench:\s+([\d,.]+) ns/iter \(\+/- ([\d,.]+)\)$')
FAILURE_HEADER = re.compile(r'^---- (\S+) stdout ----$')
SUITE_RESULT = re.compile(r'^test result: (ok|FAILED)\.')
# `<binary> --list` output: `tests::works: test` / `benches::sum: benchmark`
LIST_LINE = re.compile(r'^(\S+): (test|benchmark)$')

STATUS = {
    'ok': const.Status.GOOD,
    'FAILED': const.Status.FAIL,
    'ignored': const.Status.SKIPPED,
}


def on_timeout(signum, frame):
    raise process.SignalInterruptionError()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--binary", required=True, help="Path to the libtest binary")
    parser.add_argument("--tracefile", required=True, help="Path to the output trace log")
    parser.add_argument("--output-dir", help="Path to the output dir")
    parser.add_argument("--project-path", help="Project path relative to arcadia")
    parser.add_argument("--test-work-dir", default=".", help="Path to test work dir")
    parser.add_argument("--timeout", default=0, type=int)
    parser.add_argument(
        "--test-filter", default=[], action="append", help="Run only tests matching the filter (fnmatch on full names)"
    )
    parser.add_argument(
        "--test-binary-args", default=[], action="append", help="Additional arguments for the test binary"
    )
    parser.add_argument("--bench-run", action="store_true", help="Run benchmarks instead of tests")
    parser.add_argument("--verbose", action="store_true")

    args = parser.parse_args()
    args.binary = os.path.abspath(args.binary)
    if not os.path.exists(args.binary):
        parser.error("Test binary doesn't exist: %s" % args.binary)
    return args


def setup_logging(verbose):
    level = logging.DEBUG if verbose else logging.ERROR
    logging.basicConfig(level=level, stream=sys.stdout, format="%(asctime)s: %(levelname)s: %(message)s")


def get_suite_name(binary):
    return os.path.splitext(os.path.basename(binary))[0]


def full_test_name(suite_name, test_name):
    # libtest names are `module::test`; prefixing the binary name gives the
    # `<test>::<subtest>` shape the rest of ya expects.
    return "{}::{}".format(suite_name, test_name)


def gen_suite(project_path):
    suite = PerformedTestSuite(None, project_path)
    suite.set_work_dir(os.getcwd())
    suite.register_chunk()
    return suite


def list_tests(opts):
    kind = "benchmark" if opts.bench_run else "test"
    cmd = [opts.binary] + (["--bench"] if opts.bench_run else []) + ["--list"]
    res = process.execute(cmd, check_exit_code=False, env=os.environ.copy())
    names = []
    for line in res.std_out.split("\n"):
        match = LIST_LINE.match(line.strip())
        if match and match.group(2) == kind:
            names.append(match.group(1))
    return names


def select_tests(opts, suite_name, listed):
    """
    ya filters are fnmatch patterns over full `<suite>::<name>` names; libtest
    filters are plain substrings. Match here over the full names and hand the
    binary the exact bare names instead.
    """
    if not opts.test_filter:
        return listed
    filter_func = test_filter.make_testname_filter(opts.test_filter)
    return [name for name in listed if filter_func(full_test_name(suite_name, name))]


def run_cmd(opts, selected, run_all):
    cmd = [opts.binary]
    if opts.bench_run:
        cmd += ["--bench"]
    if not run_all:
        # An exact name per selected test: libtest treats positional filters
        # as substrings unless --exact is given.
        cmd += ["--exact"] + selected
    cmd += opts.test_binary_args
    return cmd


def parse_output(content):
    """
    -> (tests: {name: (status, metrics)}, outputs: {name: [lines]}, suite_ok: bool|None)
    """
    tests = {}
    outputs = {}
    suite_ok = None
    curr_failure = None
    for line in content.split("\n"):
        stripped = line.strip()
        match = FAILURE_HEADER.match(stripped)
        if match:
            curr_failure = match.group(1)
            outputs.setdefault(curr_failure, [])
            continue
        match = BENCH_LINE.match(stripped)
        if match:
            curr_failure = None
            ns_per_iter = float(match.group(2).replace(",", ""))
            deviation = float(match.group(3).replace(",", ""))
            tests[match.group(1)] = (const.Status.GOOD, {"ns_per_iter": ns_per_iter, "deviation_ns": deviation})
            continue
        match = TEST_LINE.match(stripped)
        if match:
            curr_failure = None
            tests[match.group(1)] = (STATUS[match.group(2)], None)
            continue
        match = SUITE_RESULT.match(stripped)
        if match:
            curr_failure = None
            suite_ok = match.group(1) == 'ok'
            continue
        if curr_failure is not None:
            if stripped == 'failures:':
                curr_failure = None
            else:
                outputs[curr_failure].append(line)
    return tests, outputs, suite_ok


def terminate(proc):
    proc.terminate()
    proc.wait()
    return proc.returncode


def run_tests(opts):
    open(opts.tracefile, "w").close()
    suite_name = get_suite_name(opts.binary)
    if not os.path.exists(opts.output_dir):
        os.makedirs(opts.output_dir)

    listed = list_tests(opts)
    selected = select_tests(opts, suite_name, listed)

    # Everything selected is dumped as not-launched up front, so a crash
    # anywhere below still reports each test instead of a bare chunk error.
    # The trace file is append-only and later entries win.
    empty_suite = gen_suite(opts.project_path)
    for name in selected:
        empty_suite.chunk.tests.append(
            facility.TestCase(
                full_test_name(suite_name, name),
                const.Status.NOT_LAUNCHED,
                "test was not launched",
                path=opts.project_path,
            )
        )
    shared.dump_trace_file(empty_suite, opts.tracefile)

    if not selected:
        return

    cmd = run_cmd(opts, selected, run_all=(selected == listed))

    suite = gen_suite(opts.project_path)
    out_path = os.path.join(opts.output_dir, 'rust.out')
    err_path = os.path.join(opts.output_dir, 'rust.err')
    start_time = time.time()
    try:
        logger.debug("cmd: %s", cmd)
        res = shared.tee_execute(cmd, out_path, err_path, strip_ansi_codes=False, on_timeout=terminate)
        exit_code = res.returncode
    except process.SignalInterruptionError:
        exit_code = const.TestRunExitCode.TimeOut
    elapsed = time.time() - start_time

    with io.open(out_path, 'r', errors='ignore', encoding='utf-8') as afile:
        std_out = afile.read()
    with io.open(err_path, 'r', errors='ignore', encoding='utf-8') as afile:
        std_err = afile.read()

    tests, outputs, suite_ok = parse_output(std_out)

    # Under --bench libtest still prints every plain #[test] as "ignored";
    # those were never in the benchmark listing and must not become phantom
    # SKIPPED entries of a bench suite.
    wanted = set(selected)
    for name, (status, metrics) in tests.items():
        if name not in wanted:
            continue
        test_name = full_test_name(suite_name, name)
        snippet = '\n'.join(outputs.get(name, []))
        test_log_path = get_test_log_file_path(opts.output_dir, test_name)
        with open(test_log_path, 'w') as log:
            log.write(snippet)
        suite.chunk.tests.append(
            facility.TestCase(
                test_name,
                status,
                snippet,
                path=opts.project_path,
                logs={'log': test_log_path, 'logsdir': opts.output_dir},
                metrics=metrics,
            )
        )

    if exit_code == const.TestRunExitCode.TimeOut:
        suite.add_chunk_error(
            '[[bad]]Chunk exceeded {}s timeout[[rst]]'.format(opts.timeout), const.Status.TIMEOUT
        )
    elif not tests and exit_code != 0:
        # The binary died before libtest printed anything parseable --
        # a crash in a constructor, a missing dynamic library, etc.
        suite.add_chunk_error(
            '[[bad]]Test binary crashed with exit code {} before reporting any tests\n{}[[rst]]'.format(
                exit_code, std_err.strip()
            ),
            const.Status.CRASHED,
        )
    elif suite_ok is None and exit_code != 0:
        suite.add_chunk_error(
            '[[bad]]Test binary exited with code {} without a final `test result:` line[[rst]]'.format(exit_code),
            const.Status.CRASHED,
        )
    elif suite_ok and exit_code != 0:
        # "test result: ok" but a nonzero exit: something outside the harness
        # failed, e.g. an atexit hook or a leaked thread aborting.
        suite.add_chunk_error(
            '[[bad]]Test binary reported `test result: ok` but exited with code {}[[rst]]'.format(exit_code),
            const.Status.CRASHED,
        )

    logger.debug("elapsed: %.2fs, exit code: %d", elapsed, exit_code)
    shared.dump_trace_file(suite, opts.tracefile)


def main():
    # The pipe readers inside process.execute/tee_execute results are reaped
    # with the process; the interpreter's ResourceWarning about them is noise
    # that would otherwise land in every suite's stderr snippet.
    warnings.simplefilter("ignore", ResourceWarning)
    args = parse_args()
    setup_logging(args.verbose)

    if hasattr(signal, "SIGUSR2"):
        signal.signal(signal.SIGUSR2, on_timeout)

    run_tests(args)
    return 0


if __name__ == "__main__":
    exit(main())
