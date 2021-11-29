#!/bin/bash
# Create git repo
read -p "Create a github repo? [y/n] " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    read -p "github namespace [$USER]: " name
    name=${name:-$USER}
    git init
    git add .
    git commit -m "initial commit"
    git push --set-upstream https://github.com/{{ cookiecutter.repo_name }}.git master
    git remote add origin https://github.com/{{ cookiecutter.repo_name }}.git
fi

echo "Done."
echo "Now open a new window of VS Code and open the folder {{ cookiecutter.repo_name }} "
echo "Then click on \"Reopen in Container\""