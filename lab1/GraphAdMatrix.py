'''
    Plik zapewnia klase GraphAdMatrix, która zapewnia reprezentacjke grafu przy pomocy macierzy sąsiedztwa
'''
from GraphMatrix import GraphMatrix
import GraphAdList
import GraphIncMatrix
from Geometric import Point, Circle

class GraphAdMatrix(GraphMatrix):
    '''
        GraphAdMatrix klasa dziedziczy po klasie GraphMatrix
        Zapewnia najwazniejsze funkcje dla reprezentacji grafu przy pomocy macierzy sąsiedztwa
    '''
    def __init__(self):
        super().__init__()

    def getEdges(self):
        '''
            Zwraca zbiór krawędzi w grafie reprezentowanym przez macierz s.
        '''
        edges = set()

        # przechodzi przez wszystkie elementy w poszukiwaniu jedynek - nastepnie row - i , column - j 1 zapisuje w secie
        for i in range(len(self._matrix)):
            for j in range(i + 1, len(self._matrix[i])):
                if self._matrix[i][j] == 1:
                    edges.add(( i + 1, j + 1 ))
        return edges
    

    def toAdList(self):
        '''
            Zwraca obiekt klasy GraphAdList. 
            Konwertuje graf z reprezentacji na reprezentacje listy sąsiedztwa
        '''
        new = GraphAdList.GraphAdList()

        # przechodzi przez wszystkie elementy elementy w macierzy (mogłoby tylko przez połowę - możliwa optymalizacja)
        # dla każdego wiersza reprezentującego wierzchołek tworzy nową pustą listę
        # następnie przechodzi przez wszystkie elementy w wierszu w poszukiwaniu sąsiadów elementu (indeksów gdzie napotyka 1)
        for i in range(len(self._matrix)):
            new._list[i + 1] = []

            for j in range(len(self._matrix[i])): 
                if self._matrix[i][j] == 1:
                    new._list[i + 1].append(j + 1)

        return new

    def toIncMatrix(self):
        '''
            Zwraca obiekt klasy GraphIncList. 
            Konwertuje graf z reprezentacji na reprezentacje listy sąsiedztwa
        '''
        new = GraphIncMatrix.GraphIncMatrix()

        # pobiera krawędzie grafu
        edges = self.getEdges()

        # przechodzi przez wszystkie krawędzie dla danego wierzchołka - (element + 1)
        # Jeśli znajduje się on w tej krawędzi zapisujemy w kolumnie 1 w przeciwnym przypadku 0
        for element in range(len(self._matrix)):
            new._matrix.append([1 if (element + 1) in edge else 0 for edge in edges])

        new._edges = edges
        return new

                




