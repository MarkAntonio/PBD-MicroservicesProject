class SQLPaymentClient:
    _TABLE_NAME = 'PaymentClient'
    _COL_ID = 'id'
    _COL_CONTRACT_ID = 'contract_id'
    _COL_VALUE = 'value'
    _COL_DATE = 'date'
    _COL_STATUS = 'status'
    _STATUS_TUPLE = ('PENDING', 'LATE',  'PAID', 'PAID_LATE')
    _COL_VALUE_PAID = 'value_paid'
    _COL_DATE_PAID = 'date_paid'
   
    _CREATE_TABLE = f'''CREATE TABLE IF NOT EXISTS {_TABLE_NAME}(
        {_COL_ID} SERIAL PRIMARY KEY,
        {_COL_CONTRACT_ID} INT NOT NULL REFERENCES paymentcontract(id),
        {_COL_VALUE} FLOAT NOT NULL,
        {_COL_DATE} DATE NOT NULL,
        status VARCHAR(9) CHECK (status IN {_STATUS_TUPLE}), 
        {_COL_VALUE_PAID} FLOAT,
        {_COL_DATE_PAID} DATE);'''
    
    _INSERT = f"INSERT INTO {_TABLE_NAME} (contract_id, value, date, status) \
        VALUES (%s, %s, %s, %s) RETURNING ID;"
    _SELECT_ALL = f'SELECT * FROM {_TABLE_NAME};'
    # _UPDATE_STATUS =  f'UPDATE {_TABLE_NAME} SET {_COL_STATUS}=%s,  WHERE ??????'
    _SELECT_BY_CONTRACT_ID = 'SELECT * FROM {} WHERE contract_id={};'
    _DELETE_ALL = 'DELETE FROM {} WHERE contract_id={};'

