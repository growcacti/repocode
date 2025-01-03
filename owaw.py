#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
script to query openweather and accuweather
"""

# pylint: skip-file

# TODO: UNIFINISHED
#
# pylint: disable=unreachable
# pylint: disable=undefined-variable
# pylint: disable=unused-variable

import os
import json
from datetime import datetime
import requests
from myutil import write_json


def getapikey(keyname):
    """get api key"""
    debug = False
    keyfn = os.environ["HOME"] + "/Private/" + "owaw-keys.json"
    with open(keyfn) as keyfile:
        data = json.load(keyfile)
    if debug:
        print(json.dumps(data))
    return data["keys"][keyname]["key"]


def my_write_json(filename, jsondata):
    """output json data to file"""
    write_json(filename, jsondata)
    print("query_openweather: output to {0}".format(filename))


def k2c(k):
    """
    k [in] temperature in k
    return c
    """
    return k - 273.15


def query_openweather(latitude, longitude):
    """
    https://openweathermap.org/api
    """
    debug = False
    appid = getapikey("openweather")
    # print('appid: '+appid)
    payload = {"lat": latitude, "lon": longitude, "appid": appid}

    url = "http://api.openweathermap.org/data/2.5/weather"
    if debug:
        print(url)

    resp = requests.get(url, params=payload)
    print("url: " + resp.url)

    data = resp.json()
    write_json("ow.json", data)
    print("-" * 40)
    print("weather.description: " + data["weather"][0]["description"])
    sunrise = datetime.fromtimestamp(data["sys"]["sunrise"])
    print("sys.sunrise: {}".format(sunrise))
    sunset = datetime.fromtimestamp(data["sys"]["sunset"])
    print("sys.sunset: {}".format(sunset))
    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]
    temp = data["main"]["temp"]
    print(
        "max: {:.1f}, min: {:.1f}, curr: {:.1f}".format(
            k2c(temp_max), k2c(temp_min), k2c(temp)
        )
    )


def query_accuweather(latitude, longitude):
    """query accuweather by latitude and longitude"""
    debug = False
    appid = getapikey("accuweather")
    baseurl = """
    http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?
    """
    baseurl = baseurl.strip()
    pos = "{0},{1}".format(latitude, longitude)
    payload = {"apikey": appid, "q": pos}
    resp = requests.get(baseurl, params=payload)
    print("url: " + resp.url)
    data = resp.json()
    write_json("aw-loc.json", data)

    return
    lockey = data["Key"]
    baseurl = """
    http://dataservice.accuweather.com/currentconditions/v1/{0}?
    """.format(
        lockey
    )
    baseurl = baseurl.strip()
    url = baseurl + urllib.urlencode({"apikey": appid})
    # print(url)
    data = query_url_for_json(url)
    my_write_json(accuweather_file, data)
    print(
        ".[0].Temperature.Metric.Value: {0}".format(
            data[0]["Temperature"]["Metric"]["Value"]
        )
    )

    baseurl = """
    http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{0}?
    """.format(
        lockey
    )
    baseurl = baseurl.strip()
    url = baseurl + urllib.urlencode({"apikey": appid, "details": "true"})
    data = query_url_for_json(url)
    my_write_json(accuweather_forcast_file, data)
    print(".[0].RainProbability: {0}".format(data[0]["RainProbability"]))


def main():
    """main"""
    openweather_file = "/tmp/ow.json"
    accuweather_file = "/tmp/aw_curr.json"
    accuweather_forcast_file = "/tmp/aw_fore.json"
    latitude = "25.292266"
    longitude = "121.567980"
    # query_openweather(latitude, longitude)
    query_accuweather(latitude, longitude)


if __name__ == "__main__":
    main()
