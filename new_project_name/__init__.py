""".. include:: ../README.md"""  # noqa

from .base import BaseClass
from .cli import cli_main

__all__ = ["BaseClass", "cli_main"]

__pdoc__ = {}
__pdoc__["_helpers"] = True
