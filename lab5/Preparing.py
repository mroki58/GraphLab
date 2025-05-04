"""
Moduł zawiera funkcję `createNetwork`, która umożliwia tworzenie grafów warstwowych
z losowymi krawędziami i wagami, oraz ich wizualizację.
"""

from Network import Network

def createNetwork(layers):
    """
    Tworzy graf warstwowy z podaną liczbą warstw, losowymi krawędziami i wagami.

    Parameters
    ----------
    layers : int
        Liczba warstw w grafie.

    Returns
    -------
    Network
        Obiekt klasy Network reprezentujący graf warstwowy.
    """
    net = Network()  # Tworzenie obiektu grafu
    net.createLayers(layers)  # Tworzenie warstw wraz z krawędziami pomiędzy nimi
    net.addRandomEdges()  # Dodanie losowych krawędzi
    net.addWeights()  # Dodanie losowych wag do krawędzi
    # net.draw()  
    return net


if __name__ == "__main__":
    """
    Przykład użycia modułu Preparing.

    Tworzy graf warstwowy z 2 warstwami, dodaje losowe krawędzie i wagi,
    a następnie wizualizuje graf.
    """
    net = createNetwork(2)  # Tworzenie grafu z 2 warstwami pomiędzy źródłem i ujściem
    net.draw()  # Wizualizacja grafu