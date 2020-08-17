"""
purpose: To learn about database programming with mysql and python
date: 2020/July/24th
author:Bhoj bahadur karki
Motivation: To be able to build my own custom ORM with python in near future.
Quote: Those who believe can, will do it.
Tutorial link: https://www.python-course.eu/sql_python.php
"""

import MySQLdb


def connect_to_database(database_name):
    pass


def disconnect_to_database(database_name):
    pass


def select_data(table_name="", columns=[]):
    pass


def insert_data(table_name="", columns=[], values=[]):
    pass


def update_data(table_name="", columns=[], values=[], id=0):
    pass


def delete_data(table_name="", id=0):
    pass

"""
Note:
point1: 

for mysql we need to create database ourself it will not create one for us automaticall. If we 
provide non-existing database name it will throw an error saying unknown database x


point 2:

Also,
we need to have user and password to login to the database.
In this tutorial I open up xampp and used previously existing user root with password "" (empty)
and database is test_bbk_db
3. we need to have mysql server started from xampp to fetch data using this client.
If the server is stopped, it wont be able to connect and will through error.


In windows mysql service is not by default running in background unlike in linux, we need to start the server
then do: 
import the MySQLdb modul
Open a connection to the SQL server
Sending and receiving commands
Closing the connection to SQL

In linux when we install mysql we start the mysql-server in the background, and thus use client to pull data

"""

# Lets have a connection
print("[x] connecting to databse company_mysql...")
connection = MySQLdb.connect(
    host="localhost",
    user="root",
    password="",
    db="test_bbk_db"
)
# create table

cursor =  connection.cursor()
cursor.execute("SELECT VERSION()")
row = cursor.fetchone()
print("version = ",row[0])

# select all
# note before doing fetchall we need to do cursor.execute()
cursor.execute("SELECT * FROM inventory")
result = cursor.fetchall()
print("[x] select using fetchall()....")
for d in result:
    print(d)


# # drop database
# # cursor.execute("DROP DATABASE company.db")
cursor.close()
print("[x] closing connection....")
connection.close()