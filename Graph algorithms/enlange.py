from collections import deque
from math import inf

def BFS(v0, adj):
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

    return d


def doubleone(T):
    for k in range(len(T)-1):
        tmp = T[k+1]

        if T[k] == tmp == 1:
            return (k,k+1)



def enlange(G,s,t):
    s_path = BFS(s,G)
    t_path = BFS(t,G)

    tb = [0]*len(G)



    for i in range(len(G)):
        #tb[i] = s_path[i] + t_path[i]
        if s_path[i] + t_path[i] != s_path[t]:
            s_path[i] = inf
            t_path[i] =  inf

    if max(s_path[s:t]) != inf:
        return None

    #print(t_path)
    tb[s] = 0

    for j in range(len(G)):
        if s_path[j] != inf:
            tb[s_path[j]] += 1


    v,u = doubleone(tb)
    v1 = v2 = 0

    for k in range(len(G)):
        if s_path[k] == v:
            v1 = k
        if s_path[k] == u:
            v2 = k

    return v1,v2

"""G = [ [1, 2],
[0, 2],
[0, 1] ]

G1 = [[1,2],[0,3],[0,6],[1,4],[3,5],[4,6],[2,5]
]
G2 = [ [1,4],  # 0
       [0,2],  # 1
       [1,3],  # 2
       [2,5],  # 3
       [0,5],  # 4
       [4,3]]

G4 = [ [1,4,3],  # 0
       [0,2],    # 1
       [1,3],    # 2
       [2,5,0],  # 3
       [0,5],    # 4
       [4,3]]
print(enlange(G4,0,2))"""

G1 = [[1, 2],
      [0, 2],
      [0, 1]]
s1 = 0
t1 = 2
r1 = (0, 2)

G2 = [[1, 4],  # 0
      [0, 2],  # 1
      [1, 3],  # 2
      [2, 5],  # 3
      [0, 5],  # 4
      [4, 3]]  # 5
s2 = 0
t2 = 3
r2 = None

s3 = 0
t3 = 2
r3 = [(0, 1), (1, 2)]

G4 = [[1, 4, 3],  # 0
      [0, 2],  # 1
      [1, 3],  # 2
      [2, 5, 0],  # 3
      [0, 5],  # 4
      [4, 3]]  # 5
s4 = 0
t4 = 2
r4 = None

TESTS = [(G1, s1, t1, r1),
         (G2, s2, t2, r2),
         (G2, s3, t3, r3),
         (G4, s4, t4, r4)
         ]


def runtests(f):
    OK = True
    for (G, s, t, r) in TESTS:
        print("----------------------")
        print("G: ", G)
        print("s: ", s)
        print("t: ", t)
        print("oczekiwany wynik: ", r)
        sol = f(G, s, t)
        print("uzyskany wynik  : ", sol)
        if not ((sol == r) or (sol in r)):
            print("PROBLEM!!!!!!")
            OK = False

    print("----------------------")
    if not OK:
        print("PROBLEMY!")
    else:
        print("OK")

runtests(enlange)