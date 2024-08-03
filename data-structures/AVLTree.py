# An AVL tree is a self-balancing Binary Search Tree where the
# difference between heights of left and right subtrees for any node
# cannot be more than one. The difference in heights is known as the
# balance factor.

# AVL trees provide faster lookups than Red-Black trees, have better
# searching time complexity compared to other trees like binary tree,
# and height cannot exceed log(n). However, they are difficult to
# implement, have high constant factors for some of the operations, are
# not used as much as Red-Black trees, take more processing for balancing,
# and provide complicated insertion and removal operations as more rotations
# are performed.

class AVLNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.par = None
        self.height = 1

class AVLTree:
    def update_height(self, root):

        if root is not None:
            left_height = root.left.height if root.left else 0
            right_height = root.right.height if root.right else 0
            root.height = max(left_height, right_height) + 1

    # Left-left rotation
    def LLR(self, root):

        temp = root.left
        root.left = temp.right

        if temp.right:
            temp.right.par = root

        temp.right = root
        temp.par = root.par
        root.par = temp

        if temp.par:
            if root.key < temp.par.key:
                temp.par.left = temp
            else:
                temp.par.right = temp

        self.update_height(root)
        self.update_height(temp)
        return temp
    
    # Right-right rotation
    def RRR(self, root):

        temp = root.right
        root.right = temp.left

        if temp.left:
            temp.left.par = root

        temp.left = root
        temp.par = root.par
        root.par = temp

        if temp.par:
            if root.key < temp.par.key:
                temp.par.left = temp
            else:
                temp.par.right = temp

        self.update_height(root)
        self.update_height(temp)
        return temp
    
    # Left-right rotation
    def LRR(self, root):

        root.left = self.RRR(root.left)
        return self.LLR(root)
    
    def balance(self, root):

        first_height = 0
        second_height = 0

        if root.left:
            first_height = root.left.height
        
        if root.right:
            second_height = root.right.height

        if abs(first_height - second_height) == 2:

            if first_height < second_height:

                right_height_one = 0
                right_height_two = 0

                if root.right.right:
                    right_height_two = root.right.right.height
                if root.right.left:
                    right_height_one = root.right.left.height
                if right_height_one > right_height_two:
                    root = self.RLR(root)
                else:
                    root = self.RRR(root)

            else:
                
                left_height_one = 0
                left_height_two = 0

                if root.left.right:
                    left_height_two = root.left.right.height
                if root.left.left:
                    left_height_one = root.left.left.height
                if left_height_one > left_height_two:
                    root = self.LLR(root)
                else:
                    root = self.LRR(root)

        return root
    
    # Right-left rotation
    def RLR(self, root):

        root.right = self.LLR(root.right)
        return self.RRR(root)
    
    def insert(self, root, parent, key):

        if root is None:
            root = AVLNode(key)
            root.par = parent
        elif root.key > key:
            root.left = self.insert(root.left, root, key)
            left_height = root.left.height if root.left else 0
            right_height = root.right.height if root.right else 0

            if abs(left_height - right_height) == 2:
                if key < root.left.key:
                    root = self.LLR(root)
                else:
                    root = self.LRR(root)

        elif root.key < key:
            root.right = self.insert(root.right, root, key)
            left_height = root.left.height if root.left else 0
            right_height = root.right.height if root.right else 0

            if abs(left_height - right_height) == 2:
                if key < root.right.key:
                    root = self.RLR(root)
                else:
                    root = self.RRR(root)

        self.update_height(root)
        return root

    def search(self, root, key):

        if root is None:
            return False
        elif root.key == key:
            return True
        elif root.key > key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)
        
    def delete(self, root, key):

        if root:
            if root.key == key:
                if root.right is None and root.left is not None:
                    
                    if root.par:

                        if root.par.key < root.key:
                            root.par.right = root.left
                        else:
                            root.par.left = root.left
                        
                        self.update_height(root.par)
                    
                    root.left.par = root.par
                    root.left = self.balance(root.left)
                    return root.left
                
                elif root.left is None and root.right is not None:

                    if root.par:
                        
                        if root.par.key < root.key:
                            root.par.right = root.right
                        else:
                            root.par.left = root. right

                        self.update_height(root.par)
                    
                    root.right.par = root.par
                    root.right = self.balance(root.right)
                    return root.right
                
                elif root.left is None and root.right is None:

                    if root.par:

                        if root.par.key < root.key:
                            root.par.right = None
                        else:
                            root.par.left = None

                        self.update_height(root.par)

                    root = None
                    return None
                
                else:

                    temp = root
                    temp = temp.right

                    while temp.left:
                        temp = temp.left

                    val = temp.key
                    root.right = self.delete(root.right, temp.key)
                    root.key = val
                    root = self.balance(root)

            elif root.key < key:

                root.right = self.delete(root.right, key)
                root = self.balance(root)

            elif root.key > key:

                root.left = self.delete(root.left, key)
                root = self.balance(root)

            self.update_height(root)

        return root

    def print_preorder(self, root):

        if root:
            parent_key = root.par.key if root.par else "NULL"
            print(f"Node: {root.key}, Parent Node: {parent_key}")
            self.print_preorder(root.left)
            self.print_preorder(root.right)