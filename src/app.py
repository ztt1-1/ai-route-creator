import string
import folium
import polyline

import streamlit as st
from streamlit_folium import st_folium

from services.map_service import MapService
from services.routes_service import RouteService
from services.weather_service import WeatherService
from services.ORS_routes_service import ORSService
from services.api import GOOGLE_API_KEY, ORS_API_KEY, WEATHER_API_KEY

from algorithm.route_generator import RouteGenerator
from algorithm.route_scoring import find_closest_route

#creates basis to save map input so when the website is refreshed, the map does not disappear, etc.
if "origin_key" not in st.session_state:
    st.session_state.origin_key = None

if "selected_route" not in st.session_state:
    st.session_state.selected_route = None

if "route_key" not in st.session_state:
    st.session_state.route_key = None

st.title('AI-Running-Route-Creator')
#description -----------------------------------------------
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
#customization ---------------------------------------------
st.header('Customization (WIP)')

terrain = st.selectbox("Terrain", ["Road", "Trail", "Sidewalk"])
elevation = st.selectbox("Route Elevation", ["Flat", "Rolling Hills", "Hilly"])
route_type = st.selectbox("Route Type", ["Out-and-Back", "Loop"])

st.divider()

distance_float = None
#input and input checking
st.header('Distance')

distance = st.text_input('Desired distance (in miles)')

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = string.punctuation.replace(".", "") #removes period from special characters to prevent false negatives

if distance:

    distance_float = float(distance)

    has_letter = False
    has_spec = False
    extra_dot = False

    #letter/special character check (user response must only be a number)
    for char in distance:

        if char in alphabet:
            has_letter = True
            break

        if char in special_characters:
            has_spec = True
            break

    #dot check (prevents responses like 1.1.1 or 1..1)
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


#services ----------------------------------------
map_service = MapService(GOOGLE_API_KEY)
weather_service = WeatherService(WEATHER_API_KEY)
route_service = RouteService(GOOGLE_API_KEY)
ors_service = ORSService(ORS_API_KEY)


#origin -----------------------------------------
st.divider()

st.header('Map Data Testing')

address_input = st.text_input("Enter origin address")

origin_lat = None
origin_long = None

#origin geocode -----------------------------------
if address_input:

    if st.session_state.origin_key != address_input:

        maps_data_response_ori = map_service.get_coordinates(address_input)

        unchanging_map_dat = maps_data_response_ori["results"][0]["geometry"]["location"]

        if maps_data_response_ori["results"]:

            origin_lat = (unchanging_map_dat["lat"])
            origin_long = (unchanging_map_dat["lng"])

            #get weather only when the address changes
            weather_data_response_ori = (weather_service.get_weather(address_input))

            st.session_state.origin_data = {
                "lat": origin_lat,
                "long": origin_long,
                "weather": weather_data_response_ori
            }

            st.session_state.origin_key = address_input

        else:

            st.error("Please enter a valid origin address (must be exact)")
            st.stop()

    else:

        origin_lat = st.session_state.origin_data["lat"]
        origin_long = st.session_state.origin_data["long"]

else:

    st.error("Please enter a valid origin address (must be exact)")
    st.stop()

#display origin weather -----------------------------------------
if st.session_state.origin_data is not None:

    weather_data_response_ori = (st.session_state.origin_data["weather"])

    st.subheader("Origin Weather")

    unchanging_weather_dat = weather_data_response_ori['current']

    st.write(f"Temperature: {unchanging_weather_dat['temp_f']}F")

    st.write(f"Humidity: {unchanging_weather_dat['humidity']}%")

    st.write(f"Wind Speed: {unchanging_weather_dat['wind_mph']} mph {unchanging_weather_dat['wind_dir']}")

    st.write(f"UV: {unchanging_weather_dat['uv']}")

#find route, the route gen code is in the button -------------------------------------------

button2_press = st.button('Find Route', key="find_route_1")

if "route_data_sec1" not in st.session_state:
    st.session_state.route_data_sec1 = None

if "route_data_sec2" not in st.session_state:
    st.session_state.route_data_sec2 = None

if "route_data_sec3" not in st.session_state:
    st.session_state.route_data_sec3 = None

if "route_data_sec4" not in st.session_state:
    st.session_state.route_data_sec4 = None

route_data_sec1 = st.session_state.route_data_sec1
route_data_sec2 = st.session_state.route_data_sec2
route_data_sec3 = st.session_state.route_data_sec3
route_data_sec4 = st.session_state.route_data_sec4

