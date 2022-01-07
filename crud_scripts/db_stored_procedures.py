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

# Create a stored procedure first in db

"""
create or replace procedure update_product(int, character(50), numeric)
language 'sql'
as
$$
update product
set name=$2, price=$3
where id=$1;
$$;

"""

# call stored procedure parameter

print("Calling stored procedure with parameter")

try:
    cursor = conn.cursor()

    params = (10, 'updated-10', 10.8)

    cursor.execute('call update_product(%s, %s, %s)', params)

    conn.commit()
    cursor.close()
except Exception as e:
    print('error in calling stored procedure')
    print(e)

print('done')


