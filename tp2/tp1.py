import os
import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/weather', methods=["GET"])
def get_weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    api_key = os.getenv("API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    req = requests.get(url)
    data = req.json()

    temperature = data.get("main", {}).get("temp", 0) - 273.15
    description = data["weather"][0]["description"] if data.get("weather") else ""
    humidity = data.get("main", {}).get("humidity", 0) 
    pressure = data.get("main", {}).get("pressure", 0) 

    wind_speed = data.get("wind", {}).get("speed", 0)
    wind_deg = data.get("wind", {}).get("deg", 0)
    weather_info = (
        f"La temperature est de {temperature:.1f}°C et le temps est {description}.\n"
        f"L'humidite est de {humidity} %.\n"
        f"La pression atmosphérique est de {pressure} hPa.\n"
        f"La vitesse du vent est de {wind_speed} m/s et sa direction est de {wind_deg} degrés."
    )
    return {"weather_info": weather_info}

if __name__ == '__main__':
    app.run(debug= True, host='0.0.0.0', port=8081)