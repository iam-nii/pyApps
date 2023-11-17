import requests
from datetime import datetime as dt
import os

APP_ID = os.getenv('APP_ID')
APP_API = os.getenv('APP_API')

EXERCISE = input("What exercise did you do today?: ")
GENDER = "male"
WEIGHT = "75"
HEIGHT = "170"
AGE = 21

headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_API,
}
params = {
    "query": EXERCISE,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE

}
url = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=url, json=params, headers=headers)
result = response.json()
print(result)

MY_SHEETY_API = os.getenv('SHEET_ENDPOINT')
sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.getenv('TOKEN')}"
}

exercise_list = [exercise for exercise in result['exercises']]


for dictionary in exercise_list:

    payload = {
        "workout":
            { # removing any column just leaves the cell blank
                "date": dt.now().strftime('%d/%m/%Y'),
                "time": dt.now().strftime("%X"),
                "exercise": dictionary['name'],
                "duration": dictionary['duration_min'],
                "calories": dictionary['nf_calories']
            }
    }
    sheet_response = requests.post(url=MY_SHEETY_API, json=payload, headers=sheety_headers)
    print(sheet_response.text)
