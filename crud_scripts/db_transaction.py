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

# insert 9 data, call commit to store, otherwise rollback()

cursor = conn.cursor()

try:
    for i in range(1,10):
        name = 'product ' + str(i)
        price = 1.2 * i


        # demo error in purpose
        if i == 5:
            price = 'hello i am error for purpose'



        insert = "insert into product (name, price, created) values (%s, %s, %s) returning id;"

        params = (name, price, datetime.now())

        cursor.execute(insert, params)

        product_id = cursor.fetchone()[0]

        print('inserted with id=', product_id)

    conn.commit()
except Exception as e:
    conn.rollback()
    print('Error in inserting data')
    print(e)

cursor.close()
conn.close()
print('Done')


