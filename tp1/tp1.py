import os
import requests

def get_weather_info(lat: float, lon: float, api_key) -> str:
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    req = requests.get(url)
    data = req.json()
    temperature = data["main"]["temp"] - 273.15
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    wind_speed = data["wind"]["speed"]
    wind_deg = data["wind"]["deg"]
    weather_info = (
        f"A Paris, la température est de {temperature:.1f}°C et le temps est {description}.\n"
        f"L'humidité à Paris est de {humidity} %.\n"
        f"La pression atmosphérique à Paris est de {pressure} hPa.\n"
        f"La vitesse du vent à Paris est de {wind_speed} m/s et sa direction est de {wind_deg} degrés."
    )
    return weather_info

lat = float(os.getenv("LAT", "48.8534"))
lon = float(os.getenv("LONG", "2.3488"))
api = os.getenv("API_KEY", "")
print(get_weather_info(lat, lon, api))