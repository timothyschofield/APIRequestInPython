"""
How to create and launch Python Virtual environment in VS Code

14 October 2023

prob1: Neither python nor pip are recognized in the terminal 
    e.g. python --version does not work

So...Create a virtual environment
    Manage > Command prompt... Python Create Enviroment
    This appears to work because the .venv folder appears 
        - but python and pip is still unknown in the terminal

So...Activate the virtual environment
    In the terminal, navigate to the folder (probably the project folder) 
    that contains the .venv folder
    In the terminal .venv\Scripts\activate
    A green (.venv) should appear to the left of the Terminal prompt
    if the virtual environment is working.
    
https://www.weatherapi.com/ is the address
but the API live at https://api.weatherapi.com/

JSON and XML Weather API and Geolocation Developer API

"""

# pip install requests
import requests

# Need API key e7bf9285cf34491ba03174746231410
url = "https://api.weatherapi.com/v1/current.json?key=e7bf9285cf34491ba03174746231410&q=London&aqi=no"

responce = requests.get(url)
json = responce.json()

print(json)
# Using single quotes for the keys, or strings in general, is breaking the JSON format specification
# And this print returns single quotes - it still works though.

"""
{
  "location": {
    "name": "London",
    "region": "City of London, Greater London",
    "country": "United Kingdom",
    "lat": 51.52,
    "lon": -0.11,
    "tz_id": "Europe/London",
    "localtime_epoch": 1697306570,
    "localtime": "2023-10-14 19:02"
  },
  "current": {
    "last_updated_epoch": 1697306400,
    "last_updated": "2023-10-14 19:00",
    "temp_c": 9,
    "temp_f": 48.2,
    "is_day": 0,
    "condition": {
      "text": "Partly cloudy",
      "icon": "//cdn.weatherapi.com/weather/64x64/night/116.png",
      "code": 1003
    },
    "wind_mph": 8.1,
    "wind_kph": 13,
    "wind_degree": 280,
    "wind_dir": "W",
    "pressure_mb": 1020,
    "pressure_in": 30.12,
    "precip_mm": 0,
    "precip_in": 0,
    "humidity": 81,
    "cloud": 25,
    "feelslike_c": 7.4,
    "feelslike_f": 45.2,
    "vis_km": 10,
    "vis_miles": 6,
    "uv": 1,
    "gust_mph": 9.4,
    "gust_kph": 15.2
  }
}

"""




