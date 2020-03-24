#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import csv
import datetime
import time

academic_year = "2018"

inp_f = "data/england_ks5final_" + academic_year + ".csv"
out_f = "data/ks5_perf_" + academic_year + ".csv"

header = ["URN", "KS5 Pupils",
          "Avg A-level Points", "Avg A-level Grade",
          "Academic Year"
          ]

f_in = f_out = writer = ""
soup = ""

urn = ks5_pupils = avg_a_level_pts = avg_a_level_grade = ""


def open_files():
    global f_out, writer

    f_out = open(out_f, "w", newline="")

    writer = csv.writer(f_out)

    write_header()


def write_header():
    writer.writerow(header)


def write_data():
    writer.writerow([urn, ks5_pupils, avg_a_level_pts, avg_a_level_grade, academic_year])


def close_files():
    f_out.close()


def main():
    global urn, ks5_pupils, avg_a_level_pts, avg_a_level_grade

    start_time = time.time()

    open_files()

    data = pd.read_csv(inp_f)

    df = pd.DataFrame(data)
    print(df)

    for row in df.index:
        urn = df["URN"][row]
        ks5_pupils = df["TPUP1618"][row]

        avg_a_level_pts = df["TALLPPE_ALEV_1618"][row]
        avg_a_level_grade = df["TALLPPEGRD_ALEV_1618"][row]

        print(urn, ks5_pupils, avg_a_level_pts, avg_a_level_grade, academic_year)

        if pd.isna(urn):
            print("*** SKIP ***")
        else:
            if pd.isna(ks5_pupils) or ks5_pupils == "NEW":
                ks5_pupils = ""
            if pd.isna(avg_a_level_pts) or avg_a_level_pts in ("SUPP", "NE"):
                avg_a_level_pts = ""
            if pd.isna(avg_a_level_grade) or avg_a_level_grade in ("SUPP", "NE"):
                avg_a_level_grade = ""
            write_data()

    close_files()

    elapsed_time = time.time() - start_time
    print("\n", datetime.timedelta(seconds=elapsed_time))


if __name__ == "__main__":
    main()
