##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import smtplib
import os
import random
import pandas as pd

SENDER_EMAIL = "seereisha16@gmail.com"
now = dt.datetime.now()
month = now.month
day = now.day
i = 0

birthdays_df = pd.read_csv("birthdays.csv")
birthdays_dict = birthdays_df.to_dict(orient="records")

for celebrant in birthdays_dict:
    i += 1

    random_file = f"letter_{random.randint(1,3)}.txt"
    with open(f"letter_templates/{random_file}", mode="r") as file:
        message_list = file.readlines()

        if celebrant["month"] == month and celebrant["day"] == day:
            message_list[0] = message_list[0].replace("[NAME]", celebrant["name"])

            with open(f"letter_templates/new_letter_{i}.csv", mode="w") as new_file:
                new_file.write("".join(message_list))

            with smtplib.SMTP("smtp.gmail.com") as connection:
                password = "lxri guro sqte visv"
                connection.starttls()
                connection.login(user=SENDER_EMAIL, password=password)

                with open(f"letter_templates/new_letter_{i}.csv", mode="r") as new_file:
                    connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=celebrant["email"],
                                        msg=f"Subject:Happy Birthday\n\n{new_file.read()}")
