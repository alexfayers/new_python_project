""".. include:: ../../README.md"""  # noqa
__version__ = "{{ cookiecutter.version }}"

import logging

from .base import {{ cookiecutter.__project_class_name }}
from .cli import cli_main

# set up logging for the package
logger = logging.getLogger(__name__)

__all__ = ["{{ cookiecutter.__project_class_name }}", "cli_main", "_helpers"]
