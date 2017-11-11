import json
import networkx as nx
import matplotlib.pyplot as plt


def generategraph():
    filename = "files/listeners.json"
    json_data = open(filename)
    datafile = json.load(json_data)

    graph = nx.Graph()
    cont = 1

    graph.add_nodes_from(list(datafile.keys()))

    for user in datafile:
        cont = 1
        for comparer in list(datafile.keys())[cont:]:
            peso = len(set(datafile[user]).intersection(datafile[comparer]))
            if peso > 0:
                graph.add_edge(list(datafile.keys()).index(user), cont + 1, weight=peso)
            cont += 1


    nx.write_gexf(graph, 'files/graph.gexf')
    json_data.close()

