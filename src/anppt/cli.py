"""Cli entry for ANPPT."""

from pathlib import Path

from cookiecutter.exceptions import OutputDirExistsException
from cookiecutter.main import cookiecutter


def cli_main() -> None:
    """Main entry point for the ANPPT CLI."""
    source_path = str(Path(__file__).parent.parent.parent.resolve().absolute())
    try:
        cookiecutter(source_path)
    except KeyboardInterrupt:
        return
    except OutputDirExistsException as e:
        print(f"{e}! Exiting...")  # noqa: T201
        return
