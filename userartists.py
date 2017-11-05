import  requests, json
from bs4 import BeautifulSoup


def getuserartists():
    filename = "listeners.json"
    usuarios = {}

    with open(filename) as json_data:
        datafile = json.load(json_data)

        for data in datafile:
            artistas = getartists(data)
            usuarios[data] = artistas

    json_data.close()

    with open(filename, 'w') as file:
        json.dump(usuarios, file)


def getartists(usuario):
    artistas = []
    url = "https://www.last.fm%s" % usuario
    response = requests.get(url)
    plain_text = response.text

    soup = BeautifulSoup(plain_text, "html.parser")

    if(response.status_code == 200):
        print(url)
        for a in soup.findAll('ol')[0].findAll('a', {'class':'link-block-target'}):
            artistname = a.contents[0]
            artistas.append(artistname)

    return artistas


getuserartists()

