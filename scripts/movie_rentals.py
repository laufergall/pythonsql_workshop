"""
sql exercises with the mock movie rentals data
"""

import json
import os

import pandas as pd
from utils_sqlite import create_connection, execute, insert_user, insert_rental

#%%

file = '../data/sqlite/movie_rentals.db'
conn = create_connection(file)

#%%

statement_01 = """ CREATE TABLE IF NOT EXISTS users (
    id integer PRIMARY KEY,
    first_name text NOT NULL,
    last_name text NOT NULL,
    email text,
    gender text
    ); """

statement_02 = """ CREATE TABLE IF NOT EXISTS rentals (
    id integer PRIMARY KEY,
	user_id integer NOT NULL,
    rental_timestamp text NOT NULL,
    title text,
    year text,
    cost text
    ); """

statement_03 = """ SELECT * FROM users LIMIT 10;"""

#%%

# load data from sources

with open(os.path.join('..', 'data', 'json', 'mock_users.json')) as f:
    mock_users = json.load(f)

#%%

with conn:

    # create table users
    execute(conn, statement_01)

    # create table purchases
    execute(conn, statement_02)

    # insert records into users

    # mock users is a list of dictionaries
    # we need to pass the columns in the same order as in the table definition
    user_ids = []
    for user in mock_users:
        user_tuple = (user['first_name'], user['last_name'], user['email'], user['gender'])
        # user_tuple looks like ('Rodolphe', 'Bernuzzi', 'rbernuzzi2s@sogou.com', 'Male')
        user_id = insert_user(conn, user_tuple)
        user_ids.append(user_id)

    """
    # equivalent to the list comprehension:
    user_ids = [insert_user(conn, (user['first_name'],
                            user['last_name'],
                            user['email'],
                            user['gender'])) for user in mock_users]
    """

query_result = execute(conn, statement_03)

# col names still not set
df = pd.DataFrame(query_result)
print(df)

#%%

#
# Exercise: read 'mock_rentals.csv' and insert records into rentals
# Tip: use the pd.read_csv() and the insert_rental() methods
#

#%%

#
# Exercise:
# Query: which 3 movies provided the largest profit overall and how much was this profit (return only 3 rows)
#

#%%

#
# Exercise:
# Query: how many times was each movie rented
#

#%%

#
# Exercise:
# Query: how many unique movies were rented between 01 August 2015 and 15 February 2016
#

#%%

#
# (Bonus) Exercise:
# Query: Considering 2016 only, how many movies did each user rent and how much did each user spend
#

#%%

#
# (Super Bonus) Exercise:
# Without using sqlite, repeat the exercises before to find out the same information from the data,
# based on pandas dataframes.
# Do you find it easier with sqlite or with pandas?
#

#%%

# We make sure we close the connection when we finish
conn.close()
