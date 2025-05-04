"""
Moduł zawiera klasę Point, która reprezentuje punkt w przestrzeni 2D.
"""

class Point:
    """
    Klasa Point reprezentuje punkt w przestrzeni 2D z etykietą.

    Attributes
    ----------
    x : float
        Współrzędna X punktu.
    y : float
        Współrzędna Y punktu.
    label : str
        Etykieta punktu.
    """

    def __init__(self, x, y, label):
        """
        Inicjalizuje obiekt klasy Point.

        Parameters
        ----------
        x : float
            Współrzędna X punktu.
        y : float
            Współrzędna Y punktu.
        label : str
            Etykieta punktu.
        """
        self.x = x
        self.y = y
        self.label = label



