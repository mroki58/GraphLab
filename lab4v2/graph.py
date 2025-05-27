from collections import defaultdict

class DirectedGraph:
    
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = defaultdict(list)  # Lista sąsiedztwa
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]  # Macierz sąsiedztwa
        self.weights = {}  # Słownik wag krawędzi
    
    def add_edge(self, u, v, weight=1, force_weight=False):
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
            self.adj_matrix[u][v] = 1
            self.weights[(u, v)] = weight
        else:
            if force_weight:
                self.weights[(u, v)] = weight
    
    def get_transpose(self):
        gt = DirectedGraph(self.V)
        for u in range(self.V):
            for v in self.adj_list[u]:
                gt.add_edge(v, u, self.weights.get((u, v), 1))
        return gt
    
    def print_graph(self):
        print("Lista sąsiedztwa:")
        for i in range(self.V):
            print(f"{i}: {self.adj_list[i]}")
        
        print("\nMacierz sąsiedztwa:")
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))
    
    def print_weighted_graph(self):
        print("Graf z wagami:")
        for (u, v), weight in self.weights.items():
            print(f"Krawędź {u} -> {v}: waga {weight}")
