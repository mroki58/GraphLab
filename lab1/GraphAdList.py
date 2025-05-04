"""
Moduł zapewnia klasę GraphAdList, która implementuje reprezentację grafu za pomocą listy sąsiedztwa.
"""

import GraphAdMatrix
import GraphIncMatrix
from Graph import Graph


class GraphAdList(Graph):
    """
    Klasa GraphAdList dziedziczy po klasie Graph.

    Zapewnia funkcjonalności do obsługi grafu w reprezentacji listy sąsiedztwa.
    """

    def __init__(self):
        """Inicjalizuje pustą listę sąsiedztwa."""
        self._list = {}

    def read_list_from_file(self, name):
        """
        Wczytuje listową reprezentację grafu z pliku i zapisuje ją w `self._list`.

        Plik wejściowy musi być w formacie:
        1. 2 3\n2. 1\n3. 1\n4.\n

        Parameters
        ----------
        name : str
            Nazwa pliku zawierającego reprezentację grafu.
        """
        with open(name) as pl:
            for line in pl:
                _line = line.strip()
                _arg, _param = _line.split('.')
                self._list[int(_arg)] = [int(i) for i in _param.lstrip().split(' ')] if _param.strip() else []

    def getEdges(self):
        """
        Zwraca zbiór krawędzi w grafie reprezentowanym przez listę sąsiedztwa.

        Returns
        -------
        set of tuple
            Zbiór krotek reprezentujących krawędzie grafu. Każda krawędź jest zapisana w postaci `(u, v)`,
            gdzie `u < v` (krawędzie są sortowane, aby uniknąć duplikatów).
        """
        edges = set()
        for key in self._list:
            for element in self._list[key]:
                edges.add(tuple(sorted([key, element])))
        return edges

    def toAdMatrix(self):
        """
        Konwertuje graf z reprezentacji listy sąsiedztwa na reprezentację macierzy sąsiedztwa.

        Returns
        -------
        GraphAdMatrix
            Obiekt klasy GraphAdMatrix reprezentujący graf w postaci macierzy sąsiedztwa.
        """
        new = GraphAdMatrix.GraphAdMatrix()
        new._matrix = [[0 for __ in range(len(self._list.keys()))] for _ in range(len(self._list.keys()))]

        for key in self._list:
            for element in self._list[key]:
                new._matrix[key - 1][element - 1] = 1

        return new

    def toIncMatrix(self):
        """
        Konwertuje graf z reprezentacji listy sąsiedztwa na reprezentację macierzy incydencji.

        Returns
        -------
        GraphIncMatrix
            Obiekt klasy GraphIncMatrix reprezentujący graf w postaci macierzy incydencji.
        """
        new = GraphIncMatrix.GraphIncMatrix()
        edges = self.getEdges()

        for element in range(len(self._list.keys())):
            new._matrix.append([1 if (element + 1) in edge else 0 for edge in edges])

        new._edges = edges
        return new











