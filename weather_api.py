import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API")
CITY = 'New Delhi'

URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"

def fetch_weather_data(city):
    try:
        response = requests.get(URL)
        data = response.json()

        if response.status_code == 200:
            temperature = data['current']['temp_c']  # Temperature in Celsius
            humidity = data['current']['humidity']  # Humidity in percentage
            wind_speed = data['current']['wind_kph']  # Wind speed in km/h
            air_pressure = data['current']['pressure_mb']  # Air pressure in hPa
            precipitation = data['current']['precip_mm']  # Precipitation in mm (last 1 hour)

            weather_data = {
                "temperature": temperature,
                "humidity": humidity,
                "precipitation": precipitation,
                "wind_speed": wind_speed,
                "air_pressure": air_pressure
            }
            return weather_data
        else:
            print(f"Error: {response.status_code}, {data.get('message')}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Fetch the current weather data
current_weather = fetch_weather_data(CITY)
print(current_weather)
