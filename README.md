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



### libraries

pip install ipython-sql

