
from connect import ConnectDataBase
from user.sql import SQLUser
from .modelo import User


class DAOUser(object):

    def __init__(self):
        self.connect = ConnectDataBase().get_instance()

    def get_user(self, user: User):
        cursor = self.connect.cursor()
        cursor.execute(SQLUser._SELECT_BY_NAME.format(SQLUser._TABLE_NAME, user.name))
        user_verified = cursor.fetchone()
        cursor.close()
        return user_verified
