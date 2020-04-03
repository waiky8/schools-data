#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import csv
import datetime
import time

academic_year = "2018"

inp_f = "data/england_cfrfull_" + academic_year + ".xlsx"
out_f = "data/financials_" + academic_year + ".csv"

my_sheet = "Raw CFR Data"

header = ["URN", "Income", "Expenditure", "Balance", "Academic Year"]

f_in = f_out = writer = ""
soup = ""

urn = expenditure = income = balance = ""


def open_files():
    global f_out, writer

    f_out = open(out_f, "w", newline="")

    writer = csv.writer(f_out)

    write_header()


def write_header():
    writer.writerow(header)


def write_data():
    writer.writerow([urn, income, expenditure, balance, academic_year])


def close_files():
    f_out.close()


def main():
    global urn, income, expenditure, balance

    start_time = time.time()

    open_files()

    data = pd.read_excel(inp_f, sheet_name=my_sheet, skiprows=3)

    df = pd.DataFrame(data)
    # print(df)

    for row in df.index:
        urn = df["URN"][row]
        income = round(df["Total Income: I01 to I08, I11 to I15, I18"][row], 2)
        expenditure = round(df["Total Expenditure:\nE01 to E29 and E31 to E32 minus I9, I10, I16 and I17"][row], 2)
        balance = round(income - expenditure, 2)
        print(urn, income, expenditure, balance, academic_year)
        write_data()

    close_files()

    elapsed_time = time.time() - start_time
    print("\n", datetime.timedelta(seconds=elapsed_time))


if __name__ == "__main__":
    main()
