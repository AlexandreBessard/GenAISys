from genaisys import make_openai_api_call
from genaisys.reason.reason import CITY_EXTRACTION_PROMPT
from genaisys.weather.weather_location import weather_location


def handle_weather(user_message):
    query = user_message['content']
    city = make_openai_api_call(query, mcontent=CITY_EXTRACTION_PROMPT)
    try:
        current_temp, current_weather_desc, wind_speed = weather_location(city)
        response = f"Current Temperature in {city}: {current_temp}°C\nWeather: {current_weather_desc}\nWind Speed: {wind_speed} m/s"
        print(response)
        return response
    except ValueError as e:
        return str(e)
