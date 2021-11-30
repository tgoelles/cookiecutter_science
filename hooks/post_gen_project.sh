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
{%- if cookiecutter.github_organisation == "1" -%}
echo "init personal repo"
gh repo create {{ cookiecutter.repo_name }} --description {{ cookiecutter.description }}
{% else %}
echo "init organisation repo"
gh repo create {{ cookiecutter.github_organisation }}/{{ cookiecutter.repo_name }} --description {{ cookiecutter.description }}
{% endif %}
git push --set-upstream origin master
{% endif %}


echo "Done."
echo "Now open a new window of VS Code and open the folder {{ cookiecutter.repo_name }} "
echo "Then click on \"Reopen in Container\""