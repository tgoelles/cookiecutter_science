#!/bin/bash

# Try to get the GitHub username using GitHub CLI
GITHUB_USERNAME=$(gh api user --jq .login 2>/dev/null)

# Fallback in case of an error or if gh is not installed/authenticated
if [ -z "$GITHUB_USERNAME" ]; then
    GITHUB_USERNAME="default_username"
fi

# Write the username to a temporary file
echo $GITHUB_USERNAME > github_username.txt
