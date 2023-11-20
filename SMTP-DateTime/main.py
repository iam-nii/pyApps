import smtplib
import datetime as dt
import random

with open("quotes.txt") as quotes_file:
    quotes = quotes_file.readlines()
    quote = random.choice(quotes)

now = dt.datetime.now()
weekday = now.weekday()
if True:
    my_email = "portopapii@gmail.com"
    my_password = "scpg eymd zzqm hybc"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="adjeiboyejnr@gmail.com",
            msg=f"Subject:Monday motivation\n\n{quote}"
        )
