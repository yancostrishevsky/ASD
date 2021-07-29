from collections import deque
def BFSADJ(v0, adj):
    n = len(adj)
    q = deque()
    d = [-1] * n
    visit = [False]*n
    q.append(v0)
    d[v0] = 0
    visit[v0] = True
    parents = [None] * n

    while len(q) > 0:
        u = q.popleft()

        for v in adj[u]:
            if visit[v] == False:
                visit[v]= True
                d[v]= d[u]+1
                parents[v] = u
                q.append(v)

    return d, parents

g = [
    [1,2],[0,4],[0,3,5],[2,4],[1,3,5],[2,4,6],[5,7],[6]
]
g2=[[0,1,1,0,0,0,0,0],
    [1,0,0,0,1,0,0,0],
    [1,0,0,1,0,1,0,0],
    [0,0,1,0,1,0,0,0],
    [0,1,0,1,0,1,0,0],
    [0,0,1,0,1,0,1,0],
    [0,0,0,0,0,1,0,1],
    [0,0,0,0,0,0,1,0]

]
#a,b = BFSADJ(0,g)
#print(a,b)
def BFSMATRIX(v0, adj):
    n = len(adj)
    q = deque()
    d = [-1] * n
    visit = [False]*n
    q.append(v0)
    d[v0] = 0
    visit[v0] = True
    parents = [None] * n

    while len(q) > 0:
        u = q.popleft()

        for i in range(len(adj[u])):
            if adj[u][i] == 1:
                if visit[i] == False:
                    visit[i]= True
                    d[i]= d[u]+1
                    parents[i] = u
                    q.append(i)

    return d, parents
#x,t= BFSMATRIX(0,g2)

#print(t)
class Vertex:
    def __init__(self):
        self.visited = False
        self.d = -1
        self.parent = None


def BFS(G,V0):
    vertex = [0for _ in range(len(G))]
    for i in range(len(G)):
        vertex[i] = Vertex()

    q = deque()
    vertex[V0].d = 0
    vertex[V0].visited = True
    q.append(V0)

    while len(q) > 0:
        u = q.popleft()
        for v in G[u]:
            if vertex[v].visited == False:
                vertex[v].visited = True
                vertex[v].d = vertex[u].d + 1
                vertex[v].parent = u
                q.append(v)

    return vertex