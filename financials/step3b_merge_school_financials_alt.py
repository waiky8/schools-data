import pandas as pd
import csv
import datetime
import time

in_f1 = "data/pri_schools_income.csv"
in_f2 = "data/pri_schools_expenditure.csv"
in_f3 = "data/pri_schools_balance.csv"
out_f = "data/pri_schools_financials.csv"

# in_f1 = "data/sec_schools_income.csv"
# in_f2 = "data/sec_schools_expenditure.csv"
# in_f3 = "data/sec_schools_balance.csv"
# out_f = "data/sec_schools_financials.csv"

header = ["URN", "Income", "Expenditure", "Balance", "Academic Year"]

f_in1 = f_in2 = f_in3 = f_out = writer = ""
urn = income = expenditure = balance = academic_year = ""


def open_files():
    global f_in1, f_in2, f_in3, f_out, writer

    f_in1 = open(in_f1, "r")
    f_in2 = open(in_f2, "r")
    f_in3 = open(in_f3, "r")
    f_out = open(out_f, "w", newline="")
    writer = csv.writer(f_out)

    write_header()


def write_header():
    writer.writerow(header)


def write_data():
    writer.writerow([urn, income, expenditure, balance, academic_year])


def close_files():
    f_in1.close()
    f_in2.close()
    f_in3.close()
    f_out.close()


def main():
    global urn, income, expenditure, balance, academic_year

    start_time = time.time()

    open_files()

    data1 = pd.read_csv(f_in1)
    df1 = pd.DataFrame(data1, columns=["URN", "Income", "Academic Year"])

    data2 = pd.read_csv(f_in2)
    df2 = pd.DataFrame(data2, columns=["URN", "Expenditure", "Academic Year"])

    data3 = pd.read_csv(f_in3)
    df3 = pd.DataFrame(data3, columns=["URN", "Balance", "Academic Year"])

    d = pd.merge(df1, df2, on=["URN", "Academic Year"])
    df = pd.merge(d, df3, on=["URN", "Academic Year"])

    for i in df.index:
        urn = df["URN"][i]
        income = df["Income"][i]
        expenditure = df["Expenditure"][i]
        balance = df["Balance"][i]
        academic_year = str(df["Academic Year"][i])[-4:]

        write_data()

    close_files()

    elapsed_time = time.time() - start_time
    print("\n", datetime.timedelta(seconds=elapsed_time))


if __name__ == "__main__":
    main()
