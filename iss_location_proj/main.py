import requests
from datetime import datetime, timedelta
import smtplib
import time
MY_LAT = 16.566175
MY_LONG = 81.521629
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    response.raise_for_status()
    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    issposition = (latitude, longitude)
    print(issposition)

    if MY_LAT-5 <= latitude <= MY_LAT + 5 and MY_LONG-5 <= longitude <= MY_LONG+5:
        return True
    return False
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response_2 = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response_2.raise_for_status()
    data = response_2.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    sunrise = datetime.fromisoformat(sunrise)
    sunset = datetime.fromisoformat(sunset)
    sunrise += timedelta(hours=5, minutes=30)
    sunset += timedelta(hours=5, minutes=30)
    sunrise = sunrise.hour
    sunset = sunset.hour
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True
    return False
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com",587)
        connection.starttls()
        connection.login("suryabhuvaneshwarreddy@gmail.com","rtmh dhyw oknw rnzn")
        connection.sendmail(from_addr="suryabhuvaneshwarreddy@gmail.com",to_addrs="suryabhuvaneswarareddy@gmail.com",msg=f"Subject:Look Up!\n\n The Iss is Above You in The Sky")
        connection.close()