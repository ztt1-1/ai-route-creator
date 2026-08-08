import requests #requests allows sending HTTP requests for API JSON data

class MapService: #creates Map_Service class, used to find the geocode data of a location
    def __init__(self, api_key):

        self.api_key = api_key #api key goes from src.services.api to src.services.map_data to here, not hardcoded for privacy
        self.url = "https://maps.googleapis.com/maps/api/geocode/json" #the link to geocoding api

    def get_coordinates(self, address): #the definition used to get the lat and long data from a location
        params = {
            "address": address,
            "key": self.api_key
        } #the parameters for the below line of code to be able to get the info from the api
        response = requests.get(self.url, params=params) #gets the api data with those parameters (above) and the url

        if response.status_code != 200: #if the request fails, do not crash code, just let user know the weather is not available and also show the error code
            print(f"Maps not available, error code: {response.status_code}")
            return None #terminates the code so nothing else runs

        map_data = response.json() #variable map_data stores the stripped JSON text of the api data
        return map_data #sends the map data to src.services.map_data so that it can use the data found through this class