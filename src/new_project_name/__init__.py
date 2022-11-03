""".. include:: ../../README.md"""  # noqa

import logging

from ._helpers import ColoredFormatter as _ColoredFormatter
from ._helpers import SuccessLogger as _SuccessLogger
from .base import BaseClass
from .cli import cli_main

# set up logging for the package
logging.setLoggerClass(_SuccessLogger)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console = logging.StreamHandler()
console.setFormatter(_ColoredFormatter("[%(name)s] (%(levelname)s): %(message)s"))
logger.addHandler(console)

__all__ = ["BaseClass", "cli_main", "_helpers", "_validation"]
