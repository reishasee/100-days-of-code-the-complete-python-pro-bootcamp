# api_key = "d09d55ba1b7a619f03bf40b75bba7b8c"
# api_call = "https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}"

import requests

LATITUDE = -2.568292,
LONGITUDE = 140.725297
API_KEY = "d09d55ba1b7a619f03bf40b75bba7b8c"

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for _ in range(0, 4):
    weather_id = weather_data["list"][_]["weather"][0]["id"]
    dt_txt = weather_data["list"][_]["dt_txt"]
    date = dt_txt.split()[0]
    time = dt_txt.split()[1]
    if weather_id < 700:
        will_rain = True

if will_rain:
    print(f"Bring an umbrella.")
