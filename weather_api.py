import requests
import numpy as np
import os
from dotenv import load_dotenv
from weather_classification import classifier_model

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


# min and max values of each feature from the training data
min_values = {'temperature': -10, 'humidity': 0.002, 'precipitation': 0.000425, 'wind_speed': 0.00669, 'air_pressure': 950}
max_values = {'temperature': 40, 'humidity': 100, 'precipitation': 100, 'wind_speed': 100, 'air_pressure': 1050}

def normalize_value(value, min_value, max_value):
    return (value - min_value) / (max_value - min_value)

def normalize_real_time_data(weather_data):
    normalized_data = {}
    normalized_data['temperature'] = normalize_value(weather_data['temperature'], min_values['temperature'], max_values['temperature'])
    normalized_data['humidity'] = normalize_value(weather_data['humidity'], min_values['humidity'], max_values['humidity'])
    normalized_data['wind_speed'] = normalize_value(weather_data['wind_speed'], min_values['wind_speed'], max_values['wind_speed'])
    normalized_data['air_pressure'] = normalize_value(weather_data['air_pressure'], min_values['air_pressure'], max_values['air_pressure'])
    normalized_data['precipitation'] = normalize_value(weather_data['precipitation'], min_values['precipitation'], max_values['precipitation'])
    return normalized_data

# Fetch real-time weather data
current_weather = fetch_weather_data(CITY)

if current_weather:
    # Normalize the real-time data
    normalized_weather_data = normalize_real_time_data(current_weather)

    # Convert to numpy array for model prediction
    features = np.array([[normalized_weather_data['temperature'],
                          normalized_weather_data['humidity'],
                          normalized_weather_data['precipitation'],
                          normalized_weather_data['wind_speed'],
                          normalized_weather_data['air_pressure']]])

    # Make a prediction using the model
    clf = classifier_model()

    prediction = clf.predict(features)

    if prediction[0] == 1:
        print("Risk of vector-borne disease spread!")
    else:
        print("No immediate risk of vector-borne disease spread.")
