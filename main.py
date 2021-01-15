import requests
from datetime import datetime


PIXELA_URL = "https://pixe.la/v1/users"
USERNAME = "mir"
TOKEN = "<Enter token>"

user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=PIXELA_URL, json=user_param)
# print(response.text)
# print(response.status_code)


GRAPH_ENDPOINT = f"{PIXELA_URL}/{USERNAME}/graphs"
GRAPH_ID = "graph1"
graph_param = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_param, headers=headers)
# print(response.text)
# print(response.status_code)

# post a pixel value
# /v1/users/<username>/graphs/<graphID>

pixel_endpoint = f"{PIXELA_URL}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
pixel_param = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "20.5",
}

# response = requests.post(url=pixel_endpoint, json=pixel_param, headers=headers)
# print(response.text)
# print(response.status_code)

# update the graph
# /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
pixel_update_endpoint = f"{PIXELA_URL}/{USERNAME}/graphs/{GRAPH_ID}/20210115"
pixel_update_param = {
    "quantity": "5.2"
}
# response = requests.put(url=pixel_update_endpoint, json=pixel_update_param, headers=headers)
# print(response.text)
# print(response.status_code)

# delete the pixel data
date = datetime(year=2021, month=1, day=15)
pixel_delete_endpoint = f"{PIXELA_URL}/{USERNAME}/graphs/{GRAPH_ID}/{date.strftime('%Y%m%d')}"
response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)
print(response.status_code)
