#Quicksort iteracyjny(za pomocą włąsnego stosu)
def partition(T, p, r):
    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def itQs(T):
    S = []
    p = 0
    r = len(T) -1
    S.append((p,r))
    while len(S) > 0:
        (p,r) = S.pop()
        if p < r:
            q = partition(T,p,r)
            if q - p > r - q:
                S.append((p,q-1))
                S.append((q+1,r))
            else:
                S.append((q + 1, r))
                S.append((p, q - 1))