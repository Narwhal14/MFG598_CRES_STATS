import customtkinter as ctk

from pandastable import Table
import stats as analysis
import form_main as form
import panda_handler as panda

rows = 11
columns = 15

baseRowSize = 50
baseColumnSize = 80
Main = ctk.CTk()
ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("dark")
i = 0
for i in range(rows):
    Main.rowconfigure(index = i,minsize=baseRowSize, pad=5, weight=1)
i = 0
for i in range(columns):
    Main.columnconfigure(index = i,minsize=baseColumnSize, pad=5, weight=1)

defaultFont = ctk.CTkFont(family='Roboto',size = 40, weight='bold')
analysisFont = ctk.CTkFont(family='Roboto',size = 30, weight='bold')

#Frame Layout Configuration
coordinateFrame = ctk.CTkFrame(Main)
coordinateTable = Table(coordinateFrame, dataframe=panda.loadedCoordinateSet, width= (9 * baseRowSize), facecolor = "#212121")
coordinateFrame.grid(row = 1, column = 0, columnspan=6, rowspan=9,sticky ="nsew")

loadButtonFrame = ctk.CTkFrame(Main )
loadButtonFrame.grid(row = 10, column = 0, columnspan=6, rowspan=1,sticky ="nsew")
loadFileButton = ctk.CTkButton(loadButtonFrame, text="Load File", command=form.loadFile_Clicked, font=defaultFont)
loadFileButton.pack(fill = "both", expand = True,  pady = 15, padx = 15)

fileNameFrame = ctk.CTkFrame(Main )
fileNameFrame.grid(row = 0, column=0, columnspan=6, rowspan=1,sticky ="nsew")
fileNameLabel = ctk.CTkLabel(fileNameFrame, text = panda.loadedFileName,font=defaultFont)
fileNameLabel.pack(fill = "both", expand = True, pady = 30, padx = 30)

plotButtonLeftFrame = ctk.CTkFrame(Main )
plotButtonLeftFrame.grid(row = 8, column=6, columnspan=3, rowspan=2,sticky ="nsew")
previousPlot = ctk.CTkButton(plotButtonLeftFrame, text = "<",  command=form.previous_Plot_Clicked ,font=('Roboto',80, 'bold'))
previousPlot.pack(fill = "both", expand = True, pady = 30, padx = 30)

plotButtonRightFrame = ctk.CTkFrame(Main )
nextPlot = ctk.CTkButton(plotButtonRightFrame, text = ">",   command=form.next_Plot_Clicked, font=('Roboto',80, 'bold') )
plotButtonRightFrame.grid(row = 8, column=9, columnspan=3, rowspan=2,sticky ="nsew")
nextPlot.pack(fill = "both", expand = True, pady = 30, padx = 30)

plotFrame = ctk.CTkFrame(Main )
plotFrame.grid(row = 1, column = 6, columnspan = 6, rowspan=7,sticky ="nsew")

plotTitleFrame = ctk.CTkFrame(Main )
plotTitleFrame.grid(row = 0, column = 6, columnspan = 6, rowspan=1,sticky ="nsew")
plotTitleLabel = ctk.CTkLabel(plotTitleFrame, font=defaultFont, text= " ")
plotTitleLabel.pack(fill = "both", expand = True, pady = 30, padx = 30)

generatePlotFrame = ctk.CTkFrame(Main )
generatePlotFrame.grid(row = 10, column = 6, columnspan = 6, rowspan=1,sticky ="nsew")
generatePlots = ctk.CTkButton(generatePlotFrame, text="generate\rplots",
                          command=form.generate_Plots_Clicked,font=defaultFont)
generatePlots.pack(fill = "both", expand = True,  pady = 15, padx = 15)

analysisLabelFrame = ctk.CTkFrame(Main)
analysisLabelFrame.grid(row = 8, column = 12, columnspan = 4, rowspan=3,sticky ="nsew")

analysisBadFrame = ctk.CTkFrame(Main)
analysisBadTable = Table(analysisBadFrame, dataframe =analysis.failedPinDF, width= (2 * baseColumnSize), facecolor = "#212121")

analysisBadDescripLabelFrame = ctk.CTkFrame(Main,fg_color= "#8B0000")
analysisBadDescripLabelFrame.grid(row = 1, column = 47, rowspan = 2,sticky ="nsew")
analysisBadDescripLabeltxt = ctk.CTkLabel(analysisBadDescripLabelFrame, text = "Bad\r\nPins",font=defaultFont, text_color= "#FFFFFF")
analysisBadDescripLabeltxt.pack(fill = "both", expand = True, pady = 30, padx = 30)
analysisBadFrame.grid(row = 1, column = 12, columnspan=7, rowspan=2,sticky ="nsew")


analysiswarnFrame = ctk.CTkFrame(Main)
analysiswarnTable= Table(analysiswarnFrame, dataframe=analysis.watchPinDF, width= (2 * baseColumnSize), facecolor = "#212121")
analysiswarnFrame.grid(row = 3, column = 12, columnspan=7, rowspan=2,sticky ="nsew")

