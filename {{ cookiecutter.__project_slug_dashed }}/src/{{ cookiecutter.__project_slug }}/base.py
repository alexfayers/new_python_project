"""The main functionality of `{{ cookiecutter.project_name }}`."""

import logging
{%- if cookiecutter.config_file_required == 'y' %}
from pathlib import Path
{%- endif %}
from typing import Any{% if cookiecutter.config_file_required == 'y' %}, TypeVar{% endif %}

{%- if cookiecutter.config_file_required == 'y' %}
import toml

D = TypeVar("D")
{%- endif %}


class {{ cookiecutter.__project_class_name }}:
    """Everything in the project comes back to here."""

    def __init__(self{% if cookiecutter.config_file_required == 'y' %}, config_file: str{% endif %}) -> None:
        """Initialises the base class for `{{ cookiecutter.__project_slug}}` by loading the config and setting up a logger.{%- if cookiecutter.config_file_required == 'y' %}

        Args:
            config_file (str): Path to a config file containing settings for the class.
        {%- endif %}"""
        self.logger = logging.getLogger(__name__).getChild(self.__class__.__qualname__)  # type: ignore

        {%- if cookiecutter.config_file_required == 'y' %}
        self._config = self._load_config(Path(config_file))
        {%- endif %}

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

    {%- if cookiecutter.config_file_required == 'y' %}
    def _load_config(self, config_file: Path) -> dict:
        """Loads the config file using toml.

        Args:
            config_file (Path): Path to a config file containing settings for the class.

        Returns:
            dict: The config file as a dictionary.
        """
        self.logger.debug("Loading config file from %s", config_file)

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
        self.logger.debug("Reading config value: %s", path)

        located_data = self._config

        for section in path:
            try:
                located_data = located_data[section]
            except (KeyError, TypeError):
                return default

        return located_data
    {%- endif %}

    def run(self) -> None:
        """The main entrypoint for the project."""
        # Add your code here...
        self.logger.warning("Todo: Everything...")
