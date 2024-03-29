# Alex's New Python Project Template

![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/alexfayers/new_python_project?label=version)
![Lines of code](https://img.shields.io/tokei/lines/github/alexfayers/new_python_project)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/alexfayers/new_python_project/CI.yml?label=tests)
![GitHub last commit](https://img.shields.io/github/last-commit/alexfayers/new_python_project)

This repository allows you to start a new python project faster. It sets up a few things for after you [create a new repository from this template](https://github.com/alexfayers/new_python_project/generate), so that you can get started on your new idea sooner.

## Installation

You can use this repo in a few ways:

- [Create a new repository from this template](https://github.com/alexfayers/new_python_project/generate) (this is the easiest method)
- [Use the helper script](#using-the-helper-script) (this is the method I use)
- [Use cookiecutter](#using-cookiecutter) (nice if you already use cookiecutter)
- [Use cruft](#using-cruft) (Good for keeping your project up to date)

After you've created your new repo, wait for the [rename_templates](.github/workflows/rename_templates.yml) workflow to complete. This will move around a few files, rename some stuff, and reset the project version so that everything's ready for you to get started.

Then you can clone the repo locally, and get started on some coding.

*I recommend using [Visual Studio Code](https://code.visualstudio.com) with my extension pack ([Alex's New Python Project Template - Extensions](https://marketplace.visualstudio.com/items?itemName=alexfayers.alexs-nppt-extensions))*

### Using cookiecutter

You can use [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/) to create a new project from this template. You can use this method like this:

```bash
$ pip install cookiecutter
$ cookiecutter gh:alexfayers/new_python_project
```

### Using the helper script

You can also install this repo as a python module and use that to create a new project. It installs a new script called `anppt` (Alex's New Python Project Template), which just wraps around cookiecutter. This method is useful if you make a lot of projects using this template (like me!). You can use this method like this:

```bash
$ pip install git+https://github.com/alexfayers/new_python_project.git
$ anppt
```

# Using cruft

You can use [cruft](https://cruft.github.io/cruft/) to create a new project from this template, which will mean that you can stay up to date with any changes to the original template. You can use this method like this:

```bash
$ pip install cruft
$ cruft create https://github.com/alexfayers/new_python_project.git
```

And then you can update your project to the latest version of the template with cruft like this:

```bash
$ cruft update
```

Easy!

## Development

The template includes a few of my preferences for writing Python:

- All function parameters and returns values must be typed.
- All functions, classes, and modules must contain docstrings (in the Google format).
- pre-commit hooks are available to enable linting and formatting to be run before you do a commit. You can either install these using `pre-commit install` or just run them once using `tox -e lint`.
- A few cool classes and functions that I use a lot are also included as submodules of your module. In the future I'll make a system to manage these, but for now you can delete them if you don't need them.
- The project is installable as a python module, allowing you to even upload the project to PyPI, if you want.

## Tox

The [tox config](tox.ini) also provides a lot of useful shortcuts. For example:

---

You can run your unit tests using:

```bash
tox
```

---

You can validate and format your code and documentation using:

```bash
tox -e lint
```

---

You can re-generate your docs locally using:

```bash
tox -e docs
```

_(Although, docs are automatically generated and updated if needed as the last step of the [CI workflow](.github/workflows/CI.yml))_

---

You can build the project into `.whl` and `.tar.gz` files using:

```bash
tox -e build
```

---

And you can even create a new release on Github using:

```bash
tox -e release patch  # for a small fix
tox -e release minor  # for a small improvement
tox -e release patch  # for a big change or feature addition
```

_The release command will also automatically update your [changelog](CHANGELOG.md) through the use of [gitchangelog](https://github.com/vaab/gitchangelog)._

---

## Documentation, reiterated

All of the documentation is generated using pdoc. Every function and every class needs a docstring anyway - it's [good practice](https://peps.python.org/pep-0257/#what-is-a-docstring).

CI tests won't pass until all the docstrings are written and formatted correctly. This may be annoying for some people initially, but it's actually really helpful in the long run, because it forces you to document as you go.

## Fetching upstream changes

If you want, you can add this repo as an upstream remote, and then you can pull any updates to the template into your own repo!

```bash
# Add the upstream remote:
git remote add upstream https://github.com/alexfayers/new_python_project
# Make sure we can't push to it:
git remote set-url --push upstream no_push
```

Then when you want to update, you can do something like this:

```bash
# pull from upstream, ignoring the fact that our new repo isn't technically the same repo as the upstream
git pull upstream main --allow-unrelated-histories
# Only accept our changes if there are merge issues - these might happen because of the rename script
git checkout --ours .
# Stage all of the new changes to stop merge issue warnings popping up everywhere
git add .
# commit all of that
git commit -m 'Merge upstream'

# ???
# profit
```
