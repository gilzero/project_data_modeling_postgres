# DROP TABLES

songplay_table_drop = ""
user_table_drop = ""
song_table_drop = ""
artist_table_drop = ""
time_table_drop = ""

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS 
""")

user_table_create = ("""
DROP TABLE IF EXISTS public.users;

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
DROP TABLE IF EXISTS public.songs;

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
DROP TABLE IF EXISTS public.artists;

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
DROP TABLE IF EXISTS public.time;

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
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")

time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create,
                        time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
