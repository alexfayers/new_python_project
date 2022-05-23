"""Called when `new_project_name` is called from the command line as a module."""

from .cli import cli_main

if __name__ == "__main__":
    cli_main()
