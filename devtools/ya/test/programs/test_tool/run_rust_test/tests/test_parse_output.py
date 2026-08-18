# coding: utf-8
"""
The libtest text format is the only contract run_rust_test has -- rustc's
`--format json` is still nightly-only -- so these pin the shapes it has to
survive rather than the shapes it happens to produce today.
"""

from devtools.ya.test import const
from devtools.ya.test.programs.test_tool.run_rust_test import run_rust_test


PASS_AND_FAIL = """
running 2 tests
test tests::fails ... FAILED
test tests::works ... ok

failures:

---- tests::fails stdout ----
thread 'tests::fails' panicked at src/lib.rs:12:9:
assertion `left == right` failed
  left: 1
 right: 2
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace


failures:
    tests::fails

test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s
"""


def test_pass_and_fail():
    tests, outputs, suite_ok = run_rust_test.parse_output(PASS_AND_FAIL)

    assert tests == {
        'tests::works': (const.Status.GOOD, None),
        'tests::fails': (const.Status.FAIL, None),
    }
    assert suite_ok is False
    assert 'assertion `left == right` failed' in '\n'.join(outputs['tests::fails'])
    assert 'tests::works' not in outputs


def test_ignored_is_skipped():
    tests, _, suite_ok = run_rust_test.parse_output(
        "running 1 test\n"
        "test tests::later ... ignored, not ready yet\n"
        "\n"
        "test result: ok. 0 passed; 0 failed; 1 ignored; 0 measured; 0 filtered out; finished in 0.00s\n"
    )

    assert tests == {'tests::later': (const.Status.SKIPPED, None)}
    assert suite_ok is True


def test_bench_metrics():
    # libtest column-pads bench names and puts thousands separators in the
    # numbers; both have to survive the trip into metrics.
    tests, _, suite_ok = run_rust_test.parse_output(
        "running 2 tests\n"
        "test benches::short          ... bench:         123.45 ns/iter (+/- 6.78)\n"
        "test benches::the_longest_one ... bench:      1,234.56 ns/iter (+/- 8.90)\n"
        "\n"
        "test result: ok. 0 passed; 0 failed; 0 ignored; 2 measured; 0 filtered out; finished in 1.00s\n"
    )

    assert tests['benches::short'] == (
        const.Status.GOOD,
        {'ns_per_iter': 123.45, 'deviation_ns': 6.78},
    )
    assert tests['benches::the_longest_one'] == (
        const.Status.GOOD,
        {'ns_per_iter': 1234.56, 'deviation_ns': 8.90},
    )
    assert suite_ok is True


def test_failure_output_is_not_parsed_as_results():
    # A test that prints something shaped like libtest's own output. Everything
    # between the header and the `failures:` summary belongs to the failing
    # test, whatever it looks like.
    tests, outputs, suite_ok = run_rust_test.parse_output(
        "running 1 test\n"
        "test tests::prints ... FAILED\n"
        "\n"
        "failures:\n"
        "\n"
        "---- tests::prints stdout ----\n"
        "test tests::phantom ... ok\n"
        "test tests::other ... bench:         1.00 ns/iter (+/- 0.10)\n"
        "thread 'tests::prints' panicked at src/lib.rs:3:5:\n"
        "boom\n"
        "\n"
        "failures:\n"
        "    tests::prints\n"
        "\n"
        "test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s\n"
    )

    assert tests == {'tests::prints': (const.Status.FAIL, None)}
    assert suite_ok is False
    snippet = '\n'.join(outputs['tests::prints'])
    assert 'tests::phantom' in snippet
    assert 'boom' in snippet


def test_no_final_result_line():
    # A binary killed mid-run prints results but never the summary; suite_ok
    # stays None so the caller can tell that apart from a clean failure.
    tests, _, suite_ok = run_rust_test.parse_output("running 2 tests\ntest tests::works ... ok\n")

    assert tests == {'tests::works': (const.Status.GOOD, None)}
    assert suite_ok is None


def test_empty_output():
    assert run_rust_test.parse_output("") == ({}, {}, None)
