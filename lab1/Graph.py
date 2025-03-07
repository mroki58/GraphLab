import math
from Geometric import Point, Circle

class Graph:
    def __init__(self):
        pass

    def calculateCords(self, circle):
        # wyznaczenie wspolrzednych punktow
        noNodes = len(self._list.keys())
        alpha = (2 * math.pi) / noNodes

        points = []
        for i in range(noNodes):
            x = circle.x + circle.r * math.cos(i * alpha - math.pi / 2)
            y = circle.y + circle.r * math.sin(i * alpha - math.pi / 2)
            points.append(Point.Point(x, y, label= str(i + 1))) 

        return points
            
    def calculateEdges(self, points):
        edges = self.getEdges()
        edge_cords = []

        # -1 poniewaz Edges sa zapisywane wraz z labelem a nie indexem
        for edge in edges: 
            edge_cords.append( (points[edge[0] - 1],   points[edge[1] - 1]) )

        return edge_cords

    def getEdges(self):
        raise Exception()

    def print(self):
        print(self._list)
