#!/bin/sh

{% if cookiecutter.generate_git_repo == 'y' -%}
echo "git init"
git init
git add .
git commit -m "initial commit"
echo "init repo at {{ cookiecutter.organisation }}"
{% if cookiecutter.organisation == 'vif' -%}
read -p "gitlab namespace [$USER]: " name
name=${name:-$USER}
git push --set-upstream https://gitlab.v2c2.at/$name/{{ cookiecutter.repo_name }}.git master
git remote add origin https://gitlab.v2c2.at/$name/{{ cookiecutter.repo_name }}.git
{% else %}
echo $PWD
gh repo create {{ cookiecutter.organisation|lower }}/{{ cookiecutter.repo_name }} --description {{ cookiecutter.description }} --source=. --private --push
{% endif %}

{% endif %}

code && code -n . || echo "code command not found"

echo "Done."
echo "Now open a new window of VS Code and open the folder {{ cookiecutter.repo_name }} "
echo "Then click on \"Reopen in Container\""
echo "Then push the git repo to github by going to the left git icon and click publish branch"