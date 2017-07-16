# Find if the linkedlsit have any loop or not.
# If yes, length of loop.
# Intersection point.

class Node:
    def __init__(self, data, nex=None):
        self.data = data
        self.nex = nex

class LinkedList:
    def __init__(self, data=None):
        if data is None:
            self.root = None
        else:
            self.root = Node(data)

    def insert(self, data):
        new_node = Node(data)
        temp = self.root
        if temp is None:
            self.root = new_node
        while temp.nex is not None:
            temp = temp.nex
        temp.nex = new_node

    def search(self, data):
        temp = self.root
        if temp is None:
            return False
        while temp is not None:
            if temp.data == data:
                return True
            temp = temp.nex
        return False

    def create_loop(self, data):
        """Helper method to create link from last node to the node which
           have data equals to data in parameter.
        """
        temp = self.root
        if temp is None:
            return False
        data_node = None
        end_node = None
        while temp.nex is not None:
            if temp.data == data:
                data_node = temp
            temp = temp.nex
        end_node = temp
        end_node.nex = data_node

    def detect_loop(self):
        temp = self.root
        if temp is None:
            return False
        slow = temp
        fast = temp
        while slow and fast and fast.nex:
            slow = slow.nex
            fast = fast.nex.nex
            if fast == slow:
                return True
        return False



if __name__ == '__main__':
    n = LinkedList(5)
    n.insert(6)
    n.insert(7)
    n.insert(8)
    n.insert(9)
    n.insert(0)
    print(n.detect_loop())
    # even length of loop
    n.create_loop(7)
    print(n.detect_loop())

    # odd length of loop
    a = LinkedList(5)
    a.insert(6)
    a.insert(7)
    a.insert(8)
    a.insert(9)
    a.insert(0)
    print(a.detect_loop())
    a.create_loop(7)
    print(a.detect_loop())
