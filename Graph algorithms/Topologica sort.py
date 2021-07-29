def topologic(G):
    deq = deque()


    def DFSADJ(G):
        nonlocal deq

        def DFSVisit(G, u):
            nonlocal visited, parent, deq
            visited[u] = True
            # czas odwieddzenia

            for v in G[u]:
                if visited[v] == False:
                    parent[v] = u
                    DFSVisit(G, v)

            deq.append(u)

        n = len(G)

        visited = [False for _ in range(n)]
        parent = [None for _ in range(n)]

        for i in range(n):
            if visited[i] == False:
                DFSVisit(G, i)
    DFSADJ(G)
    return deq