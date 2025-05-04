"""
Moduł zawiera klasę Circle, która reprezentuje okrąg w przestrzeni 2D.
"""

class Circle:
    """
    Klasa Circle reprezentuje okrąg w przestrzeni 2D.

    Attributes
    ----------
    x : float
        Współrzędna X środka okręgu.
    y : float
        Współrzędna Y środka okręgu.
    r : float
        Promień okręgu.
    """

    def __init__(self, x, y, r):
        """
        Inicjalizuje obiekt klasy Circle.

        Parameters
        ----------
        x : float
            Współrzędna X środka okręgu.
        y : float
            Współrzędna Y środka okręgu.
        r : float
            Promień okręgu.
        """
        self.x = x
        self.y = y
        self.r = r

