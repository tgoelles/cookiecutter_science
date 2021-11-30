#!/bin/bash
# Create git repo
# organisation qeustion
# create a repository in an organization
#  $ gh repo create cli/my-project
read -p "Create a github repo? [y/n] " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    git init
    git add .
    git commit -m "initial commit"
    gh repo create {{ cookiecutter.repo_name }} --description {{ cookiecutter.description }}
    git push --set-upstream origin master

fi

echo "Done."
echo "Now open a new window of VS Code and open the folder {{ cookiecutter.repo_name }} "
echo "Then click on \"Reopen in Container\""