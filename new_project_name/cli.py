"""CLI functionality of `new_project_name`."""

from .base import BaseClass


def cli_main() -> None:
    """CLI entrypoint for `new_project_name`. Uses `BaseClass`."""
    app = BaseClass("config.yml")

    app.logger.info(
        f"Hi, welcome to {app.config.INFO.NAME} by {app.config.INFO.AUTHOR}!"
    )
