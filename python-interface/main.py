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

## Constants
TIMER_INTERVAL = 10  # time in ms

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ##ui_editor.edit_ui(ui)
    ui.gridLayout.removeWidget(ui.empty_widget_1)
    ui.gridLayout.removeWidget(ui.empty_widget_2)
    ui.gridLayout.removeWidget(ui.empty_widget_3)

    ## Set window icon, title
    icon_path = os.getcwd()+'/python-interface/controlx-logo.png'
    MainWindow.setWindowIcon(QtGui.QIcon(icon_path))
    MainWindow.setWindowTitle("ControlX GUI")
    MainWindow.showMaximized()

    
    ## Create controller
    controller = controller.Controller(ui)
    
    ## Connect buttons in UI to controller functions
    ui.db_connect_button.clicked.connect(lambda: controller.connect_to_db([ui.db_host_input.text(), ui.db_login_input.text(), ui.db_password_input.text(), ui.db_db_input.text()]))
    #ui.enter_button.clicked.connect(lambda: controller.send_message(int(ui.text_input_1.text())))
    #ui.enter_button.clicked.connect(lambda: controller.insert_data(int(ui.text_input_1.text()),datetime.datetime.now()))
    #ui.start_button.clicked.connect(lambda: controller.turn_light(True))
    #ui.stop_button.clicked.connect(lambda:  controller.turn_light(False))
    ui.plc_connect_button.clicked.connect(lambda:  controller.connect_plc())
    ui.default_plc_radio.toggled.connect(lambda checked: ui.groupBox_5.setEnabled(not checked))
    ## ui.custom_plc_radio.toggled.connect(lambda checked: ui.groupBox_5.setEnabled(not checked))

    ## Create a timer and run a function in controller at every timer interval
    timer = QtCore.QTimer()
    timer.setInterval(TIMER_INTERVAL)  # 1000 milliseconds = 1 second
    timer.timeout.connect(lambda: controller.update())
    timer.start()

    ## Show main window
    MainWindow.show()
    sys.exit(app.exec_())
