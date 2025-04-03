import requests
from datetime import datetime
import smtplib, time

MY_LAT = 14.580395 # Your latitude
MY_LONG = 121.064065 # Your longitude
SENDER_EMAIL = "seereisha16@gmail.com"
RECIPIENT_EMAIL = "rbrs1116@yahoo.com.ph"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    print(data)

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.

    if iss_latitude - 5 <= MY_LAT <= iss_latitude + 5 and iss_longitude - 5 <= MY_LONG <= iss_longitude + 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            password = "lxri guro sqte visv"
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=password)
            connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=RECIPIENT_EMAIL, msg="Subject:ISS Notification\n\nLook up!")

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



