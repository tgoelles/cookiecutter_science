import os
from project_package.data import config

folder_name = config.FIGURES_FOLDER.as_posix()


def csv_for_latex() -> None:
    """Converts all csv files in the figure folder for direct use in LaTeX."""
    command = "rm " + folder_name + "/*_latex.csv"
    os.system(command)

    for file in config.FIGURES_FOLDER.glob("*.csv"):
        command1 = "sed s/{/\\\\\\\citep{/g "
        command2 = "sed s/}/}\\\\\\\\\\\\\\\\/g "
        command3 = "sed s/\\'//g "
        command = (
            "cat "
            + folder_name
            + "/"
            + file.name
            + " | "
            + command1
            + " | "
            + command2
            + " | "
            + command3
            + " > "
            + folder_name
            + "/"
            + file.stem
            + "_latex"
            + ".csv"
        )
        print(f"converting {file}")
        os.system(command)
