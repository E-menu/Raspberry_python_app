# Import module for GUI weather
import requests, json
# end

# Variables to remember API key , city name and page URL
API_KEY = "8b7c4545e3874014261a301b43f9d144"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
CITY_NAME ="Wrocław"
COMPLETE_URL = BASE_URL + "appid=" + API_KEY + "&q=" + CITY_NAME
# end

# Function, that return weather data
def weather (temperature , pressure, humidity, description):

    # Response from server and getting weather info
    response = requests.get(COMPLETE_URL)
    x = response.json()
    y = x["main"]

    current_temperature_K = y["temp"]
    temperature = round(current_temperature_K-273,2)
    pressure = y["pressure"]
    humidity = y["humidity"]
    z = x["weather"]
    description = z[0]["description"]

    # Returning modified function args
    return (temperature,pressure,humidity,description)
