# Cookiecutter Vif Science

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
  $ cookiecutter https://gitlab.v2c2.at/thomasgoelles/cookiecutter_vifscience.git
```


## Requirements:

 - Python >= 3.5
 - git
 - docker desktop
 - docker connected to our gitlab registry via (see below)
 - VS Code (optimised for it but should also work with other editors)
 - VS code extension: Remote development (by Microsoft)
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip or by conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```

## gitlab access to the docker registry

On your very first time accessing our gitlab docker registry you need to do the following steps:

1.) generate an access token:
* in gitlab => User settings => Access token
* generate a token with "read_registry" rights
* store the token savely in Keepass (optional)

2.) Login to our registry (only needed once):

``` bash
$ docker login registry-gitlab.v2c2.at -u <vornamenachname> -p <token>
```


## Getting started

* Go to the folder where you want to put the project (your local drive):

  ``` bash
    $ cookiecutter https://gitlab.v2c2.at/thomasgoelles/cookiecutter_vifscience.git
  ```

* Answer the questions
* Open the folder in VS Code (with installed remote development extension and running docker desktop)
* Say OK to reopen the folder in a container (only asked the first time)
* Read the README.md

## git and Gitlab

Cookiecutter asks you if you want to generate a gitlab repo. This initialises the git repo and pushes it to our gitlab server.
Afterwards you can invite your team members to join the project.

Every member works on their local version of the project and regularly commits and pushes their changes.
Do not work on the same folder on the network!

A note for Windows user: if you want to use git inside the container (Recommended) you need to clone the repo from WSL,
otherwise Windows  messes up the .git folder.

Git inside the container uses the same .gitconfig as Windows. (it is copyied inside the container)
So make sure that user.email and user.name are set (in Powershell):

``` bash
git config --global user.name "thomasgoelles"
git config --global user.email "thomas.goelles@v2c2.at"
```

## Developer notes

The docker image is generated at https://gitlab.v2c2.at/thomasgoelles/vifscience in order to make it independet of the cookiecutter project.

You can contribute by writting issues in gitlab or by creating a branch and merge request.

For more infor contact thomas.goelles@v2c2.at