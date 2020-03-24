#!/usr/bin/env python
# coding: utf-8

import bs4 as bs
import urllib.request
import csv
import datetime
import time

# inp_f = 'data/primary_urls.txt'
# out_f = 'data/pri_schools_list.csv'

inp_f = "data/secondary_urls.txt"
out_f = "data/sec_schools_list.csv"

header = ["Name", "Address", "URN", "Type", "URL"]

school_name = address = urn = school_type = school_url = ""
f_in = f_out = writer = ""
school_list = []
num = 0


def reset_variables():
    global school_name, address, urn, school_type, school_url
    
    school_name = ""
    address = ""
    urn = ""
    school_type = ""
    school_url = ""


def extract_data():
    global school_name, address, urn, school_type, school_url, num
    
    reset_variables()
    num = 0
    
    for school in school_list.find_all(["a", "address", "li"]):
        if school.name == 'a':
            if num != 0:
                write_data()
                reset_variables()
            school_name = school.text
            school_url = "https://reports.ofsted.gov.uk/" + school["href"]
            num += 1
        elif school.name == "address":
            address = school.text
        elif school.name == "li":
            if school.text.startswith("URN"):
                urn = school.text.replace("URN: ", "")
            elif school.text.startswith("Type"):
                school_type = school.text.replace("Type: ", "")
        else:
            print("--Unexpected Error--")

    write_data()


def open_files():
    global f_in, f_out, writer
    
    f_in = open(inp_f, "r")
    f_out = open(out_f, "w", newline="")

    writer = csv.writer(f_out)
    write_header()


def read_school_page(url):
    global school_list
    
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, "lxml")
    
    school_list = soup.find(class_="results-list list-unstyled")


def write_header():
    writer.writerow(header)


def write_data():
    writer.writerow([school_name, address, urn, school_type, school_url])
    print(num, ">>>", school_name, address, urn, school_type, school_url)


def close_files():
    f_in.close()
    f_out.close()


def main():
    global school_list
    
    start_time = time.time()
    
    open_files()
    
    for schools in f_in:
        print(schools)    
        read_school_page(schools)
        extract_data()
    
    close_files()
    
    elapsed_time = time.time() - start_time
    print("\n", datetime.timedelta(seconds=elapsed_time))


if __name__ == "__main__":
    main()
