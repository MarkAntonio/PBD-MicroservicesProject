from .modelo import PaymentContract
from connect import ConnectDataBase


class DAOPaymentContract(object):

    def __init__(self):
        self.connect = ConnectDataBase().get_instance()

    def get_PaymentContract(self, paymentContract: PaymentContract):
        return
    
    def get_all(self):
        return
