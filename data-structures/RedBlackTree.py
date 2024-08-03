# A type of balanced binary search tree that uses a
# set of rules to maintain balance, ensuring logaritmic
# time complexity for operations regardless of the
# initial shape of the tree. They are self-balancing,
# using a simple color-coding scheme to adjust the tree
# after each modification.

# Properties: the root of the tree is always black, red
# nodes cannot have red children, every path from a node
# to its descendant leaves have the same number of black
# nodes, and all leaves are black.

# Most BST operations take O(n) time where n is the height
# of the BST. A red-black tree ensures that the height of
# the tree is given by logn after every insertion and
# deletion. Additonally, they are simple to implement and
# widely used. However, they have more complex insertion
# and deletion rules, require a constant overhead, and
# are not optimal for all use cases.

class RedBlackNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.parent = None
        self.red = False

class RedBlackTree:
    def __init__(self):
        self.nil = RedBlackNode(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, key):
        
        node = RedBlackNode(key)
        node.parent = None
        node.left = self.root
        node.right = self.root
        node.red = True
        parent = None
        current = self.root

        while current != self.nil:

            parent = current

            if node.key < current.key:
                current = current.left
            elif node.key > current.key:
                current = current.right
            else:
                return
            
        node.parent = parent

        if parent == None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

        self.fix_insert(node)

    def fix_insert(self, node):

        while node != self.root and node.parent.red:
            if node.parent == node.parent.parent.right:

                uncle = node.parent.parent.left

                if uncle.red:

                    uncle.red = False
                    node.parent.red = False
                    node.parent.parent.red = True
                    node = node.parent.parent

                else:

                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)

                    node.parent.red = False
                    node.parent.parent.red = True
                    self.rotate_left(node.parent.parent)

            else:
                
                uncle = node.parent.parent.right

                if uncle.red:

                    uncle.red = False
                    node.parent.red = False
                    node.parent.parent.red = True
                    node = node.parent.parent

                else:

                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)

                    node.parent.red = False
                    node.parent.parent.red = True
                    self.rotate_right(node.parent.parent)

        self.root.red = False

    def rotate_left(self, x):

        y = x.right
        x.right = y.left
        
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent

        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def rotate_right(self, x):

        y = x.left
        x.left = y.right

        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent

        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def search(self, val):

        current = self.root

        while current != self.nil and val != current.val:

            if val < current.val:
                current = current.left
            else:
                current = current.right

        return current