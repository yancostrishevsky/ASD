G = [(0,1,1),(1,2,7),(2,3,2),(3,4,5),(4,5,6),(5,0,12),(2,0,8),(2,5,3),(0,4,4)]
class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = self


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent


def union(x,y):
    x = find(x)
    y = find(y)
    if x == y: return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank: y.rank += 1


def makeSet(x):
    return Node(x)


def Kruskal(G):
    A = []
    graph = sorted(G, key=lambda item: item[2])
    print(graph)
    dsds = []
    for i in range(len(G)):
        dsds.append(makeSet(i))

    S = 0
    counter = 0

    for vertex in graph:
        u,v,w = vertex
        counter += 1
        x = find(dsds[u])
        y = find(dsds[v])
        if x != y:
            S += 1
            A.append([u,v,w])
            union(x,y)

    return A


a = Kruskal(G)
print(a)



