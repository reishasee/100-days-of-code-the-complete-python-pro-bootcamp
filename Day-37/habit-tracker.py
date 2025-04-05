import requests
from datetime import datetime

USERNAME = "reishasee"
TOKEN = "acde1234"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Running Progress",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime.now()
progress = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
progress_config = {
    "date": "20250403",
    "quantity": "10"
}

# response = requests.post(url=progress, json=progress_config, headers=headers)
# print(response.text)

new_qty = {
    "quantity": "7.5"
}

# response = requests.put(url=f"{progress}/20250403",json=new_qty, headers=headers)
# print(response.text)

response = requests.delete(url=f"{progress}/20250403", headers=headers)
print(response.text)
