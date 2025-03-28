
def init(G,s):
    """
    Inicjalizacja słowników odległości i poprzedników dla algorytmu Dijkstry.

    Args:
        G (nx.Graph): Graf wejściowy
        s (int): Wierzchołek startowy

    Returns:
        tuple: (ds, ps) gdzie:
            ds (dict): Słownik najkrótszych odległości 
            ps (dict): Słownik poprzedników 
    """
    ds = {v: float('inf') for v in G.nodes()}
    ps = {v: None for v in G.nodes()}
    ds[s]=0
    return ds,ps

def relax(u,v,ds,ps,w):
    """
    Relaksacja krawędzi (u, v) o wadze w.
    
    Args:
        u (int): Wierzchołek źródłowy
        v (int): Wierzchołek docelowy
        ds (dict): Aktualne oszacowania odległości
        ps (dict): Aktualni poprzednicy
        w (float): Waga krawędzi między u i v
    """
    if ds[v] > ds[u] +w:
        ds[v] = ds[u]+ w
        ps[v]=u

def dijkstra(G,s):
    """
    Oblicza najkrótsze ścieżki z wierzchołka źródłowego s 

    Args:
        G (nx.Graph): Graf wejściowy (wagi krawędzi muszą być nieujemne)
        s (int): Wierzchołek źródłowy

    Returns:
        tuple: (ds, ps) gdzie:
            ds (dict): Najkrótsze odległości od s do wszystkich wierzchołków
            ps (dict): Poprzedniki w najkrótszych ścieżkach
    
    Note:
        Wszystkie wagi krawędzi muszą być nieujemne
    """
    ds,ps=init(G,s)
    S=set()
    while len(S) != len(G.nodes()):
        u =min((v for v in G.nodes() if v not in S),key=lambda v:ds[v]) # powoduje czas działania O(n^2) ,kolejka priorytetowa poprawiła by wydajność
        S.add(u)
        for v in G.neighbors(u):
            if v not in S:
                edge_data= G.get_edge_data(u, v) 
                w = edge_data['weight'] if edge_data is not None else 0 # jesli krawędź między wierzchołkami nie istnieje to w = 0
                relax(u,v,ds,ps,w)

    return ds,ps

def create_distance_matrix(G):
    """
    Tworzy macierz odległości między wszystkimi parami wierzchołków.

    Args:
    G (nx.Graph): Graf wejściowy

    Returns:
        list: Dwuwymiarowa lista, gdzie matrix[i][j] = odległość między wierzchołkiem i+1 a j+1
    """
    distance_matrix=[]

    for v in G.nodes():
        ds,ps=dijkstra(G,v)
        distance_matrix.append([ds[key] for key in ds])

    return distance_matrix

def find_the_centre_of_the_graph(distance_matrix):
    """
    Znajduje centrum grafu

    Args:
        distance_matrix (list): Macierz odległości

    Returns:
    tuple: (centrum, min_distance) gdzie:
            centrum (int): Numer wierzchołka o minimalnej sumie odległości
            min_distance (int): Minimalna suma odległości
    """
    sum_of_distances = [sum(row) for row in distance_matrix]
    min_distance =min(sum_of_distances)

    return sum_of_distances.index(min_distance) + 1 , min_distance

def find_minmax(distance_matrix):
    """
    Znajduje centrum minimax grafu

    Args:
        distance_matrix (list): Macierz odległości
    
    Returns:
        tuple: (centrum, min_distance) gdzie:
                centrum (int): Numer wierzchołka
                min_distance (int):  odległość
    """
    max_distances = [max(row) for row in distance_matrix]
    min_distance = min(max_distances)

    return max_distances.index(min_distance)+1,min_distance

