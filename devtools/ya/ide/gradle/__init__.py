import os
import sys
import logging
import shutil
import subprocess
import re
from collections.abc import Iterable
from pathlib import Path

from devtools.ya.core import config as core_config, yarg, stage_tracer
from devtools.ya.build import build_opts, graph as build_graph, ya_make
from devtools.ya.build.sem_graph import SemLang, SemConfig, SemNode, SemDep, SemGraph
from yalibrary import platform_matcher, tools
from exts import hashing
from devtools.ya.yalibrary import sjson
import xml.etree.ElementTree as eTree


class YaIdeGradleException(Exception):
    mute = True


class _JavaSemConfig(SemConfig):
    """Check and use command line options for configure roots and flags"""

    GRADLE_PROPS_FILE: Path = Path.home() / '.gradle' / 'gradle.properties'
    GRADLE_REQUIRED_PROPS: tuple[str] = (
        'bucketUsername',
        'bucketPassword',
        'systemProp.gradle.wrapperUser',
        'systemProp.gradle.wrapperPassword',
    )

    EXPORT_ROOT_BASE: Path = Path(core_config.misc_root()) / 'gradle'  # Base folder of all export roots

    def __init__(self, params):
        if platform_matcher.is_windows():
            raise YaIdeGradleException("Windows is not supported in ya ide gradle")
        super().__init__(SemLang.JAVA(), params)
        self.logger = logging.getLogger(type(self).__name__)
        self.settings_root: Path = self._get_settings_root()
        if not self.params.remove:
            self._check_gradle_props()

    def _check_gradle_props(self) -> None:
        """Check exists all required gradle properties"""
        errors = []
        if not _JavaSemConfig.GRADLE_PROPS_FILE.is_file():
            errors.append(f'File {_JavaSemConfig.GRADLE_PROPS_FILE} does not exist')
        else:
            with _JavaSemConfig.GRADLE_PROPS_FILE.open() as f:
                props = f.read()
            for prop in _JavaSemConfig.GRADLE_REQUIRED_PROPS:
                if prop not in props:
                    errors.append(f'Required property {prop} is not defined in {_JavaSemConfig.GRADLE_PROPS_FILE} file')
        if errors:
            raise YaIdeGradleException(
                '\n'.join(
                    [
                        f'Invalid Gradle properties file {_JavaSemConfig.GRADLE_PROPS_FILE}:',
                        *errors,
                        '',
                        'Please, read more about work with Bucket https://docs.yandex-team.ru/bucket/gradle#autentifikaciya'
                        'Token can be taken from here https://oauth.yandex-team.ru/authorize?response_type=token&client_id=bf8b6a8a109242daaf62bce9d6609b3b',
                    ]
                )
            )

    def _get_export_root(self) -> Path:
        """Create export_root path by hash of targets"""
        targets_hash = hashing.fast_hash(':'.join(sorted(self.params.abs_targets)))
        export_root = _JavaSemConfig.EXPORT_ROOT_BASE / targets_hash
        self.logger.info("Export root: %s", export_root)
        return export_root

    def _get_settings_root(self) -> Path:
        """Create settings_root path by options and targets"""
        settings_root = (
            self.arcadia_root / Path(self.params.settings_root)
            if self.params.settings_root
            else Path(self.params.abs_targets[0])
        )
        self.logger.info("Settings root: %s", settings_root)
        if not settings_root.exists() or not settings_root.is_dir():
            raise YaIdeGradleException('Not found settings root directory')
        return settings_root

    def in_rel_targets(self, rel_target: Path) -> bool:
        for conf_rel_target in self.params.rel_targets:
            if rel_target.is_relative_to(Path(conf_rel_target)):
                return True
        return False


