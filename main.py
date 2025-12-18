import os
import requests
from dotenv import load_dotenv
from datetime import date

load_dotenv()

def fetch_asteroid_data(api_key, start_date, end_date):
    response = requests.get(
        f'https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}'
    )
    return response.json()

def format_asteroid_data(asteroid):
    name = asteroid['name']
    hazardous = asteroid['is_potentially_hazardous_asteroid']
    hazardous_stat = "Hostile Detected" if hazardous else "Safe"
    diameter_meters = asteroid['estimated_diameter']['meters']['estimated_diameter_max']
    velocity_kph = asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']
    print(f"Asteroid {name}: Danger: {hazardous_stat} Size: {diameter_meters} meters Speed: {velocity_kph} kph")
    return f"Asteroid {name}: Danger: {hazardous_stat} Size: {diameter_meters} meters Speed: {velocity_kph} kph"
    

if __name__ == "__main__":
    today = date.today()
    api_key = os.getenv("NASA_API_KEY")
    asteroids = fetch_asteroid_data(api_key, today, today)
    for asteroid in asteroids['near_earth_objects'][str(today)]:
        format_asteroid_data(asteroid)
        





