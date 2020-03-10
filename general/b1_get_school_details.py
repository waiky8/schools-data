#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import csv
import datetime as dt
from datetime import datetime
import time

inp_f = "data/2017-2018_england_spine.xlsx"
out_f = "data/school_details_2018.csv"

header = ["URN", "Name", "Street", "City", "Postcode", "Status", "Date Opened", "Date Closed", "Type",
          "Primary", "Secondary", "Post 16", "Age From", "Age To", "Gender", "Gender Post 16", "Religion",
          "Other URN", "Local Authority"]

urn = name = street = city = postcode = status = date_opened = date_closed = school_type = ""
primary = secondary = post16 = age_from = age_to = gender = gender_post16 = religion = other_urn = local_auth = ""

f_in = f_out = writer = ""
soup = ""


def open_files():
    global f_in, f_out, writer

    f_in = open(inp_f, "r")
    f_out = open(out_f, "w", newline="")

    writer = csv.writer(f_out)
    write_header()


def write_header():
    writer.writerow(header)


def write_data():
    writer.writerow([urn, name, street, city, postcode, status, date_opened, date_closed, school_type,
                     primary, secondary, post16, age_from, age_to, gender, gender_post16, religion,
                     other_urn, local_auth])


def close_files():
    f_in.close()
    f_out.close()


def main():
    global urn, name, street, city, postcode, status, date_opened, date_closed, school_type, \
           primary, secondary, post16, age_from, age_to, gender, gender_post16, religion, other_urn, local_auth

    start_time = time.time()

    open_files()

    num = 0
    data = pd.read_excel(inp_f)

    df = pd.DataFrame(data)

    for row in df.index:
        urn = df["URN"][row]
        name = df["SCHNAME"][row]
        street = df["STREET"][row]
        city = df["TOWN"][row]
        postcode = df["POSTCODE"][row]
        status = df["ICLOSE"][row]                      # (1 = Open, 2 = Closed, 3 = Pending closure)
        date_opened = df["OPENDATE"][row]               # (if opened on or after 12th September 2015)
        date_closed = df["CLOSEDATE"][row]              # (if closed on or after 12th September 2015)
        school_type = df["MINORGROUP"][row]
        primary = df["ISPRIMARY"][row]                  # (0 = No, 1 = Yes)
        secondary = df["ISSECONDARY"][row]              # (0 = No, 1 = Yes)
        post16 = df["ISPOST16"][row]                    # (0 = No, 1 = Yes)
        age_from = df["AGEL"][row]
        age_to = df["AGEH"][row]
        gender = df["GENDER"][row]
        gender_post16 = df["SIXFGENDER"][row]
        religion = df["RELDENOM"][row]
        other_urn = df["OTHERURN"][row]                 # (if the school has opened or converted since 11th Sept 2015)
        local_auth = df["LA"][row]

        if pd.isna(date_opened):
            date_opened = ""
        else:
            date_opened = datetime.strftime(date_opened, "%Y%m%d")

        if pd.isna(date_closed):
            date_closed = ""
        else:
            date_closed = datetime.strftime(date_closed, "%Y%m%d")

        if pd.isna(other_urn):
            other_urn = ""

        num += 1

        print(num, ">>>", urn, name)

        write_data()

    close_files()

    elapsed_time = time.time() - start_time
    print("\n", dt.timedelta(seconds=elapsed_time))


if __name__ == "__main__":
    main()