class _YaSettings:
    """Save command and cwd to ya-settings.xml"""

    YA_SETTINGS_XML = 'ya-settings.xml'

    def __init__(self, java_sem_config: _JavaSemConfig):
        self.config: _JavaSemConfig = java_sem_config

    def save(self) -> None:
        self._write_xml(self._make_xml(), self.config.export_root / self.YA_SETTINGS_XML)

    @classmethod
    def _make_xml(cls) -> eTree.Element:
        xml_root = eTree.Element('root')
        cmd = eTree.SubElement(xml_root, 'cmd')
        for arg in sys.argv:
            eTree.SubElement(cmd, 'part').text = arg
        eTree.SubElement(xml_root, 'cwd').text = str(Path.cwd())
        return xml_root

    @classmethod
    def _write_xml(cls, xml_root: eTree.Element, path: Path) -> None:
        cls._elem_indent(xml_root)
        with path.open('wb') as f:
            eTree.ElementTree(xml_root).write(f, encoding="utf-8")

    @classmethod
    def _elem_indent(cls, elem, level=0) -> None:
        indent = "\n" + level * " " * 4
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = indent + " " * 4
            if not elem.tail or not elem.tail.strip():
                elem.tail = indent
            for elem in elem:
                cls._elem_indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = indent
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = indent


class _SymlinkCollector:
    """Iterate on settings and build root and call collect function for every place, where symlinks waited"""

    SETTINGS_FILES: tuple[str] = (
        "settings.gradle.kts",
        "gradlew",
        "gradlew.bat",
        _YaSettings.YA_SETTINGS_XML,
    )  # Files for symlink to settings root
    SETTINGS_MKDIRS: tuple[str] = (".gradle", ".idea")  # Folders for creating at settings root
    SETTINGS_DIRS: tuple[str] = list(SETTINGS_MKDIRS) + ["gradle"]  # Folders for symlink to settings root

    BUILD_SKIP_ROOT_DIRS: tuple[str] = list(SETTINGS_DIRS) + [
        _JavaSemConfig.YMAKE_DIR
    ]  # Skipped for build directories in export root
    BUILD_FILE: str = "build.gradle.kts"  # Filename for create build symlinks

    def __init__(self, java_sem_config: _JavaSemConfig):
        self.config: _JavaSemConfig = java_sem_config

    def collect_symlinks(self) -> Iterable[tuple[Path]]:
        yield from self._collect_settings_symlinks()
        yield from self._collect_build_symlinks()

    def _collect_settings_symlinks(self) -> Iterable[tuple[Path]]:
        """Collect symlinks for each settings files/dirs"""
        for mkdir in _SymlinkCollector.SETTINGS_MKDIRS:
            _SymlinkCollector.mkdir(self.config.export_root / mkdir)
        for export_file in self.config.export_root.iterdir():
            basename = export_file.name
            if (basename in _SymlinkCollector.SETTINGS_FILES and export_file.is_file()) or (
                basename in _SymlinkCollector.SETTINGS_DIRS and export_file.is_dir()
            ):
                arcadia_file = self.config.settings_root / basename
                yield export_file, arcadia_file

    def _collect_build_symlinks(self) -> Iterable[tuple[Path]]:
        """Collect symlinks for each build files/dirs from arcadia to export"""
        for export_file in self.config.export_root.iterdir():
            basename = export_file.name
            if basename not in _SymlinkCollector.BUILD_SKIP_ROOT_DIRS and export_file.is_dir():
                export_dir = export_file
                for walk_root, _, files in export_dir.walk():
                    for file in files:
                        if file == _SymlinkCollector.BUILD_FILE:
                            export_file = walk_root / file
                            arcadia_file = self.config.arcadia_root / export_file.relative_to(self.config.export_root)
                            yield export_file, arcadia_file
            elif basename == _SymlinkCollector.BUILD_FILE and export_file.is_file():
                arcadia_file = self.config.arcadia_root / basename
                yield export_file, arcadia_file

    @staticmethod
    def mkdir(path: Path) -> None:
        path.mkdir(0o755, parents=True, exist_ok=True)


