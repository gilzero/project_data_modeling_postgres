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

print('inserting data')

for i in range(1, 6):
    insert = ("""
        INSERT INTO product (name, price, created) VALUES (%s, %s, %s) RETURNING id;
    """)

    data = ("product " + str(i), i * 0.24, datetime.now())

    cursor.execute(insert, data)

    product_id = cursor.fetchone()[0]

    print(f"inserted with id={product_id}")

conn.commit()
cursor.close()
print('Done')

