#Zadanie 5. (Lider ciągu) Mamy daną tablicę A z n liczbami. Proszę zaproponować algorytm o złożoności
#O(n), który stwierdza, czy istnieje liczba x (tzw. lider A), która występuje w A na ponad połowie pozycji.
def lider(T):
    cnt = 1
    l = T[0]
    for i in range(1,len(T)):
        if l == T[i]:
            cnt += 1
        else:
            if cnt > 0:
                cnt -= 1
            else:
                l = T[i]
                cnt = 1
    cnt = 0
    for i in range(len(T)):
        if T[i] == l:
            cnt += 1
    if cnt > len(T)//2:
        return l
    return None