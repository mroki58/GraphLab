import networkx as nx
import Bellmann_Ford

def johnson(graph):

    G_prime = nx.DiGraph()
    G_prime.add_nodes_from(graph.nodes())
    G_prime.add_edges_from(graph.edges(data=True)) 

    new_node = max(graph.nodes()) + 1
    G_prime.add_node(new_node)
    print("Dodawanie krawędzi z nowego wierzchołka:")
    for node in graph.nodes():
        G_prime.add_edge(new_node, node, weight=0)
        print(f"  ({new_node} -> {node}) z wagą: {G_prime[new_node][node]}")


    print("\nKrawędzie w G':")
    for u, v, data in G_prime.edges(data=True):
        print(f"{u} -> {v}, waga: {data.get('weight')}")


    h, no_negative_cycles = Bellmann_Ford.bellman_ford(G_prime, new_node)
    print("Potencjały h:", h)

    if not no_negative_cycles:
        print("Graf zawiera ujemny cykl - algorytm Johnsona nie może być zastosowany.")
        return None
    
    G_reweighted = graph.copy()
    for u, v in graph.edges():
        weight = graph[u][v].get('weight', 0)
        G_reweighted[u][v]['weight'] = weight + h[u] - h[v]
    
    distances = {}
    for source in graph.nodes():
        distances[source] = {}
        
        for target in graph.nodes():
            distances[source][target] = float('inf')
        
        distances[source][source] = 0
        

        path_lengths = nx.single_source_dijkstra_path_length(G_reweighted, source)
        
        for target, length in path_lengths.items():
            distances[source][target] = length - h[source] + h[target]
    
    return distances

def print_distance_matrix(distances):

    if not distances:
        return
        
    nodes = sorted(list(distances.keys()))
    
    print("    ", end="")
    for j in nodes:
        print(f"{j:4}", end="")
    print()
    
    for i in nodes:
        print(f"{i:4}", end="")
        for j in nodes:
            dist = distances[i][j]
            if dist == float('inf'):
                print(" inf", end="")
            else:
                print(f"{dist:4.0f}", end="")
        print()