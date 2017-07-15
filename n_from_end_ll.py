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

    def n_from_end(self, n):
        temp = self.root
        if temp is None:
            return None
        first = temp
        second = temp
        i = 1;
        while (i < n) and second is not None:
            second = second.nex
            i += 1
        if i < n or i > n:
            return None
        elif (second is None) and (i == n):
            return None
        while second.nex is not None:
            first = first.nex
            second = second.nex
        return first.data


if __name__ == '__main__':
    n = LinkedList(5)
    n.insert(6)
    n.insert(7)
    n.insert(8)
    n.insert(9)
    n.insert(0)

    print(n.n_from_end(0)) # None
    print(n.n_from_end(1)) # 0
    print(n.n_from_end(5)) # 6
    print(n.n_from_end(6)) # 5
    print(n.n_from_end(7)) # None
    print(n.n_from_end(10)) # None
