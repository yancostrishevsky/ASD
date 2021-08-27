#Zadanie 7. (Partition Hoare’a) Proszę zaimplementować funkcję partition z algorytmu QuickSort
#według pomysłu Hoare’a (tj. mamy dwa indeksy, i oraz j, wędrujące z obu końców tablicy w stronę środka
#i zamieniamy elementy tablicy pod nimi jeśli mniejszy indeks wskazuje na wartość większą od piwota, a
#większy na mniejszą.

def HoraePartition(T, l, r):
    mid = (l + r) // 2
    pivot = T[mid]
    i = l - 1
    j = r + 1
    while True:
        i += 1
        while (T[i] < pivot):
            i += 1

        j -= 1
        while (T[j] > pivot):
            j -= 1

        if (i >= j):
            return j

        T[i], T[j] = T[j], T[i]