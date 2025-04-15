import os
import sys
import networkx as nx
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from DirectedGraph import DirectedGraph
import Kosaraju
import Bellmann_Ford
import Johnson  

def main():
    os.makedirs("examples", exist_ok=True)
    
    print("=== Zestaw 4 ===\n")
    

    n = 8  
    p = 0.3  
    
    print(f"Generowanie losowego digrafu G({n}, {p})...")
    digraph = DirectedGraph(n, p)
    
    print(f"Wygenerowano digraf z {digraph.G.number_of_nodes()} wierzchołkami i {digraph.G.number_of_edges()} łukami.")
    digraph.draw("random_digraph.png")
    
    # Zad. 2
    print("\n=== ZADANIE 2 ===")
    print("Znajdowanie silnie spójnych składowych...")
    sccs = Kosaraju.kosaraju(digraph)
    
    print("\nSilnie spójne składowe:")
    for i, scc in enumerate(sccs):
        print(f"Składowa {i+1}: {scc}")
        
    # Zad. 3
    print("\n=== ZADANIE 3 ===")
    print("Generowanie silnie spójnego digrafu z losowymi wagami...")
    
    n_nodes = 8
    strongly_connected_digraph = DirectedGraph(n=n_nodes, is_strongly_connected=True)
    

    strongly_connected_digraph.add_random_weights(min_weight=-5, max_weight=10)
    strongly_connected_digraph.draw("random_strongly_connected_digraph_with_weights.png")
    
    graph = strongly_connected_digraph.get_graph()
    source_node = 1 
    
    print(f"\nUruchamianie algorytmu Bellmana-Forda z wierzchołka źródłowego {source_node}...")
    distances, no_negative_cycles = Bellmann_Ford.bellman_ford(graph, source_node)
    
    if no_negative_cycles:
        print("\nGraf nie zawiera cykli o ujemnej wadze osiągalnych z wierzchołka źródłowego.")
        print("\nNajkrótsze odległości od wierzchołka 1:")
        for node in sorted(graph.nodes()):
            print(f"Do wierzchołka {node}: {distances[node]}")
    else:
        print("\nGraf zawiera cykle o ujemnej wadze osiągalne z wierzchołka źródłowego.")
        print("Odległości nie są wiarygodne w grafie z ujemnymi cyklami.")
    
    # Zad. 4
    print("\n=== ZADANIE 4 ===")
    print("Generowanie nowego grafu dla algorytmu Johnsona...")
    
    n_nodes_johnson = 8  
    johnson_graph = DirectedGraph(n=n_nodes_johnson, is_strongly_connected=True)
    johnson_graph.add_random_weights(min_weight=1, max_weight=10)  
    johnson_graph.draw("johnson_graph.png")
    
    graph_johnson = johnson_graph.get_graph()
    print(f"Wygenerowano graf z {graph_johnson.number_of_nodes()} wierzchołkami i {graph_johnson.number_of_edges()} łukami.")
    
    print("\nUruchamianie algorytmu Johnsona...")
    distances_matrix = Johnson.johnson(graph_johnson)
    
    print("\nMacierz odległości między wszystkimi parami wierzchołków:")
    Johnson.print_distance_matrix(distances_matrix)
        
if __name__ == "__main__":
    main()
