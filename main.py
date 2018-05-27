# Da o menor caminho para cada no apartir do no inicial

#import Dijkstra as dij

from Dijkstra import *

grafo = Graph()
grafo.add_node(['a','b','c','d'])
grafo.add_edge('a','b',3)
grafo.add_edge('a','c',1)
grafo.add_edge('b','d',1)
grafo.add_edge('c','d',2)

#print grafo.nodes
#print grafo.edges
#print grafo.costs

#custo, caminho = dijsktra(grafo,'a')

#print custo
#print caminho

print caminho(grafo,'a','d')

