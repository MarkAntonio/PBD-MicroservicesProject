import psycopg2
from NotaPromissoria.PaymentContract.sql import SQLPaymentContract
from .client.sql import SQLClient
from .PaymentClient.sql import SQLPaymentClient


class ConnectDataBase:
    def __init__(self):
        self.connection = psycopg2.connect(
            host='localhost',
            database='nota_promissoria_PBD_2024.1',
            user='postgres',
            password='admin'
        )

    def get_instance(self):
        return self.connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute(SQLClient._CREATE_TABLE)
        cursor.execute(SQLPaymentContract._CREATE_TABLE)
        cursor.execute(SQLPaymentClient._CREATE_TABLE)
        self.connection.commit()
        cursor.close()
