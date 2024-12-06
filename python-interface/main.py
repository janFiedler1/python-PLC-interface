# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

## Third party
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime

import controller
import database
from app import Ui_MainWindow 
import ui_editor;
import math
import random

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui_editor.edit_ui(ui)

    MainWindow.setWindowIcon(QtGui.QIcon('A://StoredData/test/python-interface/controlx-logo.png'))
    MainWindow.setWindowTitle("ControlX GUI")

    
    database_connection = database.Database("localhost", "plc_login", "test123", "plc_data_1")
    controller = controller.Controller(ui, database_connection)
    

    ui.db_connect_button.clicked.connect(lambda: controller.connect_to_db(database_connection, [ui.db_host_input.text(), ui.db_login_input.text(), ui.db_password_input.text(), ui.db_db_input.text()]))

    ## Connect the buttons ##############################
    # user_input = ui.text_input.text()
    
    # ui.enter_button.clicked.connect(controller.send_message)
    ui.enter_button.clicked.connect(lambda: controller.send_message(int(ui.text_input_1.text())))
    ui.enter_button.clicked.connect(lambda: database_connection.insert_data(int(ui.text_input_1.text()),datetime.datetime.now()))
    ui.start_button.clicked.connect(lambda: controller.turn_light(True))
    ui.stop_button.clicked.connect(lambda:  controller.turn_light(False))
    #####################################################
    # ui.plot_widget_1.plot([1,2,3,4,5], [random.randint(0,30),random.randint(0,30),random.randint(0,30),random.randint(0,30),random.randint(0,30)], pen='r')
    ######################################################

    # print(database_connection.get_data_in_time_range("2024-12-04 00:00:00", "2024-12-05 00:00:00"))
    ui.stop_button.clicked.connect(lambda:  print(database_connection.get_data()))



    ######################################################
    timer = QtCore.QTimer()
    timer.setInterval(1000)  # 1000 milliseconds = 1 second
    timer.timeout.connect(lambda: controller.update_graph())
    # timer.timeout.connect(lambda: print(database_connection.get_data()))
    timer.start()
    ######################################################



    MainWindow.show()
    sys.exit(app.exec_())