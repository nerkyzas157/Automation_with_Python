# Importing requirments
import datetime as dt
import random
import pandas  # type: ignore
import smtplib

# Opening data file and setting row value
data = pandas.read_csv("birthdays.csv")
row = -1

# Set variables to check current month and day
now = dt.datetime.now()
month = now.month
day = now.day

# Logging into email via SMTP
my_email = "email@gmail.com"
app_password = "xxxx xxxx xxxx xxxx"
connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=app_password)

# Automating birthday wishing
for m in data.month:
    for d in data.day:
        row += 1
        if month == m and day == d:
            with open(
                f"letter_templates\\letter_{random.randint(1, 3)}.txt"
            ) as starting_letter:
                letter_draft = starting_letter.read()
                email_text = letter_draft.replace("[NAME]", data.name[row])
            connection.sendmail(
                from_addr=my_email,
                to_addrs=data.email[row],
                msg=f"Subject:Happy birthday!\n\n{email_text}.",
            )
