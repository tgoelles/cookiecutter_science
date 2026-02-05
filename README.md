# Cookiecutter for Science Projects

A cookiecutter template for science and data science projects that include data, code, and dissemination.

- Optimized for data-based publications
- Optimized for use with VS Code
- Docker-based, version-controlled environment using VS Code Dev Containers
- uv based environment inside the Dev Container
- to add a package just follow to uv workflow: use the VS code terminal and to go the code folder and run: uv add pandas
- use of Dev container Features with pre-installed, Python andLaTeX
- Setup for use with Python but could also be addapted for Julia, and R
- Just commands for: collecting data, generating, figures, typsetting latex, clean temp files, clean demo files and more
- use of VS Code tasks to trigger data collection, plotting and paper compilation
- LaTeX-based paper
- tools to clean up bib files and to add a bibtex entry from doi
- Added path definitions in the `project_package` Python module
- [Kedro](https://kedro.org/)-inspired data folder structure
- filled with a demo - which can be cleaned with "make delete_demo"
- used in at least [6 papers](https://www.researchgate.net/profile/Thomas-Goelles)

For more detailed information, please see the [README of the resulting project](./%7B%7B%20cookiecutter.repo_name%20%7D%7D/README.md).

## Quick Start

```bash
cookiecutter https://github.com/tgoelles/cookiecutter_science
```

## File Structure

```
├── Makefile                        	    #  Automation script for common tasks
├── README.md                       	    #  Project overview and instructions
├── code                                   #  Python Source code and notebooks
│   ├── notebooks                          #  Jupyter notebooks for analysis
│   │   └── exploratory                    #  Exploratory data analysis
│   │       └── 1.0-tg-example.ipynb       #  Example exploratory notebook
│   └── project_package                    #  The project package where refined code goes
│       ├── pyproject.toml                 #  project_package dependencies and configuration
│       └── src                            #  Source code directory
│           └── project_package      	    #
│               ├── __init__.py            #
│               ├── data                   #  Data processing module and scripts
│               │   ├── __init__.py        #
│               │   ├── config.py          #  Configuration settings
│               │   ├── example.py         #  Example script
│               │   ├── import_data.py     #  Data import functions
│               │   └── make_dataset.py    #  Dataset creation script, used by make data
│               ├── tools                  #  Utility scripts
│               │   ├── __init__.py        #
│               │   └── convert_latex.py   #  LaTeX conversion script
│               │   └── clean_bib.py       #  Script to clean messy bib files
│               └── visualization          #  Visualization module and scripts
│                   ├── __init__.py        #
│                   ├── make_plots.py      #  Plot generation functions
│                   └── visualize.py       #  Data visualization utilities
├── data                                   #
│   ├── 01_raw                             #  Raw data, do not change the data in there
│   │   └── demo.csv                       #  Example raw data file
│   ├── 02_intermediate                    #  Processed but unrefined data
│   │   └── demo_clean.csv                 #  Example cleaned data file
│   ├── 03_primary                         #  Primary processed datasets
│   ├── 04_feature                         #  Feature-engineered datasets
│   ├── 05_model_input                     #  Data ready for modeling
│   ├── 06_models                          #  Trained models
│   ├── 07_model_output                    #  Model predictions/results
│   └── 08_reporting                       #  Reports and summaries
├── dissemination                          #  Outputs for publication/presentation
│   ├── figures                            #  Figures and plots go in here
│   │   └── demo.png                       #  Example figure
│   ├── papers                             #  LaTeX desimition for paper or Thesis
│   │   ├── paper.pdf                      #  Final paper output
│   │   └── paper.tex                      #  LaTeX source for the paper
│   └── presentations                      #  Presentation slides and materials
├── literature                             #  References and related work
│   └── references.bib                     #  Bibliography file
├── pyproject.toml                         #  All Project dependencie and tool settings, managed by uv
└── uv.lock                                #  Dependency lock file for reproducibility
```

## Tasks

Use of VS Code tasks:

![VS code Tasks](Tasks.png)

## Requirements

- **Git**: Should be part of your OS or install it [here](https://github.com/git-guides/install-git)
- **GitHub account**
- **GitHub CLI**: Install from [here](https://cli.github.com/)
- **Docker Desktop**: Install from [here](https://www.docker.com/products/docker-desktop/)
- **VS Code**: Install from [here](https://code.visualstudio.com/)
- **VS Code Extension: Remote Development**: Install from [here](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
- **Cookiecutter Python package**: Install like this:

```bash
pip install cookiecutter
```

For Mac users:

```bash
brew install cookiecutter
```

## Getting Started

1. Navigate to the folder where you want to create the project (on your local drive):

   ```bash
   cookiecutter https://github.com/tgoelles/cookiecutter_science
   ```

2. Answer the questions prompted by cookiecutter.
3. A new VS Code window will open automatically.
4. Click "OK" to reopen the folder in a container (only asked the first time).
5. Read the README.md in the generated project folder.

## Git and GitHub

Cookiecutter can generate a GitHub repository for you. This initializes the git repo and pushes it to GitHub. You can then invite your team members to join the project.

- Each team member works on their local version of the project, regularly committing and pushing changes.
- Avoid working on the same folder over a network.

### Note for Windows Users

If you want to use git inside the container (recommended), you need to clone the repo from WSL, as Windows may mess up the `.git` folder. Git inside the container uses the same `.gitconfig` as Windows, which is copied into the container.

Ensure `user.email` and `user.name` are set (in PowerShell):

```bash
git config --global user.name "your_name"
git config --global user.email "your_email@gmail.com"
```
