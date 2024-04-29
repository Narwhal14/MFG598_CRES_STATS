
import pandas as pd

filePath = "../Resources/"
originalDataSet = pd.DataFrame
loadedCoordinateSet = pd.DataFrame()
loadedFileName = ""
loadedFilePath = ""

def load_pandas(pandaTuple):
    global loadedCoordinateSet
    import_pandas((pandaTuple))
    loadedCoordinateSet = slice_pandas(originalDataSet)
    print(f"DEBUG: Loaded File : {loadedFileName}")
    print(f"DEBUG: Loaded Panda Data \r\n =============================== \r\n{loadedCoordinateSet}")

def import_pandas(pandaTuple):
    global originalDataSet
    global loadedFilePath
    global loadedFileName

    DataFrame, FilePath, FileName = pandaTuple
    originalDataSet = DataFrame
    loadedFilePath = FilePath
    loadedFileName = FileName

def slice_pandas(DataFrame):
    # site | pinNumber | X | Y | Z | Res | Pressure | Result
    wantedColumns = ['SITE', 'PINNUMBER', 'X' , 'Y', 'Z', 'RESISTANCE', 'PRESSURE', 'OVERALL_RESULT']
    DataFrame.columns = DataFrame.columns.str.upper()
    return DataFrame[DataFrame.columns.intersection(wantedColumns)]
