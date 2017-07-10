class BSTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BST:
    def __init__(self, data=None):
        if data is None:
            self.root = None
        else:
            self.root = BSTNode(data)

    def insert(self, data, cur):
        if self.root is None:
            self.root = BSTNode(data)
            return
        if cur is None:
            return BSTNode(data)
        if data > cur.data:
            cur.right = self.insert(data, cur.right)
        else:
            cur.left = self.insert(data, cur.left)
        return cur

    def travel(self, cur):
        if cur is None:
            return
        print(cur.data)
        if cur.left:
            self.travel(cur.left)
        if cur.right:
            self.travel(cur.right)
