import mysql.connector

class MySQLDataBase:
    HOST = "host"
    USERNAME = "username"
    PASSWORD = "pass"
    DBNAME = "name"
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.HOST,
                database=self.DBNAME,
                user=self.USERNAME,
                password=self.PASSWORD
            )
            print("Success DB connecntion")
        except:
            print("Error DB connection")