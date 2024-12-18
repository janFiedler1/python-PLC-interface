import mariadb
import time
from PyQt5 import QtWidgets


class Database:

    def __init__(self, host, user, password, database):
        pass

    def connect_to_mariadb(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        # try:
        self.conn = mariadb.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        # except mariadb.Error as e:
        #     print(f"Error connecting to MariaDB database: {e}")

    def insert_tag_value(self, project_id, tag, value, time):
        cursor = self.conn.cursor()
        query = "INSERT INTO `data` (`project_id`, `tag`, `value`, `time`) VALUES (?, ?, ?, ?);"
        try:
            cursor.execute(query, (project_id, tag, value, time))
            self.conn.commit()
        except mariadb.Error as e:
            print(f"Error inserting data: {e}")
        finally:
            cursor.close()
            


    def get_tag_data(self, tag, start="", end=""):
        cursor = self.conn.cursor()
        query = "select value from `data` where `tag` = '"+tag+"'"
        if(start != ""):
            query = query + " and time between \""+start+"\" and \""+end+"\" limit 30"
        else:
            query = query+" limit 30"
        try:
            if(start != ""):
                cursor.execute(query)
            else:
                cursor.execute(query)
            result = []
            for row in cursor:
                result.append(row[0])
            return result
        except mariadb.Error as e:
            print(f"Error reading data:\n {e}\n{query}")
        finally:
            cursor.close()

if __name__ == "__main__":
    database = Database("localhost", "plc_login", "test123", "plc_data_1")
    database.connect_to_mariadb("localhost", "plc_login", "test123", "plc_data_1")
    print(database.get_tag_data("MAIN.sawtooth","2024-12-17 17:53:20","2024-12-17 17:53:22"))