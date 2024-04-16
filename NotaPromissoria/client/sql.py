class SQLClient:
    _TABLE_NAME = '"client"'
    _COL_ID = 'id'
    _COL_NAME = 'name'
    _COL_DOCUMENT = 'document'

    _CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_TABLE_NAME}'\
                    f'({_COL_ID} SERIAL PRIMARY KEY,'\
                    f'{_COL_NAME} VARCHAR(255) UNIQUE,'\
                    f'{_COL_DOCUMENT} VARCHAR(255) NOT NULL);'
    
    _INSERT = F"INSERT INTO {_TABLE_NAME} (name, document) VALUES (%s, %s) RETURNING ID;"
    _SELECT = F'SELECT * FROM {_TABLE_NAME}'
    _SELECT_BY_ID = 'SELECT * FROM {} WHERE ID={}'
    _SELECT_BY_NAME = "SELECT * FROM {} WHERE NAME='{}'"
    _DELETE = 'DELETE FROM {} WHERE ID={}'
