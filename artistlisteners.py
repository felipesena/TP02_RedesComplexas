import requests, json
from bs4 import BeautifulSoup


def getartistlisteners(artista):
    namefile = "files/listeners.json"
    url = "https://www.last.fm/music/%s/+listeners?page=" % (formatanome(artista)) + "%d"

    usuarios = []

    for i in range(1, 9):
        response = requests.get(url % (i))
        plain_text = response.text
        soup = BeautifulSoup(plain_text, 'html.parser')

        if (response.status_code == 200):  # verifica se o request foi efetuado com sucesso
            for h4 in soup.findAll('h4', {'class': 'user-list-name'}):
                usuarios.append(h4.find_next('a').get('href'))

    with open(namefile, 'w') as file:
        json.dump(usuarios, file)


def formatanome(artista):
    nomes = artista.split(' ')
    formatado = nomes[0]

    if(len(nomes) == 1):
        return formatado
    else:
        for nome in nomes[1:]:
            formatado += "+" + nome


    return formatado


