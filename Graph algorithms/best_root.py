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
def DFSADJ(G,V0):


    def DFSVisit(G,u):
        nonlocal visited, parent, time, times
        visited[u] = True
        time += 1 #czas odwieddzenia
        times[u] = time
        for v in G[u]:
            if visited[v] == False:
                parent[v] = u
                DFSVisit(G,v)

        #time += 1
        #times[u] = time

    n = len(G)
    times = [0]*n
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    time = 0

    for i in range(n):
        if visited[i] == False:
            DFSVisit(G,i)

    return times

def best_root(L):
    tmp = len(L) +  3
    bestroot = 0
    for i in range(len(L)):
        dist, _ = BFSADJ(i,L)
        if max(dist) < tmp:
            bestroot = i
            tmp = max(dist)
    return bestroot
L = [ [ 2 ], [ 2 ], [ 0, 1, 3, 4, 5, 6 ],
       [ 2 ], [ 2 ], [ 2 ], [ 2 ] ]

print(best_root(L))