# create a SQLite3 database and table


# import the sqlite library
import sqlite3


# create a new database if the databse does not exist
conn = sqlite3.connect("new.db")


# get a cursor object user to execute SQL commands
cursor = conn.cursor()


# create a table
cursor.execute("""CREATE TABLE population
                (city TEXT, state TEXT, population INT)
                """)


# close the database connection
conn.close()
