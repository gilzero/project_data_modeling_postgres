import psycopg2

server = '127.0.0.1'

port = 5432

db = 'pydb'

username = 'newuser'

pwd = 'password'

cnx = psycopg2.connect(user=username,
                       password=pwd,
                       host=server,
                       database=db,
                       port=port)

print('connected')

print(cnx)

cnx.close()