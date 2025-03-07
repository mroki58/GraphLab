import random

def writeAdjList(vertexes, edges, filename):
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
    with open(filename, 'w') as pl: 
        matrix = [[0 for _ in range(len(vertexes))] for _ in range(len(vertexes))]

        for edge in edges:
            v1 = edge[0] - 1
            v2 = edge[1] - 1
            matrix[v1][v2] = 1
            matrix[v2][v1] = 1  # Jeśli graf jest nieskierowany

        # Zapisujemy macierz sąsiedztwa do pliku
        for row in matrix:
            line = ' '.join(str(cell) for cell in row) + '\n'
            pl.write(line)

            
def writeIncMatrix(vertexes, edges, filename):
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
    possibleEdges = set()

    for i in range(noOfNodes):
        for j in range(i + 1, noOfNodes):
            possibleEdges.add((i+1, j + 1))

    return possibleEdges

def _writeToFile(vertexes, edges, representation ,filename):
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
    vertexes = [i + 1 for i in range(noOfNodes)]
    edges = []
    possibleEdges = getPossibleEdges(noOfNodes)
    maxNumberOfEdges = len(possibleEdges) # n(n-1)/2 the same
    i = 0

    while i < maxNumberOfEdges and i < noOfEdges:
        random_edge = random.choice(list(possibleEdges))
        possibleEdges.remove(random_edge)
        edges.append(random_edge)
        i += 1
    
    _writeToFile(vertexes, edges, representation, filename)


   
def generateRandomWithPropabilities(noOfNodes, prop, representation='adjList.dat', filename="probRepresentation.dat"):
    vertexes = [i + 1 for i in range(noOfNodes)]
    edges = []
    possibleEdges = getPossibleEdges(noOfNodes)
    maxNumberOfEdges = len(possibleEdges) # n(n-1)/2 the same
    i = 0

    for edge in possibleEdges:
        if random.random() < prop:
            edges.append(edge)

    _writeToFile(vertexes, edges, representation, filename)

    

if __name__ == "__main__":
    generateRandomWithEdges(15, 50, representation='all', filename='ned')
    generateRandomWithPropabilities(15, 0.4, representation='all', filename='prob')





