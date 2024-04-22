from .modelo import PaymentContract
from connect import ConnectDataBase
from .sql import SQLPaymentContract


class DAOPaymentContract(object):

    def __init__(self):
        self.connect = ConnectDataBase().get_instance()

    def save(self, payment_contract: PaymentContract) -> int:
        cursor = self.connect.cursor()
        sql = SQLPaymentContract._INSERT
        # (description, value, client_id, number_months, first_payment)
        
        cursor.execute(sql, (payment_contract.description, payment_contract.value, payment_contract.created_at,payment_contract.client_id, payment_contract.number_months, payment_contract.first_payment))
        self.connect.commit()
        id = cursor.fetchone()[0]
        cursor.close()
        return id


    def get_payment_contract(self, paymentContract: PaymentContract):
        return 
    
    def get_all(self):
        return

    def rollback_transaction(self):
	    return self.connect.rollback()