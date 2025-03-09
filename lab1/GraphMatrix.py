'''
    Plik zapewnia klase po której mogą dziedziczyć reprezentacje grafu wykorzystujące liste.
'''


from Graph import Graph
from Geometric import Point, Circle
import math

class GraphMatrix(Graph):
    '''
        Klasa dziedzicząca po klasie Graph.
        Klasa overriduje wszystkie funkcje typowe dla listowej reprezentacji grafu zaimplentowane w klasie Graph
        Przechowuje listę - macierz
    '''
    def __init__(self):
        self._matrix = []

    def read_matrix_from_file(self, name):
        '''
            Wczytuje macierz z pliku.
            Format macierzy w pliku 
            1 2 3\n1 2 3\n1 2 3\n
        '''
        with open(name) as pl:
            for line in pl:
                _line = line[0:-1]    
                self._matrix.append([int(i) for i in _line.split(" ")])

    def print(self):
        '''
            Wypisuje reprezentacje macierzową grafu
        '''
        for i in range(len(self._matrix)):
            print(self._matrix[i])

    def calculateCords(self, circle):
        '''
            Zwraca punkty w jakich znajdują się wierzchołki reprezentowane na kole - circle.
            Funkcja dla reprezentacji macierzowej grafu
        '''
        # wyznaczenie wspolrzednych punktow
        noNodes = len(self._matrix)
        alpha = (2 * math.pi) / noNodes

        points = []
        for i in range(noNodes):
            x = circle.x + circle.r * math.cos(i * alpha - math.pi / 2)
            y = circle.y + circle.r * math.sin(i * alpha - math.pi / 2)
            points.append(Point.Point(x, y, label= str(i + 1))) 

        return points

    def getEdges(self):
        '''
            Funkcja do implementacji dla pozostalych klas dziedziczacych po graphMatrix.
            Więcej o niej w pliku Graph.py
        '''
        raise Exception()

