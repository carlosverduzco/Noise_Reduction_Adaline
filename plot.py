from telnetlib import SE
import matplotlib.pyplot as plt
import numpy as np
import random

class Plot():
    def __init__(self, title, xlabel, ylabel):
        self.Y = []
        self.YOut = []
        with plt.rc_context({'axes.edgecolor':'black', 'xtick.color':'red', 'ytick.color':'green', 'figure.facecolor':'#242526'}):
            self.fig, self.ax= plt.subplots()
            self.title = title
            self.xlabel = xlabel
            self.ylabel = ylabel
            self.drawTemplate()


    def loadInputs(self, Y):
        self.Y = Y
        self.drawPoints()
        return len(self.Y)

    def loadInputsWithDiff(self, YOut, YInp):
        self.Y = YInp
        self.YOut = YOut
        self.drawPoints()
        return len(self.YOut)

    def cleanPoints(self):
        self.ax.cla()
        self.drawTemplate()

    def drawTemplate(self):
        self.ax.patch.set_facecolor('#ababab')
        self.ax.set_title(self.title, color= 'white', fontweight='bold', fontsize=15)
        self.ax.set_xlabel(self.xlabel, color= 'red')
        self.ax.set_ylabel(self.ylabel, color= 'green')
        self.ax.spines['left'].set_color('green')
        self.ax.spines['bottom'].set_color('red')
        self.ax.tick_params(axis='x', colors='red')
        self.ax.tick_params(axis='y', colors='green')

    def addNoise(self, n):
        newY = []
        for y in self.Y:
            if random.random() > .5:
                newY.append(y+n)
            else:
                newY.append(y-n)
        self.Y = newY
        self.drawPoints()

    def drawPoints(self):
        self.cleanPoints()
        X = np.arange(0,len(self.Y),1)
        self.ax.plot(X,self.Y, 'r')
        if len(self.YOut):
            Xx = np.arange(0,len(self.YOut),1)
            self.ax.plot(Xx,self.YOut, 'g')
