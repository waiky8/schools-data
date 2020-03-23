#!/usr/bin/env python
# coding: utf-8

import mysql.connector
import csv
import glob
import datetime
import time

inp_files = sorted(glob.glob("data/*websites.csv"))
print(inp_files)

dbase = "schools"

# tables = ["websites"]
tables = ["school_details"]

r_name = r_urn = r_website = ""
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

    if table == "websites":
        columns = "(urn, website, timestamp) VALUES (%s, %s, %s)"
        values = (r_urn, r_website, now)

    elif table == "school_details":
        columns = "website='" + \
                  r_website + \
                  "', timestamp='" +\
                  str(now) +\
                  "' WHERE urn='" +\
                  r_urn +\
                  "'"

    else:
        print("Unrecognised table: " + table)


def write_table(table):
    mycursor = mydb.cursor()

    if table == "websites":
        sql = "REPLACE INTO websites " + columns
    elif table == "school_details":
        sql = "UPDATE school_details SET " + columns

    val = values
    print(sql, val)

    try:
        mycursor.execute(sql, val)
    except Exception as e:
        print(e)

    mydb.commit()


def close_connection():
    mydb.close()


def open_files(f):
    global f_in

    f_in = open(f, "r")


def close_files():
    f_in.close()


def main():
    global r_name, r_urn, r_website
    global columns, num

    start_time = time.time()

    connect_sql()

    num = 0

    for f in inp_files:
        open_files(f)

        header = True

        for row in csv.reader(f_in):
            r_name = row[0]
            r_urn = row[1]
            r_website = row[2]

            if header:
                header = False
                continue

            num += 1
            print(num, ">>>", r_urn, r_website)
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
