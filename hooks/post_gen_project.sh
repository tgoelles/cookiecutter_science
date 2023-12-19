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

{% if cookiecutter.organisation == 'automatic' -%}
GITHUB_USERNAME=$(gh api user --jq .login 2>/dev/null)
{% else %}
GITHUB_USERNAME={{ cookiecutter.organisation | lower}}
{% endif %}
echo "using github organisation: "$GITHUB_USERNAME

gh repo create $GITHUB_USERNAME/{{ cookiecutter.repo_name }} --description {{ cookiecutter.description }} --source=. --private --push

{% endif %}

code && code -n . || echo "code command not found"

echo "VS Code should be open now."
echo "Done!"
