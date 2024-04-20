class PaymentContract():
    def __init__(self, description, value, create_at, number_months, first_payment, client_id=None, id=None):
        self.description = description
        self.value = value
        self.create_at = create_at
        self.number_months = number_months
        self.first_payment = first_payment
        self.client_id = client_id
        self.id = id

    def __str__(self):
        return f'ID: {self.id} - description: {self.description} - value:{self.value}'\
            f'\n- create_at: {self.create_at} - number_months:{self.number_months}'\
            f'\n- first_payment:{self.first_payment} - client_id:{self.client_id} '

    def get_json(self):
        return {
            'id': self.id,
            'description': self.description,
            'value': self.value,
            'create_at': self.create_at,
            'number_months': self.number_months,
            'first_payment': self.first_payment,
            'client_id': self.client_id
        }
