Module new_project_name._helpers
================================
Helper functions and classes to make life easier. Mainly for internal use within the package.

Sub-modules
-----------
* new_project_name._helpers.color_logger
* new_project_name._helpers.config_loader
* new_project_name._helpers.decorators

Classes
-------

`ColoredFormatter(*args: Any, **kwargs: Any)`
:   A logging formatter which enables ANSI colors for each log level.
    
    Initialises a `ColoredFormatter` object.

    ### Ancestors (in MRO)

    * logging.Formatter

    ### Methods

    `format(self, record: logging.LogRecord) ‑> str`
    :   Formats the `record`, ensuring coloured output.
        
        Args:
            record (logging.LogRecord): The log record to format
        
        Returns:
            str: The formatted log record

`ColoredLogger(name: str)`
:   A logger which uses the `ColoredFormatter` to provide coloured output.
    
    Initialises a `ColoredLogger`.
    
    Args:
        name (str): The name of the logger

    ### Ancestors (in MRO)

    * logging.Logger
    * logging.Filterer

    ### Class variables

    `CONSOLE_FORMAT`
    :

    ### Methods

    `success(self, msg: str, *args: Any, **kwargs: Any) ‑> None`
    :   Enables the "success" log type for all loggers using `ColoredLogger`.
        
        Args:
            msg (str): The message to log

`Config(config_file: str)`
:   An object representation of a `yaml` config file. Each config section can be accessed as an attribute.
    
    Initialises the `Config` object.
    
    There is only one instance of a `Config` for each `config_file`, as
    it's wrapped by `.decorators.singleton` (to prevent unnecessary processing).
    
    Args:
        config_file (str): The config file to parse

    ### Methods

    `load_config(self) ‑> None`
    :   Load the config file info this `Config` object.
        
        Each key is set as an attribute of this `Config`, which contains an instance of a `ConfigSection`.