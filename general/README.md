# general data

Input / output csv files:

    20xx-20xx_england_spine.xlsx => school_details_20xx.csv
    20xx-20xx_england_spine.xlsx => ofsted_ratings_20xx.csv

Here are the related database schemas containing general info and ratings for the schools.

    "school_details":
        columns = ("urn VARCHAR(10) NOT NULL, "
                   "name VARCHAR(255) NOT NULL, "
                   "street VARCHAR(255), "
                   "city VARCHAR(255), "
                   "postcode VARCHAR(10), "
                   "status VARCHAR(2), "
                   "rating VARCHAR(30), "
                   "inspect_date VARCHAR(8), "
                   "date_opened VARCHAR(8), "
                   "date_closed VARCHAR(8), "
                   "school_type VARCHAR(50), "
                   "primary_sch VARCHAR(2), "
                   "secondary VARCHAR(2), "
                   "post16 VARCHAR(2), "
                   "age_from INT, "
                   "age_to INT, "
                   "gender VARCHAR(30), "
                   "gender_post16 VARCHAR(30), "
                   "religion VARCHAR(255), "
                   "local_auth VARCHAR(10), "
                   "other_urn VARCHAR(10), "
                   "timestamp TIMESTAMP, "
                   "PRIMARY KEY (urn)"
                   )

    "ratings":
        columns = ("urn VARCHAR(10) NOT NULL, "
                   "rating VARCHAR(30), "
                   "inspect_date VARCHAR(8), "
                   "timestamp TIMESTAMP, "
                   "PRIMARY KEY (urn, inspect_date)"
                   )
