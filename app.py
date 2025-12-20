import streamlit as st
import datetime
from main import fetch_asteroid_data, format_asteroid_data, fetch_potd
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("NASA_API_KEY")
photo = fetch_potd(api_key)

st.title("🚀 Star-Log: Asteroid Radar 🚀")

st.image(photo['hdurl'], width=700) 
search_date = st.date_input("Select Scan Date", datetime.date.today())

if st.button("Scan Sector"):
    asteroids = fetch_asteroid_data(api_key, search_date, search_date)
    
    today_str = str(search_date)
    daily_data = asteroids['near_earth_objects'].get(today_str, [])
    
    st.write(f"Found {len(daily_data)} asteroids.")
    
    for asteroid in daily_data:
        col1, col2, col3 = st.columns(3)
        stat_block = format_asteroid_data(asteroid)
        if stat_block['hazardous_stat'] == True:
            delta = 'Dangerous'
            d_color = "inverse"
        else:
            delta = 'Safe'
            d_color = "normal"         
        col1.metric('Name',stat_block['name'], delta = delta, delta_arrow = "off", delta_color = d_color)
        col2.metric('Velocity',f'{float(stat_block["velocity_kph"]):.2f}')
        col3.metric('Size in Meters',f'{float(stat_block["diameter_meters"]):.2f}')
        
        st.divider()