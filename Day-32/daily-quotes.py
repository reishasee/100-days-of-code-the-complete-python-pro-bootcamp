import datetime as dt
import random
import smtplib

with open("quotes.txt") as quotes_file:
    quotes_list = quotes_file.readlines()

random_quote = random.choice(quotes_list)

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 3:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        my_email = "seereisha16@gmail.com"
        password = "lxri guro sqte visv"
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="rbrs1116@yahoo.com.ph",
                            msg=f"Subject:Thursday Motivation\n\n{random_quote}")


