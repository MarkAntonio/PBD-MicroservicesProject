from .model import PaymentClient
from .sql import SQLPaymentClient
from PaymentContract.model import PaymentContract
from datetime import datetime, timedelta


class DAOPaymentClient:

    def __init__(self):
        from connect import ConnectDataBase

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
            sql = SQLPaymentClient._SELECT_BY_CONTRACT_ID.format(
                SQLPaymentClient._TABLE_NAME, contract_id)

            cursor.execute(sql)
            payment_row = cursor.fetchall()
            for payment_find in payment_row:
                columns = [descricao[0] for descricao in cursor.description]
                payment_dict = dict(zip(columns, payment_find))
                payment = PaymentClient(**payment_dict)
                payments_list.append(payment.get_json())

        return payments_list

    def get_installment_by_status(self, contract_id: int):
        check_Status = ('LATE', 'PENDING')
        installment = None
    
        with self.connect.cursor() as cursor:
            sql = SQLPaymentClient._SELECT_BY_STATUS
            cursor.execute(sql, (contract_id, check_Status))
            
            installment_by_status = cursor.fetchone()
            if installment_by_status:
                column_name = [descricao[0] for descricao in cursor.description]
                payment_dict = dict(zip(column_name, installment_by_status))
                installment = PaymentClient(**payment_dict)
        
        return installment

    def generate_payment_record(self, paymentContract: PaymentContract):
        # valor das parcelas
        value_payment_record = paymentContract.value / paymentContract.number_months
        datePaymentRecord = paymentContract.first_payment
        cursor = self.connect.cursor()
        sql = SQLPaymentClient._INSERT
        for i in range(paymentContract.number_months):
            # criando os Payment Clients
            #(contract_id, value, date, status)
            cursor.execute(
                sql, (str(paymentContract.id), value_payment_record, datePaymentRecord, 'PENDING'))
            datePaymentRecord += timedelta(days=30)
        self.connect.commit()
        cursor.close()

    def delete_all_by_contract_id(self, contract_id: int):
        cursor = self.connect.cursor()
        sql = SQLPaymentClient._DELETE_ALL.format(
            SQLPaymentClient._TABLE_NAME, contract_id)
        cursor.execute(sql)
        self.connect.commit()

    def pay_installment(self,payment_id: int, status: str, date_paid, value):
        cursor = self.connect.cursor()
        sql = SQLPaymentClient._PAY_INSTALLMENT
        cursor.execute(sql,(date_paid, value, status, payment_id))
        self.connect.commit()
        cursor.close()

