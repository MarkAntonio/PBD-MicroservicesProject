import datetime
class PaymentContract():

    DATE_FORMAT = "%d/%m/%Y"

    def __init__(self, description, value, number_months, first_payment: datetime.date, client_id=None, id=None):
        self.description = description
        self.value = value
        self.created_at = datetime.datetime.now()
        self.number_months = number_months
        self.first_payment = first_payment
        self.client_id = client_id
        self.id = id

    @classmethod
    def str_to_date(cls, str_date) -> datetime.date:
        """ transforma String em um objeto do tipo "date" do módulo "datetime" de acordo com o padrão de formatação pré configurado aqui.

        """
        datetime_obj = datetime.datetime.strptime(str_date, cls.DATE_FORMAT)
        return datetime_obj.date()

    @classmethod
    def date_to_string(cls, date: datetime.date) -> str:
        """ Transforma um objeto "date" do módulo datetime em uma string de acordo com o padrão de formatação pré configurado aqui.
        """
        return date.strftime(cls.DATE_FORMAT)

    def __str__(self):
        return f'ID: {self.id} - description: {self.description} - value:{self.value}'\
            f'\n- create_at: {self.create_at} - number_months:{self.number_months}'\
            f'\n- first_payment:{self.first_payment} - client_id:{self.client_id} '

    def get_json(self):
        return {
            'id': self.id,
            'description': self.description,
            'value': self.value,
            'create_at': self.created_at,
            'number_months': self.number_months,
            'first_payment': self.first_payment,
            'client_id': self.client_id
        }
