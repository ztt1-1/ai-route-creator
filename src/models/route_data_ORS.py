from src.services.api import ORS_API_KEY #imports the api key for Geocoding API
from src.services.ORS_routes_service import ORSService #imports Class Map_Service
from archive.map_data import origin_lat, origin_long, destination_lat, destination_long

class_ORS_service = ORSService(ORS_API_KEY)

data = {
    "coordinates": [
        [origin_long, origin_lat],
        [destination_long, destination_lat]
    ]
}

if origin_lat is not None and origin_long is not None and destination_lat is not None and destination_long is not None: #runs only if route_data got the lat and long information from src.models.map_data

    ORS_route_data_response = class_ORS_service.ors_get_route(data) #uses Route_Service Class to run the Class definition get_route with the information stored in 'data' variable

    print(ORS_route_data_response) #prints full JSON response for the origin address
    distance_meters = ORS_route_data_response['routes'][0]['summary']['distance']
    distance_miles = distance_meters / 1609.34
    print(distance_miles)
    duration_minutes = ORS_route_data_response['routes'][0]['summary']['duration'] / 60
    print(duration_minutes)
    polyline = ORS_route_data_response['routes'][0]['geometry']
    print(polyline)

else: #runs if origin address or destination address was not obtained

    print('Error obtaining data, check if addresses were input correctly?')