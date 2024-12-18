## main.py
## This file imports the ui model, creates a controller, connects buttons on the ui to controller functions
## and displays the model

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime

import controller
import database
from app import Ui_MainWindow 
import ui_editor;
import math
import random
import os
import sys
from alarms import Ui_Dialog

## Constants
TIMER_INTERVAL = 1000  # time in ms

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ##ui_editor.edit_ui(ui)
    ui.gridLayout.removeWidget(ui.empty_widget_1)
    ui.gridLayout.removeWidget(ui.empty_widget_2)
    ui.gridLayout.removeWidget(ui.empty_widget_3)
    ui.dateTimeEdit.setDateTime(datetime.datetime.now())
    ui.dateTimeEdit_2.setDateTime(datetime.datetime.now())

    ## Set window icon, title
    icon_path = os.getcwd()+'/python-interface/controlx-logo.png'
    MainWindow.setWindowIcon(QtGui.QIcon(icon_path))
    MainWindow.setWindowTitle("ControlX GUI")
    MainWindow.showMaximized()

    ## Edit UI
    ui.plc_connection_settings.setEnabled(False)
    ui.db_settings_form.setEnabled(False)

    dialog_box = QtWidgets.QDialog()
    dialog_ui = Ui_Dialog()
    dialog_ui.setupUi(dialog_box)
    dialog_box.setWindowTitle("Graph and Alarm Settings")
    
    ## Create controller
    controller = controller.Controller(ui)
    
    ## Connect buttons in UI to controller functions
    ui.db_connect_button.clicked.connect(lambda: controller.connect_to_db([ui.db_host_input.text(), ui.db_login_input.text(), ui.db_password_input.text(), ui.db_db_input.text()]))
    ui.plc_connect_button.clicked.connect(lambda:  controller.connect_plc())
    ui.data_settings_button.clicked.connect(lambda: dialog_box.show())
    ui.default_plc_radio.toggled.connect(lambda checked: ui.plc_connection_settings.setEnabled(not checked))
    ui.db_connection_default_radio.toggled.connect(lambda checked: ui.db_settings_form.setEnabled(not checked))
    ui.data_settings_button.clicked.connect(lambda: dialog_box.show())
    ui.live_data_button.clicked.connect(lambda: controller.set_live_data())
    ui.historical_data_button.clicked.connect(lambda: controller.set_historic_data(ui.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm:ss"), ui.dateTimeEdit_2.dateTime().toString("yyyy-MM-dd hh:mm:ss")))
    # print(ui.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm:ss"))

    ## Create a timer and run a function in controller at every timer interval
    # timer = QtCore.QTimer()
    # timer.setInterval(TIMER_INTERVAL)  # 1000 milliseconds = 1 second
    # timer.timeout.connect(lambda: controller.update())
    # timer.start()

    ## Show main window
    MainWindow.show()
    sys.exit(app.exec_())

