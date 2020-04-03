#!/usr/bin/env python
# coding: utf-8

import mysql.connector
import csv
import glob
import datetime
import time

inp_files = sorted(glob.glob("data/school_details_*.csv"))
print(inp_files)

dbase = "schools"

tables = ["school_details"]

r_urn = r_name = r_street = r_city = r_postcode = r_status = r_rating = r_inspect_date = r_date_opened = \
    r_date_closed = r_school_type = r_primary = r_secondary = r_post16 = r_age_from = r_age_to = r_gender = \
    r_gender_post16 = r_religion = r_other_urn = r_local_auth = r_website = ""

mydb = f_in = columns = values = now = num = ""


def connect_sql():
    global mydb

    mydb = mysql.connector.connect(
        host="localhost",
        user="******",
        passwd="********",
        database=dbase
    )


def get_columns(table):
    global columns, values, now

    columns = ""
    values = ""

    now = datetime.datetime.now()

    if table == "school_details":
        columns = "(urn, name, street, city, postcode, status, rating, inspect_date, date_opened, date_closed, " \
                  "school_type, primary_sch, secondary, post16, age_from, age_to, gender, gender_post16, " \
                  "religion, other_urn, local_auth, website, timestamp) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
                  "%s, %s, %s, %s, %s, %s)"
        values = (r_urn, r_name, r_street, r_city, r_postcode, r_status, r_rating, r_inspect_date, r_date_opened,
                  r_date_closed, r_school_type, r_primary, r_secondary, r_post16, r_age_from, r_age_to, r_gender,
                  r_gender_post16, r_religion, r_other_urn, r_local_auth, r_website, now)

    else:
        print("Unrecognised table: " + table)


def write_table(table):
    mycursor = mydb.cursor()

    sql = "REPLACE INTO " + table + " " + columns
    val = values

    print(sql, val)

    try:
        mycursor.execute(sql, val)
        mydb.commit()
    except Exception as e:
        print(e)


def close_connection():
    mydb.close()


def open_files(f):
    global f_in

    f_in = open(f, "r")


def close_files():
    f_in.close()


def main():
    global r_urn, r_name, r_street, r_city, r_postcode, r_status, r_rating, r_inspect_date, r_date_opened, \
        r_date_closed, r_school_type, r_primary, r_secondary, r_post16, r_age_from, r_age_to, r_gender, \
        r_gender_post16, r_religion, r_other_urn, r_local_auth, r_website
    global num

    start_time = time.time()

    connect_sql()

    num = 0

    for f in inp_files:
        open_files(f)

        header = True

        for row in csv.reader(f_in):
            r_urn = row[0]
            r_name = row[1]
            r_street = row[2]
            r_city = row[3]
            r_postcode = row[4]
            r_status = row[5]
            r_rating = row[6]
            r_inspect_date = row[7]
            r_date_opened = row[8]
            r_date_closed = row[9]
            r_school_type = row[10]
            r_primary = row[11]
            r_secondary = row[12]
            r_post16 = row[13]
            r_age_from = row[14]
            r_age_to = row[15]
            r_gender = row[16]
            r_gender_post16 = row[17]
            r_religion = row[18]
            r_other_urn = row[19].replace(".0", "")
            r_local_auth = row[20]
            r_website = ""        # populated in a separate module

            if header:
                header = False
                continue

            num += 1
            print(num, ">>>", r_urn, r_name)
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
