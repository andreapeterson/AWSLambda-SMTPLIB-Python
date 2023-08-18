import datetime as dt
import pandas as pd
import random
import os
import smtplib

# EMAIL SET-UP
MY_EMAIL = os.environ['SENDER_EMAIL']
smtp = "smtp.gmail.com"  # Use the smtp that correlates with your email above
PASSWORD = os.environ['APP_PASS']  # APP password

# CSV INTO DICT SET-UP
data = pd.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

# DATETIME SET-UP
now = dt.datetime.now()
today = (now.month, now.day)

# MAIN
if today in birthday_dict:
    birthday_info = birthday_dict.get(today)
    letter_random = random.choice(
        os.listdir("letter_templates"))  # Chooses a random letter file from letter templates folder
    with open(f"letter_templates/{letter_random}") as file:
        letter_template = file.read()
    final_letter = letter_template.replace("[NAME]", birthday_info.get("name"))

    with smtplib.SMTP_SSL(smtp, port=465) as connection:
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_info.get("email"),
                            msg=f"Subject:HAPPY BIRTHDAY!\n\n{final_letter}")
