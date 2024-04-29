import pandas as pd
import panda_handler as data
import numpy as np
import scipy as sci

failedPinDF = pd.DataFrame()
analysisDF = pd.DataFrame()
watchPinDF = pd.DataFrame()

resRange = 0
forceRange = 0
resSTD = 0
forceSTD = 0

def generateAnalysis():
    loadDataFrames()

    global analysisDF
    global failedPinDF
    global resRange
    global forceRange

    resRange = analysisDF["RESISTANCE"].max() - analysisDF["RESISTANCE"].min()
    resRange = analysisDF["RESISTANCE"].max() - analysisDF["RESISTANCE"].min()

    forceRange = analysisDF["PRESSURE"].max() - analysisDF["PRESSURE"].min()
    forceRange = analysisDF["PRESSURE"].max() - analysisDF["PRESSURE"].min()

    calculateSTD()
    calculateZ()
    calculatePOR()
    generateReplace()

    failedPinDF = analysisDF.loc[analysisDF["OVERALL_RESULT"] != "Pass"]

    print(watchPinDF)
    print(analysisDF)
    print(failedPinDF)

def loadDataFrames():
    global analysisDF




    wantedColumns = ['PINNUMBER','RESISTANCE', 'PRESSURE', "RESISTANCE_UL", "PRESSURE_UL", 'OVERALL_RESULT' ]
    analysisDF = data.originalDataSet[data.originalDataSet.columns.intersection(wantedColumns)]

def calculateZ():
    analysisDF.insert(len(analysisDF.columns), "RES Z", sci.stats.zscore(analysisDF.loc[:, "RESISTANCE"].to_numpy()))
    analysisDF.insert(len(analysisDF.columns), "FORCE Z", sci.stats.zscore(analysisDF.loc[:, "PRESSURE"].to_numpy()))
def calculateSTD():
    global resSTD
    global forceSTD

    resSTD = np.std(analysisDF["RESISTANCE"].to_numpy())
    forceSTD = np.std(analysisDF["PRESSURE"].to_numpy())

def calculatePOR():
    analysisDF.insert(len(analysisDF.columns),"RES %OR", (analysisDF["RESISTANCE"].to_numpy() / analysisDF["RESISTANCE_UL"].to_numpy()) * 100)
    analysisDF.insert(len(analysisDF.columns),"FORCE %OR", (analysisDF["PRESSURE"].to_numpy() / analysisDF["PRESSURE_UL"].to_numpy()) * 100)

def generateReplace():
    global watchPinDF

    watchPinDF = analysisDF.loc[((analysisDF["FORCE Z"] > 2) |
                                          (analysisDF["RES Z"] > 2) |
                                          (analysisDF["RES %OR"] > 75) |
                                          (analysisDF["FORCE %OR"] > 75))]




