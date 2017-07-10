class Node:
    def __init__(self, data=None, nex=None):
        self.data = data
        self.nex = nex


class Queue:
    def __init__(self, data=None):
        if data is None:
            # inserting from tail and removing from head
            self.head = None
            self.tail =None
        else:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node

    def travel(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.nex

    def enqueue(self, data):
        new_node = Node(data)
        if (self.tail is None) and (self.head is None):
            # when queue/linked-list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.nex = new_node
            self.tail = new_node

    def dequeue(self):
        if (self.tail is None) and (self.head is None):
            # when queue/linked-list is empty
            return
        ret = self.head.data
        if self.head == self.tail:
            self.tail = None
        self.head = self.head.nex
        return ret
