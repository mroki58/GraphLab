import sys
import os
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab2.GraphicSequence import is_connected,regular_graph


class ConnectedGraph:
    """
    Klasa reprezentująca graf spójny, ważony

    Attributes:
        G (nx.Graph): Obiekt grafu z biblioteki NetworkX
        matrix_weights (np.array): Macierz wag grafu
    """
    def __init__(self,n):
        """
        Inicjalizacja garfu

        Args:
            n (int): Liczba wierzchołków grafu.
        """
        k = max(2, np.random.randint(2, n - 2))
        #print("k = ", k)
        self.G = self.__generate_connected_graph(n,k)
        self.matrix_weights = nx.to_numpy_array(self.G, weight="weight")

    def __generate_connected_graph(self,n,k):
        """
        Prywatna metoda generująca spójny graf regularny.
        
        Args:
            n (int): Liczba wierzchołków
            k (int): Stopień każdego wierzchołka
            
        Returns:
            nx.Graph: Wygenerowany graf spójny z losowymi wagami
            
        Raises:
            TimeoutError: Jeśli przekroczono maksymalną liczbę prób
        """
        it=0
        max_it=10_000
        while it<max_it:
            it+=1
            G=regular_graph(n,k)
            if G is not None and is_connected(G):
                break

        if it >= max_it:
            raise TimeoutError("nie można utowrzyć grafu spójnego. Przekroczono limit prób")
        
        self.__add_random_weights(G)

        return G        

    def __add_random_weights(self,G,min_weight=1,max_weight=10):
        """
        Dodaje losowe wagi do krawędzi grafu.
        
        Args:
            G (nx.Graph): Graf do którego dodajemy wagi
            min_weight (int): Minimalna waga krawędzi (domyślnie 1)
            max_weight (int): Maksymalna waga krawędzi (domyślnie 10)
        """
        for u,v in G.edges():
            G.edges[u, v]['weight'] = np.random.randint(min_weight, max_weight) 

    def draw(self):
        """
        Wizualizacja grafu z wagami krawędzi.
        
        Zapisuje wykres do pliku 'connected_graph.png'.
        """
        path="examples"
        if not os.path.exists(path):
            os.makedirs(path)

        pos = nx.circular_layout(self.G)
        plt.figure(figsize=(6,6))
        nx.draw(self.G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=1500, font_size=12, font_weight="bold")
        edge_labels = {(u,v): self.G[u][v]['weight'] for u, v in self.G.edges}
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels, font_color="red", font_size=12)
        plt.savefig(path+'/connected_graph.png')

