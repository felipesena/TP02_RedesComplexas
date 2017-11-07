import requests, json, artistlisteners
from bs4 import BeautifulSoup


def getartistgenre():
    filename = "listeners.json"
    usuarios = {}

    url = "https://www.last.fm/music/%s"

    with open(filename) as json_data:
        datafile = json.load(json_data)
        genres = []
        i=1
        for data in datafile:
            for artist in datafile[data]:
                response = requests.get(url % artistlisteners.formatanome(artist))
                plain_text = response.text
                soup = BeautifulSoup(plain_text, "html.parser")

                for li in soup.findAll('li', {'class':'tag'}):
                    genre = li.find_next('a').get('href')
                    if genre not in genres:
                        genres.append(genre)

            print(str(i) + "/" + str(len(datafile)))
            i += 1

            usuarios[data] = genres
            genres = []

        json_data.close()

    file = open(filename, 'w')
    json.dump(usuarios, file)
    file.close()

