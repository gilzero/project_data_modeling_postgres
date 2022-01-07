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

print('updating data for a product')

cursor = conn.cursor()

params = ('nike', 99.99, 3) # name price and id

cursor.execute("update product set name=%s, price=%s where id=%s", params)

print(cursor.rowcount, ' product updated')

conn.commit()
cursor.close()
print('Update Done')



