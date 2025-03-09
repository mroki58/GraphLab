'''
    Plik zapewnia klase GraphAdMatrix, która zapewnia reprezentacjke grafu przy pomocy macierzy incydencji
'''

from GraphMatrix import GraphMatrix
import GraphAdList
import GraphAdMatrix

class GraphIncMatrix(GraphMatrix):
    '''
        GraphIncMatrix klasa dziedziczy po klasie GraphMatrix
        Zapewnia najwazniejsze funkcje dla reprezentacji grafu przy pomocy macierzy incydencji.
        Obiekt może przechowywać dodatkowy pomocniczy i prywatny składnik _edges który to może stać się 
        setem przechowującym krotki reprezentujące krawędzie grafu.
    '''
    def __init__(self):
        super().__init__()
        self._edges = None

    def calculateEdgesForInc(self):
        '''
            Zapisuje w self._edges zbiór krawędzi w grafie reprezentowanym przez macierz s.
        '''
        self._edges = set()

        # przechodzimy przez każdą z kolumn i pobieramy indeks wiersza w którym znajduje się 1
        for j in range(len(self._matrix[0])):
            edge = []
            for i in range(len(self._matrix)):
                if self._matrix[i][j] == 1:
                    edge.append(i + 1)
            self._edges.add(tuple(sorted(edge)))


    def getEdges(self):
        '''
            Zwraca zbiór krawędzi w grafie reprezentowanym przez macierz i. . Wykorzystuje funkcje calculateEdgesForInc. Która robi to samo
        '''
        self.calculateEdgesForInc()
        return self._edges

    def toAdMatrix(self):
        '''
            Zwraca obiekt klasy GraphAdMatrix. 
            Konwertuje graf z reprezentacji na reprezentacje macierzy sąsiedztwa
        '''
        # potrzebuje najbardziej aktualnej zawartości zbioru krawędzi
        self.calculateEdgesForInc()

        new = GraphAdMatrix.GraphAdMatrix()
        # Tworzy macierz wypelniona zerami
        new._matrix = [[0 for __ in range(len(self._matrix))] for _ in range(len(self._matrix))]

        # Przechodzimy przez wszystkie krawedzie i zapisujemy jedynki dla
        # indeksów macierzy i,j oraz j,i (dodajemy dla obu wierzchołków drugą krawędź)
        for edge in self._edges:
            new._matrix[edge[0] - 1][edge[1] - 1] = 1
            new._matrix[edge[1] - 1][edge[0] - 1] = 1

        return new

    def toAdList(self):
        '''
            Zwraca obiekt klasy GraphAdList. 
            Konwertuje graf z reprezentacji na reprezentacje listy sąsiedztwa
        '''
        # potrzebuje najbardziej aktualnej zawartości zbioru krawędzi
        self.calculateEdgesForInc()

        new = GraphAdList.GraphAdList()
        # Tworzy puste listy dla każdego key w dictionary reprezentującego wierzchołek
        for i in range(len(self._matrix)):
            new._list[i + 1] = []

        # Przechodzimy przez wszystkie krawedzie i zapisujemy sąsiadów dla
        # wierzchołka pierwszego wierzchołek drugi i na odwrót
        for edge in self._edges:
            new._list[edge[0]].append(edge[1])
            new._list[edge[1]].append(edge[0])

        return new



