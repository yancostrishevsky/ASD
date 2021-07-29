from collections import deque
class Vertex:
    def __init__(self):
        self.visited = False
        self.d = -1
        self.parent = None


def DFS(G):

    vertex = [0 for _ in range(len(G))]
    for i in range(len(G)):
        vertex[i] = Vertex()

    time = 0


    def DFSVisit(G,u):
        nonlocal time,vertex
        vertex[u].d = time + 1
        time +=1
        vertex[u].visited = True
        print(u)

        for v in G[u]:
            if vertex[v].visited == False:
                vertex[v].parent = u
                DFSVisit(G,v)

        time += 1

    for j in range(len(G)):
        if vertex[j].visited == False:
            DFSVisit(G,j)

    return vertex



g3 = [(0,1),(1,3),(1,2),(2,0),(2,7),(7,9),(9,10),(10,8),(8,7),(8,6),(6,5),(5,3),(3,6),(3,4),(0,4),(10,5),(4,5)]
g4 = [[1,4],[2,3],[0,7],[4,6],[5],[3],[5],[9],[7],[10],[5,8]]
#vt = DFS(g4)

#for i in vt:
 #   print(i.parent, i.d)

def DFSADJ(G,V0):


    def DFSVisit(G,u):
        nonlocal visited, parent, time, times
        visited[u] = True
        #czas odwieddzenia

        for v in G[u]:
            if visited[v] == False:
                parent[v] = u
                DFSVisit(G,v)

        time += 1
        times[u] = time

    n = len(G)
    times = [0]*n
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    time = 0

    for i in range(n):
        if visited[i] == False:
            DFSVisit(G,i)

    return times