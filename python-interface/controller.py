import datetime
import json
from pyads import Connection, PLCTYPE_UINT
from PyQt5 import QtWidgets, QtCore

import database
from graph import Graph

## Constants
TIMER_INTERVAL = 1000  # time in ms

class Controller:
    def __init__(self, ui):
        self.projectid = 1
        self.ui = ui
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
            new_graph = Graph("graph_"+str(i), self.tags[i], 30)
            self.graphs.append(new_graph)
            self.ui.gridLayout.addWidget(new_graph.get_plotwidget(),i//3, i%3, 1, 1)


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
            self.ui.plc_connection_status_label.setText("Connected")
            self.db_connected = True
            self.ui.p.setStyleSheet('background-color: green;')

    def connect_to_db(self, params):
        try:
            self.db_connection.connect_to_mariadb(params[0], params[1], params[2], params[3])
        except:
            w1 = QtWidgets.QLabel("Error connecting to database")
            w1.setFixedHeight(100)
            w1.setFixedWidth(300)
            w1.show()
        else:
            self.ui.db_connected_label.setText("Connected")
            self.db_connected = True
            self.ui.db_connection_status_box.setStyleSheet('background-color: green;')
        
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
            
    