"""
Plik zawierający klasę Graph.
"""

import math
from Geometric import Point, Circle

class Graph:
    """
    Klasa Graph do dziedziczenia.

    Zawiera definicje podstawowych funkcji typowych dla reprezentacji listowej grafu.
    Klasy dziedziczące mogą rozszerzać jej funkcjonalność.
    """

    def __init__(self):
        """Inicjalizuje pusty graf."""
        pass

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
        noNodes = len(self._list.keys())
        alpha = (2 * math.pi) / noNodes

        points = []
        for i in range(noNodes):
            x = circle.x + circle.r * math.cos(i * alpha - math.pi / 2)
            y = circle.y + circle.r * math.sin(i * alpha - math.pi / 2)
            points.append(Point.Point(x, y, label=str(i + 1)))

        return points

    def calculateEdges(self, points):
        """
        Tworzy listę krawędzi grafu na podstawie współrzędnych wierzchołków.

        Parameters
        ----------
        points : list of Point
            Lista obiektów Point reprezentujących współrzędne wierzchołków.

        Returns
        -------
        list of tuple
            Lista krotek (Point, Point) reprezentujących końce krawędzi grafu.

        Notes
        -----
        Funkcja zakłada, że etykiety wierzchołków są numerowane od 1.
        """
        edges = self.getEdges()
        edge_cords = []

        # -1 ponieważ etykiety są numerowane od 1, a indeksy w liście od 0
        for edge in edges:
            edge_cords.append((points[edge[0] - 1], points[edge[1] - 1]))

        return edge_cords

    def getEdges(self):
        """
        Zwraca listę krawędzi grafu.

        Returns
        -------
        list of tuple
            Lista krotek (int, int) reprezentujących krawędzie grafu.

        Raises
        ------
        Exception
            Metoda musi być zaimplementowana w klasie dziedziczącej.
        """
        raise Exception("Metoda getEdges musi być zaimplementowana w klasie dziedziczącej.")

    def print(self):
        """
        Wypisuje reprezentację listową grafu.

        Prints
        ------
        dict
            Reprezentacja listowa grafu.
        """
        print(self._list)
