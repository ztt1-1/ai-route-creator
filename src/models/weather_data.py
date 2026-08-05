from src.services.weather_service import Weather_Service #imports the Weather class from src.services.weather_service
from src.services.api import WEATHER_API_KEY #imports the api key from src.services.api

weather_service = Weather_Service(WEATHER_API_KEY) #gives the Weather class the api key to work with

user_location = input('Enter your location: ') #requests location from user and saves that location into variable user_location

weather_data_response = weather_service.get_weather(user_location) #weather_data is a variable that weather data that results from the storing of the api key being used for the first def in class Weather, then goes to def get_weather in class Weather, gives the inputted user_location to the class, and then runs the get request code from the Weather class

if weather_data_response: #makes sure that if there is an error with the api key, none of the below 'print' commands try to run and then cause some errors and stuff
    print(weather_data_response) #prints full weatherdata dictionary
    print(weather_data_response['location']) #prints location data
    print(f'Temperature: {weather_data_response['current']['temp_f']}F') #prints the current temperature (F)
    print(f'Humidity: {weather_data_response['current']['humidity']}%') #prints the current humidity
    print(f'Wind Speed: {weather_data_response['current']['wind_mph']} mph {weather_data_response['current']['wind_dir']}') #prints the current wind speed
    print(f'UV: {weather_data_response['current']['uv']}')  # prints the current uv index