from src.data import config
import os

folder_name = config.FIGURE_FOLDER.as_posix()


def pdf2png() -> None:
    """Converts all pdfs in the figure folder to high res png files. Especially usefull for use in Powerpoint."""
    command = "rm " + folder_name + "/converted_*.png"
    os.system(command)

    for file in config.FIGURE_FOLDER.glob("*.pdf"):
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
