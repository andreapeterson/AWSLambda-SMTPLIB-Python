import datetime as dt
import smtplib
import random
import os
import json

my_email = os.environ['SENDER_EMAIL']  
password = os.environ['APP_PASS']  


def lambda_handler(event, context):
    now = dt.datetime.now()
    day_of_week = now.weekday()
    if day_of_week == 1:
        with open("quotes.txt") as file:
            all_quotes = file.readlines()
            quote = random.choice(all_quotes)
        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:  
            connection.starttls() 
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=os.environ['RECEIVER_EMAIL'],
                                msg=f"Subject:Monday Motivation\n\n{quote}")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')}
