import sqlite3
import os

def setup_db_Schema_with_sql_file(cursor, conn):
    #Get the path to this file
    setup_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sql_file_path = os.path.join(setup_dir, "SQL_SCHEMA.sql")

    #Read the SQL schema file
    with open(sql_file_path, "r") as file:
        sql_script = file.read()

    cursor.executescript(sql_script)
    conn.commit()

def init_db(database_path):
    #Create a empty db if it does not already exist, or just connect to it
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    setup_db_Schema_with_sql_file(cursor, conn)
    conn.close()

setup_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(setup_dir, "Database.db")

init_db(db_path)