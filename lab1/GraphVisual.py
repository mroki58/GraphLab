"""
Moduł GraphVisual zapewnia funkcję `drawGraph`, która umożliwia wizualizację grafu w formie obrazka PNG.
"""

from PIL import Image, ImageDraw
import GraphAdMatrix
import GraphAdList
import GraphIncMatrix
from Geometric import Point, Circle


def drawGraph(graph, nameOfFile):
    """
    Tworzy plik PNG z wizualizacją grafu reprezentowanego przez punkty i linie na kole.

    Graf jest rysowany na obrazie o wymiarach 1200x800 pikseli. Wierzchołki są rozmieszczone równomiernie
    na okręgu o środku w środku obrazka i promieniu 350 pikseli.

    Parameters
    ----------
    graph : Graph
        Obiekt grafu dziedziczący po klasie Graph. Musi implementować metody:
        - `calculateCords(circle)`: Oblicza współrzędne wierzchołków na podstawie okręgu.
        - `calculateEdges(points)`: Oblicza współrzędne końców krawędzi na podstawie punktów.
    nameOfFile : str
        Nazwa pliku, w którym zostanie zapisany obrazek grafu.

    Notes
    -----
    - Metoda `calculateCords` przyjmuje obiekt klasy `Circle` z modułu `Geometric.Circle`.
    - Metoda `calculateEdges` przyjmuje listę punktów zwróconą przez `calculateCords`.
    - Obrazek jest zapisywany w formacie PNG.
    """
    circle = Circle.Circle(600, 400, 350)  # Okrąg, na którym rozmieszczone są wierzchołki

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
        draw.ellipse((point.x - 5, point.y - 5, point.x + 5, point.y + 5), fill="red", outline="red")
        draw.text((point.x - 15, point.y - 15), str(point.label), fill="black")

    # Zapis do pliku
    image.save(nameOfFile)


if __name__ == '__main__':
    """
    Przykład użycia modułu GraphVisual.

    - Wczytuje graf w formacie macierzy incydencji z pliku `IncMatrix.dat`.
    - Konwertuje graf na reprezentację macierzy sąsiedztwa.
    - Rysuje graf i zapisuje go do pliku `testgraph.png`.
    """
    graph1 = GraphIncMatrix.GraphIncMatrix()
    graph1.read_matrix_from_file('IncMatrix.dat')

    graph2 = graph1.toAdMatrix()
    drawGraph(graph2, "testgraph.png")



