import requests


class FlightSearch:

    def __init__(self):
        self.url = "http://api.tequila.kiwi.com/locations/query"

        self.testing = "TESTING"
        self.headers = {
            "apikey": "Q_GUE_YRkaugymlgMkZ6VfDCB64xMTX_",
        }

    def get_iat_code(self, city_name: str):
        params = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=self.url, params=params, headers=self.headers)
        city_code = response.json()['locations'][0]['code']
        return city_code