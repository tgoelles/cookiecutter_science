from pathlib import Path
import os

project_folder = Path("/workspaces/{{ cookiecutter.project_name }}")
data_folder = Path.joinpath(project_folder, "data")

delivery_folder = Path.joinpath(project_folder.parent, "delivery")
figure_folder = Path.joinpath(project_folder, "reports").joinpath("figures")
presentations_folder = Path.joinpath(project_folder, "presentations")

raw_data_folder = Path.joinpath(data_folder, "1raw")
interim_data_folder = Path.joinpath(data_folder, "2interim")
processed_data_folder = Path.joinpath(data_folder, "3processed")
external_data_folder = Path.joinpath(data_folder, "0external")
