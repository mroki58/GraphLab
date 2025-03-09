import random

def writeAdjList(vertexes, edges, filename):
    ''' Dla podanych wierzcholkow, krawedzi pliku zapisuje plik w formacie 
        zgodnym z reprezentacją grafu za pomocą listy sąsiedztwa
    '''
    with open(filename, 'w') as pl:
        for vertex in vertexes:
            line = ''
            line += str(vertex) + '.'
            for edge in edges:
                if edge[0] == vertex:
                    line += ' ' + str(edge[1])
                elif edge[1] == vertex:
                    line += ' ' + str(edge[0])
            line += '\n'
            pl.write(line)

def writeAdjMatrix(vertexes, edges, filename):
    ''' Dla podanych wierzcholkow, krawedzi pliku zapisuje plik w formacie 
        zgodnym z reprezentacją grafu za pomocą macierzy sąsiedztwa
    '''
    with open(filename, 'w') as pl: 
        matrix = [[0 for _ in range(len(vertexes))] for _ in range(len(vertexes))]

        for edge in edges:
            v1 = edge[0] - 1
            v2 = edge[1] - 1
            matrix[v1][v2] = 1
            matrix[v2][v1] = 1 

        # Zapisujemy macierz sąsiedztwa do pliku
        for row in matrix:
            line = ' '.join(str(cell) for cell in row) + '\n'
            pl.write(line)

            
def writeIncMatrix(vertexes, edges, filename):
    ''' Dla podanych wierzcholkow, krawedzi pliku zapisuje plik w formacie 
        zgodnym z reprezentacją grafu za pomocą macierzy incydencji.
        Sprawdza czy graf może być reprezentowany przez macierz incydencji - czy ma krawędzie
    '''
    if len(edges):
        with open(filename, 'w') as pl:
            for vertex in vertexes:
                row = [1 if vertex in edge else 0 for edge in edges]
                line = ''
                line += str(row[0])
                for i in range(1, len(row)):
                    line += f' {row[i]}'

                line += '\n'
                pl.write(line)


def getPossibleEdges(noOfNodes):
    '''
        Dla danej liczby wierzchołków,
        zwraca wszystkie mozliwe krawedzie w postaci zbioru
    '''
    possibleEdges = set()

    for i in range(noOfNodes):
        for j in range(i + 1, noOfNodes):
            possibleEdges.add((i+1, j + 1))

    return possibleEdges

def _writeToFile(vertexes, edges, representation ,filename):
    '''
        Funkcja pomocnicza do zapisywania elementu w pliku - self explaining
    '''
    if representation == 'adjList':
        writeAdjList(vertexes, edges, filename)
    elif representation == 'adjMatrix':
        writeAdjMatrix(vertexes, edges, filename)
    elif representation == 'incMatrix':
        writeIncMatrix(vertexes, edges, filename)
    elif representation == 'all':
        writeAdjList(vertexes, edges, filename.split('.')[0] + 'adjlist.dat')
        writeAdjMatrix(vertexes, edges, filename.split('.')[0] + 'adjmatrix.dat')
        writeIncMatrix(vertexes, edges, filename.split('.')[0] + 'incmatrix.dat')
    else:
        raise Exception('Representation for graph not supported')



def generateRandomWithEdges(noOfNodes, noOfEdges, representation="adjList", filename="representation.dat"):
    '''
        Funkcja generuje graf o okreslonej liczbie wierzcholkow i krawedzi.
        Tworzy plik o podanej nazwie w ktorym zapisuje graf w danej reprezentacji
    '''
    # Tworzymy tablice liczb reprezentujacych wierzcholki
    vertexes = [i + 1 for i in range(noOfNodes)]
    edges = []
    # Pobieramy wszystkie mozliwe krawedzie
    possibleEdges = getPossibleEdges(noOfNodes)
    maxNumberOfEdges = len(possibleEdges) # n(n-1)/2 wzór da to samo
    i = 0

    # wybieramy losową krawedz, nastepnie usuwamy ja ze zbioru mozliwych krawedzi
    # Robimy to dopóki nie wyczerpiemy zbioru możliwych krawędzi (maxNumberOfEdges) lub podaną przez usera noOfEdges - liczbe krawedzi 
    while i < maxNumberOfEdges and i < noOfEdges:
        random_edge = random.choice(list(possibleEdges))
        possibleEdges.remove(random_edge)
        edges.append(random_edge)
        i += 1
    
    # zapisujemy do pliku
    _writeToFile(vertexes, edges, representation, filename)


   
def generateRandomWithPropabilities(noOfNodes, prop, representation='adjList.dat', filename="probRepresentation.dat"):
    '''
        Funkcja generuje graf o okreslonej liczbie wierzcholkow. Dodanie każdej krawędzi do grafu jest równo prawdopodobne i równe podanej wartości prop
        Tworzy plik o podanej nazwie w ktorym zapisuje graf w danej reprezentacji
    '''
    # Podobnie jak w poprzedniej funkcji
    vertexes = [i + 1 for i in range(noOfNodes)]
    edges = []
    possibleEdges = getPossibleEdges(noOfNodes)
    maxNumberOfEdges = len(possibleEdges) # n(n-1)/2 wzór da to samo
    i = 0

    # przechodzimy wszystkie krawędzie - jeśli losowa wartość z zakresu 0-1 jest mniejsza od prawdopodobieństwa to dodajemy ją do zbioru krawędzi
    for edge in possibleEdges:
        if random.random() < prop:
            edges.append(edge)

    _writeToFile(vertexes, edges, representation, filename)

    

if __name__ == "__main__":
    generateRandomWithEdges(15, 50, representation='all', filename='ned')
    generateRandomWithPropabilities(15, 0.4, representation='all', filename='prob')





