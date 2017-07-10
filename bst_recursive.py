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
