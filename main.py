import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = os.environ.get('api_key')
account_sid = os.environ.get('account_sid')
auth_token = os.environ.get('auth_token')
phone_number = os.environ.get('phone_number')
print(type(phone_number))
weather_params = {
    "lat": 34.052235,
    "lon": -118.243683,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

weather_code_list = []
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][0:12]
will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring An Umbrella.")
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="twilio_phone_number'+12223334444'",
        body="It's Sunny. Bring Sunscreen! 😎",
        to="phone_number''+12223334444'"
    )

    print(message.status)


