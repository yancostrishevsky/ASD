from math import inf
from queue import PriorityQueue
G = [[(1, 1)],
         [(0, 1), (3, 0), (5, 1)],
         [(3, 1)],
         [(1, 0), (2, 1), (4, 0), (5, 1)],
         [(3, 0), (5, 0), (6, 1)],
         [(1, 1), (3, 1), (4, 0), (6, 0), (7, 1)],
         [(5, 0), (4, 1), (7, 1), (8, 0)],
         [(5, 1), (6, 1), (8, 0)],
         [(6, 0), (7, 0)]]

G1 = [[(1,5),(2,1),(3,8)],
       [(0,5),(3,1),(5,8)],
      [(0,1),(3,8),(6,8)],
      [(0,8),(1,1),(2,8),(4,5),(6,1)],
      [(3,5),(5,1)],
      [(1,8),(4,1),(6,5)],
      [(2,8),(3,1),(5,5)]

]

def Dijkstra(G,s):
    n = len(G)
    d = [inf]*n
    d[s] = 0
    Q = PriorityQueue()

    for i in range(n):
        Q.put((d[i], i))

    while not Q.empty():
        dist,u = Q.get()

        for v,w in G[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                Q.put((d[v], v))

    return d

distance = Dijkstra(G1,5)
print(distance)
