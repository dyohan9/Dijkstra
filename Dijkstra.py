# Referencia (original): https://gist.github.com/econchick/4666413

import collections

class Graph:
    def __init__(self):  # inicializacao da classe
        self.nodes = set()
        self.edges = collections.defaultdict(list)
        self.costs = {}

    def add_node(self, node):  # adiciona no
        for name in node:
            self.nodes.add(name)

    def add_edge(self, node_a, node_b, cost):  # adiciona caminho
        self.edges[node_a].append(node_b)  # adiciona no b no vetor de conexoes do no a
        self.edges[node_b].append(node_a)  # adiciona no a no vetor de conexoes do no b
        self.costs[(node_a, node_b)] = cost  # atribui custo do deslocamento
        self.costs[(node_b, node_a)] = cost


def dijsktra(graph, initial):  # resolve caminho menor custo
    visited = {initial: 0}  # {no: menor custo}
    nodes = set(graph.nodes)  # recupera os nos associado ao grafo
    path = {}   # {no: no de origem que prove menor custo}

    while nodes:
        min_node = None  # no de menor custo
        for node in nodes:  # dos nos visitados, acha o que tem menor custo
            if node in visited:  # o no e primeiramente adicionado como visitado, depois e processado (exemplo: no inicial)
                if min_node is None:  # descobre qual o no de menor custo
                    min_node = node  # primeiro teste
                elif visited[node] < visited[min_node]:  # substitui pelo no se seu custo for menor
                    min_node = node

        if min_node is None:  # nenhum no nunca foi visitado (if node in visited), ou seja, nao existem nos ou o inicial nunca foi especificado
            break  # cancela

        nodes.remove(min_node)  # nao testa mais

        # acaba testando duas vezes o mesmo caminho, uma vez em direcao ao ponto e outra a partir do ponto
        for edge in graph.edges[min_node]:  # para cada conexao
            cost = visited[min_node] + graph.costs[(min_node, edge)]    # candidato a menor custo
            if edge not in visited or cost < visited[edge]: # primeira vez testado caminho para o no ou reducao de custo pelo novo caminho
                visited[edge] = cost
                path[edge] = min_node

    return visited, path

def caminho(graph, inicial, final):
    visited, path = dijsktra(graph,inicial) # resolve o menor caminho
    trajeto = []    # inicialia lista do caminho
    atual = final
    while atual is not inicial:    # trilha o caminho e adiciona o trajeto na lista do final ao inicial
        trajeto.append(atual)
        atual = path[atual]

    trajeto.append(atual)   # adiciona o inicial
    trajeto.reverse()   # vira a lista para mostrar caminho inicial ao final

    return visited[final], trajeto






