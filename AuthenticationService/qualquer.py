from user.sql import SQLUser
from user.modelo import User

user = User("Chico", '123')
string = SQLUser._SELECT_BY_NAME.format(SQLUser._TABLE_NAME ,user.name, user.password)
print(string)
