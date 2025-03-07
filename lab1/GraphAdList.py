import GraphAdMatrix
import GraphIncMatrix
from Graph import Graph


class GraphAdList(Graph):
    def __init__(self):
        self._list = {}

    def read_list_from_file(self, name):
        with open(name) as pl:
            for line in pl:
                _line = line[0:-1]
                _arg, _param = _line.split('.')
                self._list[int(_arg)] = [int(i) for i in _param.lstrip().split(' ')];


    def getEdges(self):
        edges = set()
        for key in self._list:
            for element in self._list[key]:
                edges.add(tuple( sorted( [key, element])))
        return edges

    def toAdMatrix(self):
        new = GraphAdMatrix.GraphAdMatrix()
        new._matrix = [[0 for __ in range(len(self._list.keys()))] for _ in range(len(self._list.keys()))]

        for key in self._list:
            for element in self._list[key]:
                new._matrix[key - 1][element - 1] = 1

        return new

 

    def toIncMatrix(self):
        new = GraphIncMatrix.GraphIncMatrix()
        
        edges = self.getEdges()

        for element in range(len(self._list.keys())):
            new._matrix.append([1 if (element + 1) in edge else 0 for edge in edges])

        new._edges = edges
        return new











