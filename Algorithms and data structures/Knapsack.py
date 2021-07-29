def knapsack(W,P,MaxW):
    n = len(W)
    F = [[0]*(MaxW+1)for i in range(n)]


    for w in range(W[0],MaxW+1):
        F[0][w] = P[0]

    for i in range(1,n):
        for w in range(1,MaxW+1):
            F[i][w] = F[i-1][w]
            if w>= W[i]:
                F[i][w] = max(F[i][w], F[i-1][w-W[i]]+P[i])
    return F


def printSol(F,W,P,i,w):
    if i <0:
        return []
    if i == 0:
        if w >= W[0]:
            return [0]
    if w > W[i] and F[i][w] == F[i-1][w-W[1]]+ P[i]:
        return printSol(F,W,P,i-1,w-W[i]) +[i]
    return printSol(F,W,P,i-1,w)


def knapsack2(W,P,MaxW):
    n = len(W)
    suma = 0
    for i in P:
        suma += i
    F = [[0]*(suma+1)for i in range(n)]


    for w in range(P[0],suma+1):
        F[0][w] = W[0]

    for i in range(1,n):
        for w in range(1,suma +1):
            F[i][w] = F[i-1][w]
            if w>= P[i]:
                F[i][w] = max(F[i][w], F[i-1][w-P[i]]+W[i])
    t = []
    for i in range(n):
        t.append( F[i][MaxW])
    return max(t)


def knapsack3(W,P,MaxW):
    n = len(W)
    suma = 0
    for i in P:
        suma += i
    F = [[0] * (suma + 1) for i in range(n)]

    for w in range(P[0], suma + 1):
        F[0][w] = W[0]

    for i in range(1, n):
        for w in range(1, suma + 1):
            F[i][w] = F[i - 1][w]
            if w >= P[i]:
                F[i][w] = max(F[i][w], F[i - 1][w - P[i]] + W[i])
    return F, suma
profit = [10,8,4,5,3,7]
waga = [4,5,12,9,1,13]
#a = knapsack2(waga,profit,24))
a,s = knapsack3(waga,profit,24)
for i in range(6):
    print(a[i])
print(knapsack2(waga,profit,24))