import requests
import smtplib


password = "aruj ltqt spax soaw"
username = "szymonbryniakproject@gmail.com"
to_addrs = "oneplusszymonbryniak@gmail.com"

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


def send_email(message):
    message = "Subject: TEST \n\n {}".format(str(message))
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(username, to_addrs, msg=message)


def check_precipitation(weather):
    to_send = []

    for i in weather:
        for key, value in i.items():
            if key == "weather":
                for ii in value:
                    if ii.get('id') < 700:
                        print('Bring umbrella', ii.get('id'))
                        to_send.append(f'Bring umbrella {ii.get('id')}')
                    else:
                        print(ii.get('main'))
                        to_send.append(ii.get('main'))
            if key == "dt_txt":
                print(value)
                to_send.append(value)
    send_email(to_send)


check_precipitation(my_weather)

