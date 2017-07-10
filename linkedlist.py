class Node:
    def __init__(self, data=None, _next=None):
        self.data = data
        self._next = _next


class LinkedList:
    def __init__(self, data=None):
        if data is None:
            self.head = None
        else:
            self.head = Node(data)

    def travel(self):
        """Print all element in linked-list link-wise."""
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp._next

    def insert(self, data):
        """Insert elemet at begining of list."""
        temp = Node(data)
        temp._next = self.head
        self.head = temp

    def insertAt(self, data, n):
        """Insert at position index n, starting with zero."""
        temp = self.head
        if n == 0:
            new_node = Node(data)
            new_node._next = temp
            self.head = new_node
            return
        i = 0
        while (i < (n-1)) and (temp is not None):
            i += 1
            temp = temp._next
        if (i == (n-1)) and (temp is not None):
            new_node = Node(data)
            new_node._next = temp._next
            temp._next = new_node
        else:
            print("not a good position.")

    def deleteAt(self, n):
        """Delete element at given index."""
        temp =self.head
        if n == 0:
            self.head = self.head._next
            return
        i = 0
        while (i < (n-1)) and (temp is not None):
            i += 1
            temp = temp._next
        if (i == (n-1)) and (temp is not None):
            if temp._next is None:
                print("wrong position")
            else:
                temp._next = temp._next._next
        else:
            print("wrong position")

    def reverse(self):
        """Reverse the linked list."""
        prev = None
        curr = self.head
        while curr is not None:
            nex = curr._next
            curr._next = prev
            prev = curr
            curr = nex
        self.head = prev

    def recursive_reverse(self, curr):
        """Reverse the list, recursively."""
        if curr._next is None:
            self.head = curr
            return
        self.recursive_reverse(curr._next)
        curr._next._next = curr
        curr._next = None
