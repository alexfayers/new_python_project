Module new_project_name._helpers.config_loader
==============================================

Functions
---------

    
`set_attributes(config_object: object, config: Dict[str, Any]) ‑> None`
:   Set all of the keys within the `config` parameter as attributes of this `ConfigSection`.
    
    Args:
        config_object (object): The class to set the attributes on
        config (dict[str, Any]): A config section dictionary

Classes
-------

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

`ConfigSection(config: dict, section_name: str = '')`
:   An object representation of a section within a `yaml` config file.
    
    Each config item can be accessed as an attribute.
    
    Initialises a ConfigSection object.
    
    Args:
        config (dict[str, Any]): The config section to be represented by this object
        section_name (str, optional): The name of the section (used for debugging). Defaults to ''.

    ### Class variables

    `BLOCK_WRITE`
    :