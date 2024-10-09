import datetime
import logging
import os
import six

from exts import fs
from exts import func
from exts.compress import UCompressor


_LOG_FILE_NAME_FMT = '%H-%M-%S'
_LOG_DIR_NAME_FMT = '%Y-%m-%d'
_DAYS_TO_SAVE = 7
FILE_LOG_FMT = '%(asctime)s %(levelname)s (%(name)s) [%(threadName)s] %(message)s'


class TokenFilterFormatter(logging.Formatter):
    def __init__(self, fmt, replacements=None):
        super(TokenFilterFormatter, self).__init__(fmt)
        self._replacements = replacements or []
        if not replacements:
            import devtools.ya.core.sec as sec

            self._replacements = sorted(sec.mine_suppression_filter())

    def _filter(self, s):
        for r in self._replacements:
            s = s.replace(r, "[SECRET]")
        return s

    def format(self, record):
        return self._filter(super(TokenFilterFormatter, self).format(record))


class LogChunks(object):
    def __init__(self, log_dir):
        self._log_dir = fs.create_dirs(log_dir)

    def get_or_create(self, chunk_name):
        return fs.create_dirs(os.path.join(self._log_dir, chunk_name))

    def cleanup(self, predicate):
        for x in os.listdir(self._log_dir):
            if predicate(x):
                fs.remove_tree_safe(os.path.join(self._log_dir, x))


class UCFileHandler(logging.StreamHandler):
    def __init__(self, filename, codec):
        mode = "wt" if six.PY3 else "wb"

        self.compressor = UCompressor(filename, codec, mode)
        self.compressor.start()
        logging.StreamHandler.__init__(self, self.compressor.getInputStream())

    def close(self):
        self.acquire()
        try:
            try:
                try:
                    self.flush()
                finally:
                    self.compressor.stop()
            finally:
                logging.StreamHandler.close(self)
        finally:
            self.release()

    def emit(self, record):
        logging.StreamHandler.emit(self, record)


def parse_log_dir(x):
    try:
        return datetime.datetime.strptime(x, _LOG_DIR_NAME_FMT)
    except ValueError:
        return None


def with_file_log(log_dir, run_uid):
    now = datetime.datetime.now()

    chunks = LogChunks(log_dir)

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    def older_than(x):
        return now - x > datetime.timedelta(days=_DAYS_TO_SAVE) if x else False

    chunks.cleanup(func.compose(older_than, parse_log_dir))

    log_chunk = chunks.get_or_create(now.strftime(_LOG_DIR_NAME_FMT))
    file_name = os.path.join(log_chunk, now.strftime(_LOG_FILE_NAME_FMT) + '.' + run_uid + '.log')
    root.addHandler(_file_logger(file_name))

    yield file_name


def with_custom_file_log(ctx, params, replacements):
    root = logging.getLogger()

    log_file = getattr(params, 'log_file', None)
    in_memory_handler = ctx.file_in_memory_log

    if log_file:
        file_handler = _file_logger(log_file, replacements=replacements)

        for entry in in_memory_handler.storage:
            file_handler.emit(entry)
        root.addHandler(file_handler)

    in_memory_handler.close()
    root.removeHandler(in_memory_handler)

    yield


def _file_logger(log_file, loglevel=logging.DEBUG, replacements=None):
    if log_file.endswith('.uc'):
        file_handler = UCFileHandler(log_file, 'zstd_1')
    else:
        file_handler = logging.FileHandler(log_file)

    file_handler.setLevel(loglevel)

    file_handler.setFormatter(TokenFilterFormatter(FILE_LOG_FMT, replacements or []))

    return file_handler
