import requests #requests allows sending HTTP requests for API JSON data

class ORSService:
    def __init__(self, api_key):

        self.api_key = api_key
        self.url = "https://api.openrouteservice.org/v2/directions/foot-walking" #the link to the ORS_routes api

    def ors_get_route(self, data):

        response = requests.post(
            self.url,
            json=data,
            headers={"Authorization": self.api_key,"Content-Type": "application/json"}
        )

        print("STATUS:", response.status_code)

        if response.status_code != 200:
            return None

        response_data = response.json()
        distance_meters = response_data['routes'][0]['summary']['distance']
        distance_miles = distance_meters / 1609.34
        print(distance_miles)

        return response_data