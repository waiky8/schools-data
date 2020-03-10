#!/usr/bin/env python
# coding: utf-8

import mysql.connector
import csv
import glob
import datetime
import time

inp_files = sorted(glob.glob("data/ofsted_ratings_*.csv"))
print(inp_files)

dbase = "schools"

tables = ["ratings"]

r_urn = r_rating = r_inspect_date = ""
columns = values = now = num = ""
mydb = f_in = ""


def connect_sql():
    global mydb

    mydb = mysql.connector.connect(
        host="localhost",
        user="*****",
        passwd="***************",
        database=dbase
    )


def get_columns(table):
    global columns, values, now

    columns = ""
    values = ""

    now = datetime.datetime.now()

    if table == "ratings":
        columns = "(urn, rating, inspect_date, timestamp) VALUES (%s, %s, %s, %s)"
        values = (r_urn, r_rating, r_inspect_date, now)

    else:
        print("Unrecognised table: " + table)


def write_table(table):
    mycursor = mydb.cursor()

    sql = "REPLACE INTO " + table + " " + columns
    val = values
    print(sql, val)

    mycursor.execute(sql, val)
    mydb.commit()


def close_connection():
    mydb.close()


def open_files(f):
    global f_in

    f_in = open(f, "r")


def close_files():
    f_in.close()


def main():
    global r_urn, r_rating, r_inspect_date
    global columns, num

    start_time = time.time()

    connect_sql()

    num = 0

    for f in inp_files:
        open_files(f)

        header = True

        for row in csv.reader(f_in):
            r_urn = row[0]
            r_rating = row[1]
            r_inspect_date = row[2]

            if header:
                header = False
                continue

            num += 1
            print(num, ">>>", r_urn, r_rating, r_inspect_date)
            for table in tables:
                get_columns(table)
                write_table(table)

        close_files()

    close_connection()

    print("\n", num, " records inserted.")

    elapsed_time = time.time() - start_time
    print("\n", datetime.timedelta(seconds=elapsed_time))


if __name__ == "__main__":
    main()
