"""
Moduł zapewnia funkcje do generowania losowych grafów i zapisywania ich w różnych reprezentacjach.
"""

import random


def writeAdjList(vertexes, edges, filename):
    """
    Zapisuje graf w formacie listy sąsiedztwa do pliku.

    Parameters
    ----------
    vertexes : list of int
        Lista wierzchołków grafu.
    edges : list of tuple
        Lista krawędzi grafu w postaci krotek (u, v).
    filename : str
        Nazwa pliku, do którego zapisany zostanie graf.
    """
    with open(filename, 'w') as pl:
        for vertex in vertexes:
            line = f"{vertex}."
            for edge in edges:
                if edge[0] == vertex:
                    line += f" {edge[1]}"
                elif edge[1] == vertex:
                    line += f" {edge[0]}"
            line += '\n'
            pl.write(line)


def writeAdjMatrix(vertexes, edges, filename):
    """
    Zapisuje graf w formacie macierzy sąsiedztwa do pliku.

    Parameters
    ----------
    vertexes : list of int
        Lista wierzchołków grafu.
    edges : list of tuple
        Lista krawędzi grafu w postaci krotek (u, v).
    filename : str
        Nazwa pliku, do którego zapisany zostanie graf.
    """
    with open(filename, 'w') as pl:
        matrix = [[0 for _ in range(len(vertexes))] for _ in range(len(vertexes))]

        for edge in edges:
            v1 = edge[0] - 1
            v2 = edge[1] - 1
            matrix[v1][v2] = 1
            matrix[v2][v1] = 1

        for row in matrix:
            line = ' '.join(str(cell) for cell in row) + '\n'
            pl.write(line)


def writeIncMatrix(vertexes, edges, filename):
    """
    Zapisuje graf w formacie macierzy incydencji do pliku.

    Parameters
    ----------
    vertexes : list of int
        Lista wierzchołków grafu.
    edges : list of tuple
        Lista krawędzi grafu w postaci krotek (u, v).
    filename : str
        Nazwa pliku, do którego zapisany zostanie graf.

    Notes
    -----
    Funkcja sprawdza, czy graf ma krawędzie, zanim zapisze go w formacie macierzy incydencji.
    """
    if len(edges):
        with open(filename, 'w') as pl:
            for vertex in vertexes:
                row = [1 if vertex in edge else 0 for edge in edges]
                line = ' '.join(str(cell) for cell in row) + '\n'
                pl.write(line)


def getPossibleEdges(noOfNodes):
    """
    Generuje wszystkie możliwe krawędzie dla grafu o podanej liczbie wierzchołków.

    Parameters
    ----------
    noOfNodes : int
        Liczba wierzchołków w grafie.

    Returns
    -------
    set of tuple
        Zbiór krotek reprezentujących wszystkie możliwe krawędzie grafu.
    """
    possibleEdges = set()
    for i in range(noOfNodes):
        for j in range(i + 1, noOfNodes):
            possibleEdges.add((i + 1, j + 1))
    return possibleEdges


def _writeToFile(vertexes, edges, representation, filename):
    """
    Zapisuje graf w podanej reprezentacji do pliku.

    Parameters
    ----------
    vertexes : list of int
        Lista wierzchołków grafu.
    edges : list of tuple
        Lista krawędzi grafu w postaci krotek (u, v).
    representation : str
        Reprezentacja grafu ('adjList', 'adjMatrix', 'incMatrix', 'all').
    filename : str
        Nazwa pliku, do którego zapisany zostanie graf.

    Raises
    ------
    Exception
        Jeśli podana reprezentacja grafu nie jest obsługiwana.
    """
    if representation == 'adjList':
        writeAdjList(vertexes, edges, filename)
    elif representation == 'adjMatrix':
        writeAdjMatrix(vertexes, edges, filename)
    elif representation == 'incMatrix':
        writeIncMatrix(vertexes, edges, filename)
    elif representation == 'all':
        writeAdjList(vertexes, edges, filename.split('.')[0] + 'adjlist.dat')
        writeAdjMatrix(vertexes, edges, filename.split('.')[0] + 'adjmatrix.dat')
        writeIncMatrix(vertexes, edges, filename.split('.')[0] + 'incmatrix.dat')
    else:
        raise Exception('Representation for graph not supported')


def generateRandomWithEdges(noOfNodes, noOfEdges, representation="adjList", filename="representation.dat"):
    """
    Generuje graf o określonej liczbie wierzchołków i krawędzi.

    Parameters
    ----------
    noOfNodes : int
        Liczba wierzchołków w grafie.
    noOfEdges : int
        Liczba krawędzi w grafie.
    representation : str, optional
        Reprezentacja grafu ('adjList', 'adjMatrix', 'incMatrix', 'all'). Domyślnie 'adjList'.
    filename : str, optional
        Nazwa pliku, do którego zapisany zostanie graf. Domyślnie 'representation.dat'.
    """
    vertexes = [i + 1 for i in range(noOfNodes)]
    edges = []
    possibleEdges = getPossibleEdges(noOfNodes)
    maxNumberOfEdges = len(possibleEdges)

    i = 0
    while i < maxNumberOfEdges and i < noOfEdges:
        random_edge = random.choice(list(possibleEdges))
        possibleEdges.remove(random_edge)
        edges.append(random_edge)
        i += 1

    _writeToFile(vertexes, edges, representation, filename)


def generateRandomWithPropabilities(noOfNodes, prop, representation='adjList', filename="probRepresentation.dat"):
    """
    Generuje graf o określonej liczbie wierzchołków z prawdopodobieństwem dodania każdej krawędzi.

    Parameters
    ----------
    noOfNodes : int
        Liczba wierzchołków w grafie.
    prop : float
        Prawdopodobieństwo dodania każdej krawędzi (wartość z zakresu 0-1).
    representation : str, optional
        Reprezentacja grafu ('adjList', 'adjMatrix', 'incMatrix', 'all'). Domyślnie 'adjList'.
    filename : str, optional
        Nazwa pliku, do którego zapisany zostanie graf. Domyślnie 'probRepresentation.dat'.
    """
    vertexes = [i + 1 for i in range(noOfNodes)]
    edges = []
    possibleEdges = getPossibleEdges(noOfNodes)

    for edge in possibleEdges:
        if random.random() < prop:
            edges.append(edge)

    _writeToFile(vertexes, edges, representation, filename)


if __name__ == "__main__":
    generateRandomWithEdges(15, 50, representation='all', filename='ned')
    generateRandomWithPropabilities(15, 0.4, representation='all', filename='prob')





