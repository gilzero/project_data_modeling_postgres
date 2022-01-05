import psycopg2

from datetime import datetime
from prettytable import PrettyTable

server = '127.0.0.1'
port = '5432'
db = 'pydb'
username = 'newuser'
password = 'password'

print('Connecting to PostgreSQL')

cnx = psycopg2.connect(user=username, password=password, host=server,
                       database=db, port=port)

print('connected')


