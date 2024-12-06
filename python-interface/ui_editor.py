from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

def edit_ui(window):
    # window.MainWindow.setWindowIcon(QtGui.QIcon('A://StoredData/test/python-interface/controlx-logo.png'))
    # window.MainWindow.setWindowTitle("ControlX GUI")
    window.plot_widget_1 = pg.PlotWidget()
    window.plot_widget_2 = pg.PlotWidget()
    # window.plot_widget_1.plot([1,2,3,4,5], [30,35,30,35,30], pen='r')
    
    window.plot_widget_1.setMaximumSize(QtCore.QSize(200, 200))
    window.plot_widget_1.setBaseSize(QtCore.QSize(30, 30))
    window.plot_widget_1.setObjectName("plotwidget_1")
    window.verticalLayout_4.removeWidget(window.widget_2)
    window.verticalLayout_4.addWidget(window.plot_widget_1)

    window.plot_widget_2.setMaximumSize(QtCore.QSize(200, 200))
    window.plot_widget_2.setBaseSize(QtCore.QSize(30, 30))
    window.plot_widget_2.setObjectName("plot_widget_2")
    window.verticalLayout_4.removeWidget(window.widget_3)
    window.verticalLayout_4.addWidget(window.plot_widget_2)
    # self.widget_2 = QtWidgets.QWidget(self.controls_tab)
    # self.widget_2.setMinimumSize(QtCore.QSize(200, 200))
    # self.widget_2.setBaseSize(QtCore.QSize(30, 30))
    # self.widget_2.setObjectName("widget_2")
    # self.verticalLayout_4.addWidget(self.widget_2)

