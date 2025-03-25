import networkx as nx
import matplotlib.pyplot as plt
import random
import os

# Utwórz folder na zapisywane obrazy
os.makedirs("examples", exist_ok=True)


def is_graphical_sequence(sequence):
    """
    Sprawdza, czy dany ciąg stopni jest grafowy. Używa algorytmu Havel-Hakimi.

    Args:
    sequence (list): Ciąg stopni wierzchołków.

    Returns:
    bool: True jeśli ciąg jest grafowy, False w przeciwnym razie.
    """
    A = sorted(sequence, reverse=True)
    n = len(A)
    while True:
        if all(x == 0 for x in A):  # Wszystkie stopnie to 0
            return True
        if A[0] > n or any(x < 0 for x in A):  # Sprawdzanie warunków niemożliwości
            return False
        for i in range(1, A[0] + 1):
            if i < n:
                A[i] -= 1
        A[0] = 0
        A.sort(reverse=True)


def construct_graph(sequence):
    """
    Tworzy graf z podanego ciągu stopni, jeśli jest grafowy.

    Args:
    sequence (list): Ciąg stopni wierzchołków.

    Returns:
    NetworkX Graph: Graf stworzony z ciągu stopni, lub None, jeśli ciąg nie jest grafowy.
    """
    A = sequence.copy()
    if not is_graphical_sequence(A):
        return None

    G = nx.Graph()
    n = len(A)
    G.add_nodes_from(range(1, n + 1))
    NodeWithDegree = [(A[i], i + 1) for i in range(n)]

    while any(degree > 0 for degree, _ in NodeWithDegree):
        NodeWithDegree.sort(reverse=True)
        for i in range(NodeWithDegree[0][0]):
            G.add_edge(NodeWithDegree[0][1], NodeWithDegree[i + 1][1])
            NodeWithDegree[i + 1] = (NodeWithDegree[i + 1][0] - 1, NodeWithDegree[i + 1][1])
        NodeWithDegree[0] = (0, NodeWithDegree[0][1])

    return G


def randomize_graph(G, steps=100):
    """
    Losowo przekształca graf, zachowując stopnie wierzchołków (edge switching).

    Args:
    G (NetworkX Graph): Graf do przekształcenia.
    steps (int): Liczba kroków losowego przekształcania.

    Returns:
    NetworkX Graph: Zmodyfikowany graf.
    """
    G = G.copy()
    for _ in range(steps):
        edges = list(G.edges())
        if len(edges) < 2:
            break
        edge1, edge2 = random.sample(edges, 2)
        a, b = edge1
        c, d = edge2
        if not G.has_edge(a, d) and not G.has_edge(b, c) and b != c and a != d:
            G.remove_edge(a, b)
            G.remove_edge(c, d)
            G.add_edge(a, d)
            G.add_edge(b, c)
    return G


def save_graph_image(G, filename, layout=nx.circular_layout):
    """
    Zapisuje obraz grafu do pliku PNG w folderze 'examples'.

    Args:
    G (NetworkX Graph): Graf do zapisania.
    filename (str): Nazwa pliku, do którego zapisany zostanie obraz grafu.
    layout (function): Funkcja do określenia układu wierzchołków w przestrzeni 2D.
    """
    comp = connected_components(G)
    color_map = [comp[node] for node in G.nodes()]
    pos = layout(G)

    plt.figure(figsize=(6, 6))
    nx.draw(G, pos, with_labels=True, node_size=500, node_color=color_map,
            font_size=14, font_weight="bold", edge_color="gray", cmap=plt.cm.rainbow)

    path = os.path.join("examples", filename)
    plt.savefig(path)
    plt.close()
    print(f"Graph image saved to {path}")


