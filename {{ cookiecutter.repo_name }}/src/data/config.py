from pathlib import Path

PROJECT_FOLDER = Path("/workspaces/{{ cookiecutter.project_name }}")
DATA_FOLDER = Path.joinpath(PROJECT_FOLDER, "data")

FIGURE_FOLDER = Path.joinpath(PROJECT_FOLDER, "reports").joinpath("figures")
PRESENTATIONS_FOLDER = Path.joinpath(PROJECT_FOLDER, "presentations")

RAW_DATA_FOLDER = Path.joinpath(DATA_FOLDER, "01_raw")
INTERMEDIATE_DATA_FOLDER = Path.joinpath(DATA_FOLDER, "02_intermediate")
PROCESSED_DATA_FOLDER = Path.joinpath(DATA_FOLDER, "03_primary")
FEATURE_DATA_FOLDER = Path.joinpath(DATA_FOLDER, "04_feature")
MODEL_INPUT_DATA_FOLDER = Path.joinpath(DATA_FOLDER, "05_model_input")
MODELS_DATA_FOLDER = Path.joinpath(DATA_FOLDER, "06_models")
MODEL_OUTPUT_DATA_FOLDER = Path.joinpath(DATA_FOLDER, "07_model_output")
REPORTING_DATA_FOLDER = Path.joinpath(DATA_FOLDER, "08_reporting")