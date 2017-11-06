import requests, json, artistlisteners
from bs4 import BeautifulSoup


def getartistgenre():
    filename = "listeners.json"
    usuarios = {}

    url = "https://www.last.fm/music/%s"

    with open(filename) as json_data:
        datafile = json.load(json_data)

        for data in datafile:
            for artist in datafile[data]:
                response = requests.get(url % artistlisteners.getartistlisteners(artist))
                print(response.status_code)


getartistgenre()

