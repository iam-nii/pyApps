import requests
from datetime import datetime as dt

USERNAME = 'iamnii'
TOKEN = '9wv8b098wh58h9w8b985wb98h'

pixela_url = "https://pixe.la/v1/users"
pixela_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# This code is only needed to create the user account once. After that, it can be connected
# response = requests.post(url=pixela_url,json=pixela_params)
# print(response.text)


# Creating a graph
graph_endpoint = f"{pixela_url}/{USERNAME}/graphs"
GRAPH_ID = 'graph1'
graph_params = {
    'id': GRAPH_ID,
    'name': 'Coding graph',
    'unit': 'hours',
    'type': 'int',
    'color': 'momiji'
}
header = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=header)
# print(response.text)

# Posting a pixel
today = dt(year=2023, month=11, day=13)
print(today.strftime("%G%m%d"))
pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_config = {
    'date': today.strftime("%G%m%d"),
    'quantity': '3',
}

# response = requests.post(url=pixel_endpoint,json=pixel_config,headers=header)
# print(response.text)


# Updating records
pixel_update_endpoint = f"{pixel_endpoint}/{today.strftime('%G%m%d')}"

pixel_update_config = {
    'quantity': '4'
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_config, headers=header)
# print(response.text)

# Deleting a pixel

pixel_del_endpoint = pixel_update_endpoint
response = requests.delete(url=pixel_del_endpoint, headers=header)
print(response.text)
