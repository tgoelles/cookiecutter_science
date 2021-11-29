from src.data import config
import pandas as pd
import pathlib
from pathlib import Path
from typing import Dict


def get_filenames(inputpath: Path = config.raw_data_folder) -> None:
    """Prints the file nemes in the inputpath.
    
    Args:
        inputpath (str, optional): [description]. Defaults to config.raw_data_folder.
    
    Returns:
        filename as text
    """
    files_in_basepath = inputpath.iterdir()
    for item in files_in_basepath:
        if item.is_file():
            print(item.name)
    return None


def get_foldernames(inputpath: Path = config.raw_data_folder) -> None:
    """prints the folders in the inputpath.
    
    Args:
        inputpath (str, optional): [description]. Defaults to config.raw_data_folder.
    
    Returns:
        folder names as text
    """
    files_in_basepath = inputpath.iterdir()
    for item in files_in_basepath:
        if item.is_dir():
            print(item.name)
    return None



# Enter code here for the final generation of processed data
def process_rawdata() -> None:
    """ Convert all datasets and saves them in the processed folder"""
    # code comes here
    return None
