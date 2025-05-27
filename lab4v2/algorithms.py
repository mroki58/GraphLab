from graph import DirectedGraph

class KosarajuAlgorithm:
    
    def __init__(self, graph):
        self.graph = graph
        self.V = graph.V
        self.visited = [False] * self.V
        self.finish_times = []
        
        self.components = [-1] * self.V
        self.time = 0
    
    def dfs_visit_iterative(self, start_v, graph, d, f):
        stack = [(start_v, 0)]  
        
        while stack:
            v, phase = stack[-1] 
            
            if phase == 0: 
                stack[-1] = (v, 1)  
                
                self.time += 1
                d[v] = self.time
                
                for u in graph.adj_list[v]:
                    if d[u] == -1:
                        stack.append((u, 0))
            else: 
                stack.pop()  
                
                self.time += 1
                f[v] = self.time
                self.finish_times.append(v)
    
    def components_iterative(self, nr, start_v, gt, comp):
        stack = [start_v]
        comp[start_v] = nr
        
        while stack:
            v = stack.pop()
            
            for u in gt.adj_list[v]:
                if comp[u] == -1:
                    comp[u] = nr
                    stack.append(u)
    
    def kosaraju(self):
        d = [-1] * self.V
        f = [-1] * self.V
        self.time = 0
        self.finish_times = []
        
        for v in range(self.V):
            if d[v] == -1:
                self.dfs_visit_iterative(v, self.graph, d, f)
        
        gt = self.graph.get_transpose()
        comp = [-1] * self.V
        nr = 0
        
        self.finish_times.reverse()
        
        for v in self.finish_times:
            if comp[v] == -1:
                nr += 1
                comp[v] = nr
                self.components_iterative(nr, v, gt, comp)
        
        return comp, nr

class BellmanFord:
    
    def __init__(self, graph):
        self.graph = graph
        self.V = graph.V
    
    def bellman_ford(self, source):

        dist = [float('inf')] * self.V
        dist[source] = 0
        
        for _ in range(self.V - 1):
            for (u, v), weight in self.graph.weights.items():
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
        
        for (u, v), weight in self.graph.weights.items():
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                return dist, True  # ujemny cykl
        
        return dist, False

class JohnsonAlgorithm:
    
    def __init__(self, graph):
        self.graph = graph
        self.V = graph.V
    
    def add_source_vertex(self):
        extended_graph = DirectedGraph(self.V + 1)
        
        for (u, v), weight in self.graph.weights.items():
            extended_graph.add_edge(u, v, weight)
        
        source = self.V
        for v in range(self.V):
            extended_graph.add_edge(source, v, 0)
        
        return extended_graph, source
    
    def dijkstra(self, graph, source):
        dist = [float('inf')] * graph.V
        dist[source] = 0
        visited = [False] * graph.V
        
        for _ in range(graph.V):
            min_dist = float('inf')
            u = -1
            for v in range(graph.V):
                if not visited[v] and dist[v] < min_dist:
                    min_dist = dist[v]
                    u = v
            
            if u == -1:
                break
            
            visited[u] = True
            
            for v in graph.adj_list[u]:
                weight = graph.weights.get((u, v), float('inf'))
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
        
        return dist
    
    def johnson(self):
        extended_graph, source = self.add_source_vertex()
        bellman = BellmanFord(extended_graph)
        h, has_negative_cycle = bellman.bellman_ford(source)
        
        if has_negative_cycle:
            return None, True 
        
        reweighted_graph = DirectedGraph(self.V)
        for (u, v), weight in self.graph.weights.items():
            new_weight = weight + h[u] - h[v] # gwarantuje ze wagi sa nieujemne
            reweighted_graph.add_edge(u, v, new_weight)
        
        distance_matrix = [[float('inf')] * self.V for _ in range(self.V)]
        
        for u in range(self.V):
            distances = self.dijkstra(reweighted_graph, u)
            for v in range(self.V):
                if distances[v] != float('inf'):
                    distance_matrix[u][v] = distances[v] - h[u] + h[v]
        
        return distance_matrix, False
