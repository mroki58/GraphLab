def bellman_ford(graph, source):

    distances = {}
    predecessors = {}
    
    for node in graph.nodes():
        distances[node] = float('inf')
        predecessors[node] = None
        
    distances[source] = 0
    
    edges = []
    for u, v, data in graph.edges(data=True):
        if 'weight' not in data:
            print(f"Krawędź nie ma atrybutu 'weight'!")
            continue
        edges.append((u, v, data['weight']))
        
    print("\nKrawędzie grafu z wagami:")
    for u, v, weight in edges:
        print(f"({u}, {v}): {weight}")
    
    n = len(graph.nodes())
    for i in range(n - 1):
        updated = False
        print(f"\nIteracja {i+1}:")
        
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                predecessors[v] = u
                updated = True
                print(f"  Aktualizacja: d[{v}] = d[{u}] + {weight} = {distances[v]}")
        
        if not updated:
            print("  Brak aktualizacji - zakończenie wcześniej")
            break
    
    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            print(f"\nWykryto ujemny cykl przy krawędzi ({u}, {v}) z wagą {weight}")
            return distances, False
    
    return distances, True