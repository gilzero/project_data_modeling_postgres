import os
import glob
import psycopg2
import pandas as pd
from datetime import datetime
from sql_queries import *
import numpy as np
from psycopg2.extensions import register_adapter, AsIs

psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)
# psycopg2: can't adapt type 'numpy.int64' error fix:
# https://stackoverflow.com/questions/50626058/psycopg2-cant-adapt-type-numpy-int64

# Suppress SettingWithCopyWarning in Pandas
pd.options.mode.chained_assignment = None


def process_song_file(cur, filepath):
    """
    Process song data file, insert song record and artist record
    :param cur: cursor of connection
    :param filepath: data file path
    :return: n/a
    """
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data = df[['song_id', 'title', 'artist_id', 'year', 'duration']]
    song_data = tuple(song_data.values[0])
    cur.execute(song_table_insert, song_data)

    # # insert artist record
    artist_data = df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']]
    artist_data = tuple(artist_data.values[0])
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    Process event log files
    :param cur: cursor of connection
    :param filepath: data file path
    :return: n/a
    """
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page'] == 'NextSong']

    # convert timestamp column to datetime
    df['datetime'] = df['ts'].apply(lambda x: datetime.utcfromtimestamp(x / 1000))

    # start_time, hour, day, week, month, year, weekday
    df_time = df[['ts', 'datetime']]
    df_time['hour'] = df_time['datetime'].apply(lambda x: x.hour)
    df_time['day'] = df_time['datetime'].apply(lambda x: x.day)
    df_time['week'] = df_time['datetime'].apply(lambda x: x.week)
    df_time['month'] = df_time['datetime'].apply(lambda x: x.month)
    df_time['year'] = df_time['datetime'].apply(lambda x: x.year)
    df_time['weekday'] = df_time['datetime'].apply(lambda x: x.weekday())

    # time data and convert to python native numeric format.
    time_data = df_time[['ts', 'hour', 'day', 'week', 'month', 'year', 'weekday']].values
    time_data = [(int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4]), int(x[5]), int(x[6])) for x in time_data]

    # insert each rows of data
    for row in time_data:
        cur.execute(time_table_insert, row)

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

    # get user data transformed and ready.
    user_data = user_df.drop_duplicates('userId', keep='last')
    user_data = user_data.set_index('userId')
    user_data = user_data.to_records()
    user_data = list(user_data)

    # insert user records
    for row in user_data:
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():

        # songplay_id = None. auto increment by db
        start_time = row.ts
        user_id = row.userId
        level = row.level
        song_title = row.song
        artist_name = row.artist
        session_id = row.sessionId
        location = row.location
        user_agent = row.userAgent

        params = (song_title, artist_name)

        # get songid and artistid from song and artist tables
        cur.execute(song_select, params)
        results = cur.fetchone()

        if results:
            song_id, artist_id = results
        else:
            song_id, artist_id = None, None

        # insert songplay record
        songplay_data = (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    """
    Execution of functions.Process song data and event log data.
    :return: n/a
    """
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
