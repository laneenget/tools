# Implementation of a stack using a linked list. Can also be done
# with arrays. The linked list implementation of a stack can grow
# and shrink according to needs at runtime, but requires extra 
# memory due to the involvement of pointers. Random accessing is
# also not possible.

# Stacks are simple and efficient since time and space complexity
# are both constant for all methods. They follow LIFO which is
# useful in function calls and expression evaluation. They also
# use limited memeory. However, stacks can only be accessed from
# the top, making it difficult to retrieve elements in the middle
# of the stack and not suitable for random access. They also have 
# a fixed capacity, which makes them susceptible to overflow.

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return True if self.root is None else False
    
    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.root
        self.root = newNode
        print("% d pushed to stack" % (data))

    def pop(self):
        if (self.isEmpty()):
            return float("-inf")
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        return popped
    
    def peek(self):
        if self.isEmpty():
            return float("-inf")
        return self.root.data