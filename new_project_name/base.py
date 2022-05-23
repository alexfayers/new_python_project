"""The main functionality of `new_project_name`."""

import logging

from ._helpers.color_logger import ColoredLogger
from ._helpers.config_loader import Config

logging.setLoggerClass(ColoredLogger)


class BaseClass:
    """Everything in the project comes back to here."""

    def __init__(self, config_file: str):
        """Initialises the base class for `new_project_name` by loading the config and setting up a logger.

        Args:
            config_file (str): Path to a config file containing settings for the class.
        """
        self.logger = self._setup_logging()
        self.config = Config(config_file)

    def _setup_logging(self) -> logging.Logger:
        logging.setLoggerClass(ColoredLogger)
        return logging.getLogger(__name__)
