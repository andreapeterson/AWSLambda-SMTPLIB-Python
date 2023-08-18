import datetime as dt
import smtplib
import random

my_email = XXXXX  # Put your email
password = XXXXX  # Put your APP PASSWORD that you set up within your email address(you can try your
# emails password-but most likely wont work)


now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 1:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # enter smtp information specific for your email
        # #Use with statement so you dont have to write 'connection.close()'
        connection.starttls()  # Secures connection to the email server when using port 587
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=XXXXX,
                            msg=f"Subject:Monday Motivation\n\n{quote}")
