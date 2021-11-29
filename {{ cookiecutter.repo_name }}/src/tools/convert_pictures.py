from src.data import config
import os

folder_name = config.figure_folder.as_posix()


def pdf2png() -> None:
    """Converts all pdfs in the figure folder to high res png files. Especially usefull for use in Powerpoint.
    """
    command = "rm " + folder_name + "/converted_*.png"
    os.system(command)

    for file in config.figure_folder.glob("*.pdf"):
        command = (
            "convert -density 600 "
            + folder_name
            + "/"
            + file.name
            + " "
            + folder_name
            + "/"
            + "converted_"
            + file.stem
            + ".png"
        )
        print(command)
        os.system(command)
