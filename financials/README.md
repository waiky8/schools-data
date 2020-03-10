# financials data
Input / output csv files:

    england_cfrfull_20xx.xlsx => financials_20xx.csv

Here are the related database schema containing financial data for the schools.

    "financials":
        columns = ("urn VARCHAR(10) NOT NULL, "
                   "income FLOAT(10,2), "
                   "expenditure FLOAT(10,2), "
                   "balance FLOAT(10,2), "
                   "ac_year INT(4), "
                   "timestamp TIMESTAMP, "
                   "PRIMARY KEY (urn, ac_year)"
                   )
