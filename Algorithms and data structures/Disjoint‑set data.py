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

a = makeSet(3)
b = makeSet(2)
union(a,b)
print(a.parent.val)
c = makeSet(3)
print(c.parent.val)