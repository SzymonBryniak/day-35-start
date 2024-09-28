import requests

api_key = "458f91702912ebbea1aea9bbdd8f4ace"
endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
params = {
    "lat": 52.2021814,
    "lon": -2.2248693,
    "cnt": 4,
    "appid": api_key

}
response = requests.get(endpoint, params=params)
response.raise_for_status()
print(response.json())
print(response.status_code)
my_weather = response.json()['list']


def check_precipitation(weather):
    for i in weather:
        for key, value in i.items():
            if key == "weather":
                for ii in value:
                    if ii.get('id') < 700:
                        print('Bring umbrella', ii.get('id'))
                    else:
                        print(ii.get('main'))
            if key == "dt_txt":
                print(value)


check_precipitation(my_weather)
