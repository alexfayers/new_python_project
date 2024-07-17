# {{ cookiecutter.project_name }}

![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/{{ cookiecutter.github_username }}/{{ cookiecutter.__project_slug}}?label=version)
![Lines of code](https://img.shields.io/tokei/lines/github/{{ cookiecutter.github_username }}/{{ cookiecutter.__project_slug}})
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.github_username }}/{{ cookiecutter.__project_slug}}/CI.yml?label=tests)
![GitHub last commit](https://img.shields.io/github/last-commit/{{ cookiecutter.github_username }}/{{ cookiecutter.__project_slug}})

{{ cookiecutter.project_short_description }}

- [{{ cookiecutter.project_name }}](#{{ cookiecutter.project_name }})
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
$ pip install git+https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.__project_slug}}
```

### [pipx](https://pypa.github.io/pipx/)

```bash
$ pipx install git+https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.__project_slug}}
```

## Usage

You can use {{ cookiecutter.project_name }} as an importable module:

```py
from {{ cookiecutter.__project_slug}} import {{ cookiecutter.__project_class_name }}

app = {{ cookiecutter.__project_class_name }}("config.toml")

# cool stuff here...
```

Or as a command line interface:

```bash
$ python3 -m {{ cookiecutter.__project_slug_dashed}}
# or
$ {{ cookiecutter.__project_slug_dashed}}
```

## Documentation

Interactive documentation for {{ cookiecutter.project_name }} can be found within the [docs](./docs/index.html) folder.

## Contributing

If you want to contribute to {{ cookiecutter.project_name }}, you'll need [poetry](https://python-poetry.org/) and [tox](https://tox.wiki/en/latest/).

Then you can clone the repository and install the development dependencies like so:

```bash
$ git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.__project_slug}}
$ cd {{ cookiecutter.__project_slug}}
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
