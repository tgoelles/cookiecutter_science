# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}


## File Structure

```
├── .devcontainer                      # Definition of the Docker container and environment for VS Code
│   ├── Dockerfile                     # Defines the Docker container
│   ├── devcontainer.json              # Defines the devcontainer settings for VS Code
│   └── noop.txt                       # Placeholder file to ensure the COPY instruction does not fail if no environment.yml exists
├── .gitattributes                     # Git attributes for handling line endings and merge strategies
├── .gitignore                         # Git ignore file to exclude files and directories from version control
├── Makefile                           # Makefile with commands like `make data` and `make clean`
├── README.md                          # Project readme
├── code                               # Source code and notebooks
│   ├── notebooks                      # Jupyter notebooks
│   │   └── exploratory                # Data explorations
│   │       └── 1.0-tg-example.ipynb   # Jupyter notebook with naming conventions. tg are initials
│   ├── project_package                # Project-specific Python package
│   │   ├── __init__.py                # Makes project_package a Python module
│   │   ├── data                       # Scripts to download, generate and parse data
│   │   │   ├── __init__.py
│   │   │   ├── config.py              # Project-wide path definitions
│   │   │   ├── example.py             # Example script
│   │   │   ├── import_data.py         # Functions to read raw data
│   │   │   └── make_dataset.py        # Scripts to download or generate data (used in the Makefile)
│   │   ├── tools                      # Scripts and functions for general use
│   │   │   ├── __init__.py
│   │   │   └── convert_latex.py       # Functions to convert elements for use in LaTeX
│   │   └── visualization              # Scripts and functions to create visualizations
│   │       ├── __init__.py
│   │       ├── make_plots.py          # Scripts to make all plots for the publication
│   │       └── visualize.py           # Functions to produce final plots
│   └── pyproject.toml                 # Configuration file for the project
├── data                               # Data directories
│   ├── 01_raw                         # The original, immutable data dump
│   │   └── demo.csv                   # Example raw data file
│   ├── 02_intermediate                # Intermediate processed data
│   ├── 03_primary                     # cleaned data, used for the dissemination
│   ├── 04_feature                     # For Machine learning, features based on the primary data
│   ├── 05_model_input                 # The final data used for machine learning
│   ├── 06_models                      # Stored, serialized pre-trained machine learning models
│   ├── 07_model_output                # Output from trained machine learning models
│   └── 08_reporting                   # Reporting data like log files
├── dissemination                      # Materials for dissemination
│   ├── figures                        # Figures for paper generated with Python
│   │   └── demo.png                   # Example figure file
│   ├── presentations                  # All related PowerPoint files, especially for deliverables
│   └── papers                         # LaTeX-based papers
│       └── paper.tex                  # Example LaTeX paper
├── environment.yml                    # Conda environment configuration file
└── literature                         # References and explanatory materials
    └── references.bib                 # Bibliography file for LaTeX documents
```

## Important

- **Raw data is immutable**: Do not change the data in `data/01_raw`.
- **Reusable functions**: Develop reusable functions in Jupyter notebooks and then put them in the `project_package` with docstrings and type hints.
- **VS Code settings**: Some settings are already defined in `devcontainer.json`.
- **Default shell**: The default shell inside the container is zsh with the p10k theme.

## Project-Specific Packages and Settings

You can customize the development environment in multiple ways:
- **Add Python packages**: Modify the `environment.yml` file to include additional Python packages.
- **Add Dev Container features**: Use the VS Code command `Dev Container: Configure Container Features` to add features like R, Julia, and more.
- **Modify Dockerfile**: Update the Dockerfile in `.devcontainer` to add additional software not available as Dev Container features.
- **Install LaTeX packages**: Add LaTeX packages using the `postCreateCommand` in `devcontainer.json`.

## Working with Jupyter Notebooks

Use Jupyter notebooks directly in VS Code. It supports many useful functionalities.

## Working with LaTeX

An example LaTeX file is provided in `dissemination/papers`. The LaTeX extension is also pre-installed. To compile the LaTeX file:
- Open the file.
- Use the TeX symbol on the side panel.
- Select `Build LaTeX project` and use the recipe: `pdflatex -> biber -> pdflatex*2`.

Export figures to `dissemination/figures`. The path is already defined in `project_package.data.config`:

```python
from project_package.data import config

filename = config.FIGURES_FOLDER.joinpath("example.png")
```

Use functions in `project_package/tools/` to convert output like CSV, PDF, PNG for LaTeX use.

To redo all plots for the publication, run:

```sh
make plots
```

This command runs `src/visualization/make_plots.py`. Add all your final plot functions there to regenerate all plots for the publication with one command, saving time during the publication process.

## Data Handling

- **Small datasets**: Save small datasets like CSV files directly in `data/01_raw` and commit them to the repo.
- **Collect data from external sources**: Write functions to collect data from servers or databases in `code/project_package/data/make_dataset.py`.

To run the data collection function, execute:

```sh
make data
```

Or mount a data folder to the container by adding the following line to `devcontainer.json`:

```json
"mounts": ["source=WHEREVER_YOUR_DATA_IS,target=/workspace/data/01_raw/,type=bind,consistency=cached"]
```

Replace `WHEREVER_YOUR_DATA_IS` with the path to the data on the host machine, such as `/home/user/data`, which will be mapped to `data/01_raw` in the container.

## Running Tasks in VS Code

This project integrates several tasks using the Makefile. You can run these tasks directly from VS Code using the Tasks: Run Task command from the Command Palette (Ctrl+Shift+P).

Available Tasks

	•	Make Data: Generates the dataset by running the data creation scripts.
	•	Make Plots: Creates all plots for the publication.
	•	Make Paper: Compiles the LaTeX paper.
	•	Make Clean: Deletes all temporary compiled Python and LaTeX files.
	•	Make delete_demo: Deletes all demo files.

To run a task:

	1.	Open the Command Palette (Ctrl+Shift+P).
	2.	Select Tasks: Run Task.
	3.	Choose the desired task from the list.

These tasks are configured in the .vscode/tasks.json file.

## More Info

Made with the template from ttps://github.com/tgoelles/cookiecutter_science
template version: 2.1.0

Contact: thomas.goelles@gmail.com
