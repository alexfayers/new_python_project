# new_project_readable_name

new_project_description

## Installation

The Makefile provides a lot of helpers. Pretty much everything you'll need is shortcutted in there. *(If you're on Windows, you can use [git bash](https://git-scm.com/downloads) or [wsl](https://docs.microsoft.com/en-us/windows/wsl/about) to run the make commands)*

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
$ python3 -m project_name
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