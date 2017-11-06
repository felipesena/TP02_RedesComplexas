import json
import networkx as nx

def clustering():
    filename = "listeners.json"
    json_data = open(filename)
    datafile = json.load(json_data)

    for data in datafile:
        print(data)
        print(datafile[data])




clustering()

