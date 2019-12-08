class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return "Node with data: '{}'".format(self.data)

    def set_next(self, next_val):
        self.next = Node(next_val)

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def get_data(self):
        return self.data

