#!/bin/bash

# Ensure the poetry lock file is up to date
echo "[-] Making sure lock file is up to date..."

poetry lock
git add poetry.lock
git commit -m "Update poetry.lock"

# Export the base project requirements poetry into requirements.txt format.
echo "[-] Exporting main requirements..."
poetry export --format=requirements.txt \
    --only="main" \
    --without-hashes \
    --output="requirements.txt"

# Export development requirements
echo "[-] Exporting development requirements..."

poetry export --format=requirements.txt \
    --without-hashes \
    --only="dev,types" \
    --output="requirements-dev.txt"

# Export linting requirements
echo "[-] Exporting linting requirements..."

poetry export --format=requirements.txt \
    --without-hashes \
    --only="lint,types" \
    --output="requirements-lint.txt"

# Define the extra group dependencies
declare -a arr=("test" "docs" "release")

for group in "${arr[@]}"
do
    echo "[-] Exporting $group requirements..."
    poetry export --format=requirements.txt \
        --without-hashes \
        --only="$group" \
        --output="requirements-$group.txt"
done

echo "[+] All requirements exported."

git add "requirements*.txt"
git commit -m "Update requirements files"
