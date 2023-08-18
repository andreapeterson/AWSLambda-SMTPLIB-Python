# AWSLambda-SMTPLIB-Python
Using Python and the smtplib library, we can upload this into Lambda to set up scheduled emails. For MondayMotivation, it will send a motivational quote to your email. I put it in Lambda to make it send the email every Monday at 8 A.M. Check my Blog at https://dev.to/andreapeterson/send-automated-emails-smtplib-python-through-lambda-15jk for the tutorial of how I did it.

The MondayMotivation2.py file is the Python file before adding incorporating the code into a Lamda function and adding environment variables(Once you enter your information where the XXXX go, you can run this in Python, but I wanted to put in into Lambda so I don't have to run this file manually every Monday at 8 a.m.). The MondayMotivation.py file is the final code with the Lambda function and environment variables. These must be in the same folder as the quotes.txt.

For scheduled Birthday emails, the BirthdayMain.py is edited to be inserted into Lambda. Edit the birthdays.csv with any information you would like to add (add the day of today for testing) and add this to the same folder as the BirthdayMain.py. Have a folder that contains the letter templates (edit them to your liking)
