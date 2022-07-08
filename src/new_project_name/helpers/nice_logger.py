"""Nice logging features, including a "success" level and colored logging in both the terminal - and HTML."""

import copy
import html
import logging
from typing import Any, Dict

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

COLORS_HTML = {
    "WARNING": "yellow",
    "INFO": "black",
    "DEBUG": "grey",
    "CRITICAL": "darkred",
    "ERROR": "red",
    "SUCCESS": "green",
}

COLORS_BOOTSTRAP = {
    "WARNING": "warning",
    "INFO": "body",
    "DEBUG": "muted",
    "CRITICAL": "warning",
    "ERROR": "danger",
    "SUCCESS": "success",
}


RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[1;%dm"
BOLD_SEQ = "\033[1m"

SUCCESS_LEVEL = 25


class ColoredFormatter(logging.Formatter):
    """A logging formatter which enables ANSI colors for each log level."""

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
        return super().format(new_record)


class WebFormatter(logging.Formatter):
    """A logging formatter which enables ANSI colors for each log level - in HTML.

    Useful for situations where you want to show logging output in a web interface, or something like that.
    """

    COLORS: Dict[str, str] = {}
    """The find/replace map for log level colors"""

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
        if levelname in self.COLORS:
            replacement_fields = ["msg", "levelname"]

            for replacement_field in replacement_fields:
                value = new_record.__dict__[replacement_field]
                new_record.__dict__[replacement_field] = (
                    f"<span class='text-{self.COLORS[levelname]}'>"
                    f"{html.escape(value)}"
                    "</span>"
                )

        return super().format(new_record)


class HTMLFormatter(WebFormatter):
    """A logging formatter which enables ANSI colors for each log level - in HTML."""

    COLORS = COLORS_HTML


class BootstrapFormatter(WebFormatter):
    """A logging formatter which enables ANSI colors for each log level - in HTML (but with Bootstrap color names)."""

    COLORS = COLORS_BOOTSTRAP


class SuccessLogger(logging.Logger):
    """A logger which provides a `success` level - good to use with a `ColoredFormatter`."""

    def __init__(self, name: str, **kwargs: Any) -> None:
        """Initialises a `SuccessLogger`.

        Args:
            name (str): The name of the logger
        """
        super().__init__(name, **kwargs)

        # self.propagate = True  # don't propagate to parent loggers, otherwise we get duplicate messages

        logging.addLevelName(SUCCESS_LEVEL, "SUCCESS")

    def success(self, msg: str, *args: Any, **kwargs: Any) -> None:
        """Enables the "success" log type for all loggers using `SuccessLogger`.

        Args:
            msg (str): The message to log
        """
        if self.isEnabledFor(SUCCESS_LEVEL):
            self._log(SUCCESS_LEVEL, msg, args, **kwargs)
