import datetime
#from NotaPromissoria.client.dao import DAOClient


class PaymentContract():

    DATE_FORMAT = "%d/%m/%Y"
    DATETIME_FORMAT = "%d/%m/%Y %H:%M:%S"

    def __init__(self, description, value, number_months, first_payment: datetime.date, client_id=None, id=None, created_at=None):
        self.description = description
        self.value = value
        if created_at:
            self.created_at = created_at
        else:
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

    # @classmethod
    # def date_to_string(cls, date: datetime.date) -> str:
    #     """ Transforma um objeto "date" do módulo datetime em uma string de acordo com o padrão de formatação pré configurado aqui.
    #     """
    #     return date.strftime(cls.DATE_FORMAT)

    # @classmethod
    # def datetime_to_string(cls, datetime: datetime.datetime):
    #     return datetime.strftime(cls.DATETIME_FORMAT)
    
    def get_str_created_at(self):
        """Retorna o atributo self.created_at do tipo datetime como uma String formatada no padrão %d/%m/%Y %H:%M:%S. 
        ex: 29/04/2024 15:05:58
        """
        return self.created_at.strftime(self.DATETIME_FORMAT)
    
    def get_str_first_payment(self) -> str:
        """Retorna o atributo self.first_payment do tipo date como uma String formatada no padrão %d/%m/%Y. 
        ex: 29/04/2024
        """
        return self.first_payment.strftime(self.DATE_FORMAT)

    def get_json(self):
        return {
            'id': self.id,
            'description': self.description,
            'value': self.value,
            'created_at': self.get_str_created_at(),
            'number_months': self.number_months,
            'first_payment': self.get_str_first_payment(),
            'client_id': self.client_id
        }

    def __str__(self):
        return f'id: {self.id} \ndescription: {self.description} \nvalue:{self.value}'\
           f'\ncreate_at: {self.created_at} \nnumber_months:{self.number_months}'\
           f'\nfirst_payment:{self.first_payment}'

    