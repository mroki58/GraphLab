from GraphMatrix import GraphMatrix
import GraphAdList
import GraphIncMatrix
from Geometric import Point, Circle

class GraphAdMatrix(GraphMatrix):

    def __init__(self):
        super().__init__()

    def getEdges(self):
        edges = set()

        for i in range(len(self._matrix)):
            for j in range(len(self._matrix[i])):
                if self._matrix[i][j] == 1:
                    edges.add(tuple( sorted( [i + 1, j + 1] )))
        return edges
    

    def toAdList(self):
        new = GraphAdList.GraphAdList()

        for i in range(len(self._matrix)):
            new._list[i + 1] = []

            for j in range(len(self._matrix[i])): 
                if self._matrix[i][j] == 1:
                    new._list[i + 1].append(j + 1)

        return new

    def toIncMatrix(self):
        new = GraphIncMatrix.GraphIncMatrix()

        edges = self.getEdges()

        for element in range(len(self._matrix)):
            new._matrix.append([1 if (element + 1) in edge else 0 for edge in edges])

        new._edges = edges
        return new

                




