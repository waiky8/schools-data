#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import csv
import datetime
import time

academic_year = "2018"

inp_f = "data/england_ks2final_" + academic_year + ".csv"
out_f = "data/ks2_perf_" + academic_year + ".csv"

header = ["URN", "KS2 Pupils", "KS2 Boys", "KS2 Girls",
          "Reading Progress", "Reading Score", "Reading Meet Std", "Reading Exceed Std",
          "Reading Progress Band", "Reading Progress Desc",
          "Writing Progress", "Writing Score", "Writing Meet Std", "Writing Exceed Std",
          "Writing Progress Band", "Writing Progress Desc",
          "Maths Progress", "Maths Score", "Maths Meet Std", "Maths Exceed Std",
          "Maths Progress Band", "Maths Progress Desc",
          "Overall Meet Std", "Overall Exceed Std",
          "Academic Year"
          ]

f_in = f_out = writer = ""
soup = ""

urn = ks2_pupils = ks2_boys = ks2_girls = ""
reading_progress = reading_score = reading_meet_std = reading_exceed_std = \
    reading_progress_band = reading_progress_band_desc = ""
writing_progress = writing_score = writing_meet_std = writing_exceed_std = \
    writing_progress_band = writing_progress_band_desc = ""
maths_progress = maths_score = maths_meet_std = maths_exceed_std = \
    maths_progress_band = maths_progress_band_desc = ""
overall_meet_std = overall_exceed_std = ""


def get_band_desc(banding):
    if banding == "1":
        return "Well Above Average"
    elif banding == "2":
        return "Above Average"
    elif banding == "3":
        return "Average"
    elif banding == "4":
        return "Below Average"
    elif banding == "5":
        return "Well Below Average"
    else:
        return "NOT AVAIL"


def open_files():
    global f_out, writer

    f_out = open(out_f, "w", newline="")

    writer = csv.writer(f_out)

    write_header()


def write_header():
    writer.writerow(header)


def write_data():
    writer.writerow([urn, ks2_pupils, ks2_boys, ks2_girls,
                     reading_progress, reading_score, reading_meet_std, reading_exceed_std,
                     reading_progress_band, reading_progress_band_desc,
                     writing_progress, writing_score, writing_meet_std, writing_exceed_std,
                     writing_progress_band, writing_progress_band_desc,
                     maths_progress, maths_score, maths_meet_std, maths_exceed_std,
                     maths_progress_band, maths_progress_band_desc,
                     overall_meet_std, overall_exceed_std,
                     academic_year
                     ]
                    )


def close_files():
    f_out.close()


