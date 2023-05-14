"""The main functionality of `{{ cookiecutter.project_name }}`."""

import logging
from pathlib import Path
from typing import TYPE_CHECKING, Any, TypeVar

import toml

if TYPE_CHECKING:
    from ._helpers.nice_logger import SuccessLogger

D = TypeVar("D")


class {{ cookiecutter.__project_class_name }}:
    """Everything in the project comes back to here."""

    def __init__(self, config_file: str) -> None:
        """Initialises the base class for `{{ cookiecutter.project_slug}}` by loading the config and setting up a logger.

        Args:
            config_file (str): Path to a config file containing settings for the class.
        """
        self.logger: SuccessLogger = logging.getLogger(__name__).getChild(self.__class__.__qualname__)  # type: ignore

        self._config = self._load_config(Path(config_file))

    def _log_and_raise_exception(self, message: str, *args: Any, **kwargs: Any) -> None:
        """Logs an error and raises an exception.

        Args:
            message (str): The message to log and raise.
            *args (Any): Generic positional arguments
            **kwargs (Any): Generic keyword arguments

        Raises:
            Exception: The raised exception.
        """
        self.logger.error(message, *args, **kwargs)
        raise Exception(message)

    def _load_config(self, config_file: Path) -> dict:
        """Loads the config file using toml.

        Args:
            config_file (Path): Path to a config file containing settings for the class.

        Returns:
            dict: The config file as a dictionary.
        """
        self.logger.verbose("Loading config file from %s", config_file)

        try:
            with open(config_file) as f:
                try:
                    config = toml.load(f)
                except toml.TomlDecodeError:
                    self._log_and_raise_exception("Config file '%s' is not valid TOML: %s", config_file)
        except FileNotFoundError:
            self._log_and_raise_exception("Config file '%s' does not exist!", config_file)

        return config

    def read_config(self, *path: str, default: D | None = None) -> Any | D:
        """Reads a value from the config file.

        Args:
            *path (str): The path to the value in the config file.
            default (Any): The default value to return if the path does not exist.

        Returns:
            Any: The value found at the path in the config file, or the default value if the path does not exist.
        """
        self.logger.verbose("Reading config value: %s", path)

        located_data = self._config

        for section in path:
            try:
                located_data = located_data[section]
            except (KeyError, TypeError):
                return default

        return located_data
