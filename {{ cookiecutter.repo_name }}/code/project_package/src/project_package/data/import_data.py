from project_package.data import config
from pathlib import Path

import pandas as pd


# Enter code here for the final generation of processed data
def process_rawdata() -> None:
    """Convert all datasets and saves them in the intermediate folder"""
    # code comes here
    demo_file = config.RAW_DATA_FOLDER / "demo.csv"
    demo_df = pd.read_csv(demo_file)
    # delite ID column
    demo_df.drop("ID", axis=1, inplace=True)
    demo_df.to_csv(config.INTERMEDIATE_DATA_FOLDER / "demo_clean.csv", index=False)
    print("Processed data saved to intermediate folder")
    return None
