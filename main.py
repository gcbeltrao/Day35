import requests

API_KEY = "a83eb51cdd61e6fd7a63d94f50aaf5d2"

parameters = {
    "lat": -8.055190,
    "lon": -34.871181,
    "cnt": 4,
    "appid": API_KEY,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
weather_list = data["list"]


def check_weather():
    for item in weather_list:
        weather = item["weather"][0]["id"]
        if weather <= 700:
            return True


if check_weather():
    print("Bring an umbrella.")
