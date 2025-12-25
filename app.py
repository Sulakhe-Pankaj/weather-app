from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "6b189d8e39f3db314535cb0434efbc31"
DEFAULT_CITY = "Delhi"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={API_KEY}"
    try:
        data = requests.get(url, timeout=5).json()
        if data.get("cod") != 200:
            return None
        return {
            "temp": data["main"]["temp"],
            "weather": data["weather"][0]["description"],
            "min_temp": data["main"]["temp_min"],
            "max_temp": data["main"]["temp_max"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "wind_speed": data["wind"]["speed"],
            "icon": data["weather"][0]["icon"],
            "city_name": city
        }
    except:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    city = DEFAULT_CITY
    error = None

    if request.method == 'POST':
        city_input = request.form.get('name', '').strip()
        if city_input:
            city = city_input
        else:
            error = "City name cannot be empty"
            city = DEFAULT_CITY

    weather_data = get_weather(city)

    if not weather_data:
        error = "City not found"
        weather_data = get_weather(DEFAULT_CITY)

    return render_template(
        'index.html',
        temp=weather_data["temp"],
        weather=weather_data["weather"],
        min_temp=weather_data["min_temp"],
        max_temp=weather_data["max_temp"],
        humidity=weather_data["humidity"],
        pressure=weather_data["pressure"],
        wind_speed=weather_data["wind_speed"],
        icon=weather_data["icon"],
        city_name=weather_data["city_name"],
        error=error
    )

if __name__ == "__main__":
    app.run(port=5011, debug=True)
