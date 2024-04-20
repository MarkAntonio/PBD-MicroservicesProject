class SQLPaymentContract:
    _TABLE_NAME = 'PaymentContract'
    _COL_ID = 'id'
    _COL_DESCRIPTION = 'description'
    _COL_VALUE = 'value'
    _COL_CLIENT_ID = 'client_id'
    _COL_NUMBER_MONTHS = 'number_months'
    _COL_FIRST_PAYMENT = 'first_payment'

    _CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_TABLE_NAME}'\
                    f'({_COL_ID} SERIAL PRIMARY KEY,'\
                    f'{_COL_DESCRIPTION} VARCHAR(255) NOT NULL,'\
                    f'{_COL_VALUE} FLOAT NOT NULL,'\
                    f'{_COL_CLIENT_ID} INT REFERENCES client(id) NOT NULL,'\
                    f'{_COL_NUMBER_MONTHS} INT NOT NULL,'\
                    f'{_COL_FIRST_PAYMENT} DATE NOT NULL);'
    
    _INSERT = F"INSERT INTO {_TABLE_NAME} (description, value, client_id, number_months, first_payment) VALUES (%s, %s, %s, %s, %s) RETURNING ID;"
    _SELECT = F'SELECT * FROM {_TABLE_NAME}'
    _SELECT_BY_ID = 'SELECT * FROM {} WHERE ID={}'
    _SELECT_BY_NAME = "SELECT * FROM {} WHERE NAME='{}'"
    _DELETE = 'DELETE FROM {} WHERE ID={}'
