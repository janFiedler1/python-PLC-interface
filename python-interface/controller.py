import datetime
import sys
import os
from pyads import Connection, PLCTYPE_UINT
from PyQt5 import QtWidgets, QtCore, QtGui


import database
from graph import Graph
from alarms import Ui_Dialog
from ui_mainwindow import Ui_MainWindow
from settings import Ui_Dialog as Settings

## Constants
TIMER_INTERVAL = 1000  # time in ms

class Controller:
    def __init__(self):

        ################################
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.ui.dateTimeEdit.setDateTime(datetime.datetime.now())
        self.ui.dateTimeEdit_2.setDateTime(datetime.datetime.now())

        ## Set window icon, title
        icon_path = os.getcwd()+'/python-interface/controlx-logo.png'
        MainWindow.setWindowIcon(QtGui.QIcon(icon_path))
        MainWindow.setWindowTitle("ControlX GUI")
        MainWindow.showMaximized()

        ## Dialog Box
        dialog_box = QtWidgets.QDialog()
        dialog_box.setWindowTitle("Graph and Alarm Settings")
        self.dialog_ui = Ui_Dialog()
        self.dialog_ui.setupUi(dialog_box)
        

        ## Settings Box
        settings_box = QtWidgets.QDialog()
        settings_box.setWindowTitle("Settings")
        self.settings_ui = Settings()
        self.settings_ui.setupUi(settings_box)
        

        ## Edit UI
        self.settings_ui.plc_connection_settings.setEnabled(False)
        self.settings_ui.db_settings_form.setEnabled(False)
        
        ## Connect buttons in UI to controller functions
        self.ui.data_settings_button.clicked.connect(lambda: dialog_box.show())
        self.ui.data_settings_button.clicked.connect(lambda: dialog_box.show())
        self.ui.live_data_button.clicked.connect(lambda: self.set_live_data())
        self.ui.historical_data_button.clicked.connect(lambda: self.set_historic_data(self.ui.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm:ss"), self.ui.dateTimeEdit_2.dateTime().toString("yyyy-MM-dd hh:mm:ss")))
        self.ui.pushButton.clicked.connect(lambda: settings_box.show())

        self.settings_ui.db_connect_button.clicked.connect(lambda: self.connect_to_db([self.settings_ui.db_host_input.text(), self.settings_ui.db_login_input.text(), self.settings_ui.db_password_input.text(), self.settings_ui.db_db_input.text()]))
        self.settings_ui.plc_connect_button.clicked.connect(lambda:  self.connect_plc())
        self.settings_ui.default_plc_radio.toggled.connect(lambda checked: self.settings_ui.plc_connection_settings.setEnabled(not checked))
        self.settings_ui.db_connection_default_radio.toggled.connect(lambda checked: self.settings_ui.db_settings_form.setEnabled(not checked))

        ############################################################################################

        self.projectid = 1
        # self.tags = ["MAIN.counter", "MAIN.sine", "MAIN.triangle", "MAIN.sawtooth", "MAIN.null1", "MAIN.null2"]
        self.tags = ["MAIN.counter", "MAIN.sine", "MAIN.triangle", "MAIN.sawtooth"]
        self.db_connected = False
        self.live_data = False
        self.timer = QtCore.QTimer()

        self.timer.setInterval(TIMER_INTERVAL)  # 1000 milliseconds = 1 second
        self.timer.timeout.connect(lambda: self.update())

        ## Initialize db connection
        self.db_connection = database.Database("localhost", "plc_login", "test123", "plc_data_1")
        ## Populate graphs
        self.graphs = []
        for i in range(len(self.tags)):
            print("hi")
            new_graph = Graph("graph_"+str(i), self.tags[i], 30)
            self.graphs.append(new_graph)
            self.ui.gridLayout_2.addWidget(new_graph.get_plotwidget(),i//3, i%3, 1, 1)
        ##############################################################################################

        ## Show main window
        MainWindow.show()
        sys.exit(app.exec_())

        

    def connect_plc(self, ip_addr='192.168.56.1.1.1', port=851):
        try:
            self.plc_connection = Connection(ip_addr, port)
            self.plc_connection.open()
        except:
            w1 = QtWidgets.QLabel("Error connecting to PLC")
            w1.setFixedHeight(100)
            w1.setFixedWidth(300)
            w1.show()
        else:
            self.db_connected = True
            self.settings_ui.plc_connection_status_label.setText("Connected")
            self.settings_ui.plc_connection_status_box.setStyleSheet('background-color: green;')

    def connect_to_db(self, params):
        try:
            self.db_connection.connect_to_mariadb(params[0], params[1], params[2], params[3])
        except:
            w1 = QtWidgets.QLabel("Error connecting to database")
            w1.setFixedHeight(100)
            w1.setFixedWidth(300)
            w1.show()
        else:
            self.db_connected = True
            self.settings_ui.db_connected_label.setText("Connected")
            self.settings_ui.db_connection_status_box.setStyleSheet('background-color: green;')
        
    def write_value_to_plc(self, tag, value):
        # self.message = {'text': input_text, 'time': str(datetime.datetime.now())}
        self.plc_connection.write_by_name(tag, value)

    def read_value_from_plc(self, tag):
        return self.plc_connection.read_by_name(tag)

    def write_value_to_database(self, project, tag, value):
        self.db_connection.insert_data(project, tag, value)

    # TODO: create this function in Database.py
    def read_values_from_database(self, tag, amount=30, start_date="2024-12-17 00:13:23", end_date="2024-12-17 00:13:23"):
        #return self.db_connection.get_data()
        pass

    def set_live_data(self):
        self.timer.start()
        self.live_data = True

    def set_historic_data(self, start, end):
        self.timer.stop()
        self.live_data = False
        if(self.db_connected):
            for graph in self.graphs:
                values = self.db_connection.get_tag_data(graph.tag, start, end)
                print(f'{graph.name}: {values}')
                if(len(values) > 0):
                    graph.update(values)
                else:
                    graph.clear()
    
    def update(self):
        if(self.db_connected):
            for graph in self.graphs:
                value = self.read_value_from_plc(graph.tag)
                graph.add_value_and_update(value)
                self.db_connection.insert_tag_value(self.projectid, graph.tag, value, str(datetime.datetime.now()))
            #print(self.db_connection.get_data("value", "data", "tag", "MAIN.sawtooth", start="", end=""))
            #print(self.db_connection.get_data("value", "data", "tag", "MAIN.sawtooth", start="2024-12-17 00:13:23", end="2024-12-17 00:13:25"))

if __name__ == "__main__":
    controller = Controller()
    