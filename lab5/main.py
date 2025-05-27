from Preparing import createNetwork
from FordFulkerson import FordFulkerson
import networkx as nx

def main():
    """
    Przykład tworzenia grafu warstwowego, obliczania maksymalnego przepływu
    i wizualizacji grafu wraz z wynikami.
    """

    # Tworzymy graf warstwowy z 3 warstwami
    layers = 3
    print(f"Tworzenie grafu warstwowego z {layers} warstwami...")
    net = createNetwork(layers)

    graph = net.getGraph()

    max_flow = FordFulkerson(graph, s=0, t=1)
    print(f"Maksymalny przepływ w grafie: {max_flow}")

    # Wizualizacja grafu z wagami krawędzi
    print("Wyświetlanie grafu...")
    net.draw()

if __name__ == "__main__":
    main()
