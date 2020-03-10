#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import bs4 as bs
import urllib.request
import csv
import datetime
import time

inp_f = "data/2017-2018_england_spine.xlsx"
out_f = "data/ofsted_ratings_2018.csv"

header = ["URN", "Rating", "Inspection Date"]

urn = rating = inspect_date = ""
f_in = f_out = writer = ""
soup = ""


def get_rating():
    global rating, inspect_date

    rating = ""
    inspect_date = ""

    school_details = soup.find(class_="timeline")

    for school in school_details.find_all(["time", "strong"]):
        if school.name == "time":
            inspect_date = datetime.datetime.strptime(school.text, "%d %B %Y")
        elif school.name == "strong":
            rating = school.text
            write_data()

    if rating == "":
        inspect_date = ""

    return rating, inspect_date


def open_files():
    global f_in, f_out, writer

    f_in = open(inp_f, "r")
    f_out = open(out_f, "w", newline="")

    writer = csv.writer(f_out)
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
    writer.writerow(header)


def write_data():
    writer.writerow([urn, rating, inspect_date])


def close_files():
    f_in.close()
    f_out.close()


def main():
    global urn, rating, inspect_date

    start_time = time.time()

    open_files()

    num = 0
    data = pd.read_excel(inp_f)

    df = pd.DataFrame(data)

    for row in df.index:
        urn = df["URN"][row]
        ofsted_url = "http://www.ofsted.gov.uk/oxedu_providers/full/(urn)/" + str(urn)

        num += 1

        print(num, ">>>", urn, ofsted_url)

        url_exist = read_school_page(ofsted_url)
        if not url_exist:
            print("Not Found")
            continue

        rating, inspect_date = get_rating()

    close_files()

    elapsed_time = time.time() - start_time
    print("\n", datetime.timedelta(seconds=elapsed_time))


if __name__ == "__main__":
    main()
