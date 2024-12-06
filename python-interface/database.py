import mariadb
import time
from PyQt5 import QtWidgets


class Database:

    def __init__(self, host, user, password, database):
        pass
        # try:
        #     self.conn = mariadb.connect(
        #         host=host,
        #         user=user,
        #         password=password,
        #         database=database
        #     )
        # except mariadb.Error as e:
        #     print(f"Error connecting to MariaDB database: {e}")

    def connect_to_mariadb(self, host, user, password, database):
        try:
            self.conn = mariadb.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB database: {e}")


    def insert_data(self, value, datetime_value):
        cursor = self.conn.cursor()
        query = "INSERT INTO data_2 (value, time) VALUES (?, ?)"
        try:
            cursor.execute(query, (value, datetime_value))
            self.conn.commit()
        except mariadb.Error as e:
            print(f"Error inserting data: {e}")
        finally:
            cursor.close()
    
    def get_data_in_time_range(self, start_date, end_date):
        cursor = self.conn.cursor()
        query = "select * from data_2 where time between ? and ?"
        try:
            cursor.execute(query, (start_date, end_date))
            self.conn.commit()
        except mariadb.Error as e:
            print(f"Error inserting data: {e}")
        finally:
            cursor.close()

    def get_data(self):
        cursor = self.conn.cursor()
        query = "select value from data_2"
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except mariadb.Error as e:
            print(f"Error getting data: {e}")
        finally:
            cursor.close()


    def main(self):
        # Replace with your MariaDB credentials
        host = "your_host"
        user = "your_user"
        password = "your_password"
        database = "your_database"

        conn = self.connect_to_mariadb(host, user, password, database)
        if conn is None:
            return

        while True:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")
            value = 1  # Replace with your desired value
            self.insert_data(conn, current_time, value)
            time.sleep(1)
