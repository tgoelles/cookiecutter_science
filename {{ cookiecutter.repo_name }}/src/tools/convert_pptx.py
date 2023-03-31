from pathlib import Path
import glob
import os
from src.data import config

slides_path = config.PRESENTATIONS_FOLDER
libreoffice_executable = "/usr/bin/libreoffice"
pdf_path = config.FIGURE_FOLDER


def convert_pptx_as_pdf() -> None:
    """Convert all powerpoint slides to pdf."""
    print("converting pptx to pdf... ")
    for slide in slides_path.rglob("*.pptx"):
        print(slide.as_posix())
        command = (
            libreoffice_executable
            + " --headless --invisible --convert-to pdf --outdir "
            + pdf_path.as_posix()
            + " "
            + slide.as_posix()
        )
        os.system(command)


convert_pptx_as_pdf()
