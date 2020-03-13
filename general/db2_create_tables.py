#!/usr/bin/env python
# coding: utf-8

import mysql.connector

dbase = "schools"

# (1 = Yes, 0 = No)
tables = [["school_details", 1], ["ratings", 1],
          ["ks2_performance", 0], ["ks4_performance", 0], ["ks5_performance", 0],
          ["financials", 0]
          ]

mydb = ""


def get_columns(table):
    columns = ""

    if table == "school_details":
        columns = ("urn VARCHAR(10) NOT NULL, "
                   "name VARCHAR(255) NOT NULL, "
                   "street VARCHAR(255), "
                   "city VARCHAR(255), "
                   "postcode VARCHAR(10), "
                   "status VARCHAR(2), "
                   "rating VARCHAR(30), "
                   "inspect_date VARCHAR(8), "
                   "date_opened VARCHAR(8), "
                   "date_closed VARCHAR(8), "
                   "school_type VARCHAR(50), "
                   "primary_sch VARCHAR(2), "
                   "secondary VARCHAR(2), "
                   "post16 VARCHAR(2), "
                   "age_from INT, "
                   "age_to INT, "
                   "gender VARCHAR(30), "
                   "gender_post16 VARCHAR(30), "
                   "religion VARCHAR(255), "
                   "local_auth VARCHAR(10), "
                   "other_urn VARCHAR(10), "
                   "timestamp TIMESTAMP, "
                   "PRIMARY KEY (urn)"
                   )

    elif table == "ratings":
        columns = ("urn VARCHAR(10) NOT NULL, "
                   "rating VARCHAR(30), "
                   "inspect_date VARCHAR(8), "
                   "timestamp TIMESTAMP, "
                   "PRIMARY KEY (urn, inspect_date)"
                   )

    elif table == "ks2_performance":
        columns = ("urn VARCHAR(10) NOT NULL, "
                   "ks2_pupil_nos VARCHAR(10), "
                   "ks2_boys VARCHAR(10), "
                   "ks2_girls VARCHAR(10), "
                   "reading_progress VARCHAR(10), "
                   "reading_score VARCHAR(10), "
                   "reading_meet_std VARCHAR(10), "
                   "reading_exceed_std VARCHAR(10), "
                   "reading_progress_band VARCHAR(10), "
                   "reading_progress_desc VARCHAR(20), "
                   "writing_progress VARCHAR(10), "
                   "writing_score VARCHAR(10), "
                   "writing_meet_std VARCHAR(10), "
                   "writing_exceed_std VARCHAR(10), "
                   "writing_progress_band VARCHAR(10), "
                   "writing_progress_desc VARCHAR(20), "
                   "maths_progress VARCHAR(10), "
                   "maths_score VARCHAR(10), "
                   "maths_meet_std VARCHAR(10), "
                   "maths_exceed_std VARCHAR(10), "
                   "maths_progress_band VARCHAR(10), "
                   "maths_progress_desc VARCHAR(20), "
                   "overall_meet_std VARCHAR(10), "
                   "overall_exceed_std VARCHAR(10), "                   
                   "ac_year INT(4), "
                   "timestamp TIMESTAMP, "
                   "PRIMARY KEY (urn, ac_year)"
                   )

    elif table == "ks4_performance":
        columns = ("urn VARCHAR(10) NOT NULL, "
                   "ks4_pupil_nos VARCHAR(10), "
                   "ks4_boys VARCHAR(10), "
                   "ks4_girls VARCHAR(10), "
                   "progress8 VARCHAR(10), "
                   "progress8_boys VARCHAR(10), "
                   "progress8_girls VARCHAR(10), "
                   "attainment8 VARCHAR(10), "
                   "attainment8_boys VARCHAR(10), "
                   "attainment8_girls VARCHAR(10), "
                   "eng_maths_grade5 VARCHAR(10), "
                   "ebacc_ent VARCHAR(10), "
                   "ebacc_avg_score VARCHAR(10), "
                   "ebacc_avg_boys VARCHAR(10), "
                   "ebacc_avg_girls VARCHAR(10), "
                   "ebacc_grade5 VARCHAR(10), "
                   "progress8_band VARCHAR(10), "
                   "progress8_desc VARCHAR(20), "
                   "ac_year INT(4), "
                   "timestamp TIMESTAMP, "
                   "PRIMARY KEY (urn, ac_year)"
                   )

    elif table == "ks5_performance":
        columns = ("urn VARCHAR(10) NOT NULL, "
                   "ks5_pupil_nos VARCHAR(10), "
                   "avg_a_level_points VARCHAR(10), "
                   "avg_a_level_grade VARCHAR(10), "
                   "ac_year INT(4), "
                   "timestamp TIMESTAMP, "
                   "PRIMARY KEY (urn, ac_year)"
                   )

    elif table == "financials":
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


def create_table(table, columns):
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE " + table + "(" + columns + ")")

    print(table + " table created!")


def connect_sql():
    global mydb

    mydb = mysql.connector.connect(
        host="localhost",
        user="waiky",
        passwd="Programallday1!",
        database=dbase
    )


def close_connection():
    mydb.close()


def main():
    connect_sql()

    for table in tables:
        if table[1] == 0:
            continue

        columns = get_columns(table[0])
        if columns == '':
            continue
        else:
            create_table(table[0], columns)

    close_connection()


if __name__ == "__main__":
    main()