class _ExistsSymlinkCollector(_SymlinkCollector):
    """Collect exists symlinks for remove later"""

    _SYMLINKS_FILE = 'symlinks.json'

    def __init__(self, java_sem_config: _JavaSemConfig):
        super().__init__(java_sem_config)
        self.logger = logging.getLogger(type(self).__name__)
        self.symlinks: dict[Path, Path] = {}

    def collect(self) -> None:
        """Collect already exists symlinks"""
        if not self.config.export_root.exists():
            return

        try:
            if self._load():
                return
        except Exception as e:
            self.logger.error("Can't load symlinks from file %s: %s", self._symlinks_path, e)

        for export_file, arcadia_file in self.collect_symlinks():
            if arcadia_file.is_symlink() and arcadia_file.resolve() == export_file:
                self.add_symlink(arcadia_file, export_file)

    def add_symlink(self, arcadia_file: Path, export_file: Path) -> None:
        self.symlinks[arcadia_file] = export_file

    def del_symlink(self, arcadia_file: Path) -> None:
        del self.symlinks[arcadia_file]

    def save(self) -> None:
        if not self.config.export_root.exists():
            return
        symlinks_path = self._symlinks_path
        symlinks: dict[str, str] = {
            str(arcadia_file): str(export_file) for arcadia_file, export_file in self.symlinks.items()
        }
        with symlinks_path.open('wb') as f:
            sjson.dump(symlinks, f)

    def _load(self) -> bool:
        symlinks_path = self._symlinks_path
        if not symlinks_path.exists():
            return False
        with symlinks_path.open('rb') as f:
            symlinks: dict[str, str] = sjson.load(f)
        self.symlinks = {Path(arcadia_file): Path(export_file) for arcadia_file, export_file in symlinks.items()}
        return True

    @property
    def _symlinks_path(self) -> Path:
        """Make filename for store symlinks"""
        return self.config.export_root / self._SYMLINKS_FILE


class _RemoveSymlinkCollector(_SymlinkCollector):
    """Collect for remove symlinks"""

    def __init__(self, exists_symlinks: _ExistsSymlinkCollector):
        super().__init__(exists_symlinks.config)
        self.logger = logging.getLogger(type(self).__name__)
        self.symlinks: dict[Path, Path] = exists_symlinks.symlinks.copy()
        self.exists_symlinks: _ExistsSymlinkCollector = exists_symlinks

    def remove(self) -> None:
        """Remove symlinks from arcadia files to export files"""
        for arcadia_file, export_file in self.symlinks.items():
            try:
                arcadia_file.unlink()
                self.exists_symlinks.del_symlink(arcadia_file)  # remove deleted from exists
            except Exception as e:
                self.logger.warning(
                    "Can't remove symlink '%s' -> '%s': %s", arcadia_file, export_file, e, exc_info=True
                )

    def add_symlink(self, arcadia_file: Path, export_file: Path) -> None:
        self.symlinks[arcadia_file] = export_file

    def del_symlink(self, arcadia_file: Path) -> None:
        del self.symlinks[arcadia_file]


class _NewSymlinkCollector(_SymlinkCollector):
    """Collect new symlinks for create later, exclude already exists"""

    def __init__(self, exists_symlinks: _ExistsSymlinkCollector, remove_symlinks: _RemoveSymlinkCollector):
        super().__init__(exists_symlinks.config)
        self.logger = logging.getLogger(type(self).__name__)
        self.exists_symlinks: _ExistsSymlinkCollector = exists_symlinks
        self.remove_symlinks: _RemoveSymlinkCollector = remove_symlinks
        self.symlinks: dict[Path, Path] = {}
        self.has_errors: bool = False

    def collect(self):
        """Collect new symlinks for creating, skip already exists symlinks"""
        for export_file, arcadia_file in self.collect_symlinks():
            if arcadia_file in self.remove_symlinks.symlinks:
                # Already exists, don't remove it
                self.remove_symlinks.del_symlink(arcadia_file)
            elif not arcadia_file.exists():
                self.symlinks[arcadia_file] = export_file
            elif arcadia_file.is_symlink() and arcadia_file.resolve().is_relative_to(_JavaSemConfig.EXPORT_ROOT_BASE):
                self.logger.error("Already symlink to another project %s -> %s", arcadia_file, arcadia_file.resolve())
                self.has_errors = True

    def create(self) -> None:
        """Create symlinks from arcadia files to export files"""
        for arcadia_file, export_file in self.symlinks.items():
            try:
                arcadia_file.symlink_to(export_file, export_file.is_dir())
                self.exists_symlinks.add_symlink(arcadia_file, export_file)  # add created symlink as exists
            except Exception as e:
                self.logger.error("Can't create symlink '%s' -> '%s': %s", arcadia_file, export_file, e, exc_info=True)
                self.has_errors = True


