# .ONESHELL:
ENV_PREFIX=$(shell python -c "print('.venv/bin/') if __import__('pathlib').Path('.venv/bin/pip').exists() else print('.venv/Scripts/') if __import__('pathlib').Path('.venv/Scripts/pip.exe').exists() else print('')")

.PHONY: install
install:				## Install the project.
	@echo "installing new_project_name ..."
	"$(ENV_PREFIX)pip" install -e .[test]

.PHONY: format
format:					## Format the code with isort black
	@echo "formatting new_project_name ..."
	"$(ENV_PREFIX)isort" new_project_name/
	"$(ENV_PREFIX)black" new_project_name/

.PHONY: lint
lint:					## Lint the code to check for potential errors and inconsistencies.
	@echo "linting new_project_name ..."
	"$(ENV_PREFIX)flake8" new_project_name/
	"$(ENV_PREFIX)black" --check new_project_name/
	"$(ENV_PREFIX)mypy" new_project_name/

.PHONY: venv
venv:					## Create a virtual environment.
	@echo "creating virtualenv ..."
	@python -Bc "import pathlib, shutil; shutil.rmtree(pathlib.Path('.venv') if pathlib.Path('.venv').exists() else exit())"
	@python -m venv .venv
	"$(shell python -c "print('.venv/bin/') if __import__('pathlib').Path('.venv/bin/pip').exists() else print('.venv/Scripts/') if __import__('pathlib').Path('.venv/Scripts/pip.exe').exists() else print('')")pip" install pip
	"$(shell python -c "print('.venv/bin/') if __import__('pathlib').Path('.venv/bin/pip').exists() else print('.venv/Scripts/') if __import__('pathlib').Path('.venv/Scripts/pip.exe').exists() else print('')")pip" install -e .[test]
	@echo "!!! Remember to activate the environment using '$(shell python -c "print('.venv/bin/') if __import__('pathlib').Path('.venv/bin/pip').exists() else print('.venv/Scripts/') if __import__('pathlib').Path('.venv/Scripts/pip.exe').exists() else print('')")activate' !!!"

.PHONY: tests
tests: lint		## Run tests for the project.
	@echo "running tests for new_project_name ..."
	"$(ENV_PREFIX)pytest" -v tests/

.PHONY: clean
clean:					## Clean unused files.
	@echo "cleaning unused files ..."
	@python -Bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]"
	@python -Bc "import pathlib, shutil; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('__pycache__')]"
	@python -Bc "import pathlib, shutil; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('*.egg-info')]"
	@python -Bc "import pathlib, shutil; [shutil.rmtree(p) if pathlib.Path(p).exists() else None for p in ['.pytest_cache', '.mypy_cache']]"

.PHONY: docs
docs: lint	         	 ## Build the documentation.
	@echo "building documentation ..."
	"$(ENV_PREFIX)pdoc" -o docs ./new_project_name --html --force
