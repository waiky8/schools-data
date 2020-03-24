#!/usr/bin/env python
# coding: utf-8

import mysql.connector
import csv
import glob
import datetime
import time

inp_files = sorted(glob.glob("data/ks2_perf_*.csv"))
print(inp_files)

dbase = "schools"
tables = ["ks2_performance"]

r_urn = r_ks2_pupil_nos = r_ks2_boys = r_ks2_girls = ""
r_reading_progress = r_reading_score = r_reading_meet_std = r_reading_exceed_std = ""
r_reading_progress_band = r_reading_progress_desc = ""
r_writing_progress = r_writing_score = r_writing_meet_std = r_writing_exceed_std = ""
r_writing_progress_band = r_writing_progress_desc = ""
r_maths_progress = r_maths_score = r_maths_meet_std = r_maths_exceed_std = ""
r_maths_progress_band = r_maths_progress_desc = r_overall_meet_std = r_overall_exceed_std = ""
r_ac_year = ""

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

    if table == "ks2_performance":
        columns = "(urn, ks2_pupil_nos, ks2_boys, ks2_girls, " \
                  "reading_progress, reading_score, reading_meet_std, reading_exceed_std, " \
                  "reading_progress_band, reading_progress_desc, " \
                  "writing_progress, writing_score, writing_meet_std, writing_exceed_std, " \
                  "writing_progress_band, writing_progress_desc, "\
                  "maths_progress, maths_score, maths_meet_std, maths_exceed_std, " \
                  "maths_progress_band, maths_progress_desc, " \
                  "overall_meet_std, overall_exceed_std, " \
                  "ac_year, timestamp) VALUES " \
                  "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
                  "%s, %s, %s, %s, %s, %s)"
        values = (r_urn, r_ks2_pupil_nos, r_ks2_boys, r_ks2_girls,
                  r_reading_progress, r_reading_score, r_reading_meet_std, r_reading_exceed_std,
                  r_reading_progress_band, r_reading_progress_desc,
                  r_writing_progress, r_writing_score, r_writing_meet_std, r_writing_exceed_std,
                  r_writing_progress_band, r_writing_progress_desc,
                  r_maths_progress, r_maths_score, r_maths_meet_std, r_maths_exceed_std,
                  r_maths_progress_band, r_maths_progress_desc,
                  r_overall_meet_std, r_overall_exceed_std,
                  r_ac_year, now)

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
    global r_urn, r_ks2_pupil_nos, r_ks2_boys, r_ks2_girls, \
           r_reading_progress, r_reading_score, r_reading_meet_std, r_reading_exceed_std, \
           r_reading_progress_band, r_reading_progress_desc, \
           r_writing_progress, r_writing_score, r_writing_meet_std, r_writing_exceed_std, \
           r_writing_progress_band, r_writing_progress_desc, \
           r_maths_progress, r_maths_score, r_maths_meet_std, r_maths_exceed_std, \
           r_maths_progress_band, r_maths_progress_desc, \
           r_overall_meet_std, r_overall_exceed_std, \
           r_ac_year
    global num

    start_time = time.time()

    connect_sql()

    num = 0

    for f in inp_files:
        open_files(f)

        header = True

        for row in csv.reader(f_in):
            r_urn = row[0]
            r_ks2_pupil_nos = row[1]
            r_ks2_boys = row[2]
            r_ks2_girls = row[3]
            r_reading_progress = row[4]
            r_reading_score = row[5]
            r_reading_meet_std = row[6]
            r_reading_exceed_std = row[7]
            r_reading_progress_band = row[8]
            r_reading_progress_desc = row[9]
            r_writing_progress = row[10]
            r_writing_score = row[11]
            r_writing_meet_std = row[12]
            r_writing_exceed_std = row[13]
            r_writing_progress_band = row[14]
            r_writing_progress_desc = row[15]
            r_maths_progress = row[16]
            r_maths_score = row[17]
            r_maths_meet_std = row[18]
            r_maths_exceed_std = row[19]
            r_maths_progress_band = row[20]
            r_maths_progress_desc = row[21]
            r_overall_meet_std = row[22]
            r_overall_exceed_std = row[23]
            r_ac_year = row[24]

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
