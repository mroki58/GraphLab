import sys
import os
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class DirectedGraph:
    def __init__(self, n=0, p=0, is_strongly_connected=False):
        self.n = n
        if is_strongly_connected:
            self.G = self.__generate_random_strongly_connected_digraph(n)
        else:
            self.G = self.__generate_random_digraph(n, p)
        self.adjacency_matrix = nx.to_numpy_array(self.G)
        
    def __generate_random_digraph(self, n, p):
        G = nx.DiGraph()
        G.add_nodes_from(range(1, n+1))
        
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i != j and random.random() < p:
                    G.add_edge(i, j)
                    
        return G
    
    def add_random_weights(self, min_weight=-5, max_weight=10):

        for u, v in self.G.edges():
            self.G[u][v]['weight'] = np.random.randint(min_weight, max_weight+1)
    
    def __generate_random_strongly_connected_digraph(self, n):
        if n <= 0:
            return nx.DiGraph()
        if n == 1:
            G = nx.DiGraph()
            G.add_node(1)
            return G

        nodes = list(range(1, n + 1))
        random.shuffle(nodes)
        G = nx.DiGraph()
        for i in range(n):
            G.add_edge(nodes[i], nodes[(i + 1) % n])

        p = 0.3  
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i != j and not G.has_edge(i, j) and random.random() < p:
                    G.add_edge(i, j)

        while not nx.is_strongly_connected(G):
            u = random.randint(1, n)
            v = random.randint(1, n)
            if u != v and not G.has_edge(u, v):
                G.add_edge(u, v)

        return G

    def get_graph(self):
        return self.G

    def draw(self, filename="directed_graph.png"):
 
        path = "examples"
        if not os.path.exists(path):
            os.makedirs(path)
            
        pos = nx.circular_layout(self.G)
        plt.figure(figsize=(8, 8))
        
        nx.draw(self.G, pos, with_labels=True, node_color="lightblue", 
                edge_color="gray", node_size=1500, font_size=12, 
                font_weight="bold", arrowsize=15)
        
        if nx.get_edge_attributes(self.G, 'weight'):
            edge_labels = {(u, v): self.G[u][v]['weight'] for u, v in self.G.edges()}
            nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels, 
                                        font_color="red", font_size=10)
                
        plt.savefig(f"{path}/{filename}")
        plt.close()
        print(f"Graf został zapisany do {path}/{filename}")