# 1XX: Hold On
# 2XX: Here You Go
# 3XX: Go Away
# 4XX: You Screwed Up
# 5XX: I Screwed Up

from datetime import datetime
import requests
# responce=requests.get(url="http://api.open-notify.org/iss-now.json")
# # print(responce.status_code)
# responce.raise_for_status()
# latitude=responce.json()["iss_position"]["latitude"]
# longitude=responce.json()["iss_position"]["longitude"]
# iss_position=(latitude,longitude)
# print(iss_position)
MY_LAT=26.912434
MY_LONG=75.787270
parameters={
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0,

}
resource=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
resource.raise_for_status()
data=resource.json()
sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset=data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)


timenow=datetime.now()
print(timenow.hour)



