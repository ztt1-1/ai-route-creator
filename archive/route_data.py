from src.services.api import GOOGLE_API_KEY #imports the api key for Routes API
from src.services.routes_service import RouteService #imports Class Route_Service
from archive.map_data import origin_lat, origin_long, destination_lat, destination_long #imports latitude and longitude of both the origin and the destination obtained and stored in src.models.map_data

class_route_service = RouteService(GOOGLE_API_KEY) #gives Route_Service Class the API key to use to obtain data from Routes API

data = {     #stores formatted data for the API containing all the information that the route service needs to find the route between those two points
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

    "travelMode": "WALK"    #travel mode is walk because the functionality of a running route service is only meant to be used on foot
}

if origin_lat is not None and origin_long is not None: #runs only if route_data got the lat and long information from src.models.map_data

    route_data_response = class_route_service.get_route(data) #uses Route_Service Class to run the Class definition get_route with the information stored in 'data' variable

    print(route_data_response) #prints full JSON response for the origin address
    meters = int(route_data_response['routes'][0]['distanceMeters']) #variable meters equals the distance in meters that the Route_Service class obtained
    miles = round(meters / 1609.344, 2) #convert meters to miles and rounds to two decimal points

    print(f'Distance: {miles} mi') #prints distance in miles

    route_time = int(route_data_response['routes'][0]['duration'][0:-1]) #Google's JSON response provides a time value like '1234s', this code removes the 's' and turns the leftover string into an integer

    seconds = route_time % 60
    minutes = route_time // 60

    print(f'Time: {minutes} minutes and {seconds} seconds') #prints time it takes to complete the route between the two points in minutes and seconds

else: #runs if origin address or destination address was not obtained

    print('Error obtaining data, check if addresses were input correctly?')