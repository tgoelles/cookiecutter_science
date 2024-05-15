
# Cookiecutter for Science projects

A cookiecutter template for Science and Data Science projects where you have data, code and some form of dessimination.

* for Python but also for Julia and R
* docker based and version controoled environment based on VS code Dev Containers
* reports based on a LaTeX
* optimised with data based publications in mind
* optimised for use with VS Code
* added path definitions in the project_package python
* support for more custom python packages
* kedro data structure

## Quick start:

``` bash
cookiecutter https://github.com/tgoelles/cookiecutter_science
```


## Requirements:

 - git (should be part of your OS or install it: https://github.com/git-guides/install-git)
 - a GitHub account
 - [github cli](https://cli.github.com/)
 - [docker desktop](https://www.docker.com/products/docker-desktop/)
 - [VS Code](https://code.visualstudio.com/)
 - [VS code extension: Remote development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 2.0.0: This can be installed with pip or by conda depending on how you manage your Python packages:

``` bash
pip install cookiecutter
```

or for Mac also:

``` bash
brew install cookiecutter
```

## Getting started

* Go to the folder where you want to put the project (your local drive):

  ``` bash
  cookiecutter https://github.com/tgoelles/cookiecutter_science
  ```

* Answer the questions
* A new VS code window opens automatically
* Say OK to reopen the folder in a container (only asked the first time)
* Read the README.md there

## git and Github

Cookiecutter asks you if you want to generate a Github repo. This initialises the git repo and pushes it to Github.
Afterwards you can invite your team members to join the project.

Every member works on their local version of the project and regularly commits and pushes their changes.
Do not work on the same folder on the network!

A note for Windows user: if you want to use git inside the container (Recommended) you need to clone the repo from WSL,
otherwise Windows  messes up the .git folder.

Git inside the container uses the same .gitconfig as Windows. (it is copied inside the container)
So make sure that user.email and user.name are set (in Powershell):

``` bash
git config --global user.name "test"
git config --global user.email "your_name@gmail.com"
```


## Developer notes

The Docker images are maintained at a separate repo.

https://github.com/tgoelles/Python_docker

https://github.com/tgoelles/LaTex_docker

