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

# Create a stored function first in db

"""
create or replace function get_product_by_id(int)
returns table(id integer, name character(50), price numeric, created date)
language 'sql'
as
$$
select id, name, price, created
from product
where id=$1
$$

"""

# call stored

print("Calling a func")

try:
    cursor = conn.cursor()
    params = (10,)

    cursor.callproc('get_product_by_id', params)

    t = PrettyTable(['ID', 'Name', 'Price', 'Created'])

    for (id, name, price, created) in cursor:
        t.add_row([id, name, format(price, '.2f'), created])

    print(t)
    cursor.close()
except Exception as e:
    print('error in calling stored func')
    print(e)

print('done')


