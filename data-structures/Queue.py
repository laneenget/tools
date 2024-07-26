# Linear data structure following FIFO principle, meaning the
# element is added at the end and removed from the front. This
# implementation is built with a linked list.

# Queues can manage a large amount of data efficiently, as all
# methods are constant in time and space complexity. However, it
# can be time consuming if the operation takes place in the middle
# of the queue. Searching an element also takes linear time.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    # Method to add an item to the queue
    def EnQueue(self, item):

        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    # Method to remove an item from the queue
    def DeQueue(self):

        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next

        if(self.front == None):
            self.rear = None