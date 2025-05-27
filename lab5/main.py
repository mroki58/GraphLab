from Preparing import createNetwork
from FordFulkerson import FordFulkerson
import networkx as nx

def main():
    """
    Przykład tworzenia grafu warstwowego, obliczania maksymalnego przepływu
    i wizualizacji grafu wraz z wynikami.
    """

    # 1. Tworzymy graf warstwowy z 3 warstwami (możesz zmienić liczbę warstw)
    layers = 3
    print(f"Tworzenie grafu warstwowego z {layers} warstwami...")
    net = createNetwork(layers)

    # 2. Pobieramy obiekt grafu NetworkX
    graph = net.getGraph()

    # 3. Obliczamy maksymalny przepływ ze źródła (0) do ujścia (1)
    max_flow = FordFulkerson(graph, s=0, t=1)
    print(f"Maksymalny przepływ w grafie: {max_flow}")

    # 4. Wizualizacja grafu z wagami krawędzi
    print("Wyświetlanie grafu...")
    net.draw()

if __name__ == "__main__":
    main()
