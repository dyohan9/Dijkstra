# Da o menor caminho para cada no apartir do no inicial

import Dijkstra as dij

grafo = dij.Graph()
grafo.add_node('a')
grafo.add_node(['b','c'])
grafo.add_edge('a','b',1)
grafo.add_edge('a','c',2)
grafo.add_edge('b','c',3)

print(grafo.nodes)
print(grafo.edges)
print(grafo.costs)

#dij.dijsktra(grafo,'a')




