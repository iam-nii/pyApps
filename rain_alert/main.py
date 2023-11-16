import requests

weather_api = "49861fcffd5e32f5677b9c9137294e65"
yandex_api_key = "6dddd53d-6c79-46ae-8a87-3834214629fc"

lat = 59.93863
lon = 30.31413

url = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat": lat,
    "lon": lon,
    "appid": weather_api,
    "units": "metric"
}

response = requests.get(url, params=parameters)
response.raise_for_status()
data = response.json()
print(response.status_code)
weather_list = data['list']

id_zeroth = weather_list[0]['weather'][0]['id']
print(id_zeroth)

next_12hrs = []

for forecast in weather_list[0:3]:
    next_12hrs.append(forecast)

print(next_12hrs)