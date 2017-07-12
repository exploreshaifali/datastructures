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

    def max(self, cur):
        if cur is None:
            return
        if cur.right is None:
            return cur.data
        return self.min(cur.right)

    def get_height(self, cur):
        if cur is None:
            return -1
        return max(self.get_height(cur.left), self.get_height(cur.right)) + 1

    def bfs(self):
        if self.root is None:
            return
        temp = self.root
        # initialize a queue which will help in level order traversal
        q = [temp]
        while q:
            temp = q.pop(0)
            if temp.data:
                print(temp.data, end=', ')
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
