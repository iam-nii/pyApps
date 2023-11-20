from notification_manager import NotificationManager
import flight_data
import data_manager as dm
from flight_search import FlightSearch

new_dm = dm.DataManager()
flight_data = flight_data.FlightData()
sheet_data = new_dm.get_data().json()['prices']
notify = NotificationManager()

# pprint(sheet_data)

# Fill the empty iata codes in the table
# for deal in sheet_data:
#     if deal['iataCode'] == "":
#         # Create an instance of the FlightSearch class
#         search = FlightSearch()
#         params = {
#             "price": {
#                 'iataCode': f"{search.get_iat_code(deal['city'])}"
#             }
#         }
#         new_dm.send_data(deal['id'], params=params)
#

# Get the flight prices
for row in sheet_data:
    iata_code = row['iataCode']
    online_deals = flight_data.get_flight_data(iata_code,row['city'])
    if online_deals is None:
        continue
    elif online_deals["Flight Price"] <= row['lowestPrice']:
        for client in new_dm.get_users():
            notify.send_mail(online_deals, client)

