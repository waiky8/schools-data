#!/usr/bin/env python
# coding: utf-8

import mysql.connector

dbase = "schools"
mydb = ""


def connect_sql():
    global mydb
    
    mydb = mysql.connector.connect(
        host="localhost",
        user="******",
        passwd="******"
    )


def drop_database(table):
    mycursor = mydb.cursor()
    mycursor.execute("DROP DATABASE " + table)
    
    print(dbase + " database dropped!")


def close_connection():
    mydb.close()


def main():
    connect_sql()
    drop_database(dbase)
    close_connection()


if __name__ == "__main__":
    main()
