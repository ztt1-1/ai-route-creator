from src.services.api import GOOGLE_API_KEY #imports the api key for Geocoding API
from src.services.map_service import MapService #imports Class Map_Service

class_map_service = MapService(GOOGLE_API_KEY) #gives Map_Service Class the API key to use to obtain data from Geocoding API

#variable initialization for route_data to know what to do in case of faulty input
origin_lat = None
origin_long = None
destination_lat = None
destination_long = None

while True: #this is placed here to allow the program to stop when the input address is not found

#origin address code:
    origin = input("Enter start location: ")

    maps_origin_data_response = class_map_service.get_coordinates(origin) #uses Map_Service Class to run the Class definition get_coordinates with the origin address

    if maps_origin_data_response['results']: #runs only if the data response JSON contains 'results' (it will if the address given by the user exists)

        print(maps_origin_data_response) #prints full JSON response for the origin address
        print(f'latitude: {maps_origin_data_response["results"][0]["geometry"]["location"]["lat"]}, longitude: {maps_origin_data_response["results"][0]["geometry"]["location"]["lng"]}') #prints origin latitude and longitude
        #print(maps_origin_data_response.json())

        origin_lat = maps_origin_data_response["results"][0]["geometry"]["location"]["lat"] #latitude of the origin address is stored in variable origin_lat so it can be used if needed, the five bracket values dig through the JSON data for the latitude and longitude values
        origin_long = maps_origin_data_response["results"][0]["geometry"]["location"]["lng"] #longitude of the origin address is stored in variable origin_lat so it can be used if needed

    else: #runs if 'results' DNE
        print("Origin address not found, try again")
        break #ends program

#destination address code:
    destination = input("Enter end location: ")

    maps_destination_data_response = class_map_service.get_coordinates(destination) #uses Map_Service Class to run the Class definition get_coordinates with the destination address

    if maps_destination_data_response['results']: #runs only if the data response JSON contains 'results' (it will if the address given by the user exists)

        print(maps_destination_data_response) #prints full JSON response for the destination address
        print(f'latitude: {maps_destination_data_response["results"][0]["geometry"]["location"]["lat"]}, longitude: {maps_destination_data_response["results"][0]["geometry"]["location"]["lng"]}')  #prints destination latitude and longitude

        destination_lat = maps_destination_data_response["results"][0]["geometry"]["location"]["lat"] #latitude of the destination address is stored in variable destination_lat so it can be used if needed
        destination_long = maps_destination_data_response["results"][0]["geometry"]["location"]["lng"] #longitude of the destination address is stored in variable destination_lat so it can be used if needed

    else: #runs if 'results' DNE
        print("Destination address not found, try again")
        break #ends program