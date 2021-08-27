def countsort(T,n,k):
    C = [0]*n
    B = [0]*n
    for i in range(len(T)):
        C[(T[i]//k)%n] += 1
    print(C)
    for i in range(1,n):
        C[i] += C[i-1]
    for j in range(len(T) -1, -1,-1):
        C[(T[j]//k)%n] -= 1
        B[C[(T[j]//k)%n]] = T[j]
    for i in range(n):
        T[i] = B[i]
    return B