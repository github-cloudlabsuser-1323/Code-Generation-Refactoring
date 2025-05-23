import os
import requests

API_KEY = os.environ.get('OPENWEATHER_API_KEY')  # Get API key from environment variable
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    if not API_KEY:
        print("Error: OPENWEATHER_API_KEY environment variable not set.")
        return None
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather = get_weather(city)
    if weather:
        print(f"Weather in {city}: {weather['weather'][0]['description']}")
        print(f"Temperature: {weather['main']['temp']}°C")
        print(f"Humidity: {weather['main']['humidity']}%")