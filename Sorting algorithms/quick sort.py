#Zadanie 1. Proszę zaimplementować algorytm QuickSort do sortowania n elementowej tablicy tak, żeby
#zawsze używał najwyżej O(log n) dodatkowej pamięci na stosie, niezależnie od jakości podziałów w funkcji
#partition.

def quicksort(T, p, r):
    while p < r:
        q = partition(T, p, r)
        if p - q < r - q:
            quicksort(T, p, q - 1)
            p = q + 1
        else:
            quicksort(T, q + 1, r)
            r = q + 1
    return T


def partition(T, p, r):
    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1