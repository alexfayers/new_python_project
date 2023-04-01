# new_project_readable_name

![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/new_project_author/new_project_name?label=version)
![Lines of code](https://img.shields.io/tokei/lines/github/new_project_author/new_project_name)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/new_project_author/new_project_name/CI.yml?label=tests)
![GitHub last commit](https://img.shields.io/github/last-commit/new_project_author/new_project_name)

new_project_description

- [new_project_readable_name](#new_project_readable_name)
  - [Features](#Features)
  - [Installation](#Installation)
    - [pip](#pip)
    - [pipx](#pipx)
  - [Usage](#usage)
  - [Documentation](#Documentation)
  - [Contributing](#Contributing)

## Features

- [x] Installable via pip
- [x] Command-line interface
- [x] Interactive documentation
- [ ] Some new planned feature

## Installation

### pip

```bash
$ pip install git+https://github.com/new_project_author/new_project_name
```

### [pipx](https://pypa.github.io/pipx/)

```bash
$ pipx install git+https://github.com/new_project_author/new_project_name
```

## Usage

You can use new_project_readable_name as an importable module:

```py
from new_project_name import BaseClass

app = BaseClass("config.toml")

# cool stuff here...
```

Or as a command line interface:

```bash
$ python3 -m new_project_readable_name
# or
$ new_project_readable_name
```

## Documentation

Interactive documentation for new_project_readable_name can be found within the [docs](./docs/index.html) folder.

## Contributing

If you want to contribute to new_project_readable_name, you'll need [poetry](https://python-poetry.org/) and [tox](https://tox.wiki/en/latest/).

Then you can clone the repository and install the development dependencies like so:

```bash
$ git clone https://github.com/new_project_author/new_project_name
$ cd new_project_name
$ poetry install --with dev
```

Run tests like this:

```bash
$ tox
```

And lint and format your code like this:

```bash
$ tox -e lint
```
