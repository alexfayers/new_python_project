ifeq ($(OS),Windows_NT)
SHELL:=powershell.exe
.SHELLFLAGS:=-Command
endif

ENV_PREFIX:=$(shell python3 -Bc "import pathlib; print('.venv/bin/') if pathlib.Path('.venv/bin/').exists() else print('.venv/Scripts/') if pathlib.Path('.venv/Scripts/').exists() else print('')")
THIS_FILE:=$(lastword $(MAKEFILE_LIST))

.PHONY: install
install:				## Install the project.
	@echo "installing new_project_readable_name ..."
	@$(ENV_PREFIX)pip install -e .[test]

.PHONY: format
format:					## Format the code with isort black
	@echo "formatting new_project_readable_name ..."
	@echo ""
	@echo "running isort ..."
	@$(ENV_PREFIX)isort .

	@echo "running black ..."
	@$(ENV_PREFIX)black .

.PHONY: lint
lint:					## Lint the code to check for potential errors and inconsistencies.
	@echo "linting new_project_readable_name ..."
	@echo ""
	@echo "running flake8 ..."
	@$(ENV_PREFIX)flake8 .
	@echo ""

	@echo "running black ..."
	@$(ENV_PREFIX)black --check .
	@echo ""

	@echo "running mypy ..."
	@$(ENV_PREFIX)mypy .

.PHONY: venv
venv:					## Create a virtual environment.
	@echo "creating virtualenv ..."
	@python3 -Bc "import pathlib, shutil; shutil.rmtree(pathlib.Path('.venv') if pathlib.Path('.venv').exists() else exit())"
	@python3 -m venv .venv
	@$(MAKE) -f $(THIS_FILE) --no-print-directory upgrade-pip
	@$(MAKE) -f $(THIS_FILE) --no-print-directory install
	@$(MAKE) -f $(THIS_FILE) --no-print-directory venv-activate-message

.PHONY: upgrade-pip
upgrade-pip:
	@echo "upgrading pip ..."
	@$(ENV_PREFIX)python3 -m pip install --upgrade pip

.PHONY: venv-activate
venv-activate-message:
	@echo "!!! Activating your new virtualenv using '$(ENV_PREFIX)activate' !!!"

.PHONY: tests
tests: lint		## Run tests for the project.
	@echo "running tests for new_project_readable_name ..."
	$(ENV_PREFIX)pytest -v tests/

.PHONY: clean
clean:					## Clean unused files.
	@echo "cleaning unused files ..."
	@python3 -Bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]"
	@python3 -Bc "import pathlib, shutil; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('__pycache__')]"
	@python3 -Bc "import pathlib, shutil; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('*.egg-info')]"
	@python3 -Bc "import pathlib, shutil; [shutil.rmtree(p) if pathlib.Path(p).exists() else None for p in ['.pytest_cache', '.mypy_cache']]"

.PHONY: docs
docs: lint	         	 ## Build the documentation.
	@echo "building documentation ..."
	@$(ENV_PREFIX)pdoc -o docs ./new_project_name -d google

.PHONY: test
test: lint				## Run tests for the project.
	@echo "running tests for new_project_readable_name ..."
	$(ENV_PREFIX)pytest -v tests/

.PHONY: release-patch
release-patch: update-changelog		## Create a new tag for patch release.
	@echo "Releasing new patch version ..."
	@$(ENV_PREFIX)bump2version patch

.PHONY: release-minor
release-minor: update-changelog		## Create a new tag for minor release.
	@echo "Releasing new minor version ..."
	@$(ENV_PREFIX)bump2version minor

.PHONY: release-major
release-major: update-changelog		## Create a new tag for major release.
	@echo "Releasing new major version ..."
	@$(ENV_PREFIX)bump2version major

.PHONY: update-changelog
update-changelog:       ## Update the changelog.
	@echo "Updating changelog ..."
	@$(ENV_PREFIX)gitchangelog > CHANGELOG.md
	@git add CHANGELOG.md
	@git commit -m "Update changelog"
