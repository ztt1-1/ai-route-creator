import requests
from src.services.api import GOOGLE_MAPS_API_KEY
from src.models.map_data import origin_lat, origin_long, destination_lat, destination_long

url = "https://routes.googleapis.com/directions/v2:computeRoutes"

headers = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": GOOGLE_MAPS_API_KEY,
    "X-Goog-FieldMask": "routes.distanceMeters,routes.duration,routes.polyline"
}

'''origin_lat = input("Enter origin latitude: ")
origin_long = input("Enter origin longitude: ")
destination_lat = input("Enter destination latitude: ")
destination_long = input("Enter destination longitude: ")'''

data = {
    "origin": {
        "location": {
            "latLng": {
                "latitude": origin_lat,
                "longitude": origin_long
            }
        }
    },

    "destination": {
        "location": {
            "latLng": {
                "latitude": destination_lat,
                "longitude": destination_long
            }
        }
    },

    "travelMode": "WALK"
}

routes_data_response = requests.post(url, headers=headers, json=data) #gets the api data with those parameters (above) and the url
routes_json = routes_data_response.json()
print(routes_data_response.status_code)
print(routes_data_response.json())
print(f'Distance: {routes_json['routes'][0]['distanceMeters']} meters')