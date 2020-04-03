#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import csv
import datetime
import time

academic_year = "2019"

# inp_f = "data/england_ks4final_" + academic_year + ".csv"
# out_f = "data/ks4_perf_" + academic_year + ".csv"
inp_f = "data/england_ks4revised_" + academic_year + ".csv"
out_f = "data/ks4_revised_perf_" + academic_year + ".csv"

header = ["URN", "KS4 Pupils", "KS4 Boys", "KS4 Girls", "Progress 8", "Progress 8 Boys", "Progress 8 Girls",
          "Attainment 8", "Attainment 8 Boys", "Attainment 8 Girls", "Eng Maths Grade 5",
          "Entering EBacc", "EBacc Avg Score", "EBacc Avg Boys", "EBacc Avg Girls", "EBacc Grade 5",
          "Progress 8 Band", "P8 Desc", "Academic Year"
          ]

f_in = f_out = writer = ""
soup = ""

urn = ks4_pupils = ks4_boys = ks4_girls = progress8 = progress8_boys = progress8_girls = ""
attainment8 = attainment8_boys = attainment8_girls = eng_maths_grade5 = ""
ebacc_ent = ebacc_avg_score = ebacc_avg_boys = ebacc_avg_girls = ebacc_grade5 = ""
progress8_band = progress8_desc = ""


def get_progress8_band_desc(banding):
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
        return ""


def open_files():
    global f_out, writer

    f_out = open(out_f, "w", newline="")

    writer = csv.writer(f_out)

    write_header()


def write_header():
    writer.writerow(header)


def write_data():
    writer.writerow([urn, ks4_pupils, ks4_boys, ks4_girls, progress8, progress8_boys, progress8_girls,
                     attainment8, attainment8_boys, attainment8_girls, eng_maths_grade5,
                     ebacc_ent, ebacc_avg_score, ebacc_avg_boys, ebacc_avg_girls, ebacc_grade5,
                     progress8_band, progress8_desc, academic_year
                     ]
                    )


def close_files():
    f_out.close()


