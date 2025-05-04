"""
Plik zapewnia klasę GraphIncMatrix, która zapewnia reprezentację grafu przy pomocy macierzy incydencji.
"""

from GraphMatrix import GraphMatrix
import GraphAdList
import GraphAdMatrix


class GraphIncMatrix(GraphMatrix):
    """
    Klasa GraphIncMatrix dziedziczy po klasie GraphMatrix.

    Zapewnia najważniejsze funkcje dla reprezentacji grafu przy pomocy macierzy incydencji.
    Obiekt może przechowywać dodatkowy pomocniczy i prywatny składnik `_edges`, który może stać się 
    zbiorem przechowującym krotki reprezentujące krawędzie grafu.
    """

    def __init__(self):
        """
        Inicjalizuje obiekt klasy GraphIncMatrix.
        """
        super().__init__()
        self._edges = None

    def calculateEdgesForInc(self):
        """
        Zapisuje w `self._edges` zbiór krawędzi w grafie reprezentowanym przez macierz incydencji.
        """
        self._edges = set()

        # Przechodzimy przez każdą z kolumn i pobieramy indeks wiersza, w którym znajduje się 1.
        for j in range(len(self._matrix[0])):
            edge = []
            for i in range(len(self._matrix)):
                if self._matrix[i][j] == 1:
                    edge.append(i + 1)
            self._edges.add(tuple(sorted(edge)))

    def getEdges(self):
        """
        Zwraca zbiór krawędzi w grafie reprezentowanym przez macierz incydencji.

        Wykorzystuje funkcję `calculateEdgesForInc`, która aktualizuje zbiór krawędzi.

        Returns
        -------
        set of tuple
            Zbiór krotek reprezentujących krawędzie grafu.
        """
        self.calculateEdgesForInc()
        return self._edges

    def toAdMatrix(self):
        """
        Konwertuje graf z reprezentacji macierzy incydencji na reprezentację macierzy sąsiedztwa.

        Returns
        -------
        GraphAdMatrix
            Obiekt klasy GraphAdMatrix reprezentujący graf w postaci macierzy sąsiedztwa.
        """
        # Potrzebuje najbardziej aktualnej zawartości zbioru krawędzi.
        self.calculateEdgesForInc()

        new = GraphAdMatrix.GraphAdMatrix()
        # Tworzy macierz wypełnioną zerami.
        new._matrix = [[0 for __ in range(len(self._matrix))] for _ in range(len(self._matrix))]

        # Przechodzimy przez wszystkie krawędzie i zapisujemy jedynki dla
        # indeksów macierzy i,j oraz j,i (dodajemy dla obu wierzchołków drugą krawędź).
        for edge in self._edges:
            new._matrix[edge[0] - 1][edge[1] - 1] = 1
            new._matrix[edge[1] - 1][edge[0] - 1] = 1

        return new

    def toAdList(self):
        """
        Konwertuje graf z reprezentacji macierzy incydencji na reprezentację listy sąsiedztwa.

        Returns
        -------
        GraphAdList
            Obiekt klasy GraphAdList reprezentujący graf w postaci listy sąsiedztwa.
        """
        # Potrzebuje najbardziej aktualnej zawartości zbioru krawędzi.
        self.calculateEdgesForInc()

        new = GraphAdList.GraphAdList()
        # Tworzy puste listy dla każdego klucza w słowniku reprezentującym wierzchołek.
        for i in range(len(self._matrix)):
            new._list[i + 1] = []

        # Przechodzimy przez wszystkie krawędzie i zapisujemy sąsiadów dla
        # wierzchołka pierwszego wierzchołek drugi i na odwrót.
        for edge in self._edges:
            new._list[edge[0]].append(edge[1])
            new._list[edge[1]].append(edge[0])

        return new



