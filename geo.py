#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
use google geocoding API to query location, address, and etc.
refer to:
https://github.com/google/open-location-code/wiki/Plus-codes-API
"""

import sys
import os
import time
import json
import requests

DEBUG = False


def help_message():
    """help message"""
    helpmsg = """
    specify POI names to query plus code
    """
    print(helpmsg.strip())


def read_secret():
    """read secret keys"""
    home = os.environ.get("HOME")
    file = home + "/Private/geocoding-key.json"
    # read from json file
    with open(file) as sec_file:
        data = json.load(sec_file)
    key = data.get("key")
    email = data.get("email")
    if DEBUG:
        print("apikey:{0}\nemail:{1}".format(key, email))
    return (key, email)


"""
URL="https://plus.codes/api?address=${ADDR}&ekey=${KEY}&${EMAIL}"
"""


def query_geocoding(addr, key, email):
    """compose api call and request"""
    payload = {"address": addr, "ekey": key, "email": email}
    url = "https://plus.codes/api"

    r = requests.get(url, params=payload)
    print("url:", r.url)
    print("r.json():", r.json())
    print("r.text:", r.text)
    j = r.json()
    print("plus code:", j["plus_code"]["global_code"])
    print("location:", j["plus_code"]["geometry"]["location"])

    fn = "geo-{}.json".format(time.time())
    with open(fn, "wt") as geofile:
        geofile.write(json.dumps(j))
    print("output to {}".format(fn))


def main(argv):
    """main"""
    key, email = read_secret()
    if argv == []:
        argv.append("自由女神像")

    for pp in argv:
        print(pp)
        query_geocoding(pp, key, email)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        help_message()

    main(sys.argv[1:])
