from node import *


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_end(self, item):
        """adds a new node at the end of the linked list"""
        n = Node(item)
        if self.head is None:
            self.head = n
        else:
            current_node = self.head
            prev = None
            while current_node is not None:
                prev = current_node
                current_node = current_node.get_next()
            prev.next = n

    def add_to_front(self, item):
        """adds a new node at the front of the linked list"""
        n = Node(item)
        if self.head is None:
            self.head = n
        else:
            n.next = self.head
            self.head = n

    def contains_loop(self):
        """returns True or False based on whether the linked list contains a loop structure"""
        node_list = []
        if self.head is None:
            return False
        else:
            current = self.head
            while current is not None:
                if current in node_list:
                    return True
                node_list.append(current)
                current = current.get_next()
            return False

    def get_node_list(self):
        """returns a list of node names in the order they appear in the list"""
        if self.contains_loop():
            return 'List contains a loop!'

        node_list = []
        if self.head is None:
            return []
        else:
            current = self.head
            while current is not None:
                print(current)
                node_list.append(current.data)
                current = current.get_next()
            return node_list

    def get_size(self):
        """returns the size (number of nodes) in the list
        returns -1 if the list contains a loop"""
        if self.contains_loop():
            return -1

        size = 0
        if self.head is None:
            return 0
        else:
            current = self.head
            while current is not None:
                size += 1
                current = current.get_next()
            return size

    def search(self, item):
        """returns true or false based on whether a node with data=item is in the linked list"""
        if self.head is None:
            return False
        else:
            current = self.head
            while current is not None:
                if current.data == item:
                    return True
                else:
                    current = current.get_next()
            return False





