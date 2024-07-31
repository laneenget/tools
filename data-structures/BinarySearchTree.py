from collections import deque

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        
        if root is None:
            root = TreeNode(data)
            return root
        
        q = deque()
        q.append(root)

        while q:
            temp = q.popleft()

            if temp.left is None:
                temp.left = TreeNode(data)
                break
            else:
                q.append(temp.left)
            
            if temp.right is None:
                temp.right = TreeNode(data)
                break
            else:
                q.append(temp.right)

        return root
    
    def deleteDeepest(self, root, d_node):
        
        q = deque()
        q.append(root)

        while q:
            temp = q.popleft()
            if temp == d_node:
                temp = None
                del d_node
                return
            if temp.right:
                if temp.right == d_node:
                    temp.right = None
                    del d_node
                    return
                else:
                    q.append(temp.right)
            if temp.left:
                if temp.left == d_node:
                    temp.left = None
                    del d_node
                    return
                else:
                    q.append(temp.left)

    def delete(self, root, key):

        if not root:
            return None
        
        if root.left is None and root.right is None:
            if root.data == key:
                return None
            else:
                return root
            
        q = deque()
        q.append(root)
        temp = None
        key_node = None

        while q:
            temp = q.popleft()
            if temp.data == key:
                key_node = temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

        if key_node is not None:
            x = temp.data
            key_node.data = x
            self.deleteDeepest(root, temp)

        return root
    
    def search(self, root, key):

        if root is None or root.key == key:
            return root
        
        if root.key < key:
            return self.search(root.right, key)
        
        return self.search(root.left, key)

    def inorderTraversal(self, root):

        if not root:
            return
        
        self.inorderTraversal(root.left)
        print(root.data, end=" ")
        self.inorderTraversal(root.right)

    def preorderTraversal(self, root):

        if not root:
            return
        
        print(root.data, end=" ")
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

    def postorderTraversal(self, root):

        if not root:
            return
        
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        print(root.data, end=" ")

    def levelorderTraversal(self, root):

        if not root:
            return
        
        q = deque()
        q.append(root)

        while q:
            temp = q.popleft()
            print(temp.data, end=" ")
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)