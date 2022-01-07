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


cursor = conn.cursor()

cursor.execute("select id, name, price, created from product")

t = PrettyTable(['ID', 'Product', 'Price', 'Created'])

for (id, name, price, created) in cursor:
    t.add_row([id, name, price, created])

print(t)
cursor.close()
print('done')

