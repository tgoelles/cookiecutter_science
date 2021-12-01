#!/bin/bash
# Create git repo
# organisation qeustion
# create a repository in an organization
#  $ gh repo create cli/my-project

{% if cookiecutter.generate_git_repo == 'y' -%}
echo "git init"
git init
git add .
git commit -m "initial commit"
echo "init repo at {{ cookiecutter.github_organisation }}"
gh && gh repo create {{ cookiecutter.github_organisation }}/{{ cookiecutter.repo_name }} --description {{ cookiecutter.description }} || echo "github CLI gh not installed"
git push --set-upstream origin master
{% endif %}

cd {{ cookiecutter.repo_name }}

code && code -n . || echo "code command not found"

echo "Done."
echo "Now open a new window of VS Code and open the folder {{ cookiecutter.repo_name }} "
echo "Then click on \"Reopen in Container\""