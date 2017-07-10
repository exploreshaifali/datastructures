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

    def search(self, data, cur):
        if cur is None:
            return False
        if data == cur.data:
            return True
        if data > cur.data:
            return self.search(data, cur.right)
        else:
            return self.search(data, cur.left)

    def min(self, cur):
        if cur is None:
            return
        if cur.left is None:
            return cur.data
        return self.min(cur.left)
