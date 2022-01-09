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
    t = pd.to_datetime(df['ts'], unit='ms')

    # start_time, hour, day, week, month, year, weekday
    time_df = pd.DataFrame({
        'ts': t,
        'hour': t.dt.hour,
        'day': t.dt.day,
        'week': t.dt.isocalendar().week,
        'month': t.dt.month,
        'year': t.dt.year,
        'weekday': t.dt.weekday

    })


    # insert time records
    for _, row in time_df.iterrows():
        cur.execute(time_table_insert, tuple(row))

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

        start_time = pd.to_datetime(row.ts, unit='ms')  # typecast to timestamp
        user_id = row.userId
        level = row.level
        song_title = row.song
        artist_name = row.artist
        session_id = row.sessionId
        location = row.location
        user_agent = row.userAgent
        duration = row.length

        # parameters data from select song id and artist id
        params = (song_title, artist_name, duration)

        # get songid and artistid from song and artist tables
        cur.execute(song_select, params)
        results = cur.fetchone()
        # print(f"results: {results}")

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
