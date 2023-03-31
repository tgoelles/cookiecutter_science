from pathlib import Path

PROJECT_FOLDER = Path("/workspaces/{{ cookiecutter.project_name }}")
DATA_FOLDER = Path.joinpath(PROJECT_FOLDER, "data")

FIGURE_FOLDER = Path.joinpath(PROJECT_FOLDER, "reports").joinpath("figures")
PRESENTATIONS_FOLDER = Path.joinpath(PROJECT_FOLDER, "presentations")

RAW_DATA_FOLDER = Path.joinpath(DATA_FOLDER, "1raw")
INTERIM_DATA_FOLDER = Path.joinpath(DATA_FOLDER, "2interim")
PROCESSED_DATA_FOLDER = Path.joinpath(DATA_FOLDER, "3processed")
EXTERNAL_DATA_FOLDER = Path.joinpath(DATA_FOLDER, "0external")
