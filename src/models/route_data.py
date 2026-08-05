from src.services.routes_service import Route_Service
from src.services.api import GOOGLE_MAPS_API_KEY #imports the api key from src.services.api
from src.models.map_data import origin_lat, origin_long, destination_lat, destination_long

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
route_service = Route_Service(GOOGLE_MAPS_API_KEY)
routes_data_response = route_service.get_route(data)

if routes_data_response:

    meters = int(routes_data_response['routes'][0]['distanceMeters'])
    miles = round(meters / 1609.344, 2)

    print(f'Distance: {miles} mi')


    time_seconds = int(routes_data_response['routes'][0]['duration'][0:-1])

    seconds = time_seconds % 60
    minutes = time_seconds // 60

    print(f'Time: {minutes} minutes and {seconds} seconds')
