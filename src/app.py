import string
import streamlit as st
from services.map_service import MapService
from services.api import GOOGLE_API_KEY, ORS_API_KEY
from services.weather_service import WeatherService #imports the Weather class from src.services.weather_service
from services.api import WEATHER_API_KEY #imports the api key from src.services.api
from services.routes_service import RouteService
from algorithm.route_generator import RouteGenerator
from services.ORS_routes_service import ORSService




st.title('AI-Running-Route-Creator')

st.divider()

st.markdown("About this project:")
st.caption('''AI Route Creator

- generate routes of any distance
- results depending on elevation
- support for out-and-backs and loops
- sidewalk + safe road prioritization
- AI feedback

Created by Zachary (ztt1)''')

st.divider()

st.header('Customization')

terrain = st.selectbox("Terrain", ["Road", "Trail", "Sidewalk"])
elevation = st.selectbox("Route Elevation", ["Flat", "Rolling Hills", "Hilly"])
route_type = st.selectbox("Route Type", ["Out-and-Back", "Loop"])

st.divider()

#below is the code for a slider-based mileage choice

#st.header('Distance (slider)')
#distance = st.slider('Desired distance (in miles)', min_value=1, max_value=30, value=5)
#st.write(f'You chose **{distance} mile(s)**')

#button1_press = st.button('Find Route', key="find_route_1")

#if button1_press:
    #print(f'{distance} mile(s) chosen.')
    #print(terrain)
    #print(elevation)
    #print(route_type)

#st.divider()

distance_float = 0

st.header('Distance (text input)')
distance = st.text_input('Desired distance (in miles)')

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = string.punctuation.replace(".", "")
if distance:

    distance_float = float(distance)

    has_letter = False
    has_spec = False
    extra_dot = False
    for letter in distance:
        if letter in alphabet:
            has_letter = True
            break
        if letter in special_characters:
            has_spec = True
            break

    dot_test1 = distance.find(".")
    dot_test2 = distance.rfind(".")
    if dot_test1 != dot_test2:
        extra_dot = True
    if has_letter or has_spec or extra_dot:
        st.write("Please enter a valid number.")
    elif float(distance) <= 0 or float(distance) > 30:
        st.write("Choose a distance greater than 0 and less than or equal to 30.")
    else:
        st.write(f"You chose **{distance} mile(s)**")

button2_press = st.button('Find Route', key="find_route_1")

if button2_press and distance and not has_letter and not has_spec and not extra_dot and 0 < float(distance) <= 30:
    print(f'{distance} mile(s) chosen.')
    print(terrain)
    print(elevation)
    print(route_type)

#add a key to buttons with the same name to differentiate

st.divider()
st.header('Map Data Testing')
#testing

map_service = MapService(GOOGLE_API_KEY)
weather_service = WeatherService(WEATHER_API_KEY)
route_service = RouteService(GOOGLE_API_KEY)
ors_service = ORSService(ORS_API_KEY)

address_origin = st.text_input("Enter origin address")
#address_destination = st.text_input("Enter destination address")

origin_lat = None
#destination_lat = None
origin_long = None
#destination_long = None

#def display_weather(weather_data, location_name)
#future zach, for the large print bodies of code that provide basically the same info, make this definition










if address_origin:

    maps_data_response_ori = map_service.get_coordinates(address_origin)

    if maps_data_response_ori['results']:
        origin_lat = maps_data_response_ori["results"][0]["geometry"]["location"]["lat"]
        origin_long = maps_data_response_ori["results"][0]["geometry"]["location"]["lng"]
        print(f'latitude: {maps_data_response_ori["results"][0]["geometry"]["location"]["lat"]}, longitude: {maps_data_response_ori["results"][0]["geometry"]["location"]["lng"]}')

        weather_data_response_ori = weather_service.get_weather(address_origin)

        st.subheader('Origin Weather')

        st.write(f'Temperature: {weather_data_response_ori['current']['temp_f']}F')  # prints the current temperature (F)
        st.write(f'Humidity: {weather_data_response_ori['current']['humidity']}%')  # prints the current humidity
        st.write(f'Wind Speed: {weather_data_response_ori['current']['wind_mph']} mph {weather_data_response_ori['current']['wind_dir']}')  # prints the current wind speed
        st.write(f'UV: {weather_data_response_ori['current']['uv']}')  # prints the current uv index
    else:
        st.error('Please enter a valid origin address (must be exact)')
        st.stop()
else:
    st.error('Please enter a valid origin address (must be exact)')
    st.stop()