class _JavaSemGraph(SemGraph):
    """Creating and reading sem-graph"""

    OLD_AP_SEM = 'annotation_processors'
    NEW_AP_SEM = 'use_annotation_processor'
    JDK_PATH_SEM = 'jdk_path'
    JDK_VERSION_SEM = 'jdk_version'

    JDK_PATH_NOT_FOUND = 'NOT_FOUND'  # Magic const for not found JDK path
    BUILD_ROOT = '$B/'  # Build root in graph

    _FOREIGN_PLATFORM_TARGET_TYPENAME = 'NEvent.TForeignPlatformTarget'
    _FOREIGN_IDE_DEPEND_PLATFORM = 3

    def __init__(self, config: _JavaSemConfig):
        super().__init__(config, skip_invalid=True)
        self.logger = logging.getLogger(type(self).__name__)
        self._graph_data: list[SemNode | SemDep] = []
        self._graph_patched = False
        self.used_ap_class2path: dict[str, str | list[str]] = {}
        self.use_ap_node_ids: list[int] = []
        self.node2dep_ids: dict[int, list[int]] = {}
        self.dep_paths: dict[int, Path] = {}
        self._cached_jdk_paths = {}
        self.jdk_paths: dict[int, str] = {}
        self.foreign_targets: list[str] = []

    def make(self, **kwargs) -> None:
        """Make sem-graph file by ymake"""
        foreign_targets = []

        def listener(event) -> None:
            if not isinstance(event, dict):
                return
            if event.get('Type') == 'Error':
                self.logger.error("%s", event)
            if (
                event.get('_typename') == self._FOREIGN_PLATFORM_TARGET_TYPENAME
                and event.get('Platform') == self._FOREIGN_IDE_DEPEND_PLATFORM
            ):
                foreign_targets.append(event['Dir'])

        super().make(
            **kwargs, ev_listener=listener  # , foreign_on_nosem=True - TODO enable after support option in ymake
        )
        if foreign_targets:
            self.foreign_targets = list(set(foreign_targets))
            self.logger.info("Foreign targets: %s", self.foreign_targets)

        super().make(**kwargs, ev_listener=listener, dump_raw_graph=self.config.ymake_root / "raw_graph")
        self._patch_graph()

    def get_rel_targets(self) -> list[(Path, bool)]:
        """Get list of rel_targets from sem-graph with is_contrib flag for each"""
        rel_targets = []
        for node in self.read():
            if not isinstance(node, SemNode):
                continue  # interest only nodes
            if not node.name.startswith(self.BUILD_ROOT) or not node.name.endswith(
                '.jar'
            ):  # Search only *.jar with semantics
                continue
            rel_target = Path(node.name.replace(self.BUILD_ROOT, '')).parent  # Relative target - directory of *.jar
            is_contrib = False
            for semantic in node.semantics:
                if semantic.sems == ['consumer-type', 'contrib']:
                    is_contrib = True
                    break
            rel_targets.append((rel_target, is_contrib))
        return rel_targets

    def get_run_java_program_rel_targets(self) -> list[Path]:
        """Search RUN_JAVA_PROGRAMs in sem-graph and return relative targets for build"""
        try:
            run_java_program_rel_targets = []
            for node in self.read():
                if not isinstance(node, SemNode):
                    continue  # interest only nodes
                for semantic in node.semantics:
                    if (
                        len(semantic.sems) == 2
                        and semantic.sems[0] == "runs-classpath"
                        and semantic.sems[1].startswith('@')
                        and semantic.sems[1].endswith('.cplst')
                    ):
                        cplst = semantic.sems[1][len('@') : -len('.cplst')]
                        if not cplst:  # Ignore java runners without classpath
                            continue
                        # target is directory of cplst
                        run_java_program_rel_targets.append(
                            os.path.relpath(Path(cplst).parent, self.config.export_root)
                        )
            return run_java_program_rel_targets
        except Exception as e:
            raise YaIdeGradleException(f'Fail extract additional RUN_JAVA_PROGRAM targets from sem-graph: {e}') from e

    def _patch_graph(self) -> None:
        self._patch_annotation_processors()
        self._patch_jdk()
        if self._graph_patched:
            self._update_graph()

    def _update_graph(self) -> None:
        data: list[dict] = []
        for item in self._graph_data:
            data.append(item.as_dict())
        self.update(data)

    def _patch_annotation_processors(self) -> None:
        """Patch AP semantics in graph"""
        self._configure_patch_annotation_processors()
        self._get_graph_data_and_find_annotation_processors()
        self._do_patch_annotation_processors()
        if self.used_ap_class2path:  # Some patched
            self.logger.info(
                "Annotation processors patched in graph:\n%s",
                '\n'.join([f'{k} --> {v}' for k, v in self.used_ap_class2path.items()]),
            )
            self._graph_patched = True

    def _configure_patch_annotation_processors(self) -> None:
        """Read mapping AP class -> path from configure"""
        annotation_processors_file = (
            self.config.arcadia_root / "build" / "yandex_specific" / "gradle" / "annotation_processors.json"
        )
        if not annotation_processors_file.exists():
            raise YaIdeGradleException(f"Not found {annotation_processors_file}")
        with annotation_processors_file.open('rb') as f:
            self.ap_class2path = sjson.load(f)

    def _get_graph_data_and_find_annotation_processors(self) -> None:
        """Find nodes with AP semantics (old or new), collect dep ids for old AP semantics"""
        data: list[SemNode | SemDep] = []
        for item in self.read(all_nodes=True):
            if isinstance(item, SemDep):
                if item.from_id in self.node2dep_ids:  # collect dep ids for patching AP
                    self.node2dep_ids[item.from_id].append(item.to_id)
            if not isinstance(item, SemNode):
                data.append(item)  # non-node direct append to patched graph as is
                continue
            node = item
            if node.has_semantics():
                for semantic in node.semantics:
                    sem0 = semantic.sems[0]
                    if sem0 == self.OLD_AP_SEM:
                        self.node2dep_ids[node.id] = []  # require collect deps for patch AP classes to AP paths
                    elif sem0 == self.NEW_AP_SEM:
                        self.use_ap_node_ids.append(node.id)  # collect node ids to check for versions of all AP
            data.append(node)
        self._graph_data = data

    def _do_patch_annotation_processors(self) -> None:
        """Patch AP semantics in graph and check all AP with versions"""
        if not self.use_ap_node_ids and not self.node2dep_ids:
            return

        self._fill_dep_paths()

        # patch AP paths by deps paths and check AP has version
        for node in self._graph_data:
            if not isinstance(node, SemNode):
                continue
            # Interest only nodes with old or new semantics with AP
            if node.id not in self.node2dep_ids and node.id not in self.use_ap_node_ids:
                continue
            if node.id in self.node2dep_ids:  # require patch old to new semantic
                self._patch_node_annotation_processors(node)
            self._check_annotation_processors_has_version(node)

    def _fill_dep_paths(self) -> None:
        """Collect all used with AP deps as id -> path"""
        if not self.node2dep_ids:
            return

        # collect all unique dep ids
        dep_ids = []
        for node_dep_ids in self.node2dep_ids.values():
            dep_ids += node_dep_ids
        dep_ids = list(set(dep_ids))

        # collect all deps paths
        for node in self._graph_data:
            if not isinstance(node, SemNode):
                continue
            if node.id not in dep_ids:
                continue
            self.dep_paths[node.id] = Path(node.name.replace(self.BUILD_ROOT, ''))

    def _patch_node_annotation_processors(self, node: SemNode) -> None:
        """Path old AP semantics in one node"""
        for semantic in node.semantics:
            if semantic.sems[0] == self.OLD_AP_SEM:
                ap_paths = []
                ap_classes = semantic.sems[1:]
                for ap_class in ap_classes:
                    if ap_class in self.ap_class2path:
                        ap_path = self.ap_class2path[ap_class]
                        if ap_class not in self.used_ap_class2path:
                            self.used_ap_class2path[ap_class] = ap_path
                        found_in_deps = False
                        for dep_id in self.node2dep_ids[node.id]:
                            dep_path = self.dep_paths[dep_id]
                            if dep_path.is_relative_to(Path(ap_path)):  # found dep with same base path
                                ap_path_by_dep = str(dep_path)
                                ap_paths.append(ap_path_by_dep)  # patch class by path
                                found_in_deps = True
                                self._on_patch(ap_class, ap_path, ap_path_by_dep)
                                break
                        if not found_in_deps:
                            self.logger.error(
                                "Not found AP %s --> %s in dependencies of node %s[%d], skip it, all node dependencies:\n%s",
                                ap_class,
                                ap_path,
                                node.name,
                                node.id,
                                [self.dep_paths[dep_id] for dep_id in self.node2dep_ids[node.id]],
                            )
                    else:
                        self.logger.error("Not found path for AP class %s, skip it", ap_class)
                # Replace old semantic with classes by new semantic with paths
                semantic.sems = [self.NEW_AP_SEM] + ap_paths

    def _on_patch(self, ap_class: str, ap_path: str, ap_path_by_dep: str) -> None:
        """Collect AP patching class -> path | paths"""
        if self.used_ap_class2path[ap_class] == ap_path:  # in used base path
            self.used_ap_class2path[ap_class] = ap_path_by_dep  # overwrite by full path
        elif isinstance(self.used_ap_class2path[ap_class], list):  # in used list of paths
            if ap_path_by_dep not in self.used_ap_class2path[ap_class]:
                self.used_ap_class2path[ap_class].append(ap_path_by_dep)  # append found to list
        elif self.used_ap_class2path[ap_class] != ap_path_by_dep:  # some other path
            self.used_ap_class2path[ap_class] = [  # make list with 2 paths
                self.used_ap_class2path[ap_class],
                ap_path_by_dep,
            ]

    def _check_annotation_processors_has_version(self, node: SemNode) -> None:
        for semantic in node.semantics:
            if semantic.sems[0] == self.NEW_AP_SEM:
                for ap_path in semantic.sems[1:]:
                    if not _JavaSemGraph._is_path_has_version(ap_path):
                        self.logger.error(
                            "Using annotation processor without version %s in node %s", ap_path, node.as_dict()
                        )

    @staticmethod
    def _is_path_has_version(path: str) -> bool:
        return bool(re.fullmatch('^\\d+[.\\d]+.*$', Path(Path(path).parent).name))

    def _patch_jdk(self) -> None:
        """Patch JDK path and JDK version in graph"""
        for node in self._graph_data:
            if not isinstance(node, SemNode) or not node.has_semantics() or not node.name.startswith(self.BUILD_ROOT):
                continue
            rel_target = Path(node.name.replace(self.BUILD_ROOT, '')).parent
            in_rel_targets = self.config.in_rel_targets(rel_target)
            for semantic in node.semantics:
                sem0 = semantic.sems[0]
                if sem0 == self.JDK_VERSION_SEM and len(semantic.sems) > 1:
                    jdk_version = _JavaSemGraph._get_jdk_version(semantic.sems[1])
                    semantic.sems = [self.JDK_VERSION_SEM, str(jdk_version)]
                    self._graph_patched = True
                elif sem0 == self.JDK_PATH_SEM and len(semantic.sems) > 1:
                    jdk_version = _JavaSemGraph._get_jdk_version(semantic.sems[1])
                    # don't load JDK for non-targets, fill by dummy string
                    jdk_path = self.get_jdk_path(jdk_version) if in_rel_targets else f"JDK_PATH_{jdk_version}"
                    semantic.sems = [self.JDK_PATH_SEM, jdk_path]
                    self._graph_patched = True

    def get_jdk_path(self, jdk_version: int) -> str:
        try:
            if jdk_version in self._cached_jdk_paths:
                return self._cached_jdk_paths[jdk_version]
            else:
                jdk_real_path = Path(tools.tool(f'java{jdk_version}').replace('/bin/java', ''))
                jdk_path = Path.home() / ".ya" / "jdk" / str(jdk_version)
                if jdk_path.exists() and jdk_path.resolve() != jdk_real_path:
                    jdk_path.unlink()  # remove invalid symlink to JDK
                if not jdk_path.exists():  # create new symlink to JDK
                    _SymlinkCollector.mkdir(jdk_path.parent)
                    jdk_path.symlink_to(jdk_real_path, target_is_directory=True)
        except Exception as e:
            self.logger.error(f"Can't find JDK {jdk_version} in tools: {e}")
            jdk_path = self.JDK_PATH_NOT_FOUND
        jdk_path = str(jdk_path)
        self._cached_jdk_paths[jdk_version] = jdk_path
        if jdk_path != self.JDK_PATH_NOT_FOUND:
            self.jdk_paths[jdk_version] = jdk_path  # Public only valid jdk paths
        return jdk_path

    @staticmethod
    def _get_jdk_version(s: str) -> int:
        """Extract JDK version from resource var name"""
        m = re.search('(?:JDK|jdk)(\\d+)', s)
        return int(m.group(1)) if m else 0


