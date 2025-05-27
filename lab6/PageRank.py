import numpy as np

graph = {
    'A': ['E', 'F', 'I'],
    'B': ['A', 'C', 'F'],
    'C': ['B', 'D', 'E', 'L'],
    'D': ['C', 'E', 'H', 'I', 'K'],
    'E': ['C', 'G', 'H', 'I'],
    'F': ['B', 'G'],
    'G': ['E', 'F', 'H'],
    'H': ['D', 'G', 'I', 'L'],
    'I': ['D', 'E', 'H', 'J'],
    'J': ['I'],
    'K': ['D', 'I'],
    'L': ['A', 'H']
}

nodes = sorted(list(graph.keys()))
n = len(nodes)
node_to_index = {node: i for i, node in enumerate(nodes)}
index_to_node = {i: node for i, node in enumerate(nodes)}

d = 0.15  

def pagerank_random_walk(graph, nodes, d, num_steps=1000000):
    visits = {node: 0 for node in nodes}
    current_node = np.random.choice(nodes) 

    for _ in range(num_steps):
        visits[current_node] += 1
        
        if np.random.rand() < d: 
            current_node = np.random.choice(nodes)
        else: 
            if graph[current_node]:
                current_node = np.random.choice(graph[current_node])
            else:
                current_node = np.random.choice(nodes)

    total_visits = sum(visits.values())
    pagerank = {node: count / total_visits for node, count in visits.items()}
    return pagerank

print("--- PageRank z teleportacja ---")
pr_random_walk = pagerank_random_walk(graph, nodes, d)
sorted_pr_rw = sorted(pr_random_walk.items(), key=lambda item: item[1], reverse=True)
for node, pr_value in sorted_pr_rw:
    print(f"{node} ==> PageRank = {pr_value:.6f}")

def pagerank_power_iteration(graph, nodes, d, max_iterations=100, tolerance=1e-7):
    n = len(nodes)
    node_to_index = {node: i for i, node in enumerate(nodes)}

    pr_vector = np.full(n, 1/n)

    P = np.zeros((n, n))
    for i, u in enumerate(nodes):
        out_links = graph[u]
        out_degree = len(out_links)
        
        for j, v in enumerate(nodes):
            if v in out_links:
                P[j, i] = (1 - d) / out_degree 
            P[j, i] += d / n
            
        if out_degree == 0:
            for j in range(n):
                P[j, i] = 1/n 

    for iteration in range(max_iterations):
        new_pr_vector = np.dot(P, pr_vector) # p_t+1 = P * p_t 
        if np.linalg.norm(new_pr_vector - pr_vector, ord=1) < tolerance:
            break
        pr_vector = new_pr_vector
    else:
        print("nie udalo sie")

    pagerank = {index_to_node[i]: pr_vector[i] for i in range(n)}
    return pagerank

print("\n--- PageRank z wektorem obsadzen ---")
pr_power_iteration = pagerank_power_iteration(graph, nodes, d)
sorted_pr_pi = sorted(pr_power_iteration.items(), key=lambda item: item[1], reverse=True)
for node, pr_value in sorted_pr_pi:
    print(f"{node} ==> PageRank = {pr_value:.6f}")