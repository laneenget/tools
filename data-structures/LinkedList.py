# Linked lists can be made double by including a prev node value
# or circular if the last node is connected to the head
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Initialize a new node and insert it at the beginning of the list
    # replacing the current head
    def insertAtBeginning(self, new_data):

        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

    # Initialize a new node and insert it in the space after the head
    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print("The given previous node does not exist")
            return
        
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Initialize a new node and place it at the very end of the list.
    # If the list is empty, this node becomes the head.
    def insertAtEnd(self, new_data):

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    # Given a position, traverse the list and locate the key of the
    # node to be deleted.
    def deleteNode(self, position):

        # Nothing in the list to delete
        if self.head is None:
            return
        
        temp = self.head

        # If the node to be deleted is the head, make the next node
        # the head
        if position == 0:
            self.head = temp.next
            temp = None
            return
        
        # Find the key to be deleted
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        # If the key is not present
        if temp is None:
            return
        
        if temp.next is None:
            return
        
        next = temp.next.next

        temp.next = None
        
        temp.next = next

    # Search an element by key. If it exists, return true. If it does
    # not, return false.
    def search(self, key):

        current = self.head

        while current is not None:
            if current.data == key:
                return True
            
            current = current.next

        return False
    
    # Sort the linked list using an empty index node to determine
    # inequality (with Bubble Sort)
    def sortLinkedList(self, head):
        
        current = head
        index = Node(None)

        if head is None:
            return
        else:
            while current is not None:
                index = current.next

                while index is not None:
                    if current.data > index.data:
                        current.data, index.data = index.data, current.data

                    index = index.next
                current = current.next

    def printList(self):
        
        temp = self.head
        while(temp):
            print(str(temp.data) + " ", end="")
            temp = temp.next