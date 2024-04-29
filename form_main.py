from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandastable import TableModel

import form_main_designer as designer
import importer as importer
import panda_handler as panda
import plotter as plotter
import stats as analysis

shownPlotIndex = 0

def initialize():
    pass

def loadFile_Clicked():
    print("PROGRAM STATUS: Loading File")
    panda.load_pandas(importer.panda_importFile())
    updateCoordinates()
    print("PROGRAM STATUS: File Loaded")

def updatePlot():
    designer.plotFrame.destroy()
    designer.resetPlotFrame()
    plotCanvas = FigureCanvasTkAgg(plotter.plotArr[shownPlotIndex].fig, designer.plotFrame)
    plotCanvas.draw()
    plotCanvas.get_tk_widget().pack()

    match shownPlotIndex:
        case 0:
            designer.plotTitleLabel.configure(text="Resistance 3D Scatter by Coord")
        case 1:
            designer.plotTitleLabel.configure(text="Failed Pins")
        case 2:
            designer.plotTitleLabel.configure(text="Resistance vs Force")
        case 3:
            designer.plotTitleLabel.configure(text="Resistance Heat Map")

    designer.Main.update()

def updateStats():
    designer.stat_resRangeVal.configure(text=round(analysis.resRange,2))
    designer.stat_forRangeVal.configure(text=round(analysis.forceRange,2))
    designer.stat_resSTDVal.configure(text=round(analysis.resSTD,2))
    designer.stat_forSTDVal.configure(text=round(analysis.forceSTD,2))
    designer.stat_badPinVal.configure(text= round(len(analysis.failedPinDF.index), 2))
    designer.stat_badPinPercentVal.configure(text=round((len(analysis.failedPinDF.index) / len(analysis.analysisDF.index)) * 100, 2))
    designer.stat_warnPinVal.configure(text=round(len(analysis.watchPinDF.index),2))
    designer.stat_warnPinPercentVal.configure(text=round((len(analysis.watchPinDF.index) / len(analysis.analysisDF.index)) * 100, 2 ))

def updateAnalysis():
    wantedColumns = ["PINNUMBER", "RES Z", "RES %OR","FORCE Z", "FORCE %OR"]
    print("PROGRAM STATUS: Updating Analysis DF")
    designer.analysisBadTable.updateModel(TableModel(analysis.failedPinDF[wantedColumns]))
    designer.analysiswarnTable.updateModel(TableModel(analysis.watchPinDF[wantedColumns]))
    designer.analysisTable.updateModel(TableModel(analysis.analysisDF[wantedColumns]))
    print(f"DEBUG: Loaded Coordinates {panda.loadedCoordinateSet}")
    designer.analysisBadTable.height = designer.baseRowSize * 2
    designer.analysiswarnTable.height = designer.baseRowSize * 2
    designer.analysisTable.height = designer.baseRowSize * 3

    designer.analysisBadTable.width = designer.baseColumnSize * 2
    designer.analysiswarnTable.width = designer.baseColumnSize * 2
    designer.analysisTable.width = designer.baseColumnSize * 2

    designer.analysisBadTable.autoResizeColumns()
    designer.analysiswarnTable.autoResizeColumns()
    designer.analysisTable.autoResizeColumns()

    designer.analysisBadTable.show()
    designer.analysiswarnTable.show()
    designer.analysisTable.show()

    #designer.Main.update()

def generate_Plots_Clicked():
    analysis.generateAnalysis()
    updateStats()
    updateAnalysis()

    plotter.add_plot(1, panda.loadedCoordinateSet, True, "X", "Y", "RESISTANCE", "PRESSURE")
    plotter.setAxis(0, panda.loadedCoordinateSet["X"], panda.loadedCoordinateSet["Y"],
                    panda.loadedCoordinateSet["RESISTANCE"], panda.loadedCoordinateSet["PRESSURE"])

    plotter.add_plot(2, panda.loadedCoordinateSet, False, "X", "Y", Color_Label= "PIN GOOD")
    plotter.setAxis(1, panda.loadedCoordinateSet["X"], panda.loadedCoordinateSet["Y"], Color_column= panda.originalDataSet["OVERALL_RESULT"])

    plotter.add_plot(3, panda.loadedCoordinateSet, False, "PINNUMBER", "OHM", "GRAMS")
    plotter.setAxis(2, panda.loadedCoordinateSet["PINNUMBER"], panda.loadedCoordinateSet["RESISTANCE"], panda.loadedCoordinateSet["PRESSURE"])

    plotter.add_plot(4, panda.loadedCoordinateSet, False, "X" , "Y", "RESISTANCE")
    plotter.setAxis(3, panda.loadedCoordinateSet["X"], panda.loadedCoordinateSet["Y"],
                   panda.loadedCoordinateSet["RESISTANCE"])

    updatePlot()

def previous_Plot_Clicked():
    global shownPlotIndex
    if shownPlotIndex > 0:
        shownPlotIndex -= 1
    else:
        shownPlotIndex = 3

    updatePlot()

def next_Plot_Clicked():
    global shownPlotIndex
    if shownPlotIndex < 3:
        shownPlotIndex += 1
    else:  shownPlotIndex = 0
    updatePlot()



def generate_Outputs_Clicked():
    pass




def updateCoordinates():

    print("PROGRAM STATUS: Updating Coordinates")
    designer.coordinateTable.updateModel(TableModel(panda.loadedCoordinateSet))
    print(f"DEBUG: Loaded Coordinates {panda.loadedCoordinateSet}")
    designer.coordinateTable.height = designer.baseRowSize*9
    designer.coordinateTable.width = designer.baseColumnSize*6
    designer.coordinateTable.show()

    designer.coordinateTable.autoResizeColumns()

    designer.fileNameLabel.configure(text= panda.loadedFileName)
    designer.Main.update()




