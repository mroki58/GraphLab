import sys
import os
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random

def kosaraju(graph_obj):

    if hasattr(graph_obj, 'G'):
        graph = graph_obj.G
    else:
        graph = graph_obj 
    
    def dfs1(u, visited, stack):
        visited[u] = True
        for v in graph.neighbors(u):
            if not visited[v]:
                dfs1(v, visited, stack)
        stack.append(u)

    def get_transpose(graph):
        transpose = nx.DiGraph()
        for u, v in graph.edges():
            transpose.add_edge(v, u)
        transpose.add_nodes_from(graph.nodes()) 
        return transpose

    def dfs2(u, visited, component):
        visited[u] = True
        component.append(u)
        for v in transpose_graph.neighbors(u):
            if not visited[v]:
                dfs2(v, visited, component)

    n = graph.number_of_nodes()
    visited = {node: False for node in graph.nodes()}
    stack = []

    for node in graph.nodes():
        if not visited[node]:
            dfs1(node, visited, stack)

    transpose_graph = get_transpose(graph)

    visited = {node: False for node in graph.nodes()}
    strongly_connected_components = []

    while stack:
        u = stack.pop()
        if not visited[u]:
            component = []
            dfs2(u, visited, component)
            strongly_connected_components.append(set(component))

    return strongly_connected_components