import requests
from datetime import datetime
import time
import smtplib

MY_LAT = 59.934280
MY_LONG = 30.335098
MY_EMAIL = "portopapii@gmail.com"
MY_PASSWORD = "scpg eymd zzqm hybc"
iss_latitude = 0
iss_longitude = 0

# Your position is within +5 or -5 degrees of the ISS position.
def is_iss_close():
    global iss_longitude, iss_latitude
    # Getting the position of the iss
    response = requests.get(url="https://api.wheretheiss.at/v1/satellites/25544")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["latitude"])
    iss_longitude = float(data["longitude"])
    print(f"ISS CURRENT POSIITON: {iss_latitude},{iss_longitude}")
    print(f"MY CURRENT POSITION:{MY_LAT}, {MY_LONG}")

    if -5 <= iss_longitude - MY_LONG <= 5 and -5 <= iss_latitude - MY_LAT <= 5:
        print("Iss is close!!")
        return True
    else:
        print("Iss is far away")
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

# Checking  to see the time of the day
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(f"SUNRISE: {sunrise}, SUNSET: {sunset}")


time_now = datetime.now()
hour = time_now.hour
print(F"CURRENT TIME: {hour}")


def send_message():
    if sunrise < hour < sunset:
        if is_iss_close():
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs="adjeiboyejnr@gmail.com",
                                    msg=f"Subject: ISS PASSING OVER!\n\nLook Up!👆"
                                        f"ISS CURRENT POSITION: {iss_latitude}, {iss_longitude}")


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    send_message()
