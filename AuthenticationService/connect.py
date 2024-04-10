import psycopg2
from user.sql import SQLUser


class ConnectDataBase:
    def __init__(self):
        self.connection = psycopg2.connect(
            host='localhost',
            database='pbd2024_1',
            user='postgres',
            password='91397114'
        )

    def get_instance(self):
        return self.connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute(SQLUser._CREATE_TABLE)
        self.connection.commit()
        cursor.close()