def main():
    global urn, ks2_pupils, ks2_boys, ks2_girls, \
        reading_progress, reading_score, reading_meet_std, reading_exceed_std, \
        reading_progress_band, reading_progress_band_desc, \
        writing_progress, writing_score, writing_meet_std, writing_exceed_std, \
        writing_progress_band, writing_progress_band_desc, \
        maths_progress, maths_score, maths_meet_std, maths_exceed_std, \
        maths_progress_band, maths_progress_band_desc, \
        overall_meet_std, overall_exceed_std

    start_time = time.time()

    open_files()

    data = pd.read_csv(inp_f)

    df = pd.DataFrame(data)
    print(df)

    for row in df.index:
        urn = df["URN"][row]
        ks2_pupils = df["TELIG"][row]
        ks2_boys = df["BELIG"][row]
        ks2_girls = df["GELIG"][row]

        reading_progress = df["READPROG"][row]
        reading_score = df["READ_AVERAGE"][row]
        reading_meet_std = df["PTREAD_EXP"][row]
        reading_exceed_std = df["PTREAD_HIGH"][row]

        if academic_year >= "2018":
            reading_progress_band = df["READPROG_DESCR"][row]
            reading_progress_band_desc = get_band_desc(reading_progress_band)
        else:
            reading_progress_band = reading_progress_band_desc = ""

        writing_progress = df["WRITPROG"][row]
        writing_score = df["GPS_AVERAGE"][row]
        writing_meet_std = df["PTGPS_EXP"][row]
        writing_exceed_std = df["PTGPS_HIGH"][row]

        if academic_year >= "2018":
            writing_progress_band = df["WRITPROG_DESCR"][row]
            writing_progress_band_desc = get_band_desc(writing_progress_band)
        else:
            writing_progress_band = writing_progress_band_desc = ""

        maths_progress = df["MATPROG"][row]
        maths_score = df["MAT_AVERAGE"][row]
        maths_meet_std = df["PTMAT_EXP"][row]
        maths_exceed_std = df["PTMAT_HIGH"][row]

        if academic_year >= "2018":
            maths_progress_band = df["MATPROG_DESCR"][row]
            maths_progress_band_desc = get_band_desc(maths_progress_band)
        else:
            maths_progress_band = maths_progress_band_desc = ""

        overall_meet_std = df["PTRWM_EXP"][row]
        overall_exceed_std = df["PTRWM_HIGH"][row]

        print(urn, ks2_pupils, ks2_boys, ks2_girls,
              reading_progress, reading_score, reading_meet_std, reading_exceed_std,
              reading_progress_band, reading_progress_band_desc,
              writing_progress, writing_score, writing_meet_std, writing_exceed_std,
              writing_progress_band, writing_progress_band_desc,
              maths_progress, maths_score, maths_meet_std, maths_exceed_std,
              maths_progress_band, maths_progress_band_desc,
              overall_meet_std, overall_exceed_std,
              academic_year
              )

        if pd.isna(urn) or urn == " ":
            print("*** SKIP ***")
        else:
            if pd.isna(ks2_pupils) or ks2_pupils in (" ", "SUPP"):
                ks2_pupils = ""
            if pd.isna(ks2_boys) or ks2_boys in (" ", "SUPP"):
                ks2_boys = ""
            if pd.isna(ks2_girls) or ks2_girls in (" ", "SUPP"):
                ks2_girls = ""
            if pd.isna(reading_progress) or reading_progress in (" ", "SUPP"):
                reading_progress = ""
            if pd.isna(reading_score) or reading_score in (" ", "SUPP"):
                reading_score = ""
            if pd.isna(reading_meet_std) or reading_meet_std in (" ", "SUPP"):
                reading_meet_std = ""
            if pd.isna(reading_exceed_std) or reading_exceed_std in (" ", "SUPP"):
                reading_exceed_std = ""
            if pd.isna(reading_progress_band) or reading_progress_band in (" ", "SUPP"):
                reading_progress_band = ""
            if pd.isna(writing_progress) or writing_progress in (" ", "SUPP"):
                writing_progress = ""
            if pd.isna(writing_score) or writing_score in (" ", "SUPP"):
                writing_score = ""
            if pd.isna(writing_meet_std) or writing_meet_std in (" ", "SUPP"):
                writing_meet_std = ""
            if pd.isna(writing_exceed_std) or writing_exceed_std in (" ", "SUPP"):
                writing_exceed_std = ""
            if pd.isna(writing_progress_band) or writing_progress_band in (" ", "SUPP"):
                writing_progress_band = ""
            if pd.isna(maths_progress) or maths_progress in (" ", "SUPP"):
                maths_progress = ""
            if pd.isna(maths_score) or maths_score in (" ", "SUPP"):
                maths_score = ""
            if pd.isna(maths_meet_std) or maths_meet_std in (" ", "SUPP"):
                maths_meet_std = ""
            if pd.isna(maths_exceed_std) or maths_exceed_std in (" ", "SUPP"):
                maths_exceed_std = ""
            if pd.isna(maths_progress_band) or maths_progress_band in (" ", "SUPP"):
                maths_progress_band = ""
            if pd.isna(overall_meet_std) or overall_meet_std in (" ", "SUPP"):
                overall_meet_std = ""
            if pd.isna(overall_exceed_std) or overall_exceed_std in (" ", "SUPP"):
                overall_exceed_std = ""
            write_data()

    close_files()

    elapsed_time = time.time() - start_time
    print("\n", datetime.timedelta(seconds=elapsed_time))


if __name__ == "__main__":
    main()
