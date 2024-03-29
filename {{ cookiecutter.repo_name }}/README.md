# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}


## File Structure


```
    |-- .devcontainer                       <- definition of the docker container and environment for VS Code.
    |   |-- Dockerfile                      <- Defines the docker container.
    |   |-- devcontainer.json               <- Defines the devcontainer settings for VS Code.
    |-- install_dependecies.sh              <- To handle custom python packages
    |-- Makefile                            <- Makefile with commands like `make data`
    |-- README.md                           <- This readme
    |-- data
    |   |-- 01_raw                          <- The original, immutable data dump.
    |   |-- 02_intermediate                 <- Optional data model(s), which are introduced to type your raw data model(s)
    |   |-- 03_primary                      <- Domain specific data model(s) containing cleansed
    |   |-- 04_feature                      <- Analytics specific data model(s) containing a set of features defined against the primary data
    |   |-- 05_model_input                  <- Analytics specific data model(s) containing all feature data against a common dimension
    |   |-- 06_models                       <- Stored, serialised pre-trained machine learning models
    |   |-- 07_models                       <- Stored, serialised pre-trained machine learning models
    |   `-- 08_reporting                    <- Reporting data model(s) that are used to combine a set of primary, feature, model input and model output data
    |-- notebooks                           <- Jupyter notebooks.
    |   `-- exploratory                     <- Data explorations
    |       `-- 1.0-tg-example.ipynb        <- Jupyter notebook with naming conventions. tg are initials
    |-- presentations                       <- All related powerpoint files, especially for Deliverables.
    |-- references                          <- Data dictionaries, manuals, papers and all other explanatory materials.
    |-- reports                             <- Latex based reports
    |   |-- .devcontainer                   <- Latex docker container
    |   `-- figures                         <- Figures for reports generated with python.
    |-- setup.py                            <- Setup file of the src package.
    `-- src                                 <- Source code for use in this project.
        |-- __init__.py                     <- Makes src a Python module.
        |-- data                            <- Scripts to download, generate and parse data
        |   |-- __init__.py
        |   |-- config.py                   <- Project wide path definitions.
        |   |-- example.py                  <- Just an example on how the add your own source files.
        |   |-- import_data.py              <- Functions to read raw data.
        |   `-- make_dataset.py             <- Scripts to download or generate data (used in the Makefile)
        |-- features                        <- Scripts and functions to turn raw data into features for modelling.
        |-- models                          <- Scripts and functions to train models and then use trained models.
        |   |-- __init__.py
        |   |-- predict_model.py
        |   `-- train_model.py
        |-- tools                           <- Scripts and Functions for general use, like converters.
        |   |-- __init__.py
        |   |-- convert_latex.py            <- Functions to convert elements for use in latex
        |   |-- convert_pictures.py         <- Functions to convert pictures
        |   |-- convert_pptx.py             <- Functions and scripts to convert powerpoint files
        `-- visualization                   <- Scripts and functions to create visualizations.
            |-- __init__.py
            |-- make_plots.py               <- Scripts to make all plots for the publication.
            `-- visualize.py                <- Functions to produce final plots.

```

## Important

* Optimised for VS code. It should also work with other editors which would require some additional steps.
* Raw data is immutable (do not change it!)
* Develop reusable functions in jupyter notebooks and then put them in the _src_ package (with docstring and typehints)
* Open reports folder separate in a VS code window (own .devcontainer with LaTeX)
* Some VS Code settings are already defined in devcontainer.json
* the default shell inside the container is zsh with p10k theme.

## Project specific packages and settings

Change Dockerfile and environment.yml in the .devcontainer folder if you want to install additional python packages.

If you want to include custom not on pypi or github packages you might use install_dependencies.sh

## Working with Jupyter notebooks

You should work with Jupyter notebooks directly in VS code.

## Working with LaTeX

The subfolder report has its own docker container with LaTeX.

* Open a new VS Code window
* Open the reports folder
* Say ok to reopen it in the devcontainer

Export figures to reports/figures. The path is already defined in src.data.config:

```
from src.data import config
filename = config.figure_folder.joinpath("example.png")
```

Use functions in src/tools/ to convert output like csv, pdf, png for latex use.

Use

```
make plots
```
in to redo all plots for the publication. This runs src/visualization/make_plots.py. So add all your final plot functions there.
The idea is that you can run this command to redo all plots for the publication with one simple command. This saves a lot of time during the publication process.


Use

```
make convert_pptx
```
in {{ cookiecutter.project_name }} environment to convert all pptx files in presentations to pdf for use in the LaTeX report.


## Data handling

Small data sets like _csv_ files can be directly saved in _data/1raw_ and commited to the repo.
For larger datasets and more complex data it is better to write a function which collects the data from another server or database.
This can be done by writing a function in  src/data/make_dataset.py.

Then you can simply run:
```
make data
```

Or you can mount a folder with data to the container. For this you need to add the following line to devcontainer.json

```
"mounts": ["source=WHEVEVER_YOUR_DATA_IS,target=/{{ cookiecutter.project_name }}/data/1raw/,type=bind,consistency=cached"
```

WHEVEVER_YOUR_DATA_IS is the path to the data on the host machine like /home/user/data which is them mapped to the target paht in the container under data/1raw



## More info

Template based on Based on [cookiecutter-data-science](http://drivendata.github.io/cookiecutter-data-science/)

Contact thomas.goelles@gmail.com