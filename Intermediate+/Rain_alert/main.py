import requests
from twilio.rest import Client
#import os
#open terminal and write -> export api_key=7356cf7acdfa62a5545de7c22fabfb10
#api_key=os.environ.get("api_key")
api_key="7356cf7acdfa62a5545de7c22fabfb10"
MY_LAT=26.912434
MY_LONG=75.787270
ENDPOINT="https://api.openweathermap.org/data/2.8/onecall"
parameters = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "exclude":"current,minutely,daily",
        "appid": api_key,
    }
account_sid = "ACee72c4a3c7b75936ceabdb63da7ed69f"
auth_token = "b1d9d1b02f42d8d22d534e83d237f2d3"
response = requests.get(ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()
data_slice=data["hourly"][:12]
# print(data["hourly"][0]["weather"][0]["id"])
# print(data_slice)
will_rain=False
for hour_data in data_slice:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code) <700:
        will_rain=True

if will_rain:
    # print("Bring an Umbrella")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Rom Rom Bhaiyo 🙏🏻 Systum Pad Denge 📢",
        from_='+18788812643',
        to='+917073396759'
    )
    print(message.status)

