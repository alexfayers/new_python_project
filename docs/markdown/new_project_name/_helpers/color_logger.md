Module new_project_name._helpers.color_logger
=============================================

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