import psycopg2
from datetime import datetime
from prettytable import PrettyTable

server = '127.0.0.1'
port = '5432'
db = 'pydb'
username = 'newuser'
password = 'password'

print('Connecting to PostgreSQL')

conn = psycopg2.connect(user=username, password=password, host=server,
                       database=db, port=port)

print('connected')

print('Deleting data for a product')

cursor = conn.cursor()

params = (5,)

cursor.execute("delete from product where id=%s", params)

print(cursor.rowcount, ' product(s) deleted')

conn.commit()

cursor.close()
print('Delete Done')