analysiswarnDescripLabelFrame = ctk.CTkFrame(Main, fg_color = "#FFDB58")
analysiswarnDescripLabelFrame.grid(row = 3, column = 47, rowspan = 2,sticky ="nsew")
analysiswarnDescripLabeltxt = ctk.CTkLabel(analysiswarnDescripLabelFrame, text = "Warning\r\nPins",font=defaultFont, text_color= "#000000")
analysiswarnDescripLabeltxt.pack(fill = "both", expand = True, pady = 30, padx = 30)

analysisFrame = ctk.CTkFrame(Main)
analysisTable= Table(analysisFrame, dataframe=analysis.analysisDF, width= (4 * baseRowSize))

analysisDescripLabelFrame = ctk.CTkFrame(Main, fg_color = "#007172")
analysisDescripLabelFrame.grid(row = 5, column =47 , rowspan = 3,sticky ="nsew")
analysisDescripLabeltxt = ctk.CTkLabel(analysisDescripLabelFrame, text = "All\r\nPins",font=defaultFont, text_color= "#000000")
analysisDescripLabeltxt.pack(fill = "both", expand = True, pady = 30, padx = 30)
analysisFrame.grid(row = 5, column = 12, columnspan=7, rowspan=3,sticky ="nsew")

stat_resRange = ctk.CTkLabel(analysisLabelFrame, font = analysisFont, text= "Resistance Range (mOhm): ")
stat_resRangeVal = ctk.CTkLabel(analysisLabelFrame, font = analysisFont, text= " ")
stat_resRange.grid(row = 0, column = 0,columnspan = 2,sticky ="nsew")
stat_resRangeVal.grid(row =0, column = 2,sticky ="nsew")

stat_forRange = ctk.CTkLabel(analysisLabelFrame, font = analysisFont, text= "Force Range (g): ")
stat_forRangeVal = ctk.CTkLabel(analysisLabelFrame, font = analysisFont, text= " ")
stat_forRange.grid(row = 1, column = 0,columnspan = 2,sticky ="nsew")
stat_forRangeVal.grid(row = 1, column = 2,sticky ="nsew")

stat_resSTD = ctk.CTkLabel(analysisLabelFrame, font = analysisFont, text= "Resistance Deviation (mOhm): ")
stat_resSTDVal = ctk.CTkLabel(analysisLabelFrame, font = analysisFont, text= " ")
stat_resSTD.grid(row = 2, column = 0,columnspan = 2,sticky ="nsew")
stat_resSTDVal.grid(row = 2, column = 2,sticky ="nsew")

stat_forSTD = ctk.CTkLabel(analysisLabelFrame, font = analysisFont, text= "Force Deviation (g): ")
stat_forSTDVal = ctk.CTkLabel(analysisLabelFrame, font = analysisFont, text= " ")
stat_forSTD.grid(row = 3, column = 0,columnspan = 2,sticky ="nsew")
stat_forSTDVal.grid(row = 3, column = 2,sticky ="nsew")

stat_badPinCount = ctk.CTkLabel(analysisLabelFrame, font = analysisFont, text= "Bad Pin Count: ")
stat_badPinVal = ctk.CTkLabel(analysisLabelFrame, font = analysisFont, text= " ")
stat_badPinCount.grid(row = 4, column = 0,columnspan = 2,sticky ="nsew")
stat_badPinVal.grid(row = 4, column = 2,sticky ="nsew")

stat_badPinPercent = ctk.CTkLabel(analysisLabelFrame, font = analysisFont, text= "Percent Bad: ")
stat_badPinPercentVal = ctk.CTkLabel(analysisLabelFrame, font = analysisFont, text= " ")
stat_badPinPercent.grid(row = 5, column = 0,columnspan = 2,sticky ="nsew")
stat_badPinPercentVal.grid(row = 5, column = 2,sticky ="nsew")

stat_warnPinCount = ctk.CTkLabel(analysisLabelFrame, font = analysisFont, text= "Warn Pin Count: ")
stat_warnPinVal = ctk.CTkLabel(analysisLabelFrame, font = analysisFont, text= " ")
stat_warnPinCount.grid(row = 6, column = 0, columnspan = 2, sticky ="nsew")
stat_warnPinVal.grid(row = 6, column = 2,sticky ="nsew")

stat_warnPinPercent = ctk.CTkLabel(analysisLabelFrame, font = analysisFont, text= "Percent Warn: ")
stat_warnPinPercentVal = ctk.CTkLabel(analysisLabelFrame, font = analysisFont, text= " ")
stat_warnPinPercent.grid(row = 7, column = 0,columnspan = 2, sticky ="nsew")
stat_warnPinPercentVal.grid(row = 7, column = 2,sticky ="nsew")


analysisLabel2Frame = ctk.CTkFrame(Main)
analysisLabel2Frame.grid(row = 0, column=12, columnspan=5, rowspan=1,sticky ="nsew")
analysisLabel2 = ctk.CTkLabel(analysisLabel2Frame, text = "Pin Statistics",font=defaultFont)
analysisLabel2.pack(fill = "both", expand = True, pady = 30, padx = 30)

plotFrame = ctk.CTkFrame(Main)
plotFrame.grid(row=1, column=6, columnspan=6, rowspan=7, sticky="nsew")

def resetPlotFrame():

    global plotFrame
    plotFrame = ctk.CTkFrame(Main)
    plotFrame.grid(row=1, column=6, columnspan=6, rowspan=7, sticky="nsew")