def connected_components(G):
    """
    Zwraca słownik z numerami składowych spójności dla każdego wierzchołka.

    Args:
    G (NetworkX Graph): Graf, dla którego szukamy składowych spójności.

    Returns:
    dict: Słownik, gdzie klucze to wierzchołki, a wartości to numery składowych spójności.
    """
    nr = 0
    comp = {node: -1 for node in G.nodes()}
    for node in G.nodes():
        if comp[node] == -1:
            nr += 1
            comp[node] = nr
            _dfs_component(G, node, nr, comp)
    return comp


def _dfs_component(G, node, nr, comp):
    """
    Rekurencyjna funkcja do przeszukiwania grafu w głąb w celu znalezienia składowych spójności.

    Args:
    G (NetworkX Graph): Graf do przeszukiwania.
    node (int): Aktualny wierzchołek.
    nr (int): Numer składowej spójności.
    comp (dict): Słownik z numerami składowych spójności.
    """
    for neighbor in G.neighbors(node):
        if comp[neighbor] == -1:
            comp[neighbor] = nr
            _dfs_component(G, neighbor, nr, comp)


def format_components(comp):
    """
    Formatuje i drukuje składowe spójności oraz największą z nich.

    Args:
    comp (dict): Słownik składowych spójności.
    """
    components = {}
    for node, number in comp.items():
        components.setdefault(number, []).append(node)
    for c in components.values():
        c.sort()

    for i, number in enumerate(sorted(components), 1):
        print(f"{i}) {' '.join(map(str, components[number]))}")

    largest = max(components.values(), key=len)
    largest_num = [num for num, nodes in components.items() if nodes == largest][0]
    print(f"\nNajwiększa składowa ma numer {largest_num}.")


def is_connected(G):
    """
    Sprawdza, czy graf jest spójny (jedna składowa spójności).

    Args:
    G (NetworkX Graph): Graf do sprawdzenia.

    Returns:
    bool: True, jeśli graf jest spójny, False w przeciwnym razie.
    """
    comp = connected_components(G)
    return len(set(comp.values())) == 1


def is_eulerian(G):
    """
    Sprawdza, czy graf nieskierowany ma cykl Eulera.
    Warunki: graf musi być spójny oraz wszystkie stopnie wierzchołków muszą być parzyste.

    Args:
    G (NetworkX Graph): Graf do sprawdzenia.

    Returns:
    bool: True, jeśli graf ma cykl Eulera, False w przeciwnym razie.
    """
    if not is_connected(G):
        return False
    return all(deg % 2 == 0 for _, deg in G.degree())


def generate_eulerian_graph(n, min_deg=2, max_deg=6, max_attempts=1000):
    """
    Generuje spójny graf eulerowski o n wierzchołkach, w którym wszystkie stopnie są parzyste.

    Args:
    n (int): Liczba wierzchołków w grafie.
    min_deg (int): Minimalny stopień wierzchołka.
    max_deg (int): Maksymalny stopień wierzchołka.
    max_attempts (int): Maksymalna liczba prób wygenerowania grafu.

    Returns:
    NetworkX Graph: Graf eulerowski lub None, jeśli graf nie jest eulerowski.
    """
    assert min_deg % 2 == 0 and max_deg % 2 == 0, "Używaj tylko parzystych stopni!"

    for attempt in range(max_attempts):
        sequence = [random.choice(range(min_deg, max_deg + 1, 2)) for _ in range(n)]

        if not is_graphical_sequence(sequence):
            continue

        G = construct_graph(sequence)
        if G is None:
            continue

        if is_connected(G):
            return G

    print("Nie udało się wygenerować spójnego grafu eulerowskiego.")
    return None


def regular_graph(n, k):
    """
    Tworzy graf regularny o n wierzchołkach i stopniu k.

    Args:
    n (int): Liczba wierzchołków.
    k (int): Stopień wierzchołków.

    Returns:
    NetworkX Graph: Graf regularny lub None, jeśli nie udało się go wygenerować.
    """
    if k >= n or (k % 2 == 1 and n % 2 == 1):
        return None
    A = [k] * n
    G = construct_graph(A)
    if G:
        G = randomize_graph(G, 100)
    return G


