#!/bin/bash

if ! command -v gh &> /dev/null
then
    echo "GitHub CLI not installed. Please install it to continue."
    exit 1
fi

{% if cookiecutter.generate_git_repo == 'y' -%}
echo "git init"
git init
git add .
git commit -m "initial commit"

REPO_OWNER=""
if [ "{{ cookiecutter.organisation }}" == "automatic" ]; then
    REPO_OWNER=$(gh api user --jq .login 2>/dev/null)
else
    REPO_OWNER="{{ cookiecutter.organisation | lower }}"
fi

echo "using GitHub repository owner: $REPO_OWNER"

gh repo create $REPO_OWNER/{{ cookiecutter.repo_name }} --description "{{ cookiecutter.description }}" --source=. --private --push

{% endif %}

code && code -n . || echo "code command not found"

echo "VS Code should be open now."
echo "Done!"
