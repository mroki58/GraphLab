'''
    Plik zawierający klase graph
'''

import math
from Geometric import Point, Circle

class Graph:
    '''
        Klasa Graph do dziedziczenia po niej
        Zawiera definicje paru funkcji typowych dla reprezentacji listowej grafu.
    '''
    def __init__(self):
        pass

    def calculateCords(self, circle):
        '''
            Zwraca punkty w jakich znajdują się wierzchołki reprezentowane na kole - circle.
            Funkcja dla reprezentacji listowej grafu
        '''
        noNodes = len(self._list.keys())
        alpha = (2 * math.pi) / noNodes

        points = []
        for i in range(noNodes):
            x = circle.x + circle.r * math.cos(i * alpha - math.pi / 2)
            y = circle.y + circle.r * math.sin(i * alpha - math.pi / 2)
            points.append(Point.Point(x, y, label= str(i + 1))) 

        return points
            
    def calculateEdges(self, points):
        '''
            Funkcja na podstawie points i  edges pobranych z funkcji getEdges,
            zwraca liste krotek punktów przechowujących wspolrzedne końców krawędzi
        '''
        edges = self.getEdges()
        edge_cords = []

        # -1 poniewaz Edges sa zapisywane wraz z labelem a nie indexem
        for edge in edges: 
            edge_cords.append( (points[edge[0] - 1],   points[edge[1] - 1]) )

        return edge_cords

    def getEdges(self):
        '''
            Funkcja ktora należy zdefiniować w klasie dziedziczącej po Graph, jeśli ma zostać wykorzystana - do rysowania grafu.
        '''
        raise Exception()

    def print(self):
        '''
            Wypisuje liste - reprezentacje grafu. 
        '''
        print(self._list)
