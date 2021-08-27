class Heap:
    def __init__(self):
        self.size = 0
        self.dane = [None]*self.size




def insert(H, data):
    H.dane[H.size] = data
    H.size += 1

    heapify(H,0, H.size)

def left(i):
    return 2*i +1
def right(i):
    return 2*i +2
def parent(i):
    return (i-1)//2
#Naprawianie kopca
def heapify(T,n,i):
    l = left(i)
    r = right(i)
    m = i
    if l < n and T[l] > T[m]: m = l
    if r < n and T[r] > T[m]: m = r
    if m != i:
        T[i], T[m] = T[m], T[i]

        heapify(T,n,m)
#budowanie kopca z tablicy
def buildheap(H):
    n = len(H)
    for i in range(parent(n-1),-1,-1):
        heapify(H,n,i)
#Proszę zaimplementować funkcję wstawiającą dowolny element do kopca binarnego
#(tablica reprezentująca kopiec nie jest cała zapełniona()czyli nie musimy zwiekszac roziaru tablicy tylko wstawiamy w kolejne wolnej miesjce)
def append(t,data,n):
    t[n] = data
    i = n
    while i > 0 and t[i] > t[parent(i)]:
        t[i], t[parent(i)] = t[parent(i)], t[i]
        i = parent(i)

#heapsort

def heapsort(T):
    n = len(T)
    buildheap(T)
    for i in range(n-1,0,-1):
        swap(T,0,i)
        heapify(T,i,0)
    return T