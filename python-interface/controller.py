import datetime
import json
from pyads import Connection, PLCTYPE_UINT

class Controller:
    def __init__(self, ui, db_connection, ip_addr='192.168.56.1.1.1', port=851):
        self.ui = ui
        self.db_connection = db_connection
        self.plc_connection = Connection(ip_addr, port)
        self.plc_connection.open()
        self.light = "MAIN.light"
        self.counter = "MAIN.counter"
        # print(self.plc_connection.read_state())
        # print(self.plc_connection.read_by_name(self.light))

    def turn_light(self, value):
        self.plc_connection.write_by_name(self.light, value)

    def send_message(self, value):
        # self.message = {'text': input_text, 'time': str(datetime.datetime.now())}
        self.plc_connection.write_by_name(self.counter, value)

    def console_message(self):
        print("hi")

    def read_message(self):
        self.plc_connection.read_by_name()

    def connect_to_db(self, db, params):
        try:
            db.connect_to_mariadb(params[0], params[1], params[2], params[3])
            self.ui.db_connected_label.setText("Connected")
        except:
            pass

    def update_graph(self):
        self.ui.plot_widget_1.clear
        self.ui.plot_widget_1.plot([row[0] for row in self.db_connection.get_data()[-7:]])
        

