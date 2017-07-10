class Queue:
    def __init__(self, size):
        self.size = size
        # inserting from tail and removing from front.
        self.front = -1
        self.tail = -1
        self.q = [0 for i in range(size)]

    def is_empty(self):
        if self.front == self.tail == -1:
            return True
        return False

    def is_full(self):
        if (self.tail+1)%self.size == self.front:
            return True
        return False

    def enqueue(self, data):
        if self.is_full():
            return
        if self.is_empty():
            self.tail = 0
            self.front = 0
        else:
            # circular array looping
            self.tail = (self.tail + 1)%self.size
        self.q[self.tail] = data

    def dequeue(self):
        if self.is_empty():
            return
        ret = self.q[self.front]
        if self.front == self.tail:
            self.front = -1
            self.tail = -1
        else:
            self.front = (self.front + 1)%self.size
        return ret

    def travel(self):
        """Print elements in queue from front to tail."""
        i = self.front
        while i != self.tail:
            print(self.q[i])
            i = (i+1)%self.size
        if self.front != -1:
            print(self.q[i])
