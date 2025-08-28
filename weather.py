from dotenv import load_dotenv
from pprint import pprint
import requests
import os

# Load .env file
load_dotenv()

def get_current_weather(city="Kansas City"):
    api_key = os.getenv("API_KEY")

    if not api_key:
        return {"error": "API key not found. Please set API_KEY in your .env file."}

    request_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(request_url)

    if response.status_code != 200:
        return {"error": f"Request failed with status {response.status_code}", "details": response.json()}

    return response.json()

if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name: ").strip()

    if not city:
        city = "Kansas City"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)
