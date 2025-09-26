# src/weather.py
import os
import sys
import logging
from typing import Optional
import requests
from dotenv import load_dotenv

# set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# load .env (will not overwrite already-set env vars)
load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city: str, api_key: Optional[str] = None, units: str = "metric") -> dict:
    """Fetch current weather for `city` from OpenWeatherMap.
    Returns parsed JSON on success, raises RuntimeError on failure.
    """
    key = api_key or API_KEY
    if not key:
        raise RuntimeError("No WEATHER_API_KEY found in environment")

    params = {"q": city, "appid": key, "units": units}
    try:
        resp = requests.get(BASE_URL, params=params, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as e:
        logger.exception("Request failed for city=%s", city)
        raise RuntimeError(f"Weather API request failed: {e}") from e

    data = resp.json()
    # Basic sanity check
    if "weather" not in data or "main" not in data:
        raise RuntimeError(f"Unexpected response structure: {data}")
    return data

def pretty_print_weather(data: dict) -> None:
    city = data.get("name")
    main = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    feels_like = data["main"].get("feels_like")
    print(f"🌦️  Weather in {city}: {main}")
    print(f"🌡️  Temperature: {temp} °C (feels like {feels_like} °C)")

def main():
    if len(sys.argv) < 2:
        print("Usage: python src/weather.py CITY_NAME")
        sys.exit(2)
    city = " ".join(sys.argv[1:])
    data = fetch_weather(city)
    pretty_print_weather(data)

if __name__ == "__main__":
    main()
