from .modelo import PaymentContract
from connect import ConnectDataBase
from .sql import SQLPaymentContract

class DAOPaymentContract(object):

    def __init__(self):
        self.connect = ConnectDataBase().get_instance()

    def new_payment_contract(self, payment_contract:PaymentContract):
        # cursor = self.connect.cursor()
        sql = SQLPaymentContract._INSERT
        # (description, value, client_id, number_months, first_payment)
        with self.connect.cursor() as cursor:
            cursor.execute(sql, (payment_contract.description, payment_contract.value, payment_contract.client_id, payment_contract.number_months, payment_contract.first_payment))
            self.connect.commit()
        # cursor.close()
        return payment_contract.id


    def get_payment_contract(self, paymentContract: PaymentContract):
        return
    
    def get_all(self):
        return
