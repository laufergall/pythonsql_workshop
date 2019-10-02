"""
This file contains utilities for sqlite data access.
"""

import sqlite3
from typing import List, Tuple


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn


def execute(conn, statement) -> List[Tuple]:
    """ execute a sql statement with try/except
    :param conn: Connection object
    :param statement: a sql statement
    :return: execution result
    """
    if conn is not None:
        cursor = conn.cursor() 
    else:
        print('Could not connect to database!')
    
    try:
        res = cursor.execute(statement)
    except sqlite3.Error as e:
        print(e)
    return res.fetchall()


def insert_user(conn, record):
    """
    Create a new user into the users table
    :param conn:
    :param record:
    :return: user id
    """
    sql = """ INSERT INTO users(first_name,last_name,email,gender)
              VALUES(?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, record)
    return cur.lastrowid


def insert_rental(conn, record):
    """
    Create a new rental into the rentals table
    :param conn:
    :param record:
    :return: purchase id
    """
    sql = ''' INSERT INTO rentals(user_id,rental_timestamp,title,year,cost)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, record)
    return cur.lastrowid

