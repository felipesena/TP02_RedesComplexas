import  requests, json
from bs4 import BeautifulSoup


def getuserartists():
    filename = "files/listeners.json"
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

        if(len(soup.findAll('ol')) == 0):
            if len(soup.findAll('p', {'class':'no-data-message'})) > 2:
                return artistas
            else:
                for span in soup.findAll('table')[1].findAll('span', {'class':'chartlist-ellipsis-wrap'}):
                    artistname = span.find_next('a').attrs['title']
                    artistas.append(artistname)
        else:
            for a in soup.findAll('ol')[0].findAll('a', {'class':'link-block-target'}):
                artistname = a.contents[0]
                artistas.append(artistname)



    return artistas

