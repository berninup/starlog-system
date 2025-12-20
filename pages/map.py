import streamlit as st
import pandas as pd
from main import fetch_asteroid_data
import os
from dotenv import load_dotenv
import datetime

load_dotenv()
api_key = os.getenv("NASA_API_KEY")

st.title("🛸 Tactical Map: Sector Scan")

today = datetime.date.today()
asteroids = fetch_asteroid_data(api_key, today, today)
daily_data = asteroids["near_earth_objects"].get(str(today), [])

if daily_data:
    chart_data = []
    
    for asteroid in daily_data:
        chart_data.append({
            "name": asteroid['name'],
            "size": float(asteroid['estimated_diameter']['meters']['estimated_diameter_max']),
            "velocity": float(asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']),
            "miss_distance": float(asteroid['close_approach_data'][0]['miss_distance']['kilometers'])
        })

    df = pd.DataFrame(chart_data)

    st.scatter_chart(
        df,
        x='miss_distance',
        y='velocity',
        size='size',
        color='#ff4b4b'
    )
    
    st.caption("X-Axis: Distance (km) | Y-Axis: Speed (kph) | Bubble Size: Asteroid Diameter (m)")
else:
    st.warning("No asteroids detected in this sector today.")    
