from enum import IntEnum


class Level(IntEnum):
    DEBUG = 10
    INFO = 20
    WARN = 30
    ERROR = 40


class ConsoleHandler:
    def __init__(self, level, stream):
        self.level = level
        self.stream = stream

    def emit(self, level, message):
        if level < self.level:
            return
        print(f"{level.name}: {message}", file=self.stream)


class FileHandler:
    """
    ponytail: the file is opened for every line. Keep the handle open
    if this logger runs for a long time.
    """

    def __init__(self, path, level):
        self.path = path
        self.level = level

    def emit(self, level, message):
        if level < self.level:
            return
        with open(self.path, "a", encoding="utf-8") as handle:
            handle.write(f"{level.name}: {message}\n")


class Logger:
    def __init__(self, handlers):
        self.handlers = list(handlers)

    def log(self, level, message):
        for handler in self.handlers:
            handler.emit(level, message)

    def debug(self, message):
        self.log(Level.DEBUG, message)

    def info(self, message):
        self.log(Level.INFO, message)

    def warn(self, message):
        self.log(Level.WARN, message)

    def error(self, message):
        self.log(Level.ERROR, message)
