Module new_project_name
=======================
# new_project_name

new_project_description

## Installation

The Makefile provides a lot of helpers. Pretty much everything you'll need is shortcutted in there. *(If you're on Windows, you can install make from [here](http://gnuwin32.sourceforge.net/packages/make.htm))*

To install the project you only need to run:

```bash
make install
```

If you like using virtual environments, you can easily install the project within one using:

```bash
make venv
```

## Usage

```py
from project_name import BaseClass

app = BaseClass("config.yml")

app.logger.info(
    f"Hi, welcome to {app.config.INFO.NAME} by {app.config.INFO.AUTHOR}!"
)
```

```bash
$ python -m project_name
# or
$ project_name
```

---

## Development 

### Changes

If you want to make any changes, these commands are useful:

```bash
make format
make lint
```

And this one is nice for removing the trash cache files:

```bash
make clean
```

### Testing

To run linting and unit tests, just run the make command:

```bash
make tests
```

### Documentation

All of the documentation is generated using pdoc. Every function and every class needs a docstring anyway - it's good practice.

The docs won't be generated until all of the documentation is there!

```bash
make docs
```

Sub-modules
-----------
* new_project_name._helpers
* new_project_name._validation
* new_project_name.base
* new_project_name.cli

Functions
---------

    
`cli_main() ‑> None`
:   CLI entrypoint for `new_project_name`. Uses `BaseClass`.

Classes
-------

`BaseClass(config_file: str)`
:   Everything in the project comes back to here.
    
    Initialises the base class for `new_project_name` by loading the config and setting up a logger.
    
    Args:
        config_file (str): Path to a config file containing settings for the class.