import requests #lets the code use apis or something lol

class Map_Service:
    def __init__(self, api_key):

        self.api_key = api_key
        self.url = "https://maps.googleapis.com/maps/api/geocode/json" #the link to the api

    def get_coordinates(self, address):
        params = {
            "address": address,
            "key": self.api_key
        } #the parameters for the below line of code to be able to get the info from the api
        response = requests.get(self.url, params=params) #gets the api data with those parameters (above) and the url
# NOTE: NEED TO MAKE ONE FOR DESTINATION TOO, ABOVE IS JUST ORIGIN LOCATION

        if response.status_code != 200: #if the request fails, do not crash code, just let user know the weather is not available and also show the error code
            print(f"Maps not available, error code: {response.status_code}")
            return None #terminates the code so nothing else runs

        map_data = response.json()
        return map_data