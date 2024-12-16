import datetime
import json
from pyads import Connection, PLCTYPE_UINT
from PyQt5 import QtWidgets

import database
from graph import Graph

class Controller:
    def __init__(self, ui):
        self.ui = ui
        
        self.light = "MAIN.light"
        self.counter = "MAIN.counter"
        self.sine = "MAIN.sine"
        self.triangle = "MAIN.triangle"
        self.sawtooth = "MAIN.sawtooth"
        self.tags = [self.counter, self.sine, self.triangle, self.sawtooth, "MAIN.null1", "MAIN.null2"]
        self.db_connected = False
        self.plc_data_1 = [0]*30
        # print(self.plc_connection.read_state())
        # print(self.plc_connection.read_by_name(self.light))

        self.db_connection = database.Database("localhost", "plc_login", "test123", "plc_data_1")
        self.graphs = []
        for i in range(6):
            new_graph = Graph("graph_"+str(i), self.tags[i], 30)
            self.graphs.append(new_graph)
            self.ui.gridLayout.addWidget(new_graph.get_plotwidget(),i//3, i%3, 1, 1)

    def turn_light(self, value):
        self.plc_connection.write_by_name(self.light, value)

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
            self.ui.groupBox_4.setStyleSheet('background-color: green;')
        

    def send_message(self, value):
        # self.message = {'text': input_text, 'time': str(datetime.datetime.now())}
        self.plc_connection.write_by_name(self.counter, value)

    def console_message(self):
        print("hi")

    def read_message(self):
        self.plc_connection.read_by_name()

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


    def insert_data(self, value, time):
        self.db_connection.insert_data(value, time)

    def get_data(self):
        return self.db_connection.get_data()
    
    def get_value(self, tag):
        return self.plc_connection.read_by_name(tag)
    
    def update(self):
        if(self.db_connected):
            pass
            # self.graphs[0].append(self.plc_connection.read_by_name(self.sine))
            # self.graphs[0] = self.graphs[0][-30:]
            # self.ui.plot_widget_2.plotItem.clear()
            # self.ui.plot_widget_2.plot(self.plc_data_1)
            self.graphs[0].add_value_and_update(self.get_value(self.graphs[0].tag))
            # self.update_graph_1()
            # self.update_graph_2()
            for graph in self.graphs:
                graph.add_value_and_update(self.get_value(graph.tag))
            

    def update_graph_1(self):
        self.ui.plot_widget_1.plotItem.clear()
        self.ui.plot_widget_1.plot([row[0] for row in self.db_connection.get_data()[-7:]])

    def update_graph_2(self):
        self.plc_data_1.append(self.plc_connection.read_by_name(self.sine))
        self.plc_data_1 = self.plc_data_1[-30:]
        self.ui.plot_widget_2.plotItem.clear()
        self.ui.plot_widget_2.plot(self.plc_data_1)

    def update_graph(self, graph, values):
        self.plc_data_1.append(self.plc_connection.read_by_name(self.sine))
        self.plc_data_1 = self.plc_data_1[-30:]
        self.ui.plot_widget_2.plotItem.clear()
        self.ui.plot_widget_2.plot(self.plc_data_1)
        

