import matplotlib.pyplot as plt
import numpy as np
import random
import copy
from numba import jit,njit
from numba_progress import ProgressBar

MAX_IT = 200_000 
ITERATIONS = 10  

def read_file(filename):
    """
    Czyta plik z zapisanym grafem

    Args:
    -----
    filename : str 
        nazwa pliku

    Returns
    -------
    numpy array 2D
        zwraca listę 2D z wspórzędnymi wierzchołków
    """
    graph=[]
    with open(filename,"r") as file:
        for line in file:
            graph.append([int(x) for x in line.split()])
    graph=np.array(graph)
    return graph

def draw(graph,avgs,stds,bests,length):
    """
    Rysuje graf

    Args:
    -----
    graph : numpy array 2D
        lista 2D z wspórzędnymi wierzchołków
    avgs: numpy array
        przechowuje średnią długości cyklu z każdej iteracji
    stds :  numpy array
        przechowuje odchylenia standardowe z każdej iteracji
    bests : numpy array
        przechowuje najkrótsze długości cyklu każdej iteracji
    length : float
        długość cyklu

    """
    fig, axs = plt.subplots(2, 2, figsize=(12, 7))
    graph = np.vstack([graph, graph[0]])
    axs[0,0].plot(graph[:,0],graph[:,1],'-o',c='purple')
    axs[0,0].text(90,-1,f"{length:.3f}",fontsize = 12,weight='bold')

    axs[0,1].plot(avgs, label='Średnia wartość', linewidth=2,c='orange')
    axs[0,1].set_title("Średnia wartości ")
    axs[0,1].set_xlabel("Iteracja")
    axs[0,1].set_ylabel("Średnia wartość")
    axs[0,1].grid(True)
    axs[0,1].legend()

    axs[1,0].plot(stds, label='Odchylenie standardowe', linewidth=2,c='green')
    axs[1,0].set_title("Odchylenia standarowe ")
    axs[1,0].set_xlabel("Iteracja")
    axs[1,0].set_ylabel("Odchylenie standardowe")
    axs[1,0].grid(True)
    axs[1,0].legend()

    axs[1,1].plot(bests, label='Najkrótsze scieżki w każdej iteracji', linewidth=2,c='r')
    y = min(bests)
    x = np.where(bests == y)[0]
    axs[1,1].scatter(x,y, c= 'black')
    axs[1,1].set_title("Najkrótsze scieżki")
    axs[1,1].set_xlabel("Iteracja")
    axs[1,1].set_ylabel("Najkrótsze scieżki")
    axs[1,1].grid(True)
    axs[1,1].legend()

    plt.tight_layout()
    plt.show()

@njit
def vector_length(v1, v2):
    """
    oblicza długość krawędzi

    Args:
    -----
    v1, v2 : list 
        wierzchołki krawędzi. gdzie v to [x,y]

    Returns:
    --------
    float
        długość odcinka

    """
    return ((v2[0] - v1[0])**2 + (v2[1] - v1[1])**2)**0.5

@njit
def randomize_edges(graph,length):
    """
    Wykonuje operację optymalizacyjną 2-opt

    Args:
    -----
    graph : numpy array 2D
        lista 2D z wspórzędnymi wierzchołków
    length : float 
        długość cyklu

    Returns:
    --------
    new_graph : numpy array 2D
        lista 2D z wspórzędnymi wierzchołków po optymalizacji
    new_length : float 
        długość cyklu po optymalizacji
    """

    new_graph = graph.copy()
    while True:
        b, c = np.sort(np.random.choice(len(graph), size =2  ,replace=False))
        a = b-1 if b != 0 else len(graph) - 1
        d = c+1 if c != len(graph) - 1 else 0
        if a != c and a != d and b != c and b != d:
            break

    new_graph[b:c+1] = new_graph[b:c+1][::-1]
    old_edges = vector_length(graph[a], graph[b]) + vector_length(graph[c], graph[d])
    new_edges = vector_length(new_graph[a], new_graph[b]) + vector_length(new_graph[c], new_graph[d])
    new_length = length - old_edges + new_edges

    return new_graph, new_length


@njit
def calcluate_length(graph):
    """
    Oblicza długość grafu

    Args:
    -----
    graph : numpy array 2D
        lista 2D z wspórzędnymi wierzchołków

    Returns:
    --------
    s : float
        długość grafu
    """
    s=0
    for idx in range(len(graph) - 1):
        s+=vector_length(graph[idx],graph[idx+1])
    s+=vector_length(graph[0],graph[-1])
    return s

@njit
def simulated_annealing(graph,d,lengths,best_graph):
    """
    implementacja  symulowanego wyżarzania

    Args:
    -----
    graph : numpy array 2D
        lista 2D z wspórzędnymi wierzchołków
    d : float 
        długość grafu
    lengths : numpy array
        przechowuje wszystkie znalezione odległość w grafie
    best_graph : numpy array 2D
        graf o najkrótszej długości

    Returns:
    --------
    graph : numpy array 2D
        lista 2D reprezentująca znaleziony cykl Hamiltona o zminimalizowanej długości.
    d : float
        długość grafu
    best_graph : numpy array 2D
        graf o najkrótszej długości
    """
    lengths[0]=d
    T = 100
    for i in range(100,0,-1):
        T = 0.001 * i**2
        for it in range(MAX_IT):
            new_graph, d_new = randomize_edges(graph,d)
            lengths[(100-i)*MAX_IT +it] = d_new
            if  d_new < d:
                graph=new_graph
                d = d_new
                if calcluate_length(best_graph) > d:
                    best_graph=graph.copy()
            else:
                r = np.random.rand()
                if r < np.exp(-(d_new -d)/T):
                    graph = new_graph
                    d = d_new

    return graph,d,best_graph

@njit(nogil=True)
def main_loop(graph,progress,avgs,stds,bests,best_graph):
    """
    główna pętla programu

    Args:
    -----
    graph : numpy array 2D
        lista 2D reprezentująca
    progress 
        obiekt służący do wyświetlania postępu wykonywania pętli.
    avgs : numpy array
        przechowuje średnią długości cyklu z każdej iteracji
    stds :  numpy array
        przechowuje odchylenia standardowe z każdej iteracji
    bests : numpy array
        przechowuje najkrótsze długości cyklu każdej iteracji
    best_graph : numpy array 2D
        graf o najkrótszej długości

    Returns:
    --------
    graph : numpy array 2D
        lista 2D reprezentująca znaleziony cykl Hamiltona o zminimalizowanej długości.
    d : float
        długość grafu
    best_graph : numpy array 2D
        graf o najkrótszej długości
    """
    d=calcluate_length(graph)
    for i in range(ITERATIONS):
        lengths = np.empty(100*MAX_IT)
        graph,d,best_graph=simulated_annealing(graph,d,lengths,best_graph)
        avgs[i] = np.mean(lengths)
        stds[i] = np.std(lengths)
        bests[i] = d
        progress.update(1)

    return graph,d,best_graph

if __name__ == "__main__":
    graph=read_file('data.csv')
    avgs = np.empty(ITERATIONS)
    stds = np.empty(ITERATIONS)
    bests = np.empty(ITERATIONS)
    best_graph = graph.copy()
    with ProgressBar(total=ITERATIONS) as progress:
        graph,d,best_graph = main_loop(graph,progress,avgs,stds,bests,best_graph)
    draw(best_graph,avgs,stds,bests,calcluate_length(best_graph))