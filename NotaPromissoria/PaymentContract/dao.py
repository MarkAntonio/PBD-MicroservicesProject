from .model import PaymentContract
from .sql import SQLPaymentContract


class DAOPaymentContract(object):

	def __init__(self):
		from connect import ConnectDataBase

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

	def get_all(self):
		with self.connect.cursor() as cursor:
			sql = SQLPaymentContract._JOIN_CLIENT
			cursor.execute(sql)
			all_contract = cursor.fetchall()
			contracts_list = []
			if all_contract:
				columns = [descricao[0] for descricao in cursor.description ]

				for contract_find in all_contract:
					contract_dict = dict(zip(columns, contract_find))
					contract_dict['client'] = {'client_id': contract_dict['client_id'], 'name': contract_dict['name']}
					del contract_dict['client_id']
					del contract_dict['name']
					contract_dict['first_payment'] = PaymentContract.date_to_string(contract_dict['first_payment'])
					contract_dict['created_at'] = PaymentContract.datetime_to_string(contract_dict['created_at'])
					contracts_list.append(contract_dict)
		return contracts_list

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
		return payment_contract

	def update(self, new_contract: PaymentContract):
		cursor = self.connect.cursor()
		sql = SQLPaymentContract._UPDATE
		cursor.execute(sql,
                (new_contract.description, new_contract.value, str(new_contract.client_id), new_contract.number_months, new_contract.first_payment, str(new_contract.id))
			)
		self.connect.commit()
		cursor.close()

	def update_description(self, description: str, id: int):
		cursor = self.connect.cursor()
		sql = SQLPaymentContract._UPDATE_DESCRIPTION
		cursor.execute(sql, (description, str(id)))
		self.connect.commit()
		cursor.close()

	def rollback_transaction(self):
		return self.connect.rollback()
