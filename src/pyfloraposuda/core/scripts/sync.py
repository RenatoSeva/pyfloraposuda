import random
import json
import requests



def sync(indoor: bool):
    tmp = get_tmp(indoor)
    ph = get_ph()
    humidity = get_humidity()
    brightness = get_brightness()
    dictionary = {
    "tmp": tmp,
    "ph": ph,
    "brightness": brightness,
    "humidity": humidity
    }

    json_object = json.dumps(dictionary, indent=4)
    return json_object

def get_tmp(indoor):

    if indoor:
        return round(random.uniform(18.0,25.0),2)
    else:
        url_tmp = "https://goweather.herokuapp.com/weather/zagreb"
        tmp = requests.get(url = url_tmp)
        data = tmp.json()
        if data is not None:
            tmp = data["temperature"]
            splitdata = tmp.split(" ")
            return splitdata[0]
    return round(random.uniform(-10.0,40.0),2)

def get_ph():
    return round(random.uniform(5.5,7.5),2)
    

def get_humidity() :
    return random.randint(0,200)

def get_brightness():
    return random.randint(1,5)