# Changelog

## 3.120 - (2026-02-04)

### Changed
- using newer Docker image with debian trixie see https://github.com/tgoelles/LaTex_docker
- this image comes also with some nice tools
- added BIB_INTERPRETER to the make file to use biber or bibtex depending ton the journals needs


## 3.1.0 - (2025-03-20)

### Changed
- a pyproject.toml at the root of the project. All dependecies and python version go there
- changed the pyproject.toml of the project_package to only have its dependencies
- uses uv build backend

## 3.0.0 - (2025-03-19)



- switched back to custom containers as installation of additional latex packages was very slow and happening each time
- use the latex container as the base image, which includes texlive full installation
- add uv based Python environment. So deleted environment.yml and use only the pyproject.toml from now on.
- updated Readme accordingly

## 2.1.0 - (2024-05-28)

### Added
- changelog
- ignore data folder in git

### Changed
- renamed latex report to paper

## 2.0.0 - 2024-05-10
### Changed
- Latex is pre-installed and setup – no more confusion with two VS code windows and docker containers.
- Switched from custom docker containers to the official Dev container features. This makes it much more flexible and up-to-date. Now it's  easy to use R, Julia, and a lot of other tools. The complete list is here: [https://containers.dev/features](https://containers.dev/features).
- Easier to add project-specific Python packages. Just add them to `environment.yml` and rebuild the Dev container.
- Simplified folder structure focused on science: `data`, `code`, `dissemination`, and `literature`.
- Data folder structure follows Kedro conventions.
- Improved Makefile: for example, run `make paper` to compile the paper, generate figures, and compile Latex.
- Integrated VS code tasks to run the Makefile if you prefer using the GUI.
- Better templates and README.