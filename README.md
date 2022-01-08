# project_data_modeling_postgres

db working on local version macos

install with homebrew

https://formulae.brew.sh/formula/postgresql

brew services start postgresql



pdadmin 4 macos client gui of db. like phpmyadmin

created used pydb. newuser/password


ref:

https://www.sqlshack.com/setting-up-a-postgresql-database-on-mac/?utm_source=pocket_mylist


bash: 

$psql postgres


CREATE ROLE student WITH LOGIN PASSWORD 'student';

ALTER ROLE student CREATEDB;





if session in use, quick way to resolve:
make sure disconnect pgadmin connection,
via pgadmin, right click a db to disconnect

psycopg2.errors.ObjectInUse: database "sparkifydb" is being accessed by other users
DETAIL:  There is 1 other session using the database.

$ brew services restart postgresql






### libraries

pip install ipython-sql


