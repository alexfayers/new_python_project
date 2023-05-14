#!/bin/bash

# Ensure the poetry lock file is up to date
echo "[-] Making sure lock file is up to date..."

poetry lock
# git add poetry.lock
# git commit -m "Update poetry.lock"

# Export the base project requirements poetry into requirements.txt format.
echo "[-] Exporting main requirements..."
poetry export --format=requirements.txt \
    --only="main" \
    --without-hashes \
    --output="requirements.txt"

# Define the extra group dependencies
declare -a arr=("dev" "lint" "test" "docs" "release")

for group in "${arr[@]}"
do
    echo "[-] Exporting $group requirements..."
    poetry export --format=requirements.txt \
        --without-hashes \
        --only="$group" \
        --output="requirements-$group.txt"
done

echo "[+] All requirements exported."

# git add "requirements*.txt"
# git commit -m "Update requirements files"
