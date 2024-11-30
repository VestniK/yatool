import os
import logging
import collections

import exts.path2 as path2
import jbuild.gen.consts as consts
import yalibrary.graph.base as base
from jbuild.gen import configure

logger = logging.getLogger(__name__)


def dirname_unix_path(unix_path):
    return '/'.join(unix_path.split('/')[:-1])


def basename_unix_path(unix_path):
    return unix_path.split('/')[-1]


def is_contrib(path, ctx):
    return any(path.startswith(root) for root in ctx.contrib_roots)


def is_proxy_library(path, ctx):
    return is_contrib(path, ctx) and any(dirname_unix_path(dep.path) == path for dep in ctx.by_path[path].deps)


def strip_root(s):
    return s[3:]


class Context(object):
    def __init__(
        self,
        opts,
        arc_root,
        contrib_roots,
        paths,
        rclosure,
        by_path,
        resolved_sources,
        target_platform,
        global_resources,
    ):
        self.paths = paths
        self.rclosure = rclosure
        self.opts = opts
        self.arc_root = arc_root
        self.contrib_roots = contrib_roots
        self.by_path = by_path

        self.resolved_sources = resolved_sources
        self.errs = collections.defaultdict(configure.PathConfigureError)

        self.target_platform = target_platform

        self.global_resources = global_resources

    def _choose_in_classpath(self, path, accept_target, extract_artifact, direct=False):
        chosen = []

        target = self.by_path[path]
        if not is_proxy_library(target.path, self) and accept_target(target):
            chosen.append(extract_artifact(target))
        return chosen

    def classpath(self, path, type=consts.CLS, direct=False):
        return self._choose_in_classpath(
            path,
            accept_target=lambda t: t.provides_jar_of_type(type),
            extract_artifact=lambda t: t.output_jar_of_type_path(type),
            direct=direct,
        )

    def dlls(self, path):
        return self._choose_in_classpath(
            path,
            accept_target=lambda t: t.provides_dll(),
            extract_artifact=lambda t: t.output_dll_path(),
        )


def remove_prefixes(paths):
    import devtools.ya.yalibrary.checkout as checkout

    correct_paths = []

    def _pre_action(path, is_native):
        if is_native:
            correct_paths.append(path)

    checkout.PathsTree(paths).traverse(pre_action=_pre_action, skip_non_leaves=True)

    correct_paths = frozenset([base.hacked_normpath(p) for p in correct_paths])

    return [p for p in paths if p in correct_paths]


def group_by(iterable, by):
    g = collections.defaultdict(list)

    for el in iterable:
        g[by(el)].append(el)

    return g


def relativize(path, root=(consts.BUILD_ROOT, consts.SOURCE_ROOT)):
    for r in root:
        if path2.path_startswith(path, r):
            return os.path.relpath(path, r)

    return path


def resolve_java_srcs(
    srcdir, include_patterns, exclude_patterns=None, all_resources=False, resolve_kotlin=False, resolve_groovy=False
):
    import jbuild.resolve_java_srcs as resolver

    return resolver.resolve_java_srcs(
        srcdir, include_patterns, exclude_patterns or [], all_resources, resolve_kotlin, resolve_groovy
    )


def resolve_possible_srcdirs(arc_root, targets):
    return collections.defaultdict(lambda: collections.defaultdict(lambda: ([], [], [], [])))


def resolve_jdk(
    global_resources,
    prefix='JDK_DEFAULT',
    prefix_for_tests='_NO_JDK_FOR_TEST_',
    opts=None,
    for_test=False,
    jdk_version=None,
):
    if for_test and opts and consts.LOCAL_JDK_FOR_TESTS_FLAG in opts.flags:
        return opts.flags[consts.LOCAL_JDK_FOR_TESTS_FLAG]
    if opts and consts.LOCAL_JDK_FLAG in opts.flags:
        return opts.flags[consts.LOCAL_JDK_FLAG]

    if jdk_version:
        prefix = '{}{}'.format(consts.JDK_VERSION_PREFIX, jdk_version)
        jdks = [x for x in global_resources if x.startswith(prefix) and x.endswith(consts.JDK_RESOURCE_SUFFIX)]
        if len(jdks) == 1:
            return global_resources[jdks[0]]
        elif len(jdks) > 1:
            raise AssertionError('Found several jdk resources of the same version: {}'.format(jdks))
        else:
            raise AssertionError('Failed to resolve JDK{}. Global resources: {}'.format(jdk_version, global_resources))

    jdk_for_tests_resource = prefix_for_tests + consts.JDK_RESOURCE_SUFFIX
    if for_test and jdk_for_tests_resource in global_resources:
        return global_resources[jdk_for_tests_resource]

    jdk_resource = prefix + consts.JDK_RESOURCE_SUFFIX
    if jdk_resource in global_resources:
        return global_resources[jdk_resource]

    raise AssertionError('Failed to resolve jdk: {}'.format(global_resources))


def resolve_jacoco_agent(global_resources, opts=None):
    if opts and consts.LOCAL_JACOCO_AGENT_FLAG in opts.flags:
        return opts.flags[consts.LOCAL_JACOCO_AGENT_FLAG]
    return global_resources.get(consts.RESOURCE_JACOCO_AGENT, '$' + consts.RESOURCE_JACOCO_AGENT)


def resolve_kotlin_compiler(global_resources, opts=None):
    if opts and consts.LOCAL_KOTLIN_COMPILER_FLAG in opts.flags:
        return opts.flags[consts.LOCAL_KOTLIN_COMPILER_FLAG]
    return global_resources.get(consts.RESOURCE_KOTLIN_COMPILER, '$' + consts.RESOURCE_KOTLIN_COMPILER)


def resolve_jstyle_lib(global_resources, opts=None):
    if opts and consts.LOCAL_JSTYLE_LIB_FLAG in opts.flags:
        return opts.flags[consts.LOCAL_JSTYLE_LIB_FLAG]
    return global_resources.get(consts.RESOURCE_JSTYLE_LIB, '$' + consts.RESOURCE_JSTYLE_LIB)
