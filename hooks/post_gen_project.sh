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
GITHUB_USERNAME={{ cookiecutter.organisation|lower }}
if [ -f github_username.txt ]; then
    GITHUB_USERNAME=$(cat github_username.txt)
else
    GITHUB_USERNAME={{ cookiecutter.organisation|lower }}
fi
echo "using github organisation: "$GITHUB_USERNAME
echo $PWD
gh repo create $GITHUB_USERNAME/{{ cookiecutter.repo_name }} --description {{ cookiecutter.description }} --source=. --private --push
{% endif %}

{% endif %}

code && code -n . || echo "code command not found"

echo "Done."
echo "Now open a new window of VS Code and open the folder {{ cookiecutter.repo_name }} "
echo "Then click on \"Reopen in Container\""
echo "Then push the git repo to github by going to the left git icon and click publish branch"