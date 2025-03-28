from ConnectedGraph import ConnectedGraph
from Dijkstra import dijkstra,create_distance_matrix,find_the_centre_of_the_graph,find_minmax
from Kruskal import kruskal

if __name__=="__main__":
    #Zadanie 1
    graph=ConnectedGraph(7)
    graph.draw()

    #Zadanie 2
    ds,ps=dijkstra(graph.G,1)
    for key in ds:
        print(f"d({key}) = {ds[key]}")

    #Zadanie 3
    print("")
    distance_matrix=create_distance_matrix(graph.G)
    for row in distance_matrix:
        print(row)

    #Zadanie 4
    center, min_distance=find_the_centre_of_the_graph(distance_matrix)
    print(f"\ncentrum grafu = {center}  (suma odleglosci: {min_distance})")

    minimax_center, distance = find_minmax(distance_matrix)
    print(f"Centrum minimax = {minimax_center} (odleglosc od najdalszego: {distance})\n")

    #Zadanie 5
    print(f"minimalne drzewo rozpinające {kruskal(graph.matrix_weights)}")