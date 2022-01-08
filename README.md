# Project Description

Project Github address:
https://github.com/gilzero/project_data_modeling_postgres

Data modeling with Postgres and build an ETL pipeline using Python. 
Define fact and dimension tables for a star schema for a analytic focus, 
ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.


### Fact Table
1. songplays - records in log data associated with song plays i.e. records with page NextSong
- (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)

### Dimension Tables
1. users - users in the app
- (user_id, first_name, last_name, gender, level)
2. songs - songs in music database
- (song_id, title, artist_id, year, duration)
3. artists - artists in music database
- (artist_id, name, location, latitude, longitude)
4. time - timestamps of records in songplays broken down into specific units
- (start_time, hour, day, week, month, year, weekday)

---

## File Description

- etl.ipynb (general all-in-one notebook)
- create_tables.py (drop tables if exists and re-create new empty schema tables)
- etl.py (the core ETL script, load, transform and insert data to db)
- sql_queries.py (a helper script holding raw sql for other functional scripts)
- test.ipynb (for testing data reading from postgres)
- /data/... (raw data source directory, json files inside)
- /crud_scripts (connection, crud, stored procedures, stored functions etc snippet)


---

## Libraries
- psycopg2
- ipython-sql
- pandas
- numpy
- PrettyTable
- Jupyter Notebook

---

## How to Run:

under project directory, create and activate virtual env (depends on systems), e.g
```
$ source vene/bin/activate
```

Install libraries mentioned above.

Then, 
1. run create_tables.py
```
$ python create_tables.py 
```

2. run etl.py
```
$ python etl.py
```





---


## Environment

Developed and tested on local MacOS machine. 

Install postgress with homebew.
https://formulae.brew.sh/formula/postgresql

Service Start command:

```
$brew services start postgresql
```

pdadmin 4 for postgres MacOS GUI client.

created used pydb. newuser/password
ref:

https://www.sqlshack.com/setting-up-a-postgresql-database-on-mac/?utm_source=pocket_mylist


bash: 

$psql postgres


```
CREATE ROLE student WITH LOGIN PASSWORD 'student';
ALTER ROLE student CREATEDB;
```



## Resolve connection

When encounter session or connection is being occupied, e.g

psycopg2.errors.ObjectInUse: database "sparkifydb" is being accessed by other users
DETAIL:  There is 1 other session using the database.

Issue a restart of postgres
```
$ brew services restart postgresql
```


make sure disconnect pgadmin connection,
via pgadmin, right click a db to disconnect





