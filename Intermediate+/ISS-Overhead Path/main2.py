import requests
from datetime import datetime
import smtplib
my_email="sharmaeater1@gmail.com"
password="eljznatvitfzlniv"
connection=smtplib.SMTP("smtp.gmail.com",587)
MY_LAT=26.912434
MY_LONG=75.787270

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
print(iss_longitude,iss_latitude)
#Your position is within +5 or -5 degrees of the ISS position.


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

time_now = datetime.now()
hour=time_now.hour

#If the ISS is close to my current position
if iss_latitude in range(MY_LAT-5,MY_LAT+5) and iss_latitude in range(MY_LONG-5,MY_LONG+5) and hour not in range(sunrise,sunset):
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="sharmaeater2@gmail.com", msg="Subject:Urgent!\n\nHey Look Up its near.")
    connection.close()

# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



