#!/usr/bin/env python
# coding: utf-8

import bs4 as bs
import urllib.request
import csv
import datetime
import time

inp_f = "data/pri_schools_list.csv"
out_f1 = "data/pri_schools_expenditure.csv"
out_f2 = "data/pri_schools_income.csv"
out_f3 = "data/pri_schools_balance.csv"

# inp_f = "data/sec_schools_list.csv"
# out_f1 = "data/sec_schools_expenditure.csv"
# out_f2 = "data/sec_schools_income.csv"
# out_f3 = "data/sec_schools_balance.csv"

header1 = ["URN", "Expenditure", "Academic Year"]
header2 = ["URN", "Income", "Academic Year"]
header3 = ["URN", "Balance", "Academic Year"]

# Reduce spamming website by limiting rows to process (limit) and
# by skipping rows that have already been processed (skip_row)
skip_row = 0
limit = 100000

f_in = f_out1 = f_out2 = f_out3 = writer1 = writer2 = writer3 = ""
soup = ""

urn = expenditure = income = balance = academic_year = ""


def get_school_expenditure():
    global expenditure, academic_year

    url = "https://schools-financial-benchmarking.service.gov.uk/school/detail?urn=" + \
          urn + "&tab=Expenditure&format=Tables#financialSummary"

    read_school_page(url)

    school_exp = soup.find('div', {'data-group': 'TotalExpenditure'})

    if school_exp is None:
        return None

    i = 0
    for school in school_exp.find_all(['td']):
        i += 1

        if (i % 2) == 0:
            expenditure = school.text.replace("\n", "").strip()
            write_data1()
        else:
            academic_year = school.text


def get_school_income():
    global income, academic_year

    url = "https://schools-financial-benchmarking.service.gov.uk/school/detail?urn=" + \
          urn + "&tab=Income&unit=AbsoluteMoney&format=Tables#financialSummary"

    read_school_page(url)

    school_inc = soup.find('div', {'data-group': 'TotalIncome'})

    if school_inc is None:
        return None

    i = 0
    for school in school_inc.find_all(['td']):
        i += 1

        if (i % 2) == 0:
            income = school.text.replace("\n", "").strip()
            write_data2()
        else:
            academic_year = school.text


def get_school_balance():
    global balance, academic_year

    url = "https://schools-financial-benchmarking.service.gov.uk/school/detail?urn=" + \
          urn + "&tab=Balance&unit=AbsoluteMoney&format=Tables#financialSummary"

    read_school_page(url)

    school_bal = soup.find('div', {'data-group': 'InYearBalance'})

    if school_bal is None:
        return None

    i = 0
    for school in school_bal.find_all(['td']):
        i += 1

        if (i % 2) == 0:
            balance = school.text.replace("\n", "").strip()
            write_data3()
        else:
            academic_year = school.text


def open_files():
    global f_in, f_out1, f_out2, f_out3, writer1, writer2, writer3

    f_in = open(inp_f, "r")
    f_out1 = open(out_f1, "w", newline="")
    f_out2 = open(out_f2, "w", newline="")
    f_out3 = open(out_f3, "w", newline="")

    writer1 = csv.writer(f_out1)
    writer2 = csv.writer(f_out2)
    writer3 = csv.writer(f_out3)
    write_header()


def read_school_page(url):
    global soup
    url_exist = True

    try:
        source = urllib.request.urlopen(url).read()
    except urllib.request.HTTPError as err:
        url_exist = False
        print("HTTP Error:", err.code)
        return url_exist

    soup = bs.BeautifulSoup(source, "lxml")

    return url_exist


def write_header():
    writer1.writerow(header1)
    writer2.writerow(header2)
    writer3.writerow(header3)


def write_data1():
    writer1.writerow([urn, expenditure, academic_year])


def write_data2():
    writer2.writerow([urn, income, academic_year])


def write_data3():
    writer3.writerow([urn, balance, academic_year])


def close_files():
    f_in.close()
    f_out1.close()
    f_out2.close()
    f_out3.close()


def main():
    global urn, expenditure, income, balance, academic_year

    start_time = time.time()

    open_files()

    num = 0
    hdr = True
    for row in csv.reader(f_in):
        school_name = row[0]
        # address = row[1]
        urn = row[2]
        # school_type1 = row[3]
        # ofsted_url = row[4]

        if hdr:
            hdr = False
            continue

        num += 1

        if num <= skip_row:
            continue

        print(num, ">>>", school_name)
        get_school_expenditure()
        get_school_income()
        get_school_balance()

        if num == skip_row + limit:
            break

    close_files()

    elapsed_time = time.time() - start_time
    print("\n", datetime.timedelta(seconds=elapsed_time))


if __name__ == "__main__":
    main()
