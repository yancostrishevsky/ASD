from math import inf
from zad1testy import runtests




def dijkstra(G, A, B):
    n = len(G)

    d = [inf] * n
    d[A] = 0
    parent = [inf] * n
    parent[A] = 0
    visited = [False] * n

    for _ in range(n):
        u = min(range(n), key=lambda u: inf if visited[u] else d[u])
        visited[u] = True

        for v in range(n):
            if G[u][v] > 0:
                if d[u] + G[u][v] < d[v] and parent[u] !=G[u][v] :
                    d[v] = d[u] + G[u][v]
                    parent[v] = G[u][v]

    return d[B]

G1 = [[0, 5, 1, 8, 0, 0, 0],
          [5, 0, 0, 1, 0, 8, 0],
          [1, 0, 0, 8, 0, 0, 8],
          [8, 1, 8, 0, 5, 0, 1],
          [0, 0, 0, 5, 0, 1, 0],
          [0, 8, 0, 0, 1, 0, 5],
          [0, 0, 8, 1, 0, 5, 0]]

def islands(G, A, B):
    return dijkstra(G,A,B)


runtests(islands)