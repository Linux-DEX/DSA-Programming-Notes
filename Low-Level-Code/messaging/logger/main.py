import io
import os
import tempfile

from logger import ConsoleHandler, FileHandler, Level, Logger


def main():
    console = io.StringIO()
    path = tempfile.NamedTemporaryFile(delete=False).name
    try:
        logger = Logger([
            ConsoleHandler(Level.INFO, console),
            FileHandler(path, Level.DEBUG),
        ])
        logger.debug("cache miss")
        logger.info("request accepted")
        logger.warn("retrying")
        logger.error("upstream failed")

        printed = console.getvalue()
        stored = open(path, encoding="utf-8").read()
        print(printed, end="")
        print("--- file ---")
        print(stored, end="")

        assert "DEBUG" not in printed
        assert "INFO: request accepted" in printed
        assert "WARN: retrying" in printed
        assert "ERROR: upstream failed" in printed
        assert "DEBUG: cache miss" in stored
        assert "ERROR: upstream failed" in stored
    finally:
        os.remove(path)


if __name__ == "__main__":
    main()
