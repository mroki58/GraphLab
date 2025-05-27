import sys

# Importy z naszych modułów
from graph import DirectedGraph
from algorithms import KosarajuAlgorithm, BellmanFord, JohnsonAlgorithm
from utils import (generate_random_digraph, generate_strongly_connected_digraph, 
                  add_random_weights, print_distance_matrix, visualize_graph,
                  is_strongly_connected)
from collections import defaultdict

def main():    
    n = int(input("Podaj liczbę wierzchołków n: ") or "7")
    p = float(input("Podaj prawdopodobieństwo krawędzi p: ") or "0.4")
    
    print(f"\n--- ZADANIE 1 ---")
    print(f"Parametry: n={n}, p={p}")
    
    graph = generate_random_digraph(n, p)
    print(f"Wygenerowano digraf z {len(graph.weights)} krawędziami")
    graph.print_graph()
    
    visualize_graph(graph, "d:\\gówno\\GraphLab\\lab4v2\\output\\random_digraph.png", 
                   f"Losowy digraf (n={n}, p={p})")
    
    print(f"\n--- ZADANIE 2 ---")
    kosaraju = KosarajuAlgorithm(graph)
    components, num_components = kosaraju.kosaraju()
    
    print(f"Liczba silnie spójnych składowych: {num_components}")
    
    component_groups = defaultdict(list)
    for vertex, component in enumerate(components):
        component_groups[component].append(vertex)
    
    for comp_num, vertices in component_groups.items():
        print(f"Składowa {comp_num}: {vertices}")
    
    strongly_connected = num_components == 1
    print(f"Graf jest silnie spójny: {'TAK' if strongly_connected else 'NIE'}")
    
    visualize_graph(graph, "d:\\gówno\\GraphLab\\lab4v2\\output\\components.png", 
                   "Graf z zaznaczonymi silnie spójnymi składowymi", 
                   components=components)
    
    if not strongly_connected:
        print(f"\n--- Generowanie silnie spójnego digrafu ---")

        attempts = 0
        while True:
            attempts += 1
            new_graph = generate_random_digraph(n, p)
            if is_strongly_connected(new_graph):
                graph = new_graph
                break
        
        graph.print_graph()
        
        visualize_graph(graph, "d:\\gówno\\GraphLab\\lab4v2\\output\\strongly_connected.png", 
                       "Silnie spójny digraf")
    
    print(f"\n--- ZADANIE 3 ---")
    
    cycle_attempts = 0
    has_negative_cycle = True
    
    while has_negative_cycle:
        cycle_attempts += 1
        if cycle_attempts > 1:
            
            sc_attempts = 0
            while True:
                sc_attempts += 1
                new_graph = generate_random_digraph(n, p)
                if is_strongly_connected(new_graph):
                    graph = new_graph
                    print(f"Wygenerowano silnie spójny digraf")
                    break

        
        add_random_weights(graph, -5, 10)
        
        bellman = BellmanFord(graph)
        distances, has_negative_cycle = bellman.bellman_ford(0)
        
        if has_negative_cycle:
            print("Graf zawiera ujemny cykl, generuję nowy...")
        else:
            print(f"Znaleziono graf bez ujemnych cykli po {cycle_attempts} próbach!")
    
    graph.print_weighted_graph()
    
    visualize_graph(graph, "d:\\gówno\\GraphLab\\lab4v2\\output\\weighted_graph.png", 
                   "Graf z wagami", with_weights=True)
    
    print(f"\nNajkrótsze ścieżki z wierzchołka 0 (Bellman-Ford):")
    
    if has_negative_cycle: 
        print("UJEMNY CYKL")
    else:
        for i, dist in enumerate(distances):
            if dist == float('inf'):
                print(f"Do wierzchołka {i}: nieosiągalny")
            else:
                print(f"Do wierzchołka {i}: {dist}")
    
    print(f"\n--- ZADANIE 4 ---")
    
    johnson = JohnsonAlgorithm(graph)
    distance_matrix, has_negative_cycle = johnson.johnson()
    
    if has_negative_cycle:
        print("BŁĄD")
    else:
        print_distance_matrix(distance_matrix, n)
        

        print("Johnson:     ", [distance_matrix[0][i] if distance_matrix[0][i] != float('inf') else '∞' for i in range(n)])
        print("Bellman-Ford:", [distances[i] if distances[i] != float('inf') else '∞' for i in range(n)])

if __name__ == "__main__":
    main()