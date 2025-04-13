import requests
import json
import time
import os
from dotenv import load_dotenv
load_dotenv() 

def discord(a):
    webhook_url = os.getenv('WEBHOOK_ID')
    if a==0:
        message = {
        "content": "雷がなっているのでフィードを停止しました。"
    }
    if a==1:
        message = {
        "content": "雷が止んだのでフィードを再開しました。"
    }


    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(webhook_url, data=json.dumps(message), headers=headers)

    if response.status_code == 204:
        print("メッセージを送信しました！")
    else:
        print(f"エラーが発生しました: {response.status_code}")


def getweather():
    city_name = "chofu" # 主要な都市名はいけるっぽい。
    API_KEY = os.getenv('WEATHER_API') # xxxに自分のAPI Keyを入力。
    api = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={key}"

    url = api.format(city = city_name, key = API_KEY)
    print(url)
    response = requests.get(url)
    data = response.json()
    print(data["weather"][0]["main"])
    weather = data["weather"][0]["main"]
    return weather


def disconect():
    print('disconect')

def conect():
    print('conect')


# 0 = disconect
# 1 = conect
situacion = 0
while True:
    weather = getweather()
    if weather == "Thunderstorm":
        if situacion == 1:
            disconect()
            discord(0)
            situacion = 0
    elif weather != "Thunderstorm" and situacion == 0:
        conect()
        discord(1)
        situacion = 1
    time.sleep(300)