class _Exporter:
    """Generating files to export root"""

    GRADLE_JDK_VERSION = 17

    def __init__(self, java_sem_config: _JavaSemConfig, java_sem_graph: _JavaSemGraph):
        self.logger = logging.getLogger(type(self).__name__)
        self.config: _JavaSemConfig = java_sem_config
        self.sem_graph: _JavaSemGraph = java_sem_graph

    def export(self) -> None:
        """Generate files from sem-graph by yexport"""
        project_name = (
            self.config.params.gradle_name
            if self.config.params.gradle_name
            else Path(self.config.params.abs_targets[0]).name
        )
        self.logger.info("Project name: %s", project_name)

        self.logger.info("Path prefixes for skip in yexport: %s", self.config.params.rel_targets)

        attrs_for_all_templates = []

        gradle_jdk_path = self.sem_graph.get_jdk_path(self.GRADLE_JDK_VERSION)
        if gradle_jdk_path != self.sem_graph.JDK_PATH_NOT_FOUND:
            attrs_for_all_templates = [
                f"gradle_jdk_version = {self.GRADLE_JDK_VERSION}",
                f"gradle_jdk_path = '{gradle_jdk_path}'",
            ]

        yexport_toml = self.config.ymake_root / 'yexport.toml'
        with yexport_toml.open('w') as f:
            f.write(
                '\n'.join(
                    [
                        '[add_attrs.root]',
                        *attrs_for_all_templates,
                        '',
                        '[add_attrs.dir]',
                        f'build_contribs = {'true' if self.config.params.build_contribs else 'false'}',
                        f'disable_errorprone = {'true' if self.config.params.disable_errorprone else 'false'}',
                        *attrs_for_all_templates,
                        '',
                        '[add_attrs.target]',
                        *attrs_for_all_templates,
                        '',
                        '[[target_replacements]]',
                        f'skip_path_prefixes = [ "{'", "'.join(self.config.params.rel_targets)}" ]',
                        '',
                        '[[target_replacements.addition]]',
                        'name = "consumer-prebuilt"',
                        'args = []',
                        '[[target_replacements.addition]]',
                        'name = "IGNORED"',
                        'args = []',
                    ]
                )
            )

        yexport_cmd = [
            self.config.yexport_bin,
            '--arcadia-root',
            str(self.config.arcadia_root),
            '--export-root',
            str(self.config.export_root),
            '--project-root',
            str(self.config.settings_root),
            '--configuration',
            str(self.config.ymake_root),
            '--semantic-graph',
            str(self.sem_graph.sem_graph_file),
        ]
        if self.config.params.yexport_debug_mode is not None:
            yexport_cmd += ["--debug-mode", str(self.config.params.yexport_debug_mode)]
        yexport_cmd += ['--generator', 'ide-gradle', '--target', project_name]

        self.logger.info("Generate by yexport command:\n%s", ' '.join(yexport_cmd))
        r = subprocess.run(yexport_cmd, capture_output=True, text=True)
        if r.returncode != 0:
            self.logger.error("Fail generating by yexport:\n%s", r.stderr)
            raise YaIdeGradleException(f'Fail generating by yexport with exit_code={r.returncode}')

        gradle_properties_file = self.config.export_root / ".gradle" / "gradle.properties"
        if self.sem_graph.jdk_paths:
            _SymlinkCollector.mkdir(gradle_properties_file.parent)
            with (self.config.export_root / ".gradle" / "gradle.properties").open('w') as f:
                f.write(
                    '\n'.join(
                        [
                            f'org.gradle.java.home={gradle_jdk_path}' if gradle_jdk_path else None,
                            'org.gradle.java.installations.fromEnv='
                            + ','.join('JDK' + str(jdk_version) for jdk_version in self.sem_graph.jdk_paths.keys()),
                            'org.gradle.java.installations.paths='
                            + ','.join(jdk_path for jdk_path in self.sem_graph.jdk_paths.values()),
                            '',
                        ]
                    )
                )
        elif gradle_properties_file.exists():
            gradle_properties_file.unlink()


