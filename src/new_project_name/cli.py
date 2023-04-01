"""CLI functionality of `new_project_readable_name`."""

import logging
import sys
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

from . import BaseClass, __version__
from ._helpers.nice_logger import VERBOSE_LEVEL, SuccessLogger


def cli_main() -> None:
    """CLI entrypoint for `new_project_readable_name`. Uses `new_project_name.BaseClass`."""
    argparser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    argparser.add_argument("-c", "--config", help="Path to config file", type=str, default="config.toml")
    argparser.add_argument("-v", "--verbose", help="Enable verbose logging", action="count", default=0)
    argparser.add_argument("-V", "--version", help="Output the project's current version and exit", action="store_true")

    args = argparser.parse_args()
    config_file = args.config
    verbose_level: int = args.verbose

    if args.version is True:
        print(f"Version: {__version__}")
        sys.exit(1)

    package_logger: SuccessLogger = logging.getLogger("new_project_name")  # type: ignore

    # logging defaults to WARNING, then INFO, then DEBUG, then VERBOSE

    if verbose_level == 0:
        package_logger.setLevel(logging.WARNING)
    elif verbose_level == 1:
        package_logger.setLevel(logging.INFO)
    elif verbose_level == 2:
        package_logger.setLevel(logging.DEBUG)
    elif verbose_level >= 3:
        package_logger.setLevel(VERBOSE_LEVEL)

    try:
        app = BaseClass(config_file)
    except Exception:
        package_logger.fatal("Failed to initialise - exiting...")
        sys.exit(1)

    if app.read_config("debug", "enabled", default=False):
        app.logger.debug("Debug mode is enabled in the config file!")
