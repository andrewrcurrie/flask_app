from flask import Flask, render_template, request
import forecastio
from geopy.geocoders import Nominatim

def get_weather(address):
    api_key = "db962f89bf7355f0fe6f2ab6a09b5f64"
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude
    forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
    summary = forecast.summary
    temperature = forecast.temperature
    return "{} and {}° at {}".format(summary, temperature, address)

app = Flask(__name__)

@app.route("/")
def index():
    address = request.values.get('address')
    forecast = None
    if address:
        forecast = weather.get_weather(address)
    return render_template('index.html', forecast=forecast)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run()