class BSTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self, data=None):
        if not data:
            self.root = None
        else:
            self.root = BSTNode(data)

    def insert(self, data):
        new_node = BSTNode(data)
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            while temp is not None:
                if data <= temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        break
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        break
                    else:
                        temp = temp.right

    def search(self, data):
        if self.root is None:
            return False
        temp = self.root
        if temp.data == data:
            return True
        while temp is not None:
            if data > temp.data:
                if temp.right is None:
                    return False
                elif temp.data == data:
                    return True
                temp = temp.right
            else:
                if temp.left is None:
                    return False
                elif temp.data == data:
                    return True
                temp = temp.left

    def travel(self, cur):
        if cur is None:
            return
        print(cur.data, end = '')
        if cur.left:
            self.travel(cur.left)
        if cur.right:
            self.travel(cur.right)
