import random
import os
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from graph import DirectedGraph
from algorithms import KosarajuAlgorithm

def generate_random_digraph(n, p):
    graph = DirectedGraph(n)
    
    for i in range(n):
        for j in range(n):
            if i != j and random.random() < p:
                graph.add_edge(i, j)
    
    return graph

def is_strongly_connected(graph):
    kosaraju = KosarajuAlgorithm(graph)
    components, num_components = kosaraju.kosaraju()
    return num_components == 1

def generate_strongly_connected_digraph(n, max_attempts=100):
    for attempt in range(max_attempts):
        p = min(0.3 + (n-3) * 0.1, 0.8)  
        graph = generate_random_digraph(n, p)
        
        if is_strongly_connected(graph):
            return graph
    
    graph = DirectedGraph(n)
    for i in range(n):
        graph.add_edge(i, (i + 1) % n)
    
    for i in range(n):
        for j in range(n):
            if i != j and (i, j) not in graph.weights and random.random() < 0.3:
                graph.add_edge(i, j)
    
    return graph

def add_random_weights(graph, min_weight=-5, max_weight=10):
    for (u, v) in list(graph.weights.keys()):
        graph.add_edge(u, v, random.randint(min_weight, max_weight), force_weight=True)

def print_distance_matrix(matrix, n):
    print("\nMacierz odległości:")
    print("   ", end="")
    for i in range(n):
        print(f"{i:4}", end="")
    print()
    
    for i in range(n):
        print(f"{i}: ", end="")
        for j in range(n):
            if matrix[i][j] == float('inf'):
                print(" ∞ ", end=" ")
            else:
                print(f"{matrix[i][j]:3}", end=" ")
        print()

import matplotlib.pyplot as plt
import networkx as nx

def visualize_graph(graph, filename, title="Graf", with_weights=False, components=None):
    G = nx.DiGraph()
    
    for v in range(graph.V):
        G.add_node(v)
    
    for (u, v), weight in graph.weights.items():
        G.add_edge(u, v, weight=weight)
    
    pos = nx.circular_layout(G)
    
    plt.figure(figsize=(10, 8))
    
    if components:
        colors = plt.cm.get_cmap('tab10', max(components) + 1)
        node_colors = [colors(components[i]-1) for i in range(graph.V)]
        nx.draw_networkx_nodes(G, pos, node_size=700, node_color=node_colors, alpha=0.8)
    else:
        nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue', alpha=0.8)
    
    bidirectional_pairs = set()
    for (u, v) in G.edges():
        if G.has_edge(v, u):
            if u < v:
                bidirectional_pairs.add((u, v))
            else:
                bidirectional_pairs.add((v, u))
    
    regular_edges = [(u, v) for (u, v) in G.edges() if (min(u, v), max(u, v)) not in bidirectional_pairs]
    curved_edges = [(u, v) for (u, v) in G.edges() if (min(u, v), max(u, v)) in bidirectional_pairs]
    
    nx.draw_networkx_edges(G, pos, edgelist=regular_edges, arrows=True, 
                          arrowstyle='->', arrowsize=15, width=1.5)
    nx.draw_networkx_edges(G, pos, edgelist=curved_edges, arrows=True, 
                          connectionstyle='arc3,rad=0.2', arrowstyle='->', arrowsize=15, width=1.5)
    
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
    
    if with_weights:
        edge_label_positions = {}
        
        for (u, v) in G.edges():
            if (min(u, v), max(u, v)) in bidirectional_pairs:
                if u < v:
                    edge_label_positions[(u, v)] = 0.3
                else:
                    edge_label_positions[(u, v)] = 0.7
            else:
                edge_label_positions[(u, v)] = 0.5
        
        edge_labels = {(u, v): graph.weights[(u, v)] for (u, v) in graph.weights}
        
        for (u, v), weight in edge_labels.items():
            nx.draw_networkx_edge_labels(
                G, pos, 
                edge_labels={(u, v): weight},
                label_pos=edge_label_positions.get((u, v), 0.5),
                font_size=10,
                font_color='red' if edge_label_positions.get((u, v)) == 0.5 else 'blue',
                bbox=dict(facecolor='white', edgecolor='none', alpha=0.7, pad=2),
                connectionstyle='arc3,rad=0.2' if (min(u, v), max(u, v)) in bidirectional_pairs else 'arc3,rad=0'
            )
    
    plt.title(title)
    plt.axis('off')
    
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()