def fleury(G):
    """
    Zwraca cykl Eulera w postaci listy wierzchołków.

    Args:
    G (NetworkX Graph): Graf do przetworzenia.

    Returns:
    list: Cykl Eulera lub None, jeśli graf nie ma cyklu Eulera.
    """
    if not is_eulerian(G):
        print("[fleury] Graf nie ma cyklu Eulera (nie jest eulerowski).")
        return None

    G = G.copy()
    circuit = []
    current = next(iter(G.nodes()))

    def is_valid_edge(u, v):
        if G.number_of_edges(u, v) == 0:
            return False

        if len(list(G.neighbors(u))) == 1:
            return True

        G.remove_edge(u, v)
        is_still_connected = is_connected(G)
        G.add_edge(u, v)

        if is_still_connected:
            return True

        neighbors = list(G.neighbors(u))
        all_are_bridges = True
        for w in neighbors:
            if w == v:
                continue
            G.remove_edge(u, w)
            still_conn = is_connected(G)
            G.add_edge(u, w)
            if still_conn:
                all_are_bridges = False
                break

        return all_are_bridges

    def dfs_fleury(u):
        for v in list(G.neighbors(u)):
            if is_valid_edge(u, v):
                G.remove_edge(u, v)
                dfs_fleury(v)
        circuit.append(u)

    dfs_fleury(current)
    return circuit[::-1]


def hamiltonian_cycle(G):
    """
    Szuka cyklu Hamiltona w grafie.

    Args:
    G (NetworkX Graph): Graf do przetworzenia.

    Returns:
    list: Cykl Hamiltona lub None, jeśli graf nie zawiera cyklu Hamiltona.
    """
    if not is_connected(G):
        return None

    path = []
    visited = {node: False for node in G.nodes()}
    startnode = next(iter(G.nodes()))

    def dfs(v):
        path.append(v)
        visited[v] = True
        if len(path) == len(G.nodes()):
            if G.has_edge(path[-1], path[0]):
                path.append(path[0])
                return path
            else:
                path.pop()
                visited[v] = False
                return None

        for neighbor in G.neighbors(v):
            if not visited[neighbor]:
                result = dfs(neighbor)
                if result is not None:
                    return result

        path.pop()
        visited[v] = False
        return None

    return dfs(startnode)


if __name__ == "__main__":
    # Zadanie 1: Sprawdzanie ciągu graficznego i budowanie grafu
    sequence = [1, 1, 1, 1]
    A = sequence.copy()

    if is_graphical_sequence(A):
        G1 = construct_graph(A)

        save_graph_image(G1, "graph_task_1.png")
        format_components(connected_components(G1))
    else:
        print("Ciąg nie jest grafowy")

    # Zadanie 2: Randomizacja krawędzi
    G2 = randomize_graph(G1, 50)
    save_graph_image(G2, "graph_task_2.png")
    format_components(connected_components(G2))

    # Zadanie 3: Składowe spójności
    comp = connected_components(G2)
    save_graph_image(G2, "graph_task_3.png")
    format_components(comp)

    # Zadanie 4: Cykl Eulera
    G3 = generate_eulerian_graph(10, 2, 6)
    if G3:
        save_graph_image(G3, "graph_task_4.png")
        print(f"Cykl Eulera: {fleury(G3)}")

    # Zadanie 5: Graf k-regularny
    G4 = regular_graph(10, 4)
    if G4:
        save_graph_image(G4, "graph_task_5.png")
        format_components(connected_components(G4))

    # Zadanie 6: Cykl Hamiltona
    cycle = hamiltonian_cycle(G4)
    if cycle:
        print(f"Cykl Hamiltona: {cycle}")
    else:
        print("Brak cyklu Hamiltona.")

