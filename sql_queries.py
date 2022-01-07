# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS public.songplays;"
user_table_drop = "DROP TABLE IF EXISTS public.users;"
song_table_drop = "DROP TABLE IF EXISTS public.songs;"
artist_table_drop = "DROP TABLE IF EXISTS public.artists;"
time_table_drop = "DROP TABLE IF EXISTS public.time;"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS public.songplays
(
	songplay_id serial NOT NULL, 
	start_time int, 
	user_id character, 
	level character, 
	song_id character,
	artist_id character,
	session_id int, 
	location character, 
	user_agent character,
	PRIMARY KEY (songplay_id)
	
)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS public.users
(
	user_id character, 
	first_name character, 
	last_name character, 
	gender character, 
	level character
)

""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS public.songs
(
	song_id character, 
	title varchar, 
	artist_id character, 
	year int, 
	duration float
)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS public.artists
(
	artist_id character, 
	name character, 
	location character, 
	latitude float, 
	longitude float
)

""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS public.time
(
	start_time int, 
	hour character, 
	day character, 
	week character, 
	month character,
	year character,
	weekday character
)

""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id;
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s);

""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration) 
VALUES (%s, %s, %s, %s, %s);

""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude) 
VALUES (%s, %s, %s, %s, %s);
""")

time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday) 
VALUES (%s, %s, %s, %s, %s, %s, %s);
""")

# FIND SONGS

song_select = ("""
SELECT * FROM songs
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create,
                        time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
