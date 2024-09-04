# TODO: replace with library.python.find_root when respawn will be independent from scripts

import os

import typing as tp  # noqa


def is_root(path):
    return os.path.exists(os.path.join(path, ".arcadia.root")) or os.path.exists(
        os.path.join(path, 'build', 'ya.conf.json')
    )


def detect_root(path, detector=is_root):
    # type: (str, tp.Callable) -> tp.Optional[str]
    return _find_path(path, detector)


def detect_root_or_raise(path, detector=is_root):
    root = _find_path(path, detector)
    if root:
        return root
    else:
        raise Exception("Not in arcadia root")


def _find_path(starts_from, check):
    p = starts_from
    while True:
        if check(p):
            return p
        next_p = os.path.dirname(p)
        if next_p == p:
            return None
        p = next_p
