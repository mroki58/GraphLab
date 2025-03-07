from GraphMatrix import GraphMatrix
import GraphAdList
import GraphAdMatrix

class GraphIncMatrix(GraphMatrix):
    def __init__(self):
        super().__init__()
        self._edges = None

    def calculateEdgesForInc(self):
        self._edges = set()

        for j in range(len(self._matrix[0])):
            edge = []
            for i in range(len(self._matrix)):
                if self._matrix[i][j] == 1:
                    edge.append(i + 1)
            self._edges.add(tuple(sorted(edge)))


    def getEdges(self):
        self.calculateEdgesForInc()
        return self._edges

    def toAdMatrix(self):
        if self._edges is None:
            self.calculateEdgesForInc()

        new = GraphAdMatrix.GraphAdMatrix()
        new._matrix = [[0 for __ in range(len(self._matrix))] for _ in range(len(self._matrix))]

        for edge in self._edges:
            new._matrix[edge[0] - 1][edge[1] - 1] = 1
            new._matrix[edge[1] - 1][edge[0] - 1] = 1

        return new

    def toAdList(self):
        if self._edges is None:
            self.calculateEdgesForInc()

        new = GraphAdList.GraphAdList()
        for i in range(len(self._matrix)):
            new._list[i + 1] = []

        for edge in self._edges:
            new._list[edge[0]].append(edge[1])
            new._list[edge[1]].append(edge[0])

        return new



