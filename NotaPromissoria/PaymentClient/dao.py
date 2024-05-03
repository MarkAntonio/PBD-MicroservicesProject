from .modelo import PaymentClient
from .sql import SQLPaymentClient
from ..connect import ConnectDataBase


class DAOPaymentClient:

    def __init__(self):
        self.connect = ConnectDataBase().get_instance()

    def get_payments(self):
        payments_list = []
        with self.connect.cursor() as cursor:
            cursor.execute(SQLPaymentClient._SELECT_ALL)
            all_payments = cursor.fetchall()
            columns = [descricao[0] for descricao in cursor.description]
            for payment_find in all_payments:
                payment_dict = dict(zip(columns, payment_find))
                payment = PaymentClient(**payment_dict)
                payments_list.append(payment.get_json())
        
        return payments_list
    
    def get_all_payments_by_contract_id(self, contract_id: int):
        payments_list = []
        with self.connect.cursor() as cursor:
            sql = SQLPaymentClient._SELECT_BY_CONTRACT_ID.format(SQLPaymentClient._TABLE_NAME, contract_id)
            
            cursor.execute(sql)
            payment_row = cursor.fetchall()
            for payment_find in payment_row:
                columns = [descricao[0] for descricao in cursor.description]
                payment_dict = dict(zip(columns, payment_find))
                payment = PaymentClient(**payment_dict)
                payments_list.append(payment.get_json())
                
        return payments_list

    def delete_all_by_contract_id(self, contract_id: int):
        cursor = self.connect.cursor()
        sql = SQLPaymentClient._DELETE_ALL.format(SQLPaymentClient._TABLE_NAME, contract_id)
        cursor.execute(sql)
        self.connect.commit()
        