class _Builder:
    """Build required targets"""

    def __init__(self, java_sem_config: _JavaSemConfig, java_sem_graph: _JavaSemGraph):
        self.logger = logging.getLogger(type(self).__name__)
        self.config: _JavaSemConfig = java_sem_config
        self.sem_graph: _JavaSemGraph = java_sem_graph

    def build(self) -> None:
        """Extract build targets from sem-graph and build they"""
        try:
            build_rel_targets = list(
                set(self.sem_graph.foreign_targets + self.sem_graph.get_run_java_program_rel_targets())
            )
            rel_targets = self.sem_graph.get_rel_targets()
            for rel_target, is_contrib in rel_targets:
                if self.config.in_rel_targets(rel_target):
                    # Skip target, already in input targets
                    continue
                elif self.config.params.build_contribs or not is_contrib:
                    # Build all non-input or not contrib targets
                    build_rel_targets.append(rel_target)
        except Exception as e:
            raise YaIdeGradleException(
                f'Fail extract build targets from sem-graph {self.sem_graph.sem_graph_file}: {e}'
            ) from e

        if not build_rel_targets:
            return

        import app_ctx

        try:
            ya_make_opts = yarg.merge_opts(build_opts.ya_make_options(free_build_targets=True))
            opts = yarg.merge_params(ya_make_opts.initialize(self.config.params.ya_make_extra))

            arcadia_root = self.config.arcadia_root

            opts.bld_dir = self.config.params.bld_dir
            opts.arc_root = str(arcadia_root)
            opts.bld_root = self.config.params.bld_root

            opts.rel_targets = []
            opts.abs_targets = []
            for build_rel_target in build_rel_targets:  # Add all targets for build simultaneously
                opts.rel_targets.append(str(build_rel_target))
                opts.abs_targets.append(str(arcadia_root / build_rel_target))

            self.logger.info("Making building graph...")
            with app_ctx.event_queue.subscription_scope(ya_make.DisplayMessageSubscriber(opts, app_ctx.display)):
                graph, _, _, _, _ = build_graph.build_graph_and_tests(opts, check=True, display=app_ctx.display)
            self.logger.info("Building all by graph...")
            builder = ya_make.YaMake(opts, app_ctx, graph=graph, tests=[])
            return_code = builder.go()
            if return_code != 0:
                raise YaIdeGradleException('Some builds failed')
        except Exception as e:
            raise YaIdeGradleException(f'Failed in build process: {e}') from e


