class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end='--->')
            temp = temp.next
        print("None")
    def append(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = newNode

def mergeLists(l1, l2): #scalanie list
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.val <= l2.val:
        temp = l1
        temp.next =  mergeLists(l1.next, l2)
    else:
        temp = l2
        temp.next = mergeLists(l1, l2.next)
    return temp

def mergesort(head):
    if head is None or head.next is None:
        return head
    l1, l2 = divideLists(head)
    l1 = mergesort(l1)
    l2 = mergesort(l2)
    head = mergeLists(l1,l2)
    return head

def divideLists(head): #dzielenie list na pojedyncze węzły
    middle = head
    middleNext = head
    if middleNext:
        middleNext = middleNext.next
    while middleNext:
        middleNext = middleNext.next
        if middleNext:
            middleNext = middleNext.next
            middle = middle.next

    mid = middle.next
    middle.next = None #zeby rozdzielic
    return head, mid

lista = LinkedList()
lista.append(4)
lista.append(12)
lista.append(1)
lista.append(1)
lista.display()
lista.head = mergesort(lista.head)
lista.display()