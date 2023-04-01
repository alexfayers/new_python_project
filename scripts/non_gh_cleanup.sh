#!/bin/bash

# Cleanup for non-GitHub repositories
# Just removes the .github directory for now. (And then commits the changes.)

rm -rf .github
git add .
git commit -m "Remove .github directory"
