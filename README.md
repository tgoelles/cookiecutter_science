# Cookiecutter for Science Projects

A cookiecutter template for science and data science projects that include data, code, and dissemination.

- Supports Python, Julia, and R
- Docker-based, version-controlled environment using VS Code Dev Containers
- LaTeX-based paper
- Optimized for data-based publications
- Optimized for use with VS Code
- Added path definitions in the `project_package` Python module
- Supports custom Python packages
- Kedro-inspired data structure

## Quick Start

```bash
cookiecutter https://github.com/tgoelles/cookiecutter_science
```

## Requirements

- **Git**: Should be part of your OS or install it [here](https://github.com/git-guides/install-git)
- **GitHub account**
- **GitHub CLI**: Install from [here](https://cli.github.com/)
- **Docker Desktop**: Install from [here](https://www.docker.com/products/docker-desktop/)
- **VS Code**: Install from [here](https://code.visualstudio.com/)
- **VS Code Extension: Remote Development**: Install from [here](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
- **Cookiecutter Python package**: Install with pip or conda

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

## Developer Notes

The Docker images are maintained in separate repositories:

- [Python Docker Image](https://github.com/tgoelles/Python_docker)
- [LaTeX Docker Image](https://github.com/tgoelles/LaTex_docker)