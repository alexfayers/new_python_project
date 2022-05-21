"""Helper functions and classes to make life easier. Mainly for internal use within the package."""

from .color_logger import ColoredFormatter, ColoredLogger
from .config_loader import Config

__all__ = ["ColoredLogger", "ColoredFormatter", "Config"]

__pdoc__ = {}
__pdoc__["ConfigSection"] = True
