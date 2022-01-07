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


"""

CREATE TABLE public.product
(
    price numeric NOT NULL,
    name character(50) NOT NULL,
    id serial NOT NULL,
    created date NOT NULL,
    PRIMARY KEY (id)
);



"""