"""The main functionality of `new_project_name`."""

import logging

from ._helpers.config_loader import Config


class BaseClass:
    """Everything in the project comes back to here."""

    def __init__(self, config_file: str):
        """Initialises the base class for `new_project_name` by loading the config and setting up a logger.

        Args:
            config_file (str): Path to a config file containing settings for the class.
        """
        self.logger = logging.getLogger(__name__)
        self.config = Config(config_file)

        if self.config.DEBUG.ENABLED:
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)
