class User():
    def __init__(self, name, password, id=None):
        self.name = name
        self.password = password
        self.id = id

    def __str__(self):
        return f'ID: {self.id} - name: {self.name} - password:{self.password}'

    def get_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'password': self.password,
        }
