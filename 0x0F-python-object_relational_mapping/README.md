#####0x0F. Python - Object-relational mapping
##Resources
Read or watch:

Object-relational mappers
mysqlclient/MySQLdb documentation (please don’t pay attention to _mysql)
MySQLdb tutorial
SQLAlchemy tutorial
SQLAlchemy
mysqlclient/MySQLdb
Introduction to SQLAlchemy
Flask SQLAlchemy
10 common stumbling blocks for SQLAlchemy newbies
Python SQLAlchemy Cheatsheet
SQLAlchemy ORM Tutorial for Python Developers (Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)
SQLAlchemy Tutorial
Python Virtual Environments: A primer
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why Python programming is awesome
How to connect to a MySQL database from a Python script
How to SELECT rows in a MySQL table from a Python script
How to INSERT rows in a MySQL table from a Python script
What ORM means
How to map a Python Class to a MySQL table
How to create a Python Virtual Environment

#### This is the documentation we all need.
##This is a documentation for Mysqldb and Orm of a project for github. Mysqldb is a Python interface for MySQL, a relational database management system. Orm is an object-relational mapper, a tool that maps Python objects to database tables and vice versa. The project uses Mysqldb and Orm to create, read, update and delete data from a MySQL database.

#files
1.0. Get all states

This is a documentation for a project that involves creating and querying a states table in a MySQL database using Python. The project consists of two files: 0-select_states.sql and 0-select_states.py.

The file 0-select_states.sql contains the SQL commands to create the database hbtn_0e_0_usa, use it, create the states table, and insert some data into it. The states table has two columns: id and name. The id column is an integer that is auto-incremented and serves as the primary key. The name column is a variable-length string that cannot be null. The SQL commands are executed in the order they appear in the file.

The file 0-select_states.py contains the Python code to connect to the MySQL database using the MySQLdb module and the arguments passed to the script. The arguments are the username, password, and database name. The script then creates a cursor object and executes a query to select all the rows from the states table, ordered by id in ascending order. The script fetches all the results from the query and prints them in a loop. Finally, the script closes the cursor and the connection objects.

