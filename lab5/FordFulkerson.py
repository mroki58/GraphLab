from collections import deque
from Preparing import createNetwork
from copy import deepcopy
import networkx as nx

def findExtendingPath(G, s, t):
    G = deepcopy(G)

    G.nodes[s]['prev'] = None
    G.nodes[s]['no'] = 0

    queue = deque([s])

    while queue:
        node = queue.popleft()
        neighbors = list(G.neighbors(node))
        for neighbor in neighbors:
            if 'no' not in G.nodes[neighbor]:
                # to znaczy, że wierzchołek jeszcze nie był BFSowany
                no = G.nodes[node]['no']
                queue.appendleft(neighbor)

                G.nodes[neighbor]['no'] = no + 1
                G.nodes[neighbor]['prev'] = node
            if neighbor == t:
                break # nie potrzebujemy robic wiecej BFS dotarliśmy do ujścia
        print(queue)
    node = t
    path = [t]

    if G.nodes[node].get('prev') is None:
        return []

    while G.nodes[node].get('prev') is not None:
        path.append(G.nodes[node]['prev'])
        node = G.nodes[node]['prev']
    

    path.reverse()
    return path

def minimumCf(graph, path):
    return min([ graph[path[i]][path[i + 1]]['c'] for i in range(len(path) - 1)])

def updateGf(Gf, path, minCf):
    edgesInPath = [(path[i], path[i + 1]) for i in range(len(path) - 1)]

    for edge in edgesInPath:
        u = edge[0]
        v = edge[1]

        if Gf[u][v]['c'] == minCf:
            Gf.remove_edge(u, v)
        else:
            Gf[u][v]['c'] = Gf[u][v]['c'] - minCf

        if Gf.has_edge(v, u):
            Gf[v][u]['c'] = Gf[v][u]['c'] + minCf
        else:
            Gf.add_edge(v, u, c=minCf)
        
    return Gf
      


    

def FordFulkerson(graph, s = 0, t = 1):
    Gf = deepcopy(graph)
    
    for u, v in graph.edges:
        graph[u][v]['f'] = 0 


    # while istnieje sciezka rozszerzajace p z s do t w sieci Gf
    extending_path = findExtendingPath(Gf, s, t)
    while extending_path != []:
        cf = minimumCf(Gf, extending_path)
        edgesInPath = [(extending_path[i], extending_path[i + 1]) for i in range(len(extending_path) - 1)]
        for edge in edgesInPath:
            if edge in graph.edges:
                graph[edge[0]][edge[1]]['f'] = graph[edge[0]][edge[1]]['f'] + cf
            else:
                graph[edge[1]][edge[0]]['f'] = graph[edge[1]][edge[0]]['f'] - cf



        Gf = updateGf(Gf, extending_path, cf)
        extending_path = findExtendingPath(Gf, s , t)

    nbs = nx.neighbors(graph, s)
    return sum(graph[s][i]['f'] for i in nbs)

if __name__ == "__main__":
    net = createNetwork(2)
    graph = net.getGraph()
    print(FordFulkerson(graph))
    net.draw()

