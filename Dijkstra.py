# Referencia (original): https://gist.github.com/econchick/4666413

import collections

class Graph:
  def __init__(self):# Inicializacao da classe
    self.nodes = set()
    self.edges = collections.defaultdict(list)
    self.costs = {}

  def add_node(self, node):# adiciona no
    for name in node:
        self.nodes.add(name)

  def add_edge(self, from_node, to_node, cost):# adiciona caminho
    self.edges[from_node].append(to_node)# adiciona no de destino no vetor de conexoes do no de origem
    self.edges[to_node].append(from_node)# adiciona no de origem no vetor de conexoes do no de destino
    self.costs[(from_node, to_node)] = cost# atribui custo do deslocamento


def dijsktra(graph, initial):# resolve caminho mais curto
  visited = {initial: 0}# inicia a lista de nos visitados e adiciona o no inicial como custo 0
  path = {}

  nodes = set(graph.nodes)# recupera os nos associado ao grafo

  while nodes:
    min_node = None# no de menor custo
    for node in nodes:
      if node in visited:# o no e primeiramente adicionado como visitado, depois e processado (exemplo: no inicial)
        if min_node is None:# descobre qual o no de menor custo
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:#
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      print(edge)
      weight = current_weight + graph.costs[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path
















