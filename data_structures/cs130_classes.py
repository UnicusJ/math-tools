import math
class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        if len(self.data) == 0:
            return True
        return False

    def push(self,item):
        self.data.append(item)

    def pop(self):
        return self.data.pop(-1)

    def peek(self):
        return self.data[-1]

    def size(self):
        return len(self.data)

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

class Node:
    def __init__(self,init_data):
        self.data = init_data
        self.next = None

    def __str__(self):
        return str(self.data)

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self,new_data):
        self.data = new_data

    def set_next(self,new_next):
        self.next = Node(new_next)

class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        n = Node(item)
        if self.head == None:
            self.head = n
        else:
            n.next = self.head
            self.head = n

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            current = current.next
            count+=1
        return count

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def search(self,item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
                break
            current = current.next
        return False

    def remove(self, item):
        found = False
        current = self.head
        previous = None
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if found:
            if previous == None:
                self.head = self.head.next
            elif previous is not None:
                previous.next = current.next
            current.next = None

    def __iter__(self):
        return LinkedListIterator(self)


class LinkedListIterator:
    def __init__(self,head):
        self.current = head.head

    def __next__(self):
        try:
            value = self.current.data
            self.current = self.current.next
        except:
            raise StopIteration
        return value


class BinaryTree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_left(self, new_data):
        if self.left == None:
            self.left = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data)
            t.left = self.left
            self.left = t

    def set_right(self, new_data):
        if self.right == None:
            self.right = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data)
            t.right = self.right
            self.right = t

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def create_string(self, spaces):
        info = ' ' * spaces + str(self.data)
        if self.left != None:
            info += '\n(l)' + self.left.create_string(spaces+4)
        if not self.right == None:
            info += '\n(r)' + self.right.create_string(spaces+4)
        return info

    def __str__(self):
        representation = self.create_string(0)
        return representation


class Hash:

    def __init__(self, capacity):
        self.table = [None] * capacity
        self.size = 0

    def __len__(self):
        count = 0
        for item in self.table:
            if item != None:
                count += 1
        return count

    def _get_hash_string(self, s):
        sum = 0
        for pos in range(len(s)):
            sum = sum + ord(s[pos])
        return sum % len(self.table)

    def _get_index(self, item):
        h = self._get_hash_string(item)
        location = h
        step = 1
        while self.table[location] != None:
            location= (h + step) % len(self.table)
            step += 1
        return location

    def add(self, item):
        location = self._get_index(item)
        self.table[location] = item
        self.size+=1
        if self.size / len(self.table) > 0.5:
            capacity = find_prime_size(len(self.table))
            new_hash = Hash(capacity)
            for value in self.table:
                if value is not None:
                    new_hash.add(value)
            self.table = new_hash.table

def find_prime_size(current_size):
    new_size = current_size*2
    while not is_prime(new_size):
        new_size+=1
    return new_size


def is_prime(num):
    for x in range(2,num):
        if num%x==0:
            return False
    return True

def num_leaves(tree):
    if tree is None:
        return 0
    elif tree.left == None and tree.right == None:
        return 1
    else:
        return num_leaves(tree.left) + num_leaves(tree.right)

def tree_height(tree):
    if tree is None:
        return 0
    else:
        return 1 + max(tree_height(tree.left),tree_height(tree.right))

def max_in_tree(tree):
    if tree is None:
        return -1
    else:
        return max(tree.data,max_in_tree(tree.left),max_in_tree(tree.right))

def expensive_path(tree):
    if tree is None:
        return 0
    else:
        return max(tree.data+expensive_path(tree.right),tree.data+expensive_path(tree.left))

def is_balanced(tree):
    if abs(tree_height(tree.left) - tree_height(tree.right))<=1:
        return True
    return False

def insert_middle(list,value):
    list_size = list.size()
    insert_pos = list_size//2
    current = list.head
    for x in range(insert_pos-1):
        current = current.next
    temp = current.next
    current.next = Node(value)
    current.next.next = temp

def sort_list(list):
    value_list = []
    current = list.head
    while current is not None:
        value_list.append(current.data)
        current = current.next
    value_list.sort()
    l.head = Node(value_list[0])
    current = l.head
    for value in value_list[1:]:
        current.next = Node(value)
        current = current.next


l = LinkedList()
l.add('c')
l.add('f')
l.add('a')
l.add('d')



for node in l:
    print(node)
