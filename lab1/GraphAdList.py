'''
    Plik zapewnia klase GraphAdMatrix, która zapewnia reprezentacjke grafu przy pomocy listy sąsiedztwa
'''
import GraphAdMatrix
import GraphIncMatrix
from Graph import Graph


class GraphAdList(Graph):
    '''
        GraphAdList klasa dziedziczy po klasie Graph
        Zapewnia najwazniejsze funkcje dla reprezentacji grafu przy pomocy listy sąsiedztwa
    '''
    def __init__(self):
        self._list = {}

    def read_list_from_file(self, name):
        '''
            Pobiera z pliku listową reprezentacje grafu i zapisuje w self._list
            Plik o nazwie name musi być w formacie
            1. 2 3\n2. 1\n3. 1\n4.\n
        '''
        with open(name) as pl:
            for line in pl:
                _line = line[0:-1]
                _arg, _param = _line.split('.')
                self._list[int(_arg)] = [int(i) for i in _param.lstrip().split(' ')] if _param.strip() else []
                


    def getEdges(self):
        '''
            Zwraca zbiór krawędzi w grafie reprezentowanym przez listy s.
        '''
        edges = set()
        # Przechodzimy przez wszystkie wierzchołki i do zbioru zapisujemy
        # elementy listy sąsiedztwa wraz z kluczem reprezentującym wierzchołek
        # zawsze sortujemy je przed dodaniem aby nie dodać (1,5) oraz (5,1)
        for key in self._list:
            for element in self._list[key]:
                edges.add(tuple( sorted( [key, element])))
        return edges

    def toAdMatrix(self):
        '''
            Zwraca obiekt klasy GraphAdMatrix. 
            Konwertuje graf z reprezentacji na reprezentacje macierzy sąsiedztwa
        '''
        new = GraphAdMatrix.GraphAdMatrix()
        # macierz wypełniona 0
        new._matrix = [[0 for __ in range(len(self._list.keys()))] for _ in range(len(self._list.keys()))]

        # Dla każdego klucza reprezentującego wierzchołek, przehodzimy przez wszystkie elementy listy - sąsiadów.
        # Wypełniamy macierz sąsiedztwa 1 w indeksie [klucz - 1][sąsiad - 1]
        for key in self._list:
            for element in self._list[key]:
                new._matrix[key - 1][element - 1] = 1

        return new

 

    def toIncMatrix(self):
        '''
            Zwraca obiekt klasy GraphIncMatrix. 
            Konwertuje graf z reprezentacji na reprezentacje macierzy incydencji
        '''
        new = GraphIncMatrix.GraphIncMatrix()
        # Pobieramy krawędzie
        edges = self.getEdges()

        # przechodzi przez wszystkie krawędzie dla danego wierzchołka - (element + 1)
        # Jeśli znajduje się on w tej krawędzi zapisujemy w kolumnie 1 w przeciwnym przypadku 0
        for element in range(len(self._list.keys())):
            new._matrix.append([1 if (element + 1) in edge else 0 for edge in edges])

        new._edges = edges
        return new











