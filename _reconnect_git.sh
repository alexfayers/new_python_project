#!/bin/bash

# TODO: Test this further. Can produce duplicate commits in it's current state.

echo "Checking out upstream branch..."

# ensure we're on main
git checkout main &>/dev/null

firstcommit=$(git rev-list HEAD | tail -n1)

if ! git rev-parse --verify upstream &>/dev/null ; then
    echo "Upstream branch does not exist. Creating it."
    git checkout -b upstream upstream/main
else
    echo "Upstream branch exists. Switching to it."
    git checkout upstream
fi

found=0

commoncommit=""
for commit in $(git log --format=format:%H --max-count=100); do
    if [ "$(git diff $firstcommit $commit | wc -l)" = "0" ]; then
        # found the origin commit from when the template was used
        echo "Found common commit: $commit"
        commoncommit=$commit
        break
    fi
done

if [ -z "$commoncommit" ]; then
    echo "Could not find common commit between main and upstream."
    exit 1
fi

git checkout main

# make sure previous filter-branch is removed
git update-ref -d refs/original/refs/heads/main &>/dev/null

git filter-branch --commit-filter "
if [ \$# -eq 1 ]; then
git commit-tree -p $commoncommit \$1;
else
git commit-tree \"\$@\";
fi;" HEAD

# merge

# git pull upstream main

# read -p "Press enter after you've fixed any merge conflicts..." -n1

# # make sure previous filter-branch is removed
# git update-ref -d refs/original/refs/heads/main &>/dev/null

# git filter-branch --commit-filter "
# if git merge-base --is-ancestor $commoncommit \$GIT_COMMIT; then
# git commit-tree \"\$@\";
# else
# skip_commit \"\$@\";
# fi;" HEAD
