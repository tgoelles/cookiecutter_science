# Changelog

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