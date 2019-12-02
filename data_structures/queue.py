class Queue:
    def __init__(self):
        self.data = []

    def is_empty(self):
        if len(self.data) == 0:
            return True
        return False

    def enqueue(self, item):
        self.data.insert(0,item)

    def dequeue(self):
        return self.data.pop(-1)

    def size(self):
        return len(self.data)

    def peek(self):
        return self.data[-1]