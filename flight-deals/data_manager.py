import requests
# Class responsible for talking to the google sheet
class DataManager:
    def __init__(self):

        self.url = "https://api.sheety.co/9ad7a4bde625521154d813b77ccec666/flightDeals"
        self.TOKEN = "9384h9834984hf938wh498fw837497g487"
        self.payload = {
            "Authorization": f"Bearer {self.TOKEN}"
        }
        self.users_list = []

    def get_data(self):
        get_data_url = self.url + "/prices"
        response = requests.get(get_data_url, headers=self.payload)
        print(response)
        return response

    def send_data(self, row_id, params):
        # Append the id to the url
        send_url = self.url + f"/prices/{row_id}"
        response = requests.put(url=send_url, headers=self.payload, json=params)
        print(response.text)

    def get_users(self):
        get_url = self.url + f"/users"
        response = requests.get(get_url, headers=self.payload)
        for record in response.json()['users']:
            self.users_list.append(record['email'])
        print(self.users_list)

        # self.users_list.append(response.json()['users'][0]['email'])
        return self.users_list
