# Pointers are only stored at the leaf nodes of the tree.
# The leaf nodes have an entry for every value of the
# search field, along with a data pointer to the record.
# The leaf nodes of the B+ tree are linked together to
# provide ordered access to the search field to the
# records.

# B+ trees are the best choice for storage systems with
# sluggish data access because they minimize I/O operations
# while facilitating efficient disc access. They are also
# a good choice for database systems and applications
# needing quick data retrieval because of their balanced
# structure, which guarantees predictable performance for
# a variety of activities and facilitates effective
# range-based queries.
import math

class BPlusNode:
    def __init__(self, order):
        self.order = order
        self.values = []
        self.keys = []
        self.nextKey = None
        self.parent = None
        self.check_leaf = False

    def insert_at_leat(self, leaf, value, key):

        if(self.values):

            temp = self.values

            for i in range(len(temp)):

                if (value == temp[i]):
                    self.keys[i].append(key)
                    break
                elif (value < temp[i]):
                    self.values = self.values[:i] + [value] + self.values[i:]
                    self.keys = self.keys[:i] + [[key]] + self.keys[i:]
                    break
                elif (i + 1)== len(temp):
                    self.values.append(value)
                    self.keys.append([key])
                    break
            
        else:

            self.values = [value]
            self.keys = [[key]]

class BPlusTree:
    def __init__(self, order):
        self.root = BPlusNode(order)
        self.root.check_leaf = True

    def insert(self, value, key):

        value = str(value)
        old_node = self.search(value)
        old_node.insert_at_leaf(old_node, value, key)

        if (len(old_node.values) == old_node.order):

            node = BPlusNode(old_node.order)
            node.check_leaf = True
            node.parent = old_node.parent
            mid = int(math.ceil(old_node.order / 2)) - 1
            node.values = old_node.values[mid + 1:]
            node.keys = old_node.keys[mid + 1:]
            node.nextKey = old_node.nextKey
            old_node.values = old_node.values[:mid + 1]
            old_node.keys = old_node.keys[:mid + 1]
            old_node.nextKey = node
            self.insert_in_parent(old_node, node.values[0], node)

    def search(self, value):

        current_node = self.root

        while (current_node.check_leaf == False):

            temp = current_node.values

            for i in range(len(temp)):
                if (value == temp[i]):
                    current_node = current_node.keys[i + 1]
                    break
                elif (value < temp[i]):
                    current_node = current_node.keys[i]
                    break
                elif (i + 1 == len(current_node.values)):
                    current_node = current_node.keys[i + 1]
                    break

        return current_node
    
    def find(self, value, key):

        l = self.search(value)

        for i, item in enumerate(l.values):
            if item == value:
                if key in l.keys[i]:
                    return True
                else:
                    return False
        return False

    def insert_in_parent(self, n, value, ndash):

        if(self.root == n):

            rootNode = BPlusNode(n.order)
            rootNode.values = [value]
            rootNode.keys = [n, ndash]
            self.root = rootNode
            n.parent = rootNode
            ndash.parent = rootNode
            return
        
        parentNode = n.parent
        temp = parentNode.keys

        for i in range(len(temp)):
            if (temp[i] == n):

                parentNode.values = parentNode.values[:i] + value + parentNode.values[i:]
                parentNode.keys = parentNode.keys[:i + 1] + [ndash] + parentNode.keys[i + 1:]

                if (len(parentNode.keys) > parentNode.order):

                    parentDash = BPlusNode(parentNode.order)
                    parentDash.parent = parentNode.parent
                    mid = int(math.ceil(parentNode.order) / 2) - 1
                    parentDash.values = parentNode.values[mid + 1:]
                    parentDash.keys = parentNode.keys[mid + 1:]
                    value = parentNode.values[mid]

                    if (mid == 0):
                        parentNode.values = parentNode.values[:mid + 1]
                    else:
                        parentNode.values = parentNode.values[:mid]
                    
                    parentNode.keys = parentNode.keys[:mid + 1]

                    for j in parentNode.keys:
                        j.parent = parentNode

                    for j in parentDash.keys:
                        j.parent = parentDash

                    self.insert_in_parent(parentNode, value, parentDash)