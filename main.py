import requests
import datetime as dt
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

GENDER = "MALE"
WEIGHT = 87.4
HEIGHT = 1.80
AGE = 30

AUTHORIZATION = os.environ.get("AUTHORIZATION")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_test = input('Tell me which exercise you did: ')

exercise_data = {
    "query": exercise_test,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}


response = requests.post(url=exercise_endpoint, json=exercise_data, headers=headers)
result = response.json()
print(result)

sheet_endpoint = os.environ.get("SHEET_ENDPOINT")

today = dt.datetime.now().strftime("%d/%m/%Y")
time = dt.datetime.now().strftime("%X")

headers_sheet = {
    "Authorization": AUTHORIZATION
}

for exercise in result["exercises"]:
    work_out_data = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    response_sheet = requests.post(url=sheet_endpoint, json=work_out_data, auth=(USERNAME, PASSWORD))
    data_sheet = response_sheet.text
    print(data_sheet)

