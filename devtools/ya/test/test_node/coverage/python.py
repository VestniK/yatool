from . import rigel

import devtools.ya.test.dependency.testdeps as testdeps
import devtools.ya.test.dependency.uid as uid_gen
import devtools.ya.test.util.tools as util_tools
import devtools.ya.test.const


def inject_python_coverage_nodes(graph, suites, resolvers_map, opts, platform_descriptor):
    py_suite_with_deps = []
    for suite in [s for s in suites if s.get_type() == "py3test"]:
        pydeps = []
        for uid, output in rigel.get_suite_binary_deps(suite, graph):
            if graph.is_target_python3(uid):
                pydeps.append((uid, output))
        if pydeps:
            py_suite_with_deps.append((suite, pydeps))
        assert pydeps, suite

    result = []

    if getattr(opts, 'build_coverage_report', False):
        pysuites, pydeps = [], []
        for suite, deps in py_suite_with_deps:
            pysuites.append(suite)
            pydeps.extend(deps)

        if pydeps:
            merged_coverage_filename = "$(BUILD_ROOT)/py3.coverage-merged.tar"
            merge_node_uid = inject_python_coverage_merge_node(
                graph, pysuites, 'py3.coverage.tar', merged_coverage_filename, opts=opts
            )
            report_node_uid = inject_create_python_coverage_report_node(
                graph, pysuites, pydeps, merge_node_uid, merged_coverage_filename, opts
            )
            result.append(report_node_uid)

    for suite, py_bin_deps in py_suite_with_deps:
        if py_bin_deps:
            merged_coverage_filename = suite.work_dir('py3.coverage-merged.tar')
            merge_node_uid = inject_python_coverage_merge_node(
                graph, [suite], 'py3.coverage.tar', merged_coverage_filename, opts=opts
            )

            resolved_filename = devtools.ya.test.const.COVERAGE_RESOLVED_FILE_NAME_PATTERN.format("py3")
            uid = inject_python_coverage_resolve_nodes(
                graph,
                suite,
                py_bin_deps,
                merged_coverage_filename,
                resolved_filename,
                merge_node_uid,
                opts=opts,
            )
            result.append(uid)

            if resolvers_map is not None:
                resolvers_map[uid] = (resolved_filename, suite)

    return result


def inject_python_coverage_merge_node(graph, suites, source_filename, output_path, opts=None):
    test_uids = uid_gen.get_test_result_uids(suites)
    uid = uid_gen.get_uid(test_uids + [output_path], "pycov-merge")
    all_resources = {}
    for suite in suites:
        all_resources.update(suite.global_resources)

    cmd = util_tools.get_test_tool_cmd(opts, "merge_python_coverage", all_resources) + [
        "--output",
        output_path,
        "--name-filter",
        ":py3:cov",
    ]

    coverage_paths = []
    for suite in suites:
        filename = suite.work_dir(source_filename)
        coverage_paths += ["--coverage-path", filename]

    cmd += coverage_paths

    node = {
        "node-type": devtools.ya.test.const.NodeType.TEST_AUX,
        "cache": True,
        "broadcast": False,
        "inputs": [],
        "uid": uid,
        "cwd": "$(BUILD_ROOT)",
        "priority": 0,
        "deps": testdeps.unique(test_uids),
        "env": {},
        "target_properties": {},
        "outputs": [output_path],
        'kv': {
            "p": "CV",
            "pc": 'light-cyan',
            "show_out": True,
        },
        "cmds": [
            {
                "cmd_args": cmd,
                "cwd": "$(BUILD_ROOT)",
            },
        ],
    }
    graph.append_node(node, add_to_result=False)

    return uid


def inject_create_python_coverage_report_node(graph, suites, py_bin_deps, merge_node_uid, coverage_path, opts=None):
    output_path = "$(BUILD_ROOT)/py3.coverage.report.tar"
    all_resources = {}
    for suite in suites:
        all_resources.update(suite.global_resources)

    cmd = util_tools.get_test_tool_cmd(opts, "build_python_coverage_report", all_resources) + [
        "--output",
        output_path,
        "--coverage-path",
        coverage_path,
        "--source-root",
        "$(SOURCE_ROOT)",
        # "--verbose",
    ]

    deps, binaries = zip(*py_bin_deps)
    deps = list(deps) + [merge_node_uid]

    for binary in binaries:
        cmd += ["--binary", binary]

    uid = uid_gen.get_uid(deps, "pycov-report")

    node = {
        "node-type": devtools.ya.test.const.NodeType.TEST_AUX,
        "broadcast": False,
        "inputs": [],
        "uid": uid,
        "cwd": "$(BUILD_ROOT)",
        "priority": 0,
        "deps": deps,
        "env": {},
        "target_properties": {},
        "outputs": [output_path],
        "tared_outputs": [output_path],
        'kv': {
            "p": "CV",
            "pc": 'light-cyan',
            "show_out": True,
        },
        "cmds": [
            {
                'cmd_args': cmd,
                'cwd': '$(BUILD_ROOT)',
            }
        ],
    }
    graph.append_node(node, add_to_result=True)

    return uid


def inject_python_coverage_resolve_nodes(
    graph, suite, py_bin_deps, coverage_tar_path, resolved_filename, merge_node_uid, opts=None
):
    work_dir = suite.work_dir()
    output_path = "{}/{}".format(work_dir, resolved_filename)
    log_path = "{}/py3_coverage_resolve.log".format(work_dir)

    deps, binaries = zip(*py_bin_deps)
    deps = list(deps) + [merge_node_uid]

    cmd = util_tools.get_test_tool_cmd(opts, "resolve_python_coverage", suite.global_resources) + [
        "--coverage-path",
        coverage_tar_path,
        "--source-root",
        "$(SOURCE_ROOT)",
        "--output",
        output_path,
        "--log-path",
        log_path,
    ]
    for binary in binaries:
        cmd += ["--binary", binary]

    uid = uid_gen.get_uid(deps, "resolve_pycov")

    node = {
        "node-type": devtools.ya.test.const.NodeType.TEST_AUX,
        "cache": True,
        "broadcast": False,
        "inputs": [coverage_tar_path],
        "uid": uid,
        "cwd": "$(BUILD_ROOT)",
        "priority": 0,
        "deps": testdeps.unique(deps),
        "env": {},
        "target_properties": {
            "module_lang": suite.meta.module_lang,
        },
        "outputs": [output_path, log_path],
        'kv': {
            # Resolve Python coverage
            "p": "RP",
            "pc": 'cyan',
            "show_out": True,
        },
        "cmds": [
            {
                "cmd_args": cmd,
                "cwd": "$(BUILD_ROOT)",
            },
        ],
    }
    graph.append_node(node, add_to_result=True)
    return uid