class _Remover:
    """Remove all symlinks and export root"""

    def __init__(self, java_sem_config: _JavaSemConfig, remove_symlinks: _RemoveSymlinkCollector):
        self.logger = logging.getLogger(type(self).__name__)
        self.config: _JavaSemConfig = java_sem_config
        self.remove_symlinks: _RemoveSymlinkCollector = remove_symlinks

    def remove(self) -> None:
        """Remove all exists symlinks and then remove export root"""
        if self.remove_symlinks.symlinks:
            self.logger.info("Remove %d symlinks from arcadia to export root", len(self.remove_symlinks.symlinks))
            self.remove_symlinks.remove()
        if self.config.export_root.exists():
            try:
                self.logger.info("Remove export root %s", self.config.export_root)
                shutil.rmtree(self.config.export_root)
            except Exception as e:
                self.logger.warning("While removing %s: %s", self.config.export_root, e, exc_info=True)
        else:
            self.logger.info("Export root %s already not found", self.config.export_root)


def do_gradle(params):
    """Real handler of `ya ide gradle`"""
    do_gradle_stage = stage_tracer.get_tracer("gradle").start('do_gradle')

    try:
        config = _JavaSemConfig(params)

        exists_symlinks = _ExistsSymlinkCollector(config)
        exists_symlinks.collect()
        remove_symlinks = _RemoveSymlinkCollector(exists_symlinks)

        if config.params.remove:
            remover = _Remover(config, remove_symlinks)
            remover.remove()
            return

        sem_graph = _JavaSemGraph(config)
        sem_graph.make()

        exporter = _Exporter(config, sem_graph)
        exporter.export()

        ya_settings = _YaSettings(config)
        ya_settings.save()

        new_symlinks = _NewSymlinkCollector(exists_symlinks, remove_symlinks)
        new_symlinks.collect()

        if new_symlinks.has_errors:
            raise YaIdeGradleException('Some errors during creating symlinks, read the logs for more information')

        remove_symlinks.remove()
        new_symlinks.create()
        exists_symlinks.save()

        builder = _Builder(config, sem_graph)
        builder.build()

    finally:
        do_gradle_stage.finish()
