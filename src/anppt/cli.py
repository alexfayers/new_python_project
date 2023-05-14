"""Cli entry for ANPPT."""

from cookiecutter.main import cookiecutter


def cli_main() -> None:
    """Main entry point for the ANPPT CLI."""
    cookiecutter(".")
