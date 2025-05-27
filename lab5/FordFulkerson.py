"""
Moduł zawiera implementację algorytmu Forda-Fulkersona do znajdowania maksymalnego przepływu w grafie.
"""

from collections import deque
from Preparing import createNetwork
from copy import deepcopy
import networkx as nx


def findExtendingPath(G, s, t):
    """
    Znajduje ścieżkę rozszerzającą w grafie rezydualnym za pomocą BFS.

    Parameters
    ----------
    G : networkx.DiGraph
        Graf rezydualny.
    s : int
        Wierzchołek źródłowy.
    t : int
        Wierzchołek ujścia.

    Returns
    -------
    list of int
        Lista wierzchołków reprezentująca ścieżkę rozszerzającą. Jeśli ścieżka nie istnieje, zwraca pustą listę.
    """
    G = deepcopy(G)  # Tworzenie kopii grafu, aby nie modyfikować oryginału

    # Inicjalizacja BFS
    G.nodes[s]['prev'] = None
    G.nodes[s]['no'] = 0
    queue = deque([s])

    while queue:
        node = queue.popleft()
        neighbors = list(G.neighbors(node))
        for neighbor in neighbors:
            if 'no' not in G.nodes[neighbor]:  # Wierzchołek nieodwiedzony
                if G[node][neighbor]['c'] > 0:  # Krawędź ma dodatnią przepustowość
                    no = G.nodes[node]['no']
                    queue.appendleft(neighbor)

                    G.nodes[neighbor]['no'] = no + 1
                    G.nodes[neighbor]['prev'] = node
            if neighbor == t:
                break  # Znaleziono ścieżkę do ujścia
        print(queue)

    # Budowanie ścieżki od ujścia do źródła
    node = t
    path = [t]
    if G.nodes[node].get('prev') is None:
        return []  # Brak ścieżki rozszerzającej

    while G.nodes[node].get('prev') is not None:
        path.append(G.nodes[node]['prev'])
        node = G.nodes[node]['prev']

    path.reverse()
    return path


def minimumCf(graph, path):
    """
    Oblicza minimalną przepustowość na ścieżce rozszerzającej.

    Parameters
    ----------
    graph : networkx.DiGraph
        Graf rezydualny.
    path : list of int
        Ścieżka rozszerzająca.

    Returns
    -------
    int
        Minimalna przepustowość na ścieżce.
    """
    return min([graph[path[i]][path[i + 1]]['c'] for i in range(len(path) - 1)])


def updateGf(Gf, path, minCf):
    """
    Aktualizuje graf rezydualny na podstawie znalezionej ścieżki rozszerzającej.

    Parameters
    ----------
    Gf : networkx.DiGraph
        Graf rezydualny.
    path : list of int
        Ścieżka rozszerzająca.
    minCf : int
        Minimalna przepustowość na ścieżce.

    Returns
    -------
    networkx.DiGraph
        Zaktualizowany graf rezydualny.
    """
    edgesInPath = [(path[i], path[i + 1]) for i in range(len(path) - 1)]

    for edge in edgesInPath:
        u, v = edge
        Gf[u][v]['c'] -= minCf  # Zmniejszenie przepustowości na krawędzi
        if Gf.has_edge(v, u):
            Gf[v][u]['c'] += minCf  # Zwiększenie przepustowości na krawędzi rezydualnej
        else:
            Gf.add_edge(v, u, c=minCf)  # Dodanie krawędzi rezydualnej

    return Gf


def FordFulkerson(graph, s=0, t=1):
    """
    Implementacja algorytmu Forda-Fulkersona do znajdowania maksymalnego przepływu w grafie.

    Parameters
    ----------
    graph : networkx.DiGraph
        Graf wejściowy z przepustowościami na krawędziach.
    s : int
        Wierzchołek źródłowy.
    t : int
        Wierzchołek ujścia.

    Returns
    -------
    int
        Maksymalny przepływ w grafie.
    """
    Gf = deepcopy(graph)  # Tworzenie grafu rezydualnego

    # Inicjalizacja przepływu na krawędziach
    for u, v in graph.edges:
        graph[u][v]['f'] = 0

    # Szukanie ścieżek rozszerzających
    extending_path = findExtendingPath(Gf, s, t)
    while extending_path:
        cf = minimumCf(Gf, extending_path)  # Minimalna przepustowość na ścieżce
        edgesInPath = [(extending_path[i], extending_path[i + 1]) for i in range(len(extending_path) - 1)]
        for edge in edgesInPath:
            if edge in graph.edges:
                graph[edge[0]][edge[1]]['f'] += cf  # Aktualizacja przepływu na krawędzi
            else:
                graph[edge[1]][edge[0]]['f'] -= cf  # Aktualizacja przepływu na krawędzi rezydualnej

        Gf = updateGf(Gf, extending_path, cf)  # Aktualizacja grafu rezydualnego
        extending_path = findExtendingPath(Gf, s, t)

    # Obliczenie maksymalnego przepływu
    nbs = nx.neighbors(graph, s)
    return sum(graph[s][i]['f'] for i in nbs)


if __name__ == "__main__":
    """
    Przykład użycia algorytmu Forda-Fulkersona.

    Tworzy graf warstwowy, oblicza maksymalny przepływ i wizualizuje graf.
    """
    net = createNetwork(3)  # Tworzenie grafu z 2 warstwami
    graph = net.getGraph()
    print("Maksymalny przepływ:", FordFulkerson(graph))  # Obliczenie maksymalnego przepływu
    net.draw()  # Wizualizacja grafu

