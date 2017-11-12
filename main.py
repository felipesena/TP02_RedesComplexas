import artistlisteners, userartists, graph
import sys


def main():
    artistlisteners.getartistlisteners("John Mayer")
    userartists.getuserartists()
    graph.generategraph()


main()

