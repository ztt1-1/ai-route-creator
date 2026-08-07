import streamlit as st
import pandas as pd
from services.map_service import Map_Service
from services.api import GOOGLE_MAPS_API_KEY

st.title('AI-Running-Route-Creator')

st.divider()

st.header('Customization')

terrain = st.selectbox("Terrain", ["Road", "Trail", "Sidewalk"])
elevation = st.selectbox("Route Elevation", ["Flat", "Rolling Hills", "Hilly"])
route_type = st.selectbox("Route Type", ["Out-and-Back", "Loop"])

st.divider()

st.header('Distance (slider)')
distance = st.slider('Desired distance (in miles)', min_value=1, max_value=30, value=5)
st.write(f'You chose **{distance} mile(s)**')

button1_press = st.button('Find Route', key="find_route_1")

if button1_press:
    print(f'{distance} mile(s) chosen.')
    print(terrain)
    print(elevation)
    print(route_type)

st.divider()

st.header('Distance (text input)')
distance_deci = st.text_input('Desired distance (in miles)', value=distance)

if int(float(distance_deci)) <= 0 or int(float(distance_deci)) > 30:
    st.write('Choose a distance greater than 0 or less than 30.')
else:
    st.write(f'You chose **{distance_deci} mile(s)**')


button2_press = st.button('Find Route', key="find_route_2")
if button2_press and 0 <= int(float(distance_deci)) <= 30:
    print(f'{distance_deci} mile(s) chosen.')
    print(terrain)
    print(elevation)
    print(route_type)

#add a key to buttons with the same name to differentiate






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
st.header('Map Data Testing')

#testing

map_service = Map_Service(GOOGLE_MAPS_API_KEY)
address = st.text_input("Enter your address")


if address:
    maps_data_response = map_service.get_coordinates(address)

    origin_lat = maps_data_response["results"][0]["geometry"]["location"]["lat"]
    origin_long = maps_data_response["results"][0]["geometry"]["location"]["lng"]


    map_data_vis = pd.DataFrame(
        {
            "lat": [origin_lat],
            "lon": [origin_long]
        }
    )

    st.map(map_data_vis)
else:
    st.write('Please enter a valid address (must be exact)')

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