#if address_destination:

    maps_data_response_dest = map_service.get_coordinates(address_destination)

    if maps_data_response_dest['results']:
        destination_lat = maps_data_response_dest["results"][0]["geometry"]["location"]["lat"]
        destination_long = maps_data_response_dest["results"][0]["geometry"]["location"]["lng"]

        weather_data_response_dest = weather_service.get_weather(address_destination)

        st.subheader('Destination Weather')

        st.write(f'Temperature: {weather_data_response_dest['current']['temp_f']}F')  # prints the current temperature (F)
        st.write(f'Humidity: {weather_data_response_dest['current']['humidity']}%')  # prints the current humidity
        st.write(
            f'Wind Speed: {weather_data_response_dest['current']['wind_mph']} mph {weather_data_response_dest['current']['wind_dir']}')  # prints the current wind speed
        st.write(f'UV: {weather_data_response_dest['current']['uv']}')  # prints the current uv index

        map_data_vis ={
                "lat": [origin_lat],
                "lon": [origin_long],
        }
        st.map(map_data_vis)
    else:
        st.error('Please enter a valid destination address (must be exact)')
        st.stop()

#data = {
#    "origin": {
 #       "location": {
 #           "latLng": {
 #               "latitude": origin_lat,
 #               "longitude": origin_long
 #           }
 #       }
  #  },

 #   "destination": {
#        "location": {
 #           "latLng": {
  #              "latitude": destination_lat,
  #              "longitude": destination_long
  #          }
#        }
 #   },

 #       "travelMode": "WALK"
#}


#routes_data_response = route_service.get_route(data)

#if routes_data_response:
#    meters = int(routes_data_response['routes'][0]['distanceMeters'])
#    miles = round(meters / 1609.344, 2)

#    print(f'Distance: {miles} mi')
#    st.write(f'Distance: {miles} mi')

#    duration = int(routes_data_response['routes'][0]['duration'][0:-1])

#    seconds = duration % 60
#    minutes = duration // 60

#    print(f'Time: {minutes} minutes and {seconds} seconds')
#    st.write(f'Time: {minutes} minutes and {seconds} seconds')
#else:
#    st.error("Could not calculate a route.")

#streamlit run src/app.py

#st.title()
#st.header()
#st.subheader()
#st.markdown()
#st.caption()
#st.progress()


#code_example =
#def greet(name)
    #print('hello', name)

#st.code(code_example, language='python'))

#st.divider()





route_generator = RouteGenerator(ors_service)
if distance_float <= 3:
    route_data_sec1 = route_generator.generate_small_loop_sec1(
        origin_lat,
        origin_long,
        distance_float
    )
    route_data_sec2 = route_generator.generate_small_loop_sec2(
        origin_lat,
        origin_long,
        distance_float
    )
elif 3 < distance_float <= 6:
    route_data_sec1 = route_generator.generate_long_loop_sec1(
        origin_lat,
        origin_long,
        distance_float
    )
    route_data_sec2 = route_generator.generate_long_loop_sec2(
        origin_lat,
        origin_long,
        distance_float
    )
elif 6 < distance_float <= 12:
    route_data_sec1 = route_generator.generate_longer_loop_sec1(
        origin_lat,
        origin_long,
        distance_float
    )
    route_data_sec2 = route_generator.generate_longer_loop_sec2(
        origin_lat,
        origin_long,
        distance_float
    )
elif 12 < distance_float <= 20:
    route_data_sec1 = route_generator.generate_super_loop_sec1(
        origin_lat,
        origin_long,
        distance_float
    )
    route_data_sec2 = route_generator.generate_super_loop_sec2(
        origin_lat,
        origin_long,
        distance_float
    )
elif 20 < distance_float <= 30:
    route_data_sec1 = route_generator.generate_ultra_loop_sec1(
        origin_lat,
        origin_long,
        distance_float
    )
    route_data_sec2 = route_generator.generate_ultra_loop_sec2(
        origin_lat,
        origin_long,
        distance_float
    )

if route_data_sec1 is None:
    st.error("Could not generate route.")
    st.stop()
if route_data_sec2 is None:
    st.error("Could not generate route.")
    st.stop()

print(route_data_sec1)
distance_meters_sec1 = route_data_sec1['routes'][0]['summary']['distance']
distance_miles_sec1 = distance_meters_sec1 / 1609.34
print(distance_miles_sec1)
duration_minutes_sec1 = route_data_sec1['routes'][0]['summary']['duration'] / 60
print(duration_minutes_sec1)
polyline_sec1 = route_data_sec1['routes'][0]['geometry']
print(polyline_sec1)

print(route_data_sec2)
distance_meters_sec2 = route_data_sec2['routes'][0]['summary']['distance']
distance_miles_sec2 = distance_meters_sec2 / 1609.34
print(distance_miles_sec2)
duration_minutes_sec2 = route_data_sec2['routes'][0]['summary']['duration'] / 60
print(duration_minutes_sec2)
polyline_sec2 = route_data_sec2['routes'][0]['geometry']
print(polyline_sec2)
