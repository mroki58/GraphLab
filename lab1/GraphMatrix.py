"""
Plik zapewnia klasę GraphMatrix, która może być dziedziczona przez reprezentacje grafu wykorzystujące macierz.
"""

from Graph import Graph
from Geometric import Point, Circle
import math


class GraphMatrix(Graph):
    """
    Klasa GraphMatrix dziedziczy po klasie Graph.

    Klasa nadpisuje wszystkie funkcje typowe dla listowej reprezentacji grafu zaimplementowane w klasie Graph.
    Przechowuje reprezentację grafu w postaci macierzy.
    """

    def __init__(self):
        """
        Inicjalizuje pustą macierz reprezentującą graf.
        """
        self._matrix = []

    def read_matrix_from_file(self, name):
        """
        Wczytuje macierz z pliku.

        Format macierzy w pliku:
        1 2 3\n1 2 3\n1 2 3\n

        Parameters
        ----------
        name : str
            Nazwa pliku zawierającego macierz grafu.
        """
        with open(name) as pl:
            for line in pl:
                _line = line.strip()
                self._matrix.append([int(i) for i in _line.split(" ")])

    def print(self):
        """
        Wypisuje reprezentację macierzową grafu.
        """
        for row in self._matrix:
            print(row)

    def calculateCords(self, circle):
        """
        Oblicza współrzędne wierzchołków grafu rozmieszczonych równomiernie na okręgu.

        Parameters
        ----------
        circle : Circle
            Okrąg, na którym rozmieszczone są wierzchołki.

        Returns
        -------
        list of Point
            Lista obiektów Point reprezentujących współrzędne wierzchołków.
        """
        # Wyznaczenie współrzędnych punktów
        noNodes = len(self._matrix)
        alpha = (2 * math.pi) / noNodes

        points = []
        for i in range(noNodes):
            x = circle.x + circle.r * math.cos(i * alpha - math.pi / 2)
            y = circle.y + circle.r * math.sin(i * alpha - math.pi / 2)
            points.append(Point.Point(x, y, label=str(i + 1)))

        return points

    def getEdges(self):
        """
        Funkcja do implementacji dla klas dziedziczących po GraphMatrix.

        Raises
        ------
        Exception
            Wyjątek zgłaszany, jeśli metoda nie zostanie zaimplementowana w klasie potomnej.
        """
        raise Exception("Metoda getEdges musi być zaimplementowana w klasie potomnej.")

