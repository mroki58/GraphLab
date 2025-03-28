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
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        
        return self.parent[i]
    
    def union(self,x,y):
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

            
if __name__=="__main__":
    matrix_weights=[]

    with open('matrtix_weights.txt','r') as file:
        for row in file:
            matrix_weights.append([int(weight) for weight in row.strip().split()])

    kruskal(matrix_weights)



    
        


    