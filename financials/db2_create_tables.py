#!/usr/bin/env python
# coding: utf-8

import mysql.connector

dbase = "schools"

tables = ["financials"]

mydb = ""


def connect_sql():
    global mydb

    mydb = mysql.connector.connect(
        host="localhost",
        user="waiky",
        passwd="Programallday1!",
        database=dbase
    )


def create_table(table, columns):
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE " + table + "(" + columns + ")")

    print(table + " table created!")


def get_columns(table):
    columns = ""

    if table == "financials":
        columns = ("urn VARCHAR(10) NOT NULL, "
                   "income FLOAT(10,2), "
                   "expenditure FLOAT(10,2), "
                   "balance FLOAT(10,2), "
                   "ac_year INT(4), "
                   "timestamp TIMESTAMP, "
                   "PRIMARY KEY (urn, ac_year)"
                   )

    else:
        print("Unrecognised table: " + table)

    return columns


def close_connection():
    mydb.close()


def main():
    connect_sql()

    for table in tables:
        columns = get_columns(table)
        if columns == '':
            continue
        else:
            create_table(table, columns)

    close_connection()


if __name__ == "__main__":
    main()
