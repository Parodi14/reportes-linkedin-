#!/usr/bin/env python
# _*_ coding: utf8 _*_

import urllib.request
import json


def main():
    url = "https://ipinfo.io/159.65.179.52/json"
    v = urllib.request.urlopen(url).read()
    j = json.loads(v.decode('utf-8'))

    # j = json.load(v.read())
    for dato in j:
        print(dato + " : " + j[dato])


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("saliendo")
        exit()
