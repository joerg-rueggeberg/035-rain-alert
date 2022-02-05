import requests
from mail_config import send_mail

# ---------------------------------- API CONFIG ----------------------------------
parameters = {
    "lat": 0,
    "lon": 0,
    "units": "metric",
    "appid": "YOUR-API-ID",
    "exclude": "current,minutely,daily",
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

# ---------------------------------- DATA CONFIG ----------------------------------
data = response.json()
data_id_12 = []

for i in data["hourly"]:
    if data["hourly"].index(i) <= 11:
        data_id_12.append(data["hourly"][data["hourly"].index(i)]["weather"][0]["id"])


# ---------------------------------- WEATHER CHECK ----------------------------------
def check_weather():
    """ Checks if it will rain in the next 12 hours by comparing the weather ids. Sends an E-Mail afterwards."""
    rain = 0

    for wid in data_id_12:
        if wid < 700:
            rain = 1

    if rain == 1:
        return send_mail("Bring an umbrella. It will rain today!", "☹")
    else:
        return send_mail("No umbrella needed. No rain today!", "😀")


check_weather()
