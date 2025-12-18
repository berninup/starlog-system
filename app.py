import streamlit as st
import datetime
from main import fetch_asteroid_data, format_asteroid_data
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("NASA_API_KEY")

st.title("🚀 Star-Log: Asteroid Radar")

search_date = st.date_input("Select Scan Dtate", datetime.date.today())

if st.button("Scan Sector"):
    asteroids = fetch_asteroid_data(api_key, search_date, search_date)
    
    today_str = str(search_date)
    daily_data = asteroids['near_earth_objects'].get(today_str, [])
    
    st.write(f"Found {len(daily_data)} asteroids.")
    
    for asteroid in daily_data:
        stat_block = format_asteroid_data(asteroid)
        st.write(stat_block)