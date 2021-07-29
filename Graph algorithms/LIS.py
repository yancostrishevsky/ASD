def LIS(A):
    n = len(A)
    F = [1]*n

    for  i in range(1,n):
        for j in range(i):
            if A[j] < A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
    return max(F)

print(LIS([1,2,3]))