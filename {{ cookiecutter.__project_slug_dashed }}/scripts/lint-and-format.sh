#!/bin/bash -e

# Lint and format the current project

# ensure that a given command is available

function ensure_command {
    if ! command -v "$1" &> /dev/null
    then
        echo "$1 could not be found. Please install it."
        exit 1
    fi
}

ensure_command "ruff"
ensure_command "mypy"

# Lint the project

ruff check --fix
mypy src

# Format the project

ruff format
