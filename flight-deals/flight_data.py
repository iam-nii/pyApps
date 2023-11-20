import os
import datetime
import requests
from pprint import pprint
TOKEN = os.getenv("TOKEN")

#Getting the dates
# Current date in the required format (ddmmyyyy)
CURRENT_DATE = datetime.datetime.now()
DATE_FROM = CURRENT_DATE.strftime("%d/%m/%Y")

# Getting the next six month date in the required format(ddmmyyyy)
SIX_MONTHS = CURRENT_DATE + datetime.timedelta(days=6*30)
DATE_TO = SIX_MONTHS.strftime("%d/%m/%Y")


class FlightData:

    def __init__(self):
        self.url = "http://api.tequila.kiwi.com/v2/search"
        self.headers = {
            "apikey": "Q_GUE_YRkaugymlgMkZ6VfDCB64xMTX_",
        }
        self.count = 0
        self.flight_data = {
            "stop_overs": 0,
            "via_city": ""
        }
        self.payload = {
            # The fly_from will be changed later. LON is just for testing purposes
            "fly_from": "LON",
            "date_from": DATE_FROM,
            "date_to": DATE_TO,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }

    def get_flight_data(self, iata_code: str, city:str):
        self.payload["fly_to"] = iata_code
        response = requests.get(url=self.url, headers=self.headers, params=self.payload)
        result = response.json()
        print(result)
        try:
            data = result['data'][0]
        except IndexError:
            self.payload["max_stopovers"] = 2
            response = requests.get(url=self.url, headers=self.headers, params=self.payload)
            data = response.json()['data'][0]
            pprint(data)
            self.flight_data['stop-over'] = 1
            self.flight_data['via_city'] = data["route"][1]["cityTo"]
            self.flight_data["Flight Price"] = data["price"]
            self.flight_data["Departure City"] = data["route"][0]["cityFrom"]
            self.flight_data["Departure IATA CODE"] = data['cityCodeFrom']
            self.flight_data["Arrival City"] = data['cityTo']
            self.flight_data["Arrival IATA Code"] = data['cityCodeTo']
            self.flight_data["Outbound"] = data["route"][0]["local_departure"].split("T")[0]
            self.flight_data["Inbound"] = data["route"][1]["local_departure"].split("T")[0]
            return self.flight_data

        else:
            self.flight_data["Flight Price"] = data['price']
            self.flight_data["Departure City"] = data['cityFrom']
            self.flight_data["Departure IATA CODE"] = data['cityCodeFrom']
            self.flight_data["Arrival City"] = data['cityTo']
            self.flight_data["Arrival IATA Code"] = data['cityCodeTo']
            self.flight_data["Outbound"] = data["route"][0]["local_departure"].split("T")[0]
            self.flight_data["Inbound"] = data["route"][1]["local_departure"].split("T")[0]

            pprint(f"{self.flight_data['Arrival City']}: ${self.flight_data['Flight Price']}")
            return self.flight_data