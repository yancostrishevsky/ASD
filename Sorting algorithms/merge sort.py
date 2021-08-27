def mergesortv2(T):

    arrLen = len(T)


    def ms(T, left, right):#do funkcji przekazuje tablice i zakres
        if left < right:#wykonuje sie tak dlugo dopoki mamy wiecej niz 1 element
            mid = (left + right) // 2 #wyznaczamy srodek czyli miejsce podzialu
            ms(T, left, mid)#rekurencyjnie wywolujemy funkcje od poczatku do granicy i od granicy do konca
            ms(T, mid + 1, right)#od mid + 1 zeby dwa razy nie uwzglednic indexu srodka
            mergev2(T, left, mid, right)#scalanie


    def mergev2(t, left, mid, right):
        array = [None] * len(t)#tworzymy pomocniczą tablice
        for i in range(len(t)):
            array[i] = t[i]

        temp1 = left#wskazania na początki podtablic
        temp2 = mid + 1
        curr = left#zeby kontrolowac na jaki index wpisujemy najmniejszy element

        while temp1 <= mid and temp2 <= right:
            if array[temp1] <= array[temp2]:
                t[curr] = array[temp1]
                temp1 += 1
            else:
                t[curr] = array[temp2]
                temp2 += 1
            curr += 1
#w sytuacji gdy wyczerpalismy wszystkie elementy z drugiej podtablicy, nie trzeba robic w druga strone bo elementy sa juz wpisane w wynikowej jesli braknie ich w pierwszej
        while temp1 <= mid:
            t[curr] = array[temp1]
            curr += 1
            temp1 += 1

    ms(T, 0, arrLen - 1)
    return T