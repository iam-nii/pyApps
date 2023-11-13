import pandas
import random
import smtplib
import datetime as dt

MY_EMAIL = "portopapii@gmail.com"
MY_PASSWORD = "scpg eymd zzqm hybc"
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
data = pandas.DataFrame(pandas.read_csv("birthdays.csv"))

now = dt.datetime.now()
day = now.day
month = now.month
name = ""
email = ""
message = "It's not anyone's birthday today :)"


# 2. Check if today matches a birthday in the birthdays.csv
for index, row in data.iterrows():
    if row['day'] == day and row['month'] == month:
        name = row['name']
        email = row['email']
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

        letters_templates = ["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt",
                             "./letter_templates/letter_3.txt"]
        letter_link = random.choice(letters_templates)
        with open(letter_link) as letter_file:
            message = letter_file.read()
            print(message)
            message = message.replace("[NAME]", name.title())


# 4. Send the letter generated in step 3 to that person's email address.
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=f"Subject:Happy Birthday!\n\n{message}")




