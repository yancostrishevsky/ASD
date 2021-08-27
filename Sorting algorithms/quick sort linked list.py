# |||||||||||||||||||||||||||||          QUICKSORT LISTY JEDNOKIERUNKOWEJ  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# Alogrytm bierze jako pivot pierwszy element z przekazanej listy, mniejsze od niego elementy przepina na poczatek listy,
# natomiast równe pivotowi do osobnej listy z wartownikiem (pivot_copies), którą w razie potrzeby (jeśli pivot się powtórzył)
# łączy z pozostałymi elementami. Partition zwraca wskazanie na poczatek listy, a takze na pierwszy i ostatni element o wartosci pivota
#
# Funkcje quicksort oraz partition przyjmuja dwa argumenty, wskazania na poczatek i koniec zakresu listy odsylaczowej, który ma zostać posortowany
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def partition2(A, end):
    s = A
    pivot = A
    pivot_copies = Node()

    while A.next != end:
        if pivot.value > A.next.value:
            temp = A.next
            A.next = A.next.next
            temp.next = s
            s = temp
        elif pivot.value == A.next.value:
            temp = A.next
            A.next = A.next.next
            temp.next = pivot_copies.next
            pivot_copies.next = temp
        else:
            A = A.next

    pivot_copies = pivot_copies.next
    if pivot_copies != None:
        temp = pivot.next
        pivot.next = pivot_copies
        while pivot_copies.next != None: pivot_copies = pivot_copies.next
        pivot_copies.next = temp
        return (s, pivot, pivot_copies)

    return (s, pivot, pivot)


def quicksortList(A, end):
    if A != end:
        A, p_start, p_end = partition2(A, end)
        A = quicksortList(A, p_start)
        p_end.next = quicksortList(p_end.next, end)

    return A