import os

import requests
from ..config import settings

def weather_location(city_name):
    # Fetch the API key from environment variables
    api_key = settings.WEATHER_KEY
    if not api_key:
      raise ValueError("API Key is not set. Please check your initialization.")
    # OpenWeatherMap API URL for city name
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={api_key}"
    # Fetch real-time weather data
    response = requests.get(url)
    weather_data = response.json()
    # Check for API errors
    if response.status_code != 200 or 'main' not in weather_data:
        error_msg = weather_data.get('message', 'Unknown error')
        raise ValueError(f"Could not get weather for '{city_name}': {error_msg}")
    # Extract relevant data
    current_temp = weather_data['main']['temp']
    current_weather_desc = weather_data['weather'][0]['description']
    wind_speed = weather_data['wind']['speed']
    return current_temp, current_weather_desc, wind_speed