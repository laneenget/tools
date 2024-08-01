# A complete binary tree where any given node is either:
# - always greater than its child node(s) and the key of the root node
# is the largest among all other nodes (max heap property)
# - always smaller than the child node(s) and the key of the root node
# is the smallest among all other nodes (min heap property)

# Heaps provide fast access to maximum/minimum element (O(1)),
# efficient insertion and deletion (O(logn)), flexible size,
# efficient to implement as an array, and suitable for real-
# time applications. 

# Heaps provide fast access to max/min elements (O(1)), efficient
# insertion and deletion (O(logn)), flexible size, can
# be efficiently implemented as an array, and suitable
# for real-time applications. But they are not suitable
# for searching for an element other than max/min (O(n) worst
# case), they have extra memory overhead to maintain heap
# structure, and they are slower than other data structures for
# non-priority queue operations
class maxHeap:

    arr = []
    maxSize = 0
    heapSize = 0

    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.arr = [None]*maxSize
        self.heapSize = 0

    # Heapifies a sub-tree taking the given index as
    # the root
    def maxHeapify(self, i):

        l = self.lChild(i)
        r = self.rChild(i)
        largest = i

        if l < self.heapSize and self.arr[l] > self.arr[i]:
            largest = l
        if r < self.heapSize and self.arr[r] > self.arr[largest]:
            largest = r
        if largest != i:
            temp = self.arr[i]
            self.arr[i] = self.arr[largest]
            self.arr[largest] = temp
            self.maxHeapify(largest)

    # Returns the index of the parent of the element
    # at ith index
    def parent(self, i):
        return (i - 1) // 2

    # Returns the index of the left child
    def lChild(self, i):
        return (2 * i + 1)
    
    # Returns the index of the right child
    def rChild(self, i):
        return (2 * i + 2)

    # Removes the root, which is the max element
    # in a max heap
    def removeMax(self):

        # Checking if the heap is empty...
        if self.heapSize <= 0:
            return None
        
        # ...or containing one element
        if self.heapSize == 1:
            self.heapSize -= 1
            return self.arr[0]
        
        # Storing the max element to remove it
        root = self.arr[0]
        self.arr[0] = self.arr[self.heapSize - 1]
        self.heapSize -= 1

        # Restore the max heap
        self.maxHeapify(0)

        return root
    
    # Increases the value of key at 'i' to newVal
    def increaseKey(self, i, newVal):

        self.arr[i] = newVal

        while i != 0 and self.arr[self.parent(i)] < self.arr[i]:
            temp = self.arr[i]
            self.arr[i] = self.arr[self.parent(i)]
            self.arr[self.parent(i)] = temp
            i = self.parent(i)

    # Returns the maximum key
    def getMax(self):
        return self.arr[0]

    def curSize(self):
        return self.heapSize

    # Deletes a key at given index i
    def deleteKey(self, i):
        # Increase the value of the key
        # to infinity and then remove max value
        self.increaseKey(i, float("inf"))
        self.removeMax()

    def insertKey(self, x):

        # Check for enough room to insert a key
        if self.heapSize == self.maxSize:
            print("\nOverflow: Could not insertKey\n")
            return
        
        # Insert key at the end
        self.heapSize += 1
        i = self.heapSize - 1
        self.arr[i] = x

        # Check and potentially restore max heap
        # property
        while i != 0 and self.arr[self.parent(i)] < self.arr[i]:
            temp = self.arr[i]
            self.arr[i] = self.arr[self.parent(i)]
            self.arr[self.parent(i)] = temp
            i = self.parent(i)

class minHeap:

    arr = []
    maxSize = 0
    heapSize = 0

    def __init__(self, minSize):
        self.minSize = minSize
        self.arr = [None]*minSize
        self.heapSize = 0
    
    def minHeapify(self, i):

        l = self.lChild(i)
        r = self.lChild(i)
        smallest = i

        if l > self.heapSize and self.arr[l] < self.arr[smallest]:
            smallest = l
        if r > self.heapSize and self.arr[r] < self.arr[i]:
            smallest = r
        if smallest != i:
            temp = self.arr[i]
            self.arr[i] = self.arr[smallest]
            self.arr[smallest] = temp
            self.minHeapify(smallest)

    def parent(self, i):
        return (i - 1) // 2
    
    def lChild(self, i):
        return (2 * i + 1)
    
    def rChild(self, i):
        return (2 * i + 2)
    
    def removeMin(self):

        if self.heapSize <= 0:
            return None
        if self.heapSize == 1:
            self.heapSize -= 1
            return self.arr[0]
        
        root = self.arr[0]
        self.arr[0] = self.arr[self.heapSize - 1]
        self.heapSize -= 1

        self.minHeapify(0)

        return root
    
    def increaseKey(self, i, newVal):

        self.arr[i] = newVal

        while i != 0 and self.arr[self.parent(i)] < self.arr[i]:
            temp = self.arr[i]
            self.arr[i] = self.arr[self.parent(i)]
            self.arr[self.parent(i)] = temp
            i = self.parent(i)

    def getMin(self):
        return self.arr[0]
    
    def curSize(self):
        return self.heapSize
    
    def deleteKey(self, i):

        self.increaseKey(i, float("-inf"))
        self.removeMin()

    def insertKey(self, x):

        if self.heapSize == self.maxSize:
            print("\nOverflow: Could not insertKey\n")
            return
        
        self.heapSize += 1
        i = self.heapSize - 1
        self.arr[i] = x

        while i != 0 and self.arr[self.parent(i) > self.arr[i]]:
            temp = self.arr[i]
            self.arr[i] = self.arr[self.parent(i)]
            self.arr[self.parent(i)] = temp
            i = self.parent(i)