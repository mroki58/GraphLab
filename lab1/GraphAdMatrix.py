"""
Plik zapewnia klasę GraphAdMatrix, która zapewnia reprezentację grafu przy pomocy macierzy sąsiedztwa.
"""

from GraphMatrix import GraphMatrix
import GraphAdList
import GraphIncMatrix
from Geometric import Point, Circle


class GraphAdMatrix(GraphMatrix):
    """
    Klasa GraphAdMatrix dziedziczy po klasie GraphMatrix.

    Zapewnia najważniejsze funkcje dla reprezentacji grafu przy pomocy macierzy sąsiedztwa.
    """

    def __init__(self):
        """Inicjalizuje obiekt klasy GraphAdMatrix."""
        super().__init__()

    def getEdges(self):
        """
        Zwraca zbiór krawędzi w grafie reprezentowanym przez macierz sąsiedztwa.

        Returns
        -------
        set of tuple
            Zbiór krotek reprezentujących krawędzie grafu. Każda krawędź jest zapisana w postaci `(u, v)`,
            gdzie `u < v` (krawędzie są sortowane, aby uniknąć duplikatów).
        """
        edges = set()

        # Przechodzi przez wszystkie elementy w poszukiwaniu jedynek.
        # Następnie zapisuje w secie krawędzie w postaci (row - i, column - j).
        for i in range(len(self._matrix)):
            for j in range(i + 1, len(self._matrix[i])):
                if self._matrix[i][j] == 1:
                    edges.add((i + 1, j + 1))
        return edges

    def toAdList(self):
        """
        Konwertuje graf z reprezentacji macierzy sąsiedztwa na reprezentację listy sąsiedztwa.

        Returns
        -------
        GraphAdList
            Obiekt klasy GraphAdList reprezentujący graf w postaci listy sąsiedztwa.
        """
        new = GraphAdList.GraphAdList()

        # Przechodzi przez wszystkie elementy w macierzy (mogłoby tylko przez połowę - możliwa optymalizacja).
        # Dla każdego wiersza reprezentującego wierzchołek tworzy nową pustą listę.
        # Następnie przechodzi przez wszystkie elementy w wierszu w poszukiwaniu sąsiadów elementu (indeksów, gdzie napotyka 1).
        for i in range(len(self._matrix)):
            new._list[i + 1] = []

            for j in range(len(self._matrix[i])):
                if self._matrix[i][j] == 1:
                    new._list[i + 1].append(j + 1)

        return new

    def toIncMatrix(self):
        """
        Konwertuje graf z reprezentacji macierzy sąsiedztwa na reprezentację macierzy incydencji.

        Returns
        -------
        GraphIncMatrix
            Obiekt klasy GraphIncMatrix reprezentujący graf w postaci macierzy incydencji.
        """
        new = GraphIncMatrix.GraphIncMatrix()

        # Pobiera krawędzie grafu.
        edges = self.getEdges()

        # Przechodzi przez wszystkie krawędzie dla danego wierzchołka (element + 1).
        # Jeśli znajduje się on w tej krawędzi, zapisuje w kolumnie 1, w przeciwnym przypadku 0.
        for element in range(len(self._matrix)):
            new._matrix.append([1 if (element + 1) in edge else 0 for edge in edges])

        new._edges = edges
        return new






