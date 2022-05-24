"""CLI functionality of `new_project_name`."""

from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

from .base import BaseClass


def cli_main() -> None:
    """CLI entrypoint for `new_project_name`. Uses `BaseClass`."""
    argparser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    argparser.add_argument(
        "-c", "--config", help="Path to config file", type=str, default="config.yml"
    )

    args = argparser.parse_args()
    config_file = args.config

    app = BaseClass(config_file)

    app.logger.info(
        f"Hi, welcome to {app.config.INFO.NAME} by {app.config.INFO.AUTHOR}!"
    )

    app.logger.debug("We're in debug mode!")
