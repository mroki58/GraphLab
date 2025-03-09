'''
    GraphVisual zapewnia funkcje drawGraph
'''


from PIL import Image, ImageDraw, ImageFont
import GraphAdMatrix
import GraphAdList
import GraphIncMatrix
from Geometric import Point, Circle


def drawGraph(graph, nameOfFile):
    ''' Tworzy plik png z grafem reprezentowanym przez punkty i linie na kole 
        Jako argument funkcja przyjmuje graf do rysowania oraz nazwe pliku w ktorym sie on znajduje 
        Wazne jest, ze obiekt graf musi byc klasy dziedziczacej po klasie Graph i zapewnia metody
        calculateCords(circle), gdzie circle to obiekt reprezentujacy okrag klasy Circle z modulu Geometric.Circle
        oraz calculateEdges, ktora jako argument przyjmuje element zwrócony przez klase calculateGraph (calculate Edges jest zaimplementowane w klasie Graph i mozna jedynie zaimplementować w nowej klasie klase getEdges), która ma zwracać punkty,
        calculateEdges oblicza współrzędne końców krawędzi z otrzymanych punktów.

        Obrazek .png jest wymiarów 1200x800. Graf reprezentuje koło o środku w środku obrazka oraz o promieniu 350 pikseli.
    '''
    circle = Circle.Circle(600, 400, 350)  

    cordsOfPoints = graph.calculateCords(circle)
    edges = graph.calculateEdges(cordsOfPoints)

    # Rozmiar obrazu
    width, height = 1200, 800
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)


    # Rysowanie krawędzi
    for point1, point2 in edges:
        draw.line((point1.x, point1.y, point2.x, point2.y), fill="black", width=1)

    # Rysowanie wierzchołków i etykiet
    for point in cordsOfPoints:
        draw.ellipse((point.x-5, point.y-5, point.x+5, point.y+5), fill="red", outline="red")
        draw.text((point.x-15, point.y-15), str(point.label), fill="black")

    # Zapis do pliku
    image.save(nameOfFile)

if __name__ == '__main__':
    graph1 = GraphIncMatrix.GraphIncMatrix()
    graph1.read_matrix_from_file('IncMatrix.dat')

    graph2 = graph1.toAdMatrix()
    drawGraph(graph2, "testgraph.png")

   

