# new_project_readable_name

new_project_description

## Installation

To install the project you only need to clone the repo and run pip install:

```bash
git clone https://github.com/new_project_author/new_project_name
cd new_project_name
pip install .
```

If you like using virtual environments, you can easily install the project within one using [pipx](https://pypa.github.io/pipx/):

```bash
pipx install .
```

## Usage

You can use new_project_readable_name as an importable module:

```py
from project_name import BaseClass

app = BaseClass("config.yml")

app.logger.info(
    f"Hi, welcome to {app.config.INFO.NAME} by {app.config.INFO.AUTHOR}!"
)
```

Or as a command line interface:

```bash
$ python3 -m project_name
# or
$ project_name
```

## Documentation

Documentation for new_project_readable_name can be found at [https://new_project_author.github.io/new_project_name](https://new_project_author.github.io/new_project_name).
