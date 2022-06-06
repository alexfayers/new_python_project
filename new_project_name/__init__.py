""".. include:: ../README.md"""  # noqa

import logging

from .base import BaseClass
from .cli import cli_main
from .helpers import ColoredFormatter, Config, SuccessLogger

# set up logging for the package
logging.setLoggerClass(SuccessLogger)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console = logging.StreamHandler()
console.setFormatter(ColoredFormatter("[%(name)s] (%(levelname)s): %(message)s"))
logger.addHandler(console)

__all__ = ["BaseClass", "cli_main", "Config", "helpers", "validation"]
