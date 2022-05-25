""".. include:: ../README.md"""  # noqa

import logging

from ._helpers import ColoredFormatter, Config, SuccessLogger
from .base import BaseClass
from .cli import cli_main

# set up logging for the package
logging.setLoggerClass(SuccessLogger)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console = logging.StreamHandler()
console.setFormatter(ColoredFormatter("[%(name)s] (%(levelname)s): %(message)s"))
logger.addHandler(console)

__all__ = ["BaseClass", "cli_main", "Config"]

__pdoc__ = {}
__pdoc__["_helpers"] = True
__pdoc__["_validation"] = True
