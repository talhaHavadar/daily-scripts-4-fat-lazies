"""
Determine whether a doubly linked list is a palindrome. What if it's singly linked list?

eg.
1 <-> 4 <-> 3 <-> 4 <-> 1 returns True

"""

class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

n1 = Node(1)
n2 = Node(4)
n3 = Node(3)
n4 = Node(4)
n5 = Node(1)
n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2
n3.next = n4
n4.prev = n3
n4.next = n5
n5.prev = n4

f1 = Node(1)
f2 = Node(4)
f1.next = f2
f2.prev = f1

ff1 = Node(1)
ff2 = Node(2)
ff3 = Node(3)
ff4 = Node(4)
ff1.next = ff2
ff2.prev = ff1
ff2.next = ff3
ff3.prev = ff2
ff3.next = ff4
ff4.prev = ff3

def doubly_palindrome(l: Node):
    # find last node and size of the list in the mean time
    last = l
    size = 0
    while last and last.next:
        last = last.next
        size += 1
    else:
        if last:
            size += 1

    if size == 1 or size == 0:
        return True

    # start comparing from first and last elements
    first = l
    while not first is last:
        if first.value != last.value:
            return False
        first = first.next
        last = last.prev

    return True


def singly_palindrome(l: Node):
    # find the middle node
    last = l
    middle = l
    while last and last.next and last.next.next:
        last = last.next.next
        middle = middle.next

    # if there is 2 element in list
    if middle is last and middle.next:
        return middle.value == middle.next.value
    elif middle is last: # 1 element
        return True

    # reverse linking of second half of the list
    prev = middle
    current = middle.next
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    # comparing
    first = l
    last = prev
    while not first is last:
        if first.value != last.value:
            return False
        first = first.next
        last = last.next

    return True

print(doubly_palindrome(n1))
print(singly_palindrome(n1))

print(doubly_palindrome(f1))
print(singly_palindrome(f1))

print(doubly_palindrome(ff1))
print(singly_palindrome(ff1))
