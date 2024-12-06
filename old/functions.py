import datetime
import json
from pyads import Connection, PLCTYPE_UINT

class Controller:
    def __init__(self, ip_addr='192.168.56.1.1.1', port=851):
        self.plc_connection = Connection(ip_addr, port)
        self.plc_connection.open()
        self.light = "MAIN.light"
        self.counter = "MAIN.counter"
        print(self.plc_connection.read_state())
        print(self.plc_connection.read_by_name(self.light))

    def turn_light(self, value):
        self.plc_connection.write_by_name(self.light, value)

    def send_message(self, value):
        # self.message = {'text': input_text, 'time': str(datetime.datetime.now())}
        self.plc_connection.write_by_name(self.counter, value)

    def console_message(self):
        print("hi")

    def read_message(self):
        self.plc_connection.read_by_name()
