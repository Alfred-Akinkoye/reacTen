#DATABASE LOGIC
import sqlite3
from sqlite3 import Error
global user_name
user_name = "Things"
###CREATING ITEMS###
#creating the connection to the sql Database
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect("testDB.db")
        return conn
    except Error as e:
        print(e)

    return conn
#creating history table
def create_history_table(conn):
    Table_string = """ CREATE TABLE HISTORY (
                                        Username text NOT NULL,
                                        GameNO integer NOT NULL,
                                        Result text NOT NULL,
                                        GameMode integer NOT NULL,
                                        Score integer NOT NULL
                                    ); """
    try:
        cursor = conn.cursor()
        cursor.execute(Table_string)
    except Error as e:
        print(e)

#Creating match tables
def create_match_table(conn, id):
    text = """ (
                        ShotNO integer NOT NULL,
                        TargetForce integer NOT NULL,
                        ShooterSpeed integer NOT NULL,
                        HITorMISS integer NOT NULL,
                        User text NOT NULL
                    ); """
    Table_string = """ CREATE TABLE Match_""" + str(id) + text
    try:
        cursor = conn.cursor()
        cursor.execute(Table_string)
    except Error as e:
        print(e)

#Creating user Table
def create_userdata_table(conn):
    Table_string = """ CREATE TABLE USERS (
                                        username text NOT NULL,
                                        password text NOT NULL
                                    ); """
    try:
        cursor = conn.cursor()
        cursor.execute(Table_string)
    except Error as e:
        print(e)

###APPENDING ITEMS###
