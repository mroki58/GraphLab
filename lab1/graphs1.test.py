import os
import GraphAdMatrix
import GraphAdList
import GraphIncMatrix
from GraphVisual import drawGraph
from GraphRandom import generateRandomWithEdges, generateRandomWithPropabilities

# Tworzenie folderu png jesli nie istnieje
os.makedirs("png", exist_ok=True)

graph1 = GraphAdMatrix.GraphAdMatrix()
graph1.read_matrix_from_file('AdMatrix.dat')

drawGraph(graph1, 'png/AdM.png')

print('Macierz sasiedztwa -> Lista sasiedztwa')
graph2 = graph1.toAdList()
graph2.print()

drawGraph(graph2, 'png/AdM->AdL.png')

print('Macierz sasiedztwa -> Macierz incydencji')
graph3 = graph1.toIncMatrix()
graph3.print()
print('Krawedzie: ')
print(graph3._edges)

drawGraph(graph3, 'png/AdM->IncM.png')


print('***************************')

graph2 = GraphAdList.GraphAdList()
graph2.read_list_from_file('AdList.dat')

drawGraph(graph2, 'png/AdL.png')

print('Lista sasiedztwa -> Macierz sasiedztwa')
graph1 = graph2.toAdMatrix()
graph1.print()

drawGraph(graph1, 'png/AdL->AdM.png')

print('Lista sasiedztwa -> Macierz incydencji')
graph3 = graph2.toIncMatrix()
graph3.print()
print('Krawedzie: ')
print(graph3._edges)

drawGraph(graph3, 'png/AdL->IncM.png')

print('***************************')

graph3 = GraphIncMatrix.GraphIncMatrix()
graph3.read_matrix_from_file('IncMatrix.dat')
graph3.print()

drawGraph(graph3, 'png/IncM.png')

print('Macierz incydencji -> Macierz sasiedztwa')
graph1 = graph3.toAdMatrix()
graph1.print()

drawGraph(graph1, 'png/IncM->AdM.png')

print('Macierz incydencji -> Lista sasiedztwa')
graph2 = graph3.toAdList()
graph2.print()

drawGraph(graph2, 'png/IncM->AdL.png')

#jakis blad
# generateRandomWithEdges(100, 400, 'adjList', 'ned.dat')
generateRandomWithPropabilities(50, 0.05, 'incMatrix', 'prob.dat')

# graph4 = GraphAdList.GraphAdList()
# graph4.read_list_from_file('ned.dat')

# drawGraph(graph4, 'wygenerowany1.png')

graph5 = GraphIncMatrix.GraphIncMatrix()
graph5.read_matrix_from_file('prob.dat')

drawGraph(graph5, 'wygenerowany2.png')