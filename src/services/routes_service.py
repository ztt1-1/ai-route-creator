import requests #lets the code use apis or something lol

class Route: #creates Route class, used to find a route between lat and long pts on the map
    def __init__(self, api_key): #this is the definition that takes the api key that src.models.weather_data took from src.services.api

        self.api_key = api_key #api key goes from src.services.api to src.services.route_data to here, not hardcoded for privacy lol #boi
        self.url = "https://routes.googleapis.com/directions/v2:computeRoutes" #the link to the api

    def get_route(self, headers, data): #the definition used to get the route, takes lat/long data and the headers and the transportation type from src.services.route_data from user input
        data = {"key": self.api_key} #the parameters for the below line of code to be able to get the info from the api
        response = requests.get(self.url, headers=headers, json=data) #gets the api data with those parameters (above) and the url

        if response.status_code != 200: #if the request fails, do not crash code, just let user know the weather is not available and also show the error code
            print(f"Weather not available, error code: {response.status_code}")
            return None #terminates the code so nothing else runs

        weather_data = response.json() #variable weather_data stores the stripped JSON text of the api data, 'tis only a bit different from the raw text but whatever it's easier to use
        return weather_data #sends the weather data to src.services.weather_service so that src.services.weather_service can print the data found through this class

    #note to future zach, FINISH THIS!!!!! figure out data and response stuff (not finished), thx!