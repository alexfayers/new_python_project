import copy
import logging
from typing import Any

# Config stuff

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

COLORS = {
    "WARNING": YELLOW,
    "INFO": WHITE,
    "DEBUG": BLUE,
    "CRITICAL": YELLOW,
    "ERROR": RED,
    "SUCCESS": GREEN,
}

RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[1;%dm"
BOLD_SEQ = "\033[1m"

SUCCESS_LEVEL = 25


class ColoredFormatter(logging.Formatter):
    """A logging formatter which enables ANSI colors for each log level."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialises a `ColoredFormatter` object."""
        super(ColoredFormatter, self).__init__(*args, **kwargs)

    def format(self, record: logging.LogRecord) -> str:
        """Formats the `record`, ensuring coloured output.

        Args:
            record (logging.LogRecord): The log record to format

        Returns:
            str: The formatted log record
        """
        new_record = copy.copy(
            record
        )  # create a copy of the record so that the original is not changed

        levelname = new_record.levelname
        if levelname in COLORS:
            levelname_color = (
                COLOR_SEQ % (30 + COLORS[levelname]) + levelname + RESET_SEQ
            )
            new_record.levelname = levelname_color
        return super(ColoredFormatter, self).format(new_record)


class ColoredLogger(logging.Logger):
    """A logger which uses the `ColoredFormatter` to provide coloured output."""

    CONSOLE_FORMAT = "[%(name)s] (%(levelname)s): %(message)s"

    def __init__(self, name: str) -> None:
        """Initialises a `ColoredLogger`.

        Args:
            name (str): The name of the logger
        """
        super(ColoredLogger, self).__init__(name, logging.DEBUG)

        logging.SUCCESS = SUCCESS_LEVEL  # type: ignore
        logging.addLevelName(logging.SUCCESS, "SUCCESS")  # type: ignore

        setattr(
            self,
            "success",
            lambda message, *args: self._log(
                logging.SUCCESS, message, args  # type: ignore
            ),
        )

        console = logging.StreamHandler()
        console.setFormatter(ColoredFormatter(self.CONSOLE_FORMAT))

        self.addHandler(console)

    def success(self, msg: str, *args: Any, **kwargs: Any) -> None:
        """Enables the "success" log type for all loggers using `ColoredLogger`.

        Args:
            msg (str): The message to log
        """
        if self.isEnabledFor(SUCCESS_LEVEL):
            self._log(SUCCESS_LEVEL, msg, args, **kwargs)
