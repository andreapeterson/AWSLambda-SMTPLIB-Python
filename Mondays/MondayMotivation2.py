import datetime as dt
import smtplib
import random

my_email = "petersonandrea437@gmail.com"  # Put your email
password = "hntpbibfnbrtkjks"  # Put your APP PASSWORD that you set up within your email address(you can try your
# emails password-but most likely wont work)


now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 4:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # enter smtp information specific for your email
        # #Use with statement so you dont have to write 'connection.close()'
        connection.starttls()  # Secures connection to the email server when using port 587
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="andrea.peterson432@gmail.com",
                            msg=f"Subject:Monday Motivation\n\n{quote}")
