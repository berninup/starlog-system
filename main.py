import os
import requests
from dotenv import load_dotenv
from datetime import date


load_dotenv()

nasa_api_key = os.getenv("NASA_API_KEY")
today = date.today()
print("Today's date:", today)
start_date = today
end_date = today

r = requests.get(f'https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={nasa_api_key}')

data = r.json()

print(data['near_earth_objects'][str(today)])



for asteroid in data['near_earth_objects'][str(today)]:
    name = asteroid['name']
    hazardous = asteroid['is_potentially_hazardous_asteroid']
    if hazardous == True:
        hazardous_stat = "Hostile Detected"
    else:
        hazardous_stat = "Safe"
    diameter_meters = asteroid['estimated_diameter']['meters']['estimated_diameter_max']
    velocity_kph = asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']
    print(f"Asteroid {name}: Danger: {hazardous_stat} Size: {diameter_meters} meters Speed: {velocity_kph} kph")
    