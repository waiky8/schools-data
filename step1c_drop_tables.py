#!/usr/bin/env python
# coding: utf-8

import mysql.connector

dbase = "schools"

# (1 = Yes, 2 = No)
tables = [["school_details", 1], ["ratings", 0],
          ["ks2_performance", 0], ["ks4_performance", 0], ["ks5_performance", 0],
          ["financials", 0], ["websites", 0]
          ]

mydb = ""


def connect_sql():
    global mydb
    
    mydb = mysql.connector.connect(
        host="localhost",
        user="waiky",
        passwd="Programallday1!",
        database=dbase
    )


def drop_table(table):
    mycursor = mydb.cursor()
    mycursor.execute("DROP TABLE IF EXISTS " + table)
    
    print(table + " table dropped!")


def close_connection():
    mydb.close()


def main():
    connect_sql()
    
    for table in tables:
        if table[1] == 1:
            drop_table(table[0])
    
    close_connection()


if __name__ == "__main__":
    main()
