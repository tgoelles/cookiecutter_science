from pathlib import Path

PROJECT_FOLDER = Path("/workspace")

DATA_FOLDER = Path.joinpath(PROJECT_FOLDER, "data")
DISSEMINATION_FOLDER = Path.joinpath(PROJECT_FOLDER, "dissemination")


FIGURES_FOLDER = Path.joinpath(DISSEMINATION_FOLDER, "figures")
PRESENTATIONS_FOLDER = Path.joinpath(DISSEMINATION_FOLDER, "presentations")
REPORTS_FOLDER = Path.joinpath(DISSEMINATION_FOLDER, "reports")

RAW_DATA_FOLDER = Path.joinpath(DATA_FOLDER, "01_raw")
INTERMEDIATE_DATA_FOLDER = Path.joinpath(DATA_FOLDER, "02_intermediate")
PROCESSED_DATA_FOLDER = Path.joinpath(DATA_FOLDER, "03_primary")
FEATURE_DATA_FOLDER = Path.joinpath(DATA_FOLDER, "04_feature")
MODEL_INPUT_DATA_FOLDER = Path.joinpath(DATA_FOLDER, "05_model_input")
MODELS_DATA_FOLDER = Path.joinpath(DATA_FOLDER, "06_models")
MODEL_OUTPUT_DATA_FOLDER = Path.joinpath(DATA_FOLDER, "07_model_output")
REPORTING_DATA_FOLDER = Path.joinpath(DATA_FOLDER, "08_reporting")
