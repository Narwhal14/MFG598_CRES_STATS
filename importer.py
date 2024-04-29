import csv
import tkinter as tk
from tkinter import filedialog
from pandastable import Table, TableModel

import pandas
import pandas as pd


def panda_importFile():
    FilePath = tk.filedialog.askopenfilename()
    DataFrame = pd.read_csv(FilePath)
    FileName = FilePath.split("/")[-1]
    print(f"PROGRAM STATUS: Loading {FileName}")
    return (DataFrame, FilePath, FileName)

