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
