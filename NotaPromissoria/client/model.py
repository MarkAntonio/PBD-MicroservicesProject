class Client():
    def __init__(self, name, document=None, id=None):
        self.name = name
        self.document = document
        self.id = id

    def __str__(self):
        return f'ID: {self.id} - name: {self.name} - document:{self.document}'

    def get_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'document': self.document,
        }
