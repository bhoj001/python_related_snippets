"""
purpose: To learn about database programming with sqlite3 and python
date: 2020/July/24th
author:Bhoj bahadur karki
Motivation: To be able to build my own custom ORM with python in near future.
Quote: Those who believe can, will do it.
"""

import sqlite3


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

# Lets have a connection
print("[x] connecting to databse company.db...")
connection = sqlite3.connect("company.db") # this will create database if it does not exist.
# create table

cursor =  connection.cursor()

# drop table if exist
sql_cmd = """DROP TABLE employee"""
cursor.execute(sql_cmd)
# Note: default CURRENT_TIMESTAMP will add default value to the data
print("[x] creating table....")
sql_command = """
CREATE TABLE employee ( 
staff_number INTEGER PRIMARY KEY AUTOINCREMENT, 
first_name VARCHAR(20), 
last_name VARCHAR(30), 
gender CHAR(1), 
joining DATE default CURRENT_TIMESTAMP NOT NULL,
birth_date DATE);"""

cursor.execute(sql_command)

print("[x] inserting data....")
# insert data
sql_insert = """INSERT INTO employee ( first_name, last_name, gender, birth_date)
    VALUES ( "Bhoj", "Karki", "m", "1993-2-1");"""
cursor.execute(sql_insert)

sql_command = """INSERT INTO employee ( first_name, last_name, gender, birth_date)
    VALUES ( "Yogesh", "Silwal", "m", "1993-1-1");"""
cursor.execute(sql_command)

sql_command = """INSERT INTO employee ( first_name, last_name, gender, birth_date)
    VALUES ( "hari", "Silwal", "m", "1993-1-1");"""
cursor.execute(sql_command)

sql_command = """INSERT INTO employee ( first_name, last_name, gender, birth_date)
    VALUES ( "hari2", "Silwal", "m", "1993-1-1");"""
cursor.execute(sql_command)

sql_command = """INSERT INTO employee ( first_name, last_name, gender, birth_date)
    VALUES ( "hari3", "Silwal", "m", "1993-1-1");"""
cursor.execute(sql_command)
# Note: don't forget to commit if you want to save data
connection.commit()

print('[x] deleting data....')
# delete data
sql_delete ="DELETE FROM employee where staff_number=5"
cursor.execute(sql_delete)

# Note: don't forget to commit if you want to save data
connection.commit()

print('[x] selecting data....')
# select data and print to console
sql_select = "Select * from employee"
data = cursor.execute(sql_select)
print("[x] select using cursor.execute()....")
for item in data:
    print(item)

# updating data
print("[x] updating data...")
sql_update = "UPDATE employee SET first_name='monika', last_name='jordan',gender='f',joining= CURRENT_TIMESTAMP where staff_number=3"
cursor.execute(sql_update)
# print(dir(cursor))
# select all
# note before doing fetchall we need to do cursor.execute()
cursor.execute("SELECT * FROM employee")
result = cursor.fetchall()
print("[x] select using fetchall()....")
for d in result:
    print(d)

print('[x] select using fetchone()....')
# do cursor.execute if you want to get data everytime
cursor.execute("SELECT * FROM employee")
fetch_one_result = cursor.fetchone()
print(fetch_one_result)



print("[x] closing connection....")
connection.close()