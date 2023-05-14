"""Cli entry for ANPPT."""

from pathlib import Path

from cookiecutter.main import cookiecutter


def cli_main() -> None:
    """Main entry point for the ANPPT CLI."""
    source_path = str(Path(__file__).parent.parent.parent.resolve().absolute())
    cookiecutter(source_path)
