"""CLI functionality of `{{ cookiecutter.project_name }}`."""

import logging
import sys
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

from rich.logging import RichHandler

from . import {{ cookiecutter.__project_class_name }}, __version__


def cli_main() -> None:
    """CLI entrypoint for `{{ cookiecutter.project_name }}`. Uses `{{ cookiecutter.__project_slug}}.{{ cookiecutter.__project_class_name }}`."""
    argparser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    {%- if cookiecutter.config_file_required == 'y' %}
    argparser.add_argument("-c", "--config", help="Path to config file", type=str, default="config.toml")
    {%- endif %}
    argparser.add_argument("-v", "--verbose", help="Enable verbose logging", action="count", default=0)
    argparser.add_argument("-V", "--version", help="Output the project's current version and exit", action="store_true")

    args = argparser.parse_args()
    {%- if cookiecutter.config_file_required == 'y' %}
    config_file = args.config
    {%- endif %}
    verbose_level: int = args.verbose

    package_logger = logging.getLogger("{{ cookiecutter.__project_slug}}")

    # initialise log handling
    package_logger.addHandler(RichHandler(rich_tracebacks=True))

    # logging defaults to WARNING, then INFO, then DEBUG, then VERBOSE

    if verbose_level == 0:
        package_logger.setLevel(logging.WARNING)
    elif verbose_level == 1:
        package_logger.setLevel(logging.INFO)
    elif verbose_level >= 2:
        package_logger.setLevel(logging.DEBUG)

    if args.version is True:
        package_logger.setLevel(logging.INFO)
        package_logger.info(f"Version: {__version__}")
        sys.exit(1)

    try:
        app = {{ cookiecutter.__project_class_name }}({% if cookiecutter.config_file_required == 'y' %}config_file{% endif %})
    except Exception:
        package_logger.fatal("Failed to initialise - exiting...")
        sys.exit(1)

    {%- if cookiecutter.config_file_required == 'y' %}
    # NOTE: example config read
    if app.read_config("debug", "enabled", default=False):
        app.logger.debug("Debug mode is enabled in the config file!")
    {%- endif %}

    # NOTE: main functionality starts from here
    app.run()
