# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}


## File Structure

```
├── Makefile                        	   #  Automation script for common tasks
├── README.md                       	   #  Project overview and instructions
├── code                                   #  Python Source code and notebooks
│   ├── notebooks                          #  Jupyter notebooks for analysis
│   │   └── exploratory                    #  Exploratory data analysis
│   │       └── 1.0-tg-example.ipynb       #  Example exploratory notebook
│   └── project_package                    #  The project package where refined code goes
│       ├── pyproject.toml                 #  project_package dependencies and configuration
│       └── src                            #  Source code directory
│           └── project_package      	   #
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
├── pyproject.toml                         #  All Project dependencies and tool settings, managed by uv
└── uv.lock                                #  Dependency lock file for reproducibility
```

## Important

- **The image contains texlive full** and uv to hand Python
- **Raw data is immutable**: Do not change the data in `data/01_raw`.
- **Reusable functions**: Develop reusable functions in Jupyter notebooks and then put them in the `project_package` with docstrings and type hints.
- **VS Code settings**: Some settings are already defined in `devcontainer.json`.
- **Default shell**: The default shell inside the container is bash.

## Project-Specific Packages and Settings

You can customize the development environment in multiple ways:

- **Add Python packages**: Modify the `pyproject.toml`  (in the root folder of the projecT) file to include additional Python packages or simply use $ uv add PACKAGENAME
- **Modify Dockerfile**: Update the Dockerfile in `.devcontainer` to add additional Linux software or Latex Packages.

## Working with Jupyter Notebooks

Use Jupyter notebooks directly in VS Code. It supports many useful functionalities. Use the .venv Kernel.

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
template version: 3.1.0

Contact: thomas.goelles@gmail.com
