# Hash Tables are used for:
# Constant time lookup and insertion
# Cryptographic applications
# Indexing data

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    # Takes a key and returns an index in the array where the key-value
    # pair should be stored
    def _hash(self, key):
        return hash(key) % self.capacity
    
    # Inserts a key-value pair into the has table
    def insert(self, key, value):
        
        # Find the index for the key using the _hash method
        index = self._hash(key)

        # If there is no linked list at the index, create a new node with
        # the key-value pair and set it as the head of the list. If there
        # a linked list at the index, iterate through the list until the
        # last node is found or the key already exists, and update the
        # value if the key exists.
        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    # Retrieves the value associated with a given key. 
    def search(self, key):

        index = self._hash(key)

        # Gets the index where the key-value pair should be stored
        current = self.table[index]

        # Searches the linked list at that index for the key. If it
        # finds the key, it returns the associated value
        while current:
            if current.key == key:
                return current.value
            current = current.next

    # Remove a key-value pair from the hash table
    def remove(self, key):

        # Gets the index where the key-value pair should be stored
        index = self._hash(key)

        previous = None
        current = self.table[index]

        # Searches the linked list at that index for the key. If the
        # key is found, it removes the node from the list.
        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current
            current = current.next