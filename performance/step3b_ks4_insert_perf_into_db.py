#!/usr/bin/env python
# coding: utf-8

import mysql.connector
import csv
import glob
import datetime
import time

inp_files = sorted(glob.glob("data/ks4_perf_*.csv"))
print(inp_files)

dbase = "schools"
tables = ["ks4_performance"]

r_urn = r_ks4_pupil_nos = r_ks4_boys = r_ks4_girls = ""
r_progress8 = r_progress8_boys = r_progress8_girls = ""
r_attainment8 = r_attainment8_boys = r_attainment8_girls = r_eng_maths_grade5 = ""
r_ebacc_ent = r_ebacc_avg_score = r_ebacc_avg_boys = r_ebacc_avg_girls = r_ebacc_grade5 = ""
r_progress8_band = r_progress8_desc = r_ac_year = ""

mydb = f_in = columns = values = now = num = ""


def connect_sql():
    global mydb

    mydb = mysql.connector.connect(
        host="localhost",
        user="waiky",
        passwd="Programallday1!",
        database=dbase
    )


def get_columns(table):
    global columns, values, now

    columns = ""
    values = ""

    now = datetime.datetime.now()

    if table == "ks4_performance":
        columns = "(urn, ks4_pupil_nos, ks4_boys, ks4_girls, " \
                  "progress8, progress8_boys, progress8_girls, " \
                  "attainment8, attainment8_boys, attainment8_girls, eng_maths_grade5, " \
                  "ebacc_ent, ebacc_avg_score, ebacc_avg_boys, ebacc_avg_girls, ebacc_grade5, " \
                  "progress8_band, progress8_desc, ac_year, timestamp) VALUES " \
                  "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (r_urn, r_ks4_pupil_nos, r_ks4_boys, r_ks4_girls,
                  r_progress8, r_progress8_boys, r_progress8_girls,
                  r_attainment8, r_attainment8_boys, r_attainment8_girls, r_eng_maths_grade5,
                  r_ebacc_ent, r_ebacc_avg_score, r_ebacc_avg_boys, r_ebacc_avg_girls, r_ebacc_grade5,
                  r_progress8_band, r_progress8_desc, r_ac_year, now)

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
    global r_urn, r_ks4_pupil_nos, r_ks4_boys, r_ks4_girls, \
           r_progress8, r_progress8_boys, r_progress8_girls, \
           r_attainment8, r_attainment8_boys, r_attainment8_girls, r_eng_maths_grade5, \
           r_ebacc_ent, r_ebacc_avg_score, r_ebacc_avg_boys, r_ebacc_avg_girls, r_ebacc_grade5, \
           r_progress8_band, r_progress8_desc, r_ac_year
    global num

    start_time = time.time()

    connect_sql()

    num = 0

    for f in inp_files:
        open_files(f)

        header = True

        for row in csv.reader(f_in):
            r_urn = row[0]
            r_ks4_pupil_nos = row[1]
            r_ks4_boys = row[2]
            r_ks4_girls = row[3]
            r_progress8 = row[4]
            r_progress8_boys = row[5]
            r_progress8_girls = row[6]
            r_attainment8 = row[7]
            r_attainment8_boys = row[8]
            r_attainment8_girls = row[9]
            r_eng_maths_grade5 = row[10]
            r_ebacc_ent = row[11]
            r_ebacc_avg_score = row[12]
            r_ebacc_avg_boys = row[13]
            r_ebacc_avg_girls = row[14]
            r_ebacc_grade5 = row[15]
            r_progress8_band = row[16]
            r_progress8_desc = row[17]
            r_ac_year = row[18]

            if header:
                header = False
                continue

            num += 1
            print(num, ">>>", r_urn, r_ac_year)
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
