# Write plot functions here
from project_package.data import config

import pandas as pd


def demo_fig():
    """
    A demo figure
    """
    demofile = config.INTERMEDIATE_DATA_FOLDER / "demo_clean.csv"
    demo_df = pd.read_csv(demofile)
    demo_fig = demo_df.plot(x="Age", y="Salary", kind="scatter")
    figure_file = config.FIGURES_FOLDER / "demo.png"
    demo_fig.get_figure().savefig(figure_file)
    print(f"Saved figure to {figure_file}")
