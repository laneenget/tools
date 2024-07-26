# Hierarchical structures used to represent and organize data in a
# way that is easy to navigate and search for, as all nodes are
# connected by edges that signy a hierarchical relationship. The
# topmost node is called the root, with the nodes below it called
# child nodes. A child node -- in this case referred to as a parent
# node -- can have their own child nodes, and any nodes with no child
# nodes are called leaf nodes.

# Some other terminology to consider: an ancestor of a node is any
# predecessor node included on the path from the node to the root,
# a descendant is similar but in the opposite direction. Siblings
# are child nodes of the same parent. The level of the node is the
# count of edges on the path from the root node to that node. An
# internal node is a node with at least one child. A subtree is any
# node of a tree along with its descendants.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class Tree:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return True if self.root is None else False

    def pre_order_traversal(self, node):
        
        if node is None:
            return
        
        print(node.data)
        for child in node.children:
            self.pre_order_traversal(child)

    def depth_first_search(self, node, target):

        if node is None:
            return False
        if node.data == target:
            return True
        for child in node.children:
            if self.depth_first_search(child, target):
                return True
        return False
    
    def insert_node(self, node):
        
        if self.root is None:
            self.root = node
        else:
            self.root.add_child(node)

    def delete_node(self, target):

        if self.root is None:
            return None
        
        self.root.children = [child for child in self.root.children if child.data != target]
        for child in self.root.children:
            self.delete_node(child, target)

    def tree_height(self, node):

        if node is None:
            return 0
        if not node.children:
            return 1
        return 1 + max(self.tree_height(child) for child in node.children)
    
    