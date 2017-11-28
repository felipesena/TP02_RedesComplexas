import json
import networkx as nx


def generategraph():
    filename = "files/listeners.json"
    graphpath = 'files/graph.gexf'
    json_data = open(filename)
    datafile = json.load(json_data)

    graph = nx.Graph()

    for user in datafile:
        cont = list(datafile.keys()).index(user) + 1

        for comparer in list(datafile.keys())[cont:]:
            peso = len(set(datafile[user]).intersection(datafile[comparer]))
            if peso > 0:
                graph.add_edge(list(datafile.keys()).index(user), cont + 1, weight=peso)
            else:
                graph.add_node(list(datafile.keys()).index(user))
            cont += 1

    nx.write_gexf(graph, graphpath)
    json_data.close()
    print("Grafo gerado com sucesso! (%s)" % graphpath)
    getresults(graph)



def getresults(graph):
    print("Analisando grafo...")
    print("Média do grau dos nodos: " + str(nx.average_degree_connectivity(graph)))
    print("Coeficiente de clusterização: " + str(nx.average_clustering(graph)))
    for g in nx.connected_component_subgraphs(graph):
        print("Distância média dos nós: " + str(nx.average_shortest_path_length(g)))
    print("Betweenness das arestas: " + str(nx.edge_betweenness(graph)))
    print("Betweenness dos nodos: " + str(nx.betweenness_centrality(graph)))



