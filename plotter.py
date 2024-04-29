import numpy as np
import pandas as pd
from matplotlib import pyplot as plt, cm
from pandas import DataFrame
import stats as analysis

import panda_handler as panda

# supported types
# 1) 3d Scatter
# 2) 2d Scatter
# 2) 2d Line
# 3) 2d Heat Map
plotArr = []
def add_plot(plt_type, DF, is3D: bool, X_Label, Y_Label, Z_Label="", Color_Label=""):
    plotArr.append(plots(len(plotArr) + 1,plt_type, DF, is3D, X_Label, Y_Label, Z_Label, Color_Label))

def setAxis(plotIndex, X_column, Y_column, Z_column=pd.Series({'Z' : []}), Color_column=pd.Series({'COLOR' : []}) ):
    plotArr[plotIndex].set_plot_axis(X_column, Y_column, Z_column, Color_column)


class plots:
    df: DataFrame
    axis_df: DataFrame

    fig: plt.figure
    ax: plt.axes

    is3D: bool
    hasZ: bool
    hasColor: bool

    x_label: str
    y_label: str
    z_label: str
    color_label: str

    def __init__(self,figNum,plt_type, DF, is3D: bool, X_Label, Y_Label, Z_Label="", Color_Label=""):
        #if (is3D):
            #self.ax = self.fig.add_subplot(111,projection='3d')
        #else:
           # self.ax = self.fig.add_subplot()
        COLOR = 'ffffff'
        plt.rcParams['text.color'] = COLOR
        plt.rcParams['axes.labelcolor'] = COLOR
        plt.rcParams['xtick.color'] = COLOR
        plt.rcParams['ytick.color'] = COLOR

        self.ax2 = None
        self.fig = plt.figure(figNum , figsize=(9,9))
        self.df = DF
        self.is3D = is3D
        self.x_label = X_Label
        self.y_label = Y_Label
        self.z_label = Z_Label
        self.color_label = Color_Label
        self.plotType = plt_type
        self.fig.set_facecolor("#212121")
        self.fig.set_edgecolor("#212121")

    def generate_heat_map(self):

        self.ax = plt.axes()
        self.axis_df.sort_values(by=["X", "Y"],inplace=True)


        print(self.axis_df)
        heatmapDF = pd.DataFrame()

        xVals = self.axis_df["X"].value_counts().index
        yVals = self.axis_df["Y"].value_counts().index

        testData = pd.DataFrame(columns = xVals, index=yVals)
        print(testData)

        for x in xVals:
            for y in yVals:
                if (len(self.axis_df[(self.axis_df['Y'] == y) & (self.axis_df['X'] == x)]['RESISTANCE'].values) != 0):
                    testData.at[y,x] = self.axis_df[(self.axis_df['Y'] == y) & (self.axis_df['X'] == x)]['RESISTANCE'].values[0]

        testData.sort_index(axis=0, ascending = True, inplace=True)
        testData.sort_index(axis=1, ascending = True, inplace=True)
        print(testData)
        print(heatmapDF)

        hmArr = testData.fillna(0).to_numpy()

        im = self.ax.imshow(hmArr, cmap = "nipy_spectral")



        self.ax.set_xticks(np.arange(len(xVals)), labels = xVals)
        self.ax.set_yticks(np.arange(len(yVals)), labels=yVals)

        plt.setp(self.ax.get_xticklabels(), rotation=45, ha="right",
                 rotation_mode="anchor")


        for i in range(len(xVals)):
            for j in range(len(yVals)):
                text = self.ax.text(j, i, hmArr[i, j],
                               ha="center", va="center", color="black")



        self.ax.set_title("Resistance Map")
        self.fig.tight_layout()
        pass

    def generate_3d_scatter(self):
        self.ax = plt.axes(projection='3d',facecolor = "#212121")
        colmap = cm.ScalarMappable(cmap="plasma" )
        colmap.set_array(self.axis_df[self.axis_df.columns[2]])
        self.ax.scatter(self.axis_df[self.axis_df.columns[0]], self.axis_df[self.axis_df.columns[1]], self.axis_df[self.axis_df.columns[2]],  s=300, c = self.axis_df[self.axis_df.columns[2]] ,cmap="plasma")
        self.fig.colorbar(colmap, ax=self.ax, orientation = 'horizontal')

        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.set_zlabel("Resistance (mOhm)")
    def generate_2d_scatter(self):
        self.ax = plt.axes(facecolor = "#212121")
        for point in self.axis_df.index:

            if self.axis_df.loc[point]["OVERALL_RESULT"] == "Fail":
                self.ax.scatter(self.axis_df.loc[point]["X"], self.axis_df.loc[point]["Y"]  ,marker="s",  s=300,c = "red")
            elif self.axis_df.loc[point]["PINNUMBER"] in analysis.watchPinDF["PINNUMBER"].values:
                self.ax.scatter(self.axis_df.loc[point]["X"], self.axis_df.loc[point]["Y"]  ,marker="s",  s=300,c = "yellow")
            else:
                self.ax.scatter(self.axis_df.loc[point]["X"], self.axis_df.loc[point]["Y"] , marker="s",s=300, c="green")


        self.ax.set_xticks(self.axis_df[self.axis_df.columns[0]])
        self.ax.set_xticklabels(self.axis_df[self.axis_df.columns[0]], rotation = 45)


        self.ax.set_yticks(self.axis_df[self.axis_df.columns[1]])
        self.ax.set_yticklabels(self.axis_df[self.axis_df.columns[1]])
        pass

    def generate_2d_line(self):

        self.ax = plt.axes(facecolor = "#212121")
        self.ax2 = self.ax.twinx()

        self.ax.plot(self.axis_df[self.axis_df.columns[0]],
                     self.axis_df[self.axis_df.columns[1]],
                     label = "Resistance (mOhms)", lw = 5)

        self.ax.set_ylabel("Resistance (mOhm)")
        self.ax.set_xlabel("Pin #")
        self.ax2.plot(self.axis_df[self.axis_df.columns[0]],
                     self.axis_df[self.axis_df.columns[2]],
                     label="Force (g)", color = "purple", lw = 3,linestyle = ":")
        self.ax.set_xticks(self.axis_df[self.axis_df.columns[0]])
        self.ax.set_xticklabels(self.axis_df[self.axis_df.columns[0]], rotation = 90)
        self.ax.tick_params(direction = "in", pad = 5)
        self.ax2.set_ylabel("Force (g)")
        self.fig.suptitle("Resistance / Force")
        self.ax.legend(facecolor = "#212121", loc=9)
        self.ax2.legend(facecolor = "#212121", loc=1)
        pass

    def generate_plots(self):
        if self.plotType == 1:
            self.generate_3d_scatter()
        elif self.plotType == 2:
            self.generate_2d_scatter()
        elif self.plotType == 3:
            self.generate_2d_line()
        elif self.plotType == 4:
            self.generate_heat_map()


    def set_plot_axis(self, X_column, Y_column, Z_column=pd.Series({'Z' : []}), Color_column=pd.Series({'COLOR' :[]}) ):
        self.axis_df = DataFrame()
        self.axis_df[X_column.name] = X_column
        self.axis_df[Y_column.name] = Y_column
        if not Z_column.empty:
            self.axis_df[Z_column.name] = Z_column
            self.hasZ = True
        else:
            self.hasZ = False
        if not Color_column.empty:
            self.axis_df[Color_column.name] = Color_column
            self.hasColor = True
        else:
            self.hasColor = False


        self.axis_df["PINNUMBER"] = panda.originalDataSet["PINNUMBER"]

        self.generate_plots()




