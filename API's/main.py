import requests
from datetime import datetime
MY_LAT = 59.934280
MY_LONG = 30.335098
# response = requests.get(url="https://bible-api.com/john 3:16")
# response.raise_for_status()
#
# data = response.json()
# print(data['verses'][0]['text'])

response = requests.get(url="https://api.wheretheiss.at/v1/satellites/25544")
response.raise_for_status()
data = response.json()
print(data)
latitude = data['latitude']
longitude = data['longitude']
print(longitude)


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
# response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
#
# data = response.json()
# sunrise = data['results']['sunrise']
# sunset = data['results']['sunset']
#
# time_now = datetime.now()
# time = time_now.time()
# print(sunrise)