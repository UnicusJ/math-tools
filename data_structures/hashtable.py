class Hash:

    def __init__(self, capacity):
        """
        hash table is represented as a python list with a fixed size.
        empty positions are represented by None until they are filled.
        """
        self.table = [None] * capacity
        self.size = 0

    def __len__(self):
        """
        returns the number of non-None elements currently in the hashtable
        """
        count = 0
        for item in self.table:
            if item is not None:
                count += 1
        return count

    def _get_hash_string(self, s):
        """
        given a string, computes the hash of the string, and returns the result.
        computes hash by adding the ordinal numbers of chars, and returns the sum % table size
        """
        sum = 0
        for pos in range(len(s)):
            sum = sum + ord(s[pos])
        return sum % len(self.table)

    def _get_index(self, item):
        """
        uses linear probing to find the index location of an empty position in the table to insert the new element.
        """
        h = self._get_hash_string(item)
        location = h
        step = 1
        while self.table[location] is not None:
            location= (h + step) % len(self.table)
            step += 1
        return location

    def add(self, item):
        """
        given a string input, adds it to the hash table using linear probing for collision handling.
        if the load factor exceeds 0.5, the table size is automatically increased to the lowest prime above 2*table_size
        """
        location = self._get_index(item)
        self.table[location] = item
        self.size += 1
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
        new_size += 1
    return new_size


def is_prime(num):
    for x in range(2,num):
        if numm % x == 0:
            return False
    return True
