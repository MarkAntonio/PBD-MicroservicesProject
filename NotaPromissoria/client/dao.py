from .modelo import Client
from .sql import SQLClient
from ..connect import ConnectDataBase


class DAOClient(object):

    def __init__(self):
        self.connect = ConnectDataBase().get_instance()

    def get_Client(self, client: Client):
        cursor = self.connect.cursor()
        cursor.execute(SQLClient._SELECT_BY_NAME.format(SQLClient._TABLE_NAME, client.name))
        client_verified = cursor.fetchone()
        cursor.close()
        return client_verified
    
    def get_all(self) -> list[dict[str, any]]:
        cursor = self.connect.cursor()
        sql = SQLClient._SELECT
        cursor.execute(sql)
        all_client = cursor.fetchall()
        clients_list = []
        columns = [descricao[0] for descricao in cursor.description ]
        
        for client_find in all_client:
            client_json = dict(zip(columns, client_find))
            client = Client(**client_json)
            clients_list.append(client.get_json())
        cursor.close()
        return clients_list

    def get_Client_by_id(self, id):
        cursor = self.connect.cursor()
        cursor.execute(SQLClient._SELECT_BY_ID.format(SQLClient._TABLE_NAME, id))
        client_verified = cursor.fetchone()
        cursor.close()
        return client_verified
        