def main():
    global urn, ks4_pupils, ks4_boys, ks4_girls, progress8, progress8_boys, progress8_girls, \
        attainment8, attainment8_boys, attainment8_girls, eng_maths_grade5, \
        ebacc_ent, ebacc_avg_score, ebacc_avg_boys, ebacc_avg_girls, ebacc_grade5, \
        progress8_band, progress8_desc

    start_time = time.time()

    open_files()

    data = pd.read_csv(inp_f)

    df = pd.DataFrame(data)
    print(df)

    for row in df.index:
        urn = df["URN"][row]
        ks4_pupils = df["TPUP"][row]
        ks4_boys = df["BPUP"][row]
        ks4_girls = df["GPUP"][row]

        progress8 = df["P8MEA"][row]
        progress8_boys = df["P8MEA_BOYS"][row]
        progress8_girls = df["P8MEA_GIRLS"][row]
        # progress8_eng = df["P8MEAENG"][row]
        # progress8_mat = df["P8MEAMAT"][row]
        # progress8_ebacc = df["P8MEAEBAC"][row]

        attainment8 = df["ATT8SCR"][row]
        attainment8_boys = df["ATT8SCR_BOYS"][row]
        attainment8_girls = df["ATT8SCR_GIRLS"][row]
        # attainment8_eng = df["ATT8SCRENG"][row]
        # attainment8_mat = df["ATT8SCRMAT"][row]
        # attainment8_ebacc = df["ATT8SCREBAC"][row]
        # attainment8_eng_boys = df["ATT8SCRENG_BOYS"][row]
        # attainment8_mat_boys = df["ATT8SCRMAT_BOYS"][row]
        # attainment8_ebacc_boys = df["ATT8SCREBAC_BOYS"][row]
        # attainment8_eng_girls = df["ATT8SCRENG_GIRLS"][row]
        # attainment8_mat_girls = df["ATT8SCRMAT_GIRLS"][row]
        # attainment8_ebacc_girls = df["ATT8SCREBAC_GIRLS"][row]

        if academic_year == "2016":
            eng_maths_grade5 = df["PTL2BASICS_LL_PTQ_EE"][row]
        else:
            eng_maths_grade5 = df["PTL2BASICS_95"][row]

        ebacc_ent = df["PTEBACC_E_PTQ_EE"][row]

        if academic_year == "2016":
            ebacc_grade5 = df["PTEBACC_PTQ_EE"][row]
        else:
            ebacc_grade5 = df["PTEBACC_95"][row]

        if academic_year >= "2018":
            ebacc_avg_score = df["EBACCAPS"][row]
            ebacc_avg_boys = df["EBACCAPS_BOYS"][row]
            ebacc_avg_girls = df["EBACCAPS_GIRLS"][row]
            progress8_band = df["P8_BANDING"][row]
            progress8_desc = get_progress8_band_desc(progress8_band)
        else:
            ebacc_avg_score = ebacc_avg_boys = ebacc_avg_girls = progress8_band = progress8_desc = ""

        print(urn, ks4_pupils, ks4_boys, ks4_girls, progress8, progress8_boys, progress8_girls,
              attainment8, attainment8_boys, attainment8_girls, eng_maths_grade5,
              ebacc_ent, ebacc_avg_score, ebacc_avg_boys, ebacc_avg_girls, ebacc_grade5,
              progress8_band, progress8_desc, academic_year
              )

        if pd.isna(urn) or urn == " ":
            print("*** SKIP ***")
        else:
            if pd.isna(ks4_pupils) or ks4_pupils == " ":
                ks4_pupils = ""
            if pd.isna(ks4_boys) or ks4_boys in (" ", "SUPP"):
                ks4_boys = ""
            if pd.isna(ks4_girls) or ks4_girls in (" ", "SUPP"):
                ks4_girls = ""
            if pd.isna(progress8) or progress8 in (" ", "NE", "NP", "SUPP", "LOWCOV"):
                progress8 = ""
            if pd.isna(progress8_boys) or progress8_boys in (" ", "NE", "NP", "SUPP", "LOWCOV"):
                progress8_boys = ""
            if pd.isna(progress8_girls) or progress8_girls in (" ", "NE", "NP", "SUPP", "LOWCOV"):
                progress8_girls = ""
            if pd.isna(attainment8) or attainment8 in (" ", "NE", "SUPP"):
                attainment8 = ""
            if pd.isna(attainment8_boys) or attainment8_boys in (" ", "NE", "SUPP"):
                attainment8_boys = ""
            if pd.isna(attainment8_girls) or attainment8_girls in (" ", "NE", "SUPP"):
                attainment8_girls = ""
            if pd.isna(eng_maths_grade5) or eng_maths_grade5 in (" ", "NE", "SUPP"):
                eng_maths_grade5 = ""
            if pd.isna(ebacc_ent) or ebacc_ent in (" ", "NE", "SUPP"):
                ebacc_ent = ""
            if pd.isna(ebacc_avg_score) or ebacc_avg_score in ("NE", "SUPP"):
                ebacc_avg_score = ""
            if pd.isna(ebacc_avg_boys) or ebacc_avg_boys in ("NE", "SUPP"):
                ebacc_avg_boys = ""
            if pd.isna(ebacc_avg_girls) or ebacc_avg_girls in ("NE", "SUPP"):
                ebacc_avg_girls = ""
            if pd.isna(ebacc_grade5) or ebacc_grade5 in (" ", "NE", "SUPP"):
                ebacc_grade5 = ""
            if pd.isna(progress8_band) or progress8_band == "SUPP":
                progress8_band = ""
            if pd.isna(progress8_desc):
                progress8_desc = ""

            write_data()

    close_files()

    elapsed_time = time.time() - start_time
    print("\n", datetime.timedelta(seconds=elapsed_time))


if __name__ == "__main__":
    main()
