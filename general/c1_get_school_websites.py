#!/usr/bin/env python
# coding: utf-8

import bs4 as bs
import urllib.request
import csv
import datetime
import time

inp_f = "data/pri_schools_list.csv"
out_f = "data/pri_school_websites.csv"
level = "Primary"

# inp_f = "data/sec_schools_list.csv"
# out_f = "data/sec_school_websites.csv"
# level = "Secondary"

header = ["Name", "URN", "Website"]

# Reduce spamming website by limiting rows to process (limit) and
# by skipping rows that have already been processed (skip_row)
skip_row = 0
limit = 100000

school_name = urn = school_url = ""
f_in = f_out = writer = ""
soup = ""


def get_school_websites():
    l_school_type2 = ""
    l_religion = ""
    l_local_auth = ""
    l_region = ""
    l_school_url = ""

    school_details = soup.find(class_="module info-block info-block--details")

    if school_details is None:
        return l_school_type2, l_religion, l_local_auth, l_region, l_school_url

    num = 0
    for school in school_details.find_all(["span"]):

        if school.text == "Type":
            num = 1
            continue
        elif school.text == "Religious character":
            num = 2
            continue
        elif school.text == "Local authority":
            num = 3
            continue
        elif school.text == "Region":
            num = 4
            continue
        elif school.text == "Website":
            num = 5
            continue

        if num in range(1, 4):
            pass
        elif num == 5:
            l_school_url = school.text
            break

    return l_school_url


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
    writer.writerow([school_name, urn, school_url])


def close_files():
    f_in.close()
    f_out.close()


def main():
    global school_name, urn, school_url

    start_time = time.time()

    open_files()

    num = 0
    hdr = True
    for row in csv.reader(f_in):
        school_name = row[0]
        # address = row[1]
        urn = row[2]
        # school_type1 = row[3]
        ofsted_url = row[4]

        if hdr:
            hdr = False
            continue

        num += 1

        if num <= skip_row:
            continue

        print(num, ">>>", school_name, ofsted_url)

        url_exist = read_school_page(ofsted_url)
        if not url_exist:
            print("Not Found")
            continue

        school_url = get_school_websites()

        write_data()

        if num == skip_row + limit:
            break

    close_files()

    elapsed_time = time.time() - start_time
    print("\n", datetime.timedelta(seconds=elapsed_time))


if __name__ == "__main__":
    main()
