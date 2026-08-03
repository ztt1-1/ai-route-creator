'''import requests
from src.services.api import GOOGLE_MAPS_API_KEY

address = input("Enter address: ")

url = "https://maps.googleapis.com/maps/api/geocode/json"

params = {
    "address": address,
    "key": GOOGLE_MAPS_API_KEY
}

maps_data_response = requests.get(url, params=params)
response_json = maps_data_response.json()
print(maps_data_response.status_code)
print(maps_data_response.json())
print(f'latitude: {response_json["results"][0]["geometry"]["location"]["lat"]}, longitude: {response_json["results"][0]["geometry"]["location"]["lng"]}')'''

