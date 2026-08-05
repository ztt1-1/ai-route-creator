import requests #lets the code use api requests

class Route_Service: #creates Route class, used to find a route between origin lat and long pts on the map and destination lat and long pts on the map (Google)
    def __init__(self, api_key): #this is the definition that takes the api key that src.services.route_data took from src.services.api

        self.api_key = api_key #api key goes from src.services.api to src.services.route_data to here, not hardcoded for privacy lol #boi
        self.url = "https://routes.googleapis.com/directions/v2:computeRoutes" #the link to the routes api

    def get_route(self, data): #the definition used to get the route, takes lat/long data and the headers and the transportation type from src.services.route_data from user input
        response = requests.post(self.url, headers= {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": self.api_key,
        "X-Goog-FieldMask": "routes.distanceMeters,routes.duration,routes.polyline"},
        json=data) #gets the api data with those parameters (above) and the url

        if response.status_code != 200: #if the request fails, do not crash code, just let user know routes api is not available and also show the error code for easy debug
            print(f"Routes not available, error code: {response.status_code}")
            return None #terminates the code so nothing else runs

        route_data = response.json() #variable route_data stores the stripped JSON text of the api data
        return route_data #sends the route data to src.services.routes_service so that src.services.routes_service can use the data found through this class
