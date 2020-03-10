# performance data
Input / output csv files:

    england_ks2final_20xx.csv => ks2_perf_20xx.csv
    england_ks3final_20xx.csv => ks2_perf_20xx.csv
    england_ks5final_20xx.csv => ks2_perf_20xx.csv

Here are the related database schemas containing performance data for the schools.

    "ks2_performance":
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

    "ks4_performance":
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

    "ks5_performance":
        columns = ("urn VARCHAR(10) NOT NULL, "
                   "ks5_pupil_nos VARCHAR(10), "
                   "avg_a_level_points VARCHAR(10), "
                   "avg_a_level_grade VARCHAR(10), "
                   "ac_year INT(4), "
                   "timestamp TIMESTAMP, "
                   "PRIMARY KEY (urn, ac_year)"
                   )
