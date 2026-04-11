import os
import re

from ymake import parser


sys_includes_re = re.compile('#include\\s+<([^>]+)>')
local_includes_re = re.compile('#include\\s+"([^"]+)"')
imports_re = re.compile('import\\s+([^;]+)\\s*;')


@parser("cppm")
class CppModuleParser:
    def __init__(self, path, unit):
        self._includes = []
        with open(path) as f:
            for line in f:
                result = sys_includes_re.search(line)
                if result:
                    self._includes += ['$U/' + result.group(1)]
                    continue

                result = local_includes_re.search(line)
                if result:
                    self._includes += ['$U/' + result.group(1)]
                    continue

                result = imports_re.search(line)
                if result:
                    self._includes += [os.path.join('$B', unit.get('MODDIR'), 'mods', result.group(1) + '.pcm')]
                    continue

    def includes(self):
        return self._includes
