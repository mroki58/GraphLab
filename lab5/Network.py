import networkx as nx
import matplotlib.pyplot as plt
import random
import os

class Network:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._idOfLastVertex = 0
        self._N = 0

    def createLayers(self, N):
        self._graph.add_node(0, label="S", layer =0)
        self._graph.add_node(1, label="T", layer =(N + 1))

        previousLayer = [0]

        k = 2

        for i in range(N):
            vertexInLayers = random.randint(2, N)
            nextLayer = []
            for j in range(vertexInLayers):
                self._graph.add_node(k, layer=(i + 1))
                nextLayer.append(k)
                k += 1
            
            self._createEdgesBetweenLayers(previousLayer, nextLayer)
            previousLayer = nextLayer  

        self._createEdgesBetweenLayers(previousLayer, [1])

        self._idOfLastVertex = k - 1
        self._N = N


   
    def _createEdgesBetweenLayers(self, previousLayer, nextLayer):      
        usedFromNext = set()
        usedFromPrev = set()

        i = 0

        while usedFromNext != set(nextLayer) or usedFromPrev != set(previousLayer):
            v = previousLayer[i % len(previousLayer)]
            u = random.choice(nextLayer)

            usedFromPrev.add(v)
            usedFromNext.add(u)

            if not self._graph.has_edge(v, u):
                self._graph.add_edge(v, u)
            i += 1


    def addRandomEdges(self):
        randomEdgesToAdd = 2 * self._N
        edges = self._graph.edges()
        edges_set = set(edges)

        i = 0
        while i < randomEdgesToAdd:
            v = random.randint(0, self._idOfLastVertex)
            u = random.randint(0, self._idOfLastVertex)

            if u == v:
                continue

            if v == 1 or u == 0:
                continue

            if (v, u) in edges_set:
                continue

            self._graph.add_edge(v, u)
            edges_set.add((v,u))
            i += 1

                

    def addWeights(self):
        for u, v in self._graph.edges():
            self._graph[u][v]['c'] = random.randint(1, 10)  



    def draw(self):
        pos = nx.multipartite_layout(self._graph, subset_key="layer")
        labels = nx.get_node_attributes(self._graph, 'label')  
        edge_labels = nx.get_edge_attributes(self._graph, 'c') 


        nx.draw(self._graph, pos, with_labels=True, labels=labels)
        nx.draw_networkx_edge_labels(self._graph, pos, edge_labels=edge_labels, label_pos=0.2)
        plt.show()

    def getGraph(self):
        return self._graph


if __name__ == "__main__":
    net = Network()
    net.createLayers(2)
    net.addRandomEdges()
    net.addWeights()
    net.draw()




