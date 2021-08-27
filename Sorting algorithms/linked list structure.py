#1. Zdefiniować klasę w Pythonie realizującą listę jednokierunkową.
class Node:
   def __init__(self):
    self.value = None
    self.next = None

def display(head):
    if head is not None:
        print(head.value, end=' ')
        display(head.next)

#2. Zaimplementować wstawianie do posortowanej listy.
def insertNode(head, element):
    while head.next is not None and head.next.value < element.value:
        head = head.next
    element.next = head.next
    head.next = element

#3. Zaimplementować usuwanie maksimum z listy.
def delMax(List):
    p = List.next
    p_prev = prev = List
    List = List.next
    while prev.next is not None:
        if prev.next.value > p.value:
            p_prev = prev
            p = prev.next
        prev = prev.next
    p_prev.next = p.next
    return List

#Proszę zaimplementować funkcję odwracającą listę jednokierunkową

def reverse(List):
    if List is None:
        return
    prev = None
    nxt = List.next
    while List:
        List.next = prev
        prev = List
        List = nxt
        if nxt != None:
            nxt = nxt.next
    return prev


"""wartownik = Node()
node1 = Node()
node1.value = 2
node2 = Node()
node2.value = 5
wartownik.next = node1
insertNode(wartownik,node2)
display(wartownik)
delMax(wartownik)
display(wartownik)"""