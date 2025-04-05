import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import os

APP_ID = os.environ["ENV_NIX_APP_ID"]
API_KEY = os.environ["ENV_NIX_API_KEY"]
HOST_DOMAIN = os.environ["ENV_NIX_HOST_DOMAIN"]
ENDPOINT = os.environ["ENV_NIX_ENDPOINT"]
SHEET_ENDPOINT = os.environ["ENV_SHEETY_ENDPOINT"]
SHEET_NAME = os.environ["ENV_SHEET_NAME"]
USERNAME = os.environ["ENV_USERNAME"]
PASSWORD = os.environ["ENV_PASSWORD"]

request_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

nutritionix_params = {
    "query": input("What exercise/s did you do? ")
}

workout_data = requests.post(url=f"{HOST_DOMAIN}{ENDPOINT}", json=nutritionix_params, headers=request_headers)

for _ in range(len(workout_data.json()["exercises"])):
    exercise = workout_data.json()["exercises"][_]["name"].title()
    duration = workout_data.json()["exercises"][_]["duration_min"]
    calories = workout_data.json()["exercises"][_]["nf_calories"]

    dt = datetime
    today = dt.now()
    date = today.strftime(f"%d/%m/%Y")
    time = today.strftime("%X")

    prop = SHEET_NAME.split("s")[0]

    excel_params = {
        prop: {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }

    basic = HTTPBasicAuth(USERNAME, PASSWORD)

    header = {
        "Authorization": "Basic cmVpc2hhc2VlOmZecEF6NkdTQUgxRFMyXlNzJUFM"
    }

    response = requests.post(url=SHEET_ENDPOINT, json=excel_params, auth=basic)
    print(response.text)



