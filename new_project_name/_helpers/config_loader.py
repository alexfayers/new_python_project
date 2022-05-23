import logging
import sys
from typing import Any

import yaml

from .decorators import singleton


def set_attributes(config_object: object, config: dict[str, Any]) -> None:
    """Set all of the keys within the `config` parameter as attributes of this `ConfigSection`.

    Args:
        config_object (object): The class to set the attributes on
        config (dict[str, Any]): A config section dictionary
    """
    for key, value in config.items():
        if isinstance(value, dict):
            subsection = ConfigSection(value)
            section_name = getattr(config_object, "_section_name", "")
            subsection._section_name = (
                f"{section_name}{'->' if section_name else ''}{key}"
            )
            setattr(config_object, key, subsection)
        else:
            setattr(config_object, key, value)


class ConfigSection:
    """An object representation of a section within a `yaml` config file.

    Each config item can be accessed as an attribute.
    """

    BLOCK_WRITE = False

    def __init__(self, config: dict[str, Any]):
        """Initialises a ConfigSection object.

        Args:
            config (dict[str, Any]): The config section to be represented by this object
        """
        self._section_name = ""

        set_attributes(self, config)

        self.BLOCK_WRITE = True

    def __setattr__(self, name: str, value: Any) -> None:
        """Called when an attribute is attempted to be set.

        Prevents changes to attributes if the `BLOCK_WRITE` flag is set to True.

        Args:
            name (str): The attribute which is being set
            value (Any): The new value of the attribute

        Raises:
            AttributeError: Raised if the `BLOCK_WRITE` flag is set to True
        """
        if not self.BLOCK_WRITE or name == "_section_name":
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"{name} is not writable")

    def __repr__(self) -> str:
        """The string representation of the `ConfigSection` object."""
        return f"{self.__dict__}"

    def __str__(self) -> str:
        """The string representation of the `ConfigSection` object."""
        return self.__repr__()

    def __getattr__(self, name: str) -> None:
        """Called when `self.__getattribute__` raises an error.

        If this is called, we can be pretty sure that the target attribute does not
        exist, and raise our own error.

        Args:
            name (str): The attribute which is being accessed

        Raises:
            AttributeError: Raised if the attribute does not exist
        """
        if not name.startswith("_"):
            raise AttributeError(
                f"The '{name}' key does not exist in the '{self._section_name}' section"  # noqa
            )


@singleton
class Config:
    """An object representation of a `yaml` config file. Each config section can be accessed as an attribute."""

    def __init__(self, config_file: str):
        """Initialises the `Config` object.

        There is only one instance of a `Config` for each `config_file`, as
        it's wrapped by `.decorators.singleton` (to prevent unnecessary processing).

        Args:
            config_file (str): The config file to parse
        """
        self.config_file = config_file

        self.load_config()

    def load_config(self) -> None:
        """Load the config file info this `Config` object.

        Each key is set as an attribute of this `Config`, which contains an instance of a `ConfigSection`.
        """
        with open(self.config_file, "r") as f:
            try:
                config = yaml.safe_load(f)
            except yaml.YAMLError as e:
                logging.error("Error in configuration file!")
                logging.error(e)
                sys.exit(1)

        set_attributes(self, config)

    def __repr__(self) -> str:
        """The string representation of the `Config` object."""
        return f"{self.__dict__}"

    def __str__(self) -> str:
        """The string representation of the `Config` object."""
        return self.__repr__()

    def __getattr__(self, name: str) -> Any:
        """Defined to stop mypy from complaining about the `Config` object not having any attributes.

        Args:
            name (str): The attribute which is being accessed

        Returns:
            Any: A pretend return value to fool mypy
        """
        return
