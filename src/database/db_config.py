import sqlite3
from sqlite3 import Error

def start_db():

    print("Starting process...")

    try:
        with open("src/database/sql_files/create_tables.sql", "r") as create_table:
            sql = create_table.read()
        conn = sqlite3.connect("src/database/db_users.db")
        print("Database connected...")
        cur = conn.cursor()
        cur.executescript(sql)
        conn.commit()
    except Error as e:
        print(e)

    print("Script done...")

def connect_db():
    conn = sqlite3.connect("src/database/db_users.db")
    return conn