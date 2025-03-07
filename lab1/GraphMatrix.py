from Graph import Graph
from Geometric import Point, Circle
import math

class GraphMatrix(Graph):
    def __init__(self):
        self._matrix = []

    def read_matrix_from_file(self, name):
        with open(name) as pl:
            for line in pl:
                _line = line[0:-1]    
                self._matrix.append([int(i) for i in _line.split(" ")])

    def print(self):
        for i in range(len(self._matrix)):
            print(self._matrix[i])

    def calculateCords(self, circle):
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
        raise Exception()

