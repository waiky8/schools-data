#!/usr/bin/env python
# coding: utf-8

import mysql.connector

dbase = "schools"
mydb = ""


def connect_sql():
    global mydb
    
    mydb = mysql.connector.connect(
        host="localhost",
        user="waiky",
        passwd="Programallday1!"
    )


def create_database():
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE " + dbase)
    
    print(dbase + " database created!")


def close_connection():
    mydb.close()


def main():
    connect_sql()
    create_database()
    close_connection()


if __name__ == "__main__":
    main()
