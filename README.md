
# Cookiecutter for Science projects

_A logical, reasonably standardized, but flexible project structure for doing and sharing Python data science work._
Based on [cookiecutter-data-science](http://drivendata.github.io/cookiecutter-data-science/) and enhanced by:

* docker based python environment
* reports based on a LaTeX docker container
* deleted some useless clutter
* optimised with data based publications in mind
* optimised for use with VS Code
* added path definitions in the src python package
* support for more custom python packages

## Quick start:

``` bash
  $ cookiecutter https://github.com/tgoelles/cookiecutter_science
```


## Requirements:

 - git
 - github cli
 - docker desktop
 - VS Code (optimised for it but should also work with other editors)
 - VS code extension: Remote development (by Microsoft)
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip or by conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or for Mac also:

``` bash
$ brew install cookiecutter
```

## Getting started

* Go to the folder where you want to put the project (your local drive):

  ``` bash
    $ cookiecutter https://github.com/tgoelles/cookiecutter_science
  ```

* Answer the questions
* Open the folder in VS Code (with installed remote development extension and running docker desktop)
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

The Docker image is maintained at a separate repo.
https://github.com/tgoelles/Python_docker


