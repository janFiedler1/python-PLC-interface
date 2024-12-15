from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

def edit_ui(window):
    window.plot_widget_1 = pg.PlotWidget()
    window.plot_widget_2 = pg.PlotWidget()
    # window.plot_widget_1.plot([1,2,3,4,5], [30,35,30,35,30], pen='r')
    
    #window.plot_widget_1.setMaximumSize(QtCore.QSize(250, 250))
    window.plot_widget_1.setBaseSize(QtCore.QSize(200, 200))
    window.plot_widget_1.setObjectName("plotwidget_1")
    window.gridLayout.removeWidget(window.empty_widget_1)
    window.gridLayout.addWidget(window.plot_widget_1,0, 1, 1, 1)

    #window.plot_widget_2.setMaximumSize(QtCore.QSize(250, 250))
    window.plot_widget_2.setBaseSize(QtCore.QSize(200, 200))
    window.plot_widget_2.setObjectName("plot_widget_2")
    window.gridLayout.removeWidget(window.empty_widget_1)
    window.gridLayout.addWidget(window.plot_widget_2, 0, 2, 1, 1)

    window.plot_widget_2.plotItem.setYRange(-1.3,1.3)

    window.db_password_input.setEchoMode(QtWidgets.QLineEdit.Password)


