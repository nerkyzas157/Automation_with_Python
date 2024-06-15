import requests  # type: ignore
from datetime import datetime
import smtplib
import time

MY_LAT = 54.687157
MY_LONG = 25.279652

# Connected to ISS API and necessary extracted data
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Defined a function to compare ISS coordinated to my coordinates with some wiggle room
def match_positions():
    if (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
        and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    ):
        return True


# Connected to sunrise-sunset API and necessary extracted data
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

# Set a variable for current hour
time_now = datetime.now()
hour = time_now.hour

# Established connection with Gmail via SMTP
my_email = "email@gmail.com"
app_password = "xxxx xxxx xxxx xxxx"

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=app_password)


# Created a loop that every 60 checks for ISS coordinates and notifies if it's above me
while True:
    time.sleep(60)
    if match_positions() == True:
        if hour >= sunset + 1 or hour <= sunrise - 1:
            connection.sendmail(
                from_addr=my_email,
                to_addrs="email@gmail.com",
                msg="Subject:ISS Notification\n\nHello!\nLook into the sky and see the ISS flying through it!",
            )
            # Set a timer to one hour so I don't get spammed with emails
            time.sleep(3600)
