""".. include:: ../../README.md"""  # noqa

import logging

from .base import BaseClass
from .cli import cli_main
from .helpers import ColoredFormatter as _ColoredFormatter
from .helpers import SuccessLogger as _SuccessLogger

# set up logging for the package
logging.setLoggerClass(_SuccessLogger)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console = logging.StreamHandler()
console.setFormatter(_ColoredFormatter("[%(name)s] (%(levelname)s): %(message)s"))
logger.addHandler(console)

__all__ = ["BaseClass", "cli_main", "helpers", "validation"]
