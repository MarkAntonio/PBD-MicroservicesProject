import datetime


class PaymentClient:

    DATE_FORMAT = "%d/%m/%Y"
    DATETIME_FORMAT = "%d/%m/%Y %H:%M:%S"

    def __init__(self, contract_id: int, value: float, date: datetime.date, status: str, value_paid: float = None, date_paid: datetime.date = None, id: int = None):
        self.contract_id = contract_id
        self.value = value
        self.date = date
        self.status = status
        self.value_paid = value_paid
        self.date_paid = date_paid
        self.id = id
    
    def get_str_date(self):
        """Retorna o atributo self.created_at do tipo datetime como uma String formatada no padrão %d/%m/%Y %H:%M:%S. 
        ex: 29/04/2024 15:05:58
        """
        return self.date.strftime(self.DATETIME_FORMAT)
    
    def get_str_date_paid(self) -> str:
        """Retorna o atributo self.first_payment do tipo date como uma String formatada no padrão %d/%m/%Y. 
        ex: 29/04/2024
        """
        if self.date_paid is not None:
            return self.date_paid.strftime(self.DATE_FORMAT)
        return None

    def get_json(self):
        return {
            'id': self.id,
            'value': self.value,
            'date': self.get_str_date(),
            'status': self.status,
            'value_paid': self.value_paid,
            'date_paid': self.get_str_date_paid()
        }
    
    def __str__(self):
        return f'id: {self.id}, contract_id: {self.contract_id}, value: {self.value}, date: {self.get_str_date()}, status: {self.status}, value_paid: {self.value_paid}, date_paid: {self.get_str_date_paid()}'
    
