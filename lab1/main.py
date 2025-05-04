import os
import networkx as nx
import matplotlib.pyplot as plt
from GraphAdMatrix import GraphAdMatrix
from GraphAdList import GraphAdList
from GraphIncMatrix import GraphIncMatrix
from GraphVisual import drawGraph
from GraphRandom import generateRandomWithEdges, generateRandomWithPropabilities

# Tworzenie folderu "answer" w katalogu "lab1"
output_folder = "answer"
os.makedirs(output_folder, exist_ok=True)

# Parametry grafów
num_nodes = 10
num_edges = 15
edge_probability = 0.3

# Generowanie grafów w modelu Erdős–Rényi (model 1: stała liczba krawędzi)
for i in range(1, 6):
    filename = f"{output_folder}/graph_model1_{i}.dat"
    generateRandomWithEdges(num_nodes, num_edges, "adjList", filename)

    # Wczytanie grafu z listy sąsiedztwa
    graph = GraphAdList()
    graph.read_list_from_file(filename)

    # Wizualizacja na kole
    drawGraph(graph, f"{output_folder}/graph_model1_{i}_circle.png")

    # Konwersja i wizualizacja w innych formatach
    ad_matrix = graph.toAdMatrix()
    drawGraph(ad_matrix, f"{output_folder}/graph_model1_{i}_matrix_circle.png")

    inc_matrix = graph.toIncMatrix()
    drawGraph(inc_matrix, f"{output_folder}/graph_model1_{i}_incidence_circle.png")

    # Wizualizacja bez koła (z wykorzystaniem NetworkX)
    nx_graph = nx.DiGraph()
    for u, neighbors in graph._list.items():
        for v in neighbors:
            nx_graph.add_edge(u, v)
    plt.figure()
    nx.draw(nx_graph, with_labels=True, node_color="lightblue", font_weight="bold")
    plt.savefig(f"{output_folder}/graph_model1_{i}_networkx.png")
    plt.close()

# Generowanie grafów w modelu Erdős–Rényi (model 2: prawdopodobieństwo krawędzi)
for i in range(1, 6):
    filename = f"{output_folder}/graph_model2_{i}.dat"
    generateRandomWithPropabilities(num_nodes, edge_probability, "adjList", filename)

    # Wczytanie grafu z listy sąsiedztwa
    graph = GraphAdList()
    graph.read_list_from_file(filename)

    # Wizualizacja na kole
    drawGraph(graph, f"{output_folder}/graph_model2_{i}_circle.png")

    # Konwersja i wizualizacja w innych formatach
    ad_matrix = graph.toAdMatrix()
    drawGraph(ad_matrix, f"{output_folder}/graph_model2_{i}_matrix_circle.png")

    inc_matrix = graph.toIncMatrix()
    drawGraph(inc_matrix, f"{output_folder}/graph_model2_{i}_incidence_circle.png")

    # Wizualizacja bez koła (z wykorzystaniem NetworkX)
    nx_graph = nx.DiGraph()
    for u, neighbors in graph._list.items():
        for v in neighbors:
            nx_graph.add_edge(u, v)
    plt.figure()
    nx.draw(nx_graph, with_labels=True, node_color="lightblue", font_weight="bold")
    plt.savefig(f"{output_folder}/graph_model2_{i}_networkx.png")
    plt.close()