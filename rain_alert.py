import requests
from twilio.rest import Client
api_key = ""
account_sid = ''
auth_token = ""

parameters = {
    #Ewiniar
    "lat":22.5744,
    "lon":88.3629,
    "appid":api_key,
    "cnt":4
}
response = requests.get(url="http://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
print(response.status_code)
weather_data = response.json()
print(weather_data)
# if weather_data["list"][0]["weather"][0]["id"] < 700:
#     print("Bring an Umbrella")
# else:
#     print("no rain this time")
will_rain_today = False
for hour_data in weather_data["list"]:
    if hour_data["weather"][0]["id"] < 700:
        will_rain_today = True

if will_rain_today:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today,remember to bring an umbrella.",
        from_='+12512998318',
        to='+918597136342'
    )
    print(message.status)
