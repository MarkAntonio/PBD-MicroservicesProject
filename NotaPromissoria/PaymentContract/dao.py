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

	def get_by_id(self, id: int) -> PaymentContract:
		payment_contract = None
		with self.connect.cursor() as cursor:
			sql = SQLPaymentContract._SELECT_BY_ID\
				.format(SQLPaymentContract._TABLE_NAME, id)

			cursor.execute(sql)
			row = cursor.fetchone()
			if row:
				column_name = [descricao[0] for descricao in cursor.description]
				contract_dict = dict(zip(column_name, row))
				payment_contract = PaymentContract(**contract_dict)
				print(payment_contract)
		return payment_contract

	def update(self, new_contract: PaymentContract):
		cursor = self.connect.cursor()
		sql = SQLPaymentContract._UPDATE
		cursor.execute(sql,
                (new_contract.description, new_contract.value, new_contract.client_id, new_contract.number_months, new_contract.first_payment, str(new_contract.id))
			)
		self.connect.commit()
		cursor.close()

	def get_all(self):
		return

	def rollback_transaction(self):
		return self.connect.rollback()
