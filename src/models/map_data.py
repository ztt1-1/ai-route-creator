import requests
from src.services.api import GOOGLE_MAPS_API_KEY

origin = input("Enter start location: ")

url = "https://maps.googleapis.com/maps/api/geocode/json"

params_origin = {
    "address": origin,
    "key": GOOGLE_MAPS_API_KEY
}

maps_origin_data_response = requests.get(url, params=params_origin)
response_origin_json = maps_origin_data_response.json()
print(maps_origin_data_response.status_code)
print(maps_origin_data_response.json())
print(f'latitude: {response_origin_json["results"][0]["geometry"]["location"]["lat"]}, longitude: {response_origin_json["results"][0]["geometry"]["location"]["lng"]}')

origin_lat = response_origin_json["results"][0]["geometry"]["location"]["lat"]
origin_long = response_origin_json["results"][0]["geometry"]["location"]["lng"]



destination = input("Enter end location: ")

params_destination = {
    "address": destination,
    "key": GOOGLE_MAPS_API_KEY
}

maps_destination_data_response = requests.get(url, params=params_destination)
response_destination_json = maps_destination_data_response.json()
print(maps_destination_data_response.json())
print(f'latitude: {response_destination_json["results"][0]["geometry"]["location"]["lat"]}, longitude: {response_destination_json["results"][0]["geometry"]["location"]["lng"]}')

destination_lat = response_destination_json["results"][0]["geometry"]["location"]["lat"]
destination_long = response_destination_json["results"][0]["geometry"]["location"]["lng"]