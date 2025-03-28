class DSU:
    """
    Struktura danych Disjoint Set Union.
    Używana do efektywnego zarządzania zbiorami rozłącznymi i znajdowania ich reprezentantów.
    """
    def __init__(self,n):
        """
        Inicjalizacja struktury DSU.
        
        Args:
            n (int): Liczba elementów (wierzchołków grafu)
        """
        self.parent = list(range(n))
        self.rank= [1] * n

    def find(self,i):
        """
        Znajduje reprezentanta zbioru, do którego należy element i.

        Args:
            i (int): Indeks elementu

        Returns:
            int: Reprezentant zbioru zawierającego i
        """
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        
        return self.parent[i]
    
    def union(self,x,y):
        """
        Łączy zbiory zawierające elementy x i y.
        
        Args:
            x (int): Pierwszy element
            y (int): Drugi element
            
        Returns:
            bool: True jeśli zbiory zostały połączone, False jeśli już były w tym samym zbiorze
        """
        s1 =self.find(x)
        s2 =self.find(y)

        if s1 != s2:
            if self.rank[s1] < self.rank[s2]:
                self.parent[s1]=s2
            elif self.rank[s1] > self.rank[s2]:
                self.parent[s2] = s1
            else:
                self.parent[s2] = s1
                self.rank[s1] +=1
            return True
        return False


def kruskal(matrix_weights):
    """
    Algorytm Kruskala znajdowania minimalnego drzewa rozpinającego (MST) w grafie.

    Args:
        matrix_weights (list): Macierz wag. Wartość 0 oznacza brak krawędzi.

    Returns:
        list: Lista krawędzi MST w formacie (u, v, w), gdzie:
              - u, v to numery wierzchołków
              - w to waga krawędzi
    
    Note:
        Wagi krawędzi muszą być nieujemne
    """

    edges=[]
    n =len(matrix_weights)
    for row in range(n):
        for column in range(row+1,n):
            if matrix_weights[row][column] != 0:
                edges.append((matrix_weights[row][column], row, column))

    edges.sort()
    dsu = DSU(n)
    minimum_spannig_tree = []

    for weight,u,v in edges:
        if dsu.union(u,v):
            minimum_spannig_tree.append((u+1,v+1,weight))
        if len(minimum_spannig_tree) == n-1:
            break

    return minimum_spannig_tree

            



    
        


    