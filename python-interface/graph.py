from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

class Graph:
    def __init__(self, name, tag, xRange, yMin=0, yMax=100):
        self.name = name
        self.tag = tag
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setBaseSize(QtCore.QSize(200, 200))
        self.plot_widget.setMaximumSize(QtCore.QSize(400, 400))
        #self.plot_widget.setAspectLocked(1)
        self.plot_widget.setObjectName(name)
        #self.plot_widget.plotItem.setYRange(yMin, yMax)
        self.values = [0 for x in range(xRange)]
        self.xRange = xRange

    def add_value_and_update(self, value):
        self.values.append(value)
        self.values = self.values[-self.xRange:]
        self.plot_widget.plotItem.clear()
        self.plot_widget.plot(self.values)

    def update(self, values):
        self.values = values
        self.plot_widget.plotItem.clear()
        self.plot_widget.plot(self.values)
        
    def clear(self):
        self.plot_widget.plotItem.clear()

    def get_plotwidget(self):
        return self.plot_widget