if button2_press and distance and not has_letter and not has_spec and not extra_dot and 0 < float(distance) <= 30:

    #only for debug
    print(f'{distance} mile(s) chosen.')
    print(terrain)
    print(elevation)
    print(route_type)

    route_generator = RouteGenerator(ors_service)

    route_dat = origin_lat, origin_long, distance_float

    #small_loop gen
    if distance_float <= 3:
        st.session_state.route_data_sec1 = route_generator.generate_small_loop_sec1(origin_lat, origin_long, distance_float)
        st.session_state.route_data_sec2 = route_generator.generate_small_loop_sec2(origin_lat, origin_long, distance_float)
        st.session_state.route_data_sec3 = route_generator.generate_small_loop_sec3(origin_lat, origin_long, distance_float)
        st.session_state.route_data_sec4 = route_generator.generate_small_loop_sec4(origin_lat, origin_long, distance_float)
    #long_loop gen
    elif 3 < distance_float <= 6:
        st.session_state.route_data_sec1 = route_generator.generate_long_loop_sec1(origin_lat, origin_long, distance_float)
        st.session_state.route_data_sec2 = route_generator.generate_long_loop_sec2(origin_lat, origin_long, distance_float)
        st.session_state.route_data_sec3 = route_generator.generate_long_loop_sec3(origin_lat, origin_long, distance_float)
        st.session_state.route_data_sec4 = route_generator.generate_long_loop_sec4(origin_lat, origin_long, distance_float)
    #longer_loop gen
    elif 6 < distance_float <= 12:
        st.session_state.route_data_sec1 = route_generator.generate_longer_loop_sec1(origin_lat, origin_long, distance_float)
        st.session_state.route_data_sec2 = route_generator.generate_longer_loop_sec2(origin_lat, origin_long, distance_float)
        st.session_state.route_data_sec3 = route_generator.generate_longer_loop_sec3(origin_lat, origin_long, distance_float)
        st.session_state.route_data_sec4 = route_generator.generate_longer_loop_sec4(origin_lat, origin_long, distance_float)
    #super_loop gen
    elif 12 < distance_float <= 20:
        st.session_state.route_data_sec1 = route_generator.generate_super_loop_sec1(origin_lat, origin_long, distance_float)
        st.session_state.route_data_sec2 = route_generator.generate_super_loop_sec2(origin_lat, origin_long, distance_float)
        st.session_state.route_data_sec3 = route_generator.generate_super_loop_sec3(origin_lat, origin_long, distance_float)
        st.session_state.route_data_sec4 = route_generator.generate_super_loop_sec4(origin_lat, origin_long, distance_float)
    #ultra_loop gen
    elif 20 < distance_float <= 30:
        st.session_state.route_data_sec1 = route_generator.generate_ultra_loop_sec1(origin_lat, origin_long, distance_float)
        st.session_state.route_data_sec2 = route_generator.generate_ultra_loop_sec2(origin_lat, origin_long, distance_float)
        st.session_state.route_data_sec3 = route_generator.generate_ultra_loop_sec3(origin_lat, origin_long, distance_float)
        st.session_state.route_data_sec4 = route_generator.generate_ultra_loop_sec4(origin_lat, origin_long, distance_float)

    route_data_sec1 = st.session_state.route_data_sec1
    route_data_sec2 = st.session_state.route_data_sec2
    route_data_sec3 = st.session_state.route_data_sec3
    route_data_sec4 = st.session_state.route_data_sec4

    if route_data_sec1 is None or route_data_sec2 is None or route_data_sec3 is None or route_data_sec4 is None:
        st.error("Could not generate route.")
        st.stop()

    route_distances = [route_data_sec1, route_data_sec2, route_data_sec3, route_data_sec4]

    closest_difference = find_closest_route(distance_float, route_distances)

    st.session_state.selected_route = closest_difference[0]

def bulk_info(route_data_secNum):
    distance_meters = route_data_secNum['routes'][0]['summary']['distance']
    distance_miles = distance_meters / 1609.34
    duration_minutes = route_data_secNum['routes'][0]['summary']['duration'] / 60
    polyline = route_data_secNum['routes'][0]['geometry']

    return distance_miles, duration_minutes, polyline

if (route_data_sec1 is not None and route_data_sec2 is not None and route_data_sec3 is not None and route_data_sec4 is not None):
    distance1, duration1, polyline1 = bulk_info(route_data_sec1)
    distance2, duration2, polyline2 = bulk_info(route_data_sec2)
    distance3, duration3, polyline3 = bulk_info(route_data_sec3)
    distance4, duration4, polyline4 = bulk_info(route_data_sec4)

#save the selected route --------------------------
selected_route = st.session_state.selected_route

#save the inputs that produced this route (WIP) -----
#st.session_state.route_key = (
#    origin_lat,
#    origin_long,
#    distance_float,
#    terrain,
#    elevation,
#    route_type
#)

if st.session_state.selected_route is not None:
    #debug
    print(f"{st.session_state.selected_route['summary']['distance'] / 1609.34:.2f} MILES.")

    print(st.session_state.selected_route["geometry"])

    #display route with map ----------------------------------------------------
if st.session_state.selected_route is not None:

    selected_route = st.session_state.selected_route

    distance_miles = (
        selected_route["summary"]["distance"] / 1609.34
    )

    st.subheader(f"{distance_miles:.2f} MILES.")

    geometry = selected_route["geometry"]

    route_points = polyline.decode(geometry)

    m = folium.Map(
        location=route_points[0],
        zoom_start=14
    )

    folium.PolyLine(
        locations=route_points,
        weight=5
    ).add_to(m)

    m.fit_bounds(route_points)

    st_folium(
        m,
        width=700,
        height=500
    )

#add a key to buttons with the same name to differentiate

#def display_weather(weather_data, location_name)
#future zach, for the large print bodies of code that provide basically the same info, make this definition