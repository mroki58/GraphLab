"""
Moduł zawiera klasę Network, która umożliwia tworzenie i wizualizację grafów warstwowych.
"""

import networkx as nx
import matplotlib.pyplot as plt
import random
import os
import numpy as np



class Network:
    """
    Klasa Network reprezentuje graf skierowany z warstwami wierzchołków.

    Umożliwia tworzenie grafów warstwowych, dodawanie losowych krawędzi, przypisywanie wag do krawędzi
    oraz wizualizację grafu.
    """

    def __init__(self):
        """
        Inicjalizuje pusty graf skierowany.
        """
        self._graph = nx.DiGraph()  # Graf skierowany
        self._idOfLastVertex = 0  # Identyfikator ostatniego wierzchołka
        self._N = 0  # Liczba warstw w grafie

    def createLayers(self, N):
        """
        Tworzy graf warstwowy z N warstwami.

        Parameters
        ----------
        N : int
            Liczba warstw w grafie.
        """
        # Dodanie wierzchołków źródła (S) i ujścia (T)
        self._graph.add_node(0, label="S", layer=0)
        self._graph.add_node(1, label="T", layer=(N + 1))

        previousLayer = [0]  # Wierzchołki w poprzedniej warstwie
        k = 2  # Identyfikator pierwszego wierzchołka w warstwach

        # Tworzenie warstw
        for i in range(N):
            vertexInLayers = random.randint(2, N)  # Liczba wierzchołków w warstwie
            nextLayer = []
            for j in range(vertexInLayers):
                self._graph.add_node(k, layer=(i + 1))  # Dodanie wierzchołka do warstwy
                nextLayer.append(k)
                k += 1

            # Tworzenie krawędzi między warstwami
            self._createEdgesBetweenLayers(previousLayer, nextLayer)
            previousLayer = nextLayer

        # Połączenie ostatniej warstwy z ujściem (T)
        self._createEdgesBetweenLayers(previousLayer, [1])

        # Aktualizacja identyfikatora ostatniego wierzchołka i liczby warstw
        self._idOfLastVertex = k - 1
        self._N = N

    def _createEdgesBetweenLayers(self, previousLayer, nextLayer):
        """
        Tworzy krawędzie między wierzchołkami dwóch sąsiednich warstw.

        Parameters
        ----------
        previousLayer : list of int
            Lista wierzchołków w poprzedniej warstwie.
        nextLayer : list of int
            Lista wierzchołków w następnej warstwie.
        """
        usedFromNext = set()  # Wierzchołki z następnej warstwy, które zostały użyte
        usedFromPrev = set()  # Wierzchołki z poprzedniej warstwy, które zostały użyte

        i = 0
        # Tworzenie krawędzi, aż wszystkie wierzchołki zostaną połączone
        while usedFromNext != set(nextLayer) or usedFromPrev != set(previousLayer):
            v = previousLayer[i % len(previousLayer)]  # Wierzchołek z poprzedniej warstwy
            u = random.choice(nextLayer)  # Losowy wierzchołek z następnej warstwy

            usedFromPrev.add(v)
            usedFromNext.add(u)

            # Dodanie krawędzi, jeśli jeszcze nie istnieje
            if not self._graph.has_edge(v, u):
                self._graph.add_edge(v, u)
            i += 1

    

    def addRandomEdges(self):
        """
        Dodaje losowe krawędzie między wierzchołkami grafu.

        Liczba dodanych krawędzi jest równa dwukrotności liczby warstw w grafie.
        """
        randomEdgesToAdd = 2 * self._N  # liczba krawędzi do dodania
        edges_set = set(self._graph.edges())

        i = 0
        while i < randomEdgesToAdd:
            v = random.randint(0, self._idOfLastVertex)
            u = random.randint(0, self._idOfLastVertex)

            if (
                u == v or          # bez pętli
                v == 1 or          # nie wychodzą z ujścia
                u == 0 or          # nie wchodzą do źródła
                (v, u) in edges_set or
                (u, v) in edges_set  # sprawdzamy też krawędzie w przeciwnym kierunku
            ):
                continue

            self._graph.add_edge(v, u)
            edges_set.add((v, u))
            i += 1


    def addWeights(self):
        """
        Przypisuje losowe wagi do krawędzi grafu.

        Wagi są losowane z zakresu od 1 do 10.
        """
        for u, v in self._graph.edges():
            self._graph[u][v]['c'] = random.randint(1, 10)

    

    def draw(self):
        
        """
         Rysuje graf i wyświetla go w oknie.

         Wierzchołki są rozmieszczone zgodnie z ich warstwami,
         z lekkim losowym przesunięciem, żeby uniknąć nakładania się krawędzi.
         """
        pos = nx.multipartite_layout(self._graph, subset_key="layer")

        
        for node in pos:
            dx = np.random.uniform(-0.2, 0.2)
            dy = np.random.uniform(-0.2, 0.2)
            pos[node] = (pos[node][0] + dx, pos[node][1] + dy)

        labels = nx.get_node_attributes(self._graph, 'label')

        
        edge_labels = {}
        for u, v, data in self._graph.edges(data=True):
            flow = data.get('f', 0)          
            capacity = data.get('c', None)   
            if capacity is not None:
                edge_labels[(u, v)] = f"{flow} / {capacity}"
            else:
                edge_labels[(u, v)] = f"{flow}"

        nx.draw(self._graph, pos, with_labels=True, labels=labels)
        nx.draw_networkx_edge_labels(self._graph, pos, edge_labels=edge_labels, label_pos=0.3)
        plt.savefig("network_flow.png", dpi=300, bbox_inches='tight')
        plt.show()


    

    def getGraph(self):
        """
        Zwraca obiekt grafu NetworkX.

        Returns
        -------
        networkx.DiGraph
            Obiekt grafu skierowanego.
        """
        return self._graph


if __name__ == "__main__":
    # Przykład użycia klasy Network
    net = Network()
    net.createLayers(2)  # Tworzenie grafu z 2 warstwami
    net.addRandomEdges()  # Dodanie losowych krawędzi
    net.addWeights()  # Dodanie wag do krawędzi
    net.draw()  # Wizualizacja grafu




