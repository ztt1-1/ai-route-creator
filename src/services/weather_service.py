import requests #lets the code use apis or something lol

class Weather: #creates Weather class, used to find weather data
    def __init__(self, api_key): #this is the definition that takes the api key that src.models.weather_data took from src.services.api

        self.api_key = api_key #api key goes from tests.api to services.weather_data to here, not hardcoded for privacy lol
        self.url = "http://api.weatherapi.com/v1/current.json" #the link to the api

    def get_weather(self, location): #the definition used to get the weather, takes location from src.services.weather_data from user input

        parameters = {"key": self.api_key, "q": location} #the parameters for the below line of code to be able to get the info from the api
        response = requests.get(self.url, params=parameters) #gets the api data with those parameters (above) and the url

        if response.status_code != 200: #if the request fails, do not crash code, just let user know the weather is not available and also show the error code
            print(f"Weather not available, error code: {response.status_code}")
            return None #terminates the code so nothing else runs

        weather_data = response.json() #variable weather_data stores the stripped JSON text of the api data, 'tis only a bit different from the raw text but whatever it's easier to use
        return weather_data #sends the weather data to src.services.weather_service so that src.services.weather_service can print the data found through this class