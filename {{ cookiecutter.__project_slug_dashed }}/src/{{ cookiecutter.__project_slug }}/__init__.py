""".. include:: ../../README.md"""  # noqa
__version__ = "{{ cookiecutter.version }}"

import logging

from ._helpers import ColoredFormatter as _ColoredFormatter
from ._helpers import SuccessLogger as _SuccessLogger
from .base import {{ cookiecutter.__project_class_name }}
from .cli import cli_main

# set up logging for the package
logging.setLoggerClass(_SuccessLogger)
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
console = logging.StreamHandler()
console.setFormatter(_ColoredFormatter("[%(name)s] (%(levelname)s): %(message)s"))
logger.addHandler(console)

__all__ = ["{{ cookiecutter.__project_class_name }}", "cli_main", "_helpers"]
