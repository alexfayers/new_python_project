""".. include:: ../README.md"""  # noqa

import logging

from ._helpers import ColoredLogger as ColoredLogger
from .base import BaseClass
from .cli import cli_main

logging.setLoggerClass(ColoredLogger)
logging.getLogger(__name__).setLevel(logging.DEBUG)

__all__ = ["BaseClass", "cli_main"]

__pdoc__ = {}
__pdoc__["_helpers"] = True
__pdoc__["_validation"] = True
