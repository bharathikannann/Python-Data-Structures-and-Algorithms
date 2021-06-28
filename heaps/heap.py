# Our Binary Heap
class BinaryHeap:
    # Initialization
    def __init__(self):
        self.heap = []
        self.size = 0
    
    # Empty or not
    def isEmpty(self):
        return self.size == 0
    
    # Get top element
    def peek(self):
        if self.isEmpty():
            print("Heap is empty")
        else:
            return self.heap[0]
    
    # Add method helper function
    def __add(self, data):
        # Add at last, increase size and shift up
        self.heap.append(data)
        self.size += 1
        self.shiftUp()
        
    # Add method to add all data in a list
    def add(self, data):
        if isinstance(data, int):
            self.__add(data)
        else:
            for i in data:
                self.__add(i)
        
    # Remove the top element
    def remove(self):
        if self.isEmpty():
            print("Heap is empty")
            return
        else:
            # Add last data at first, reduce size and shift down
            mindata = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.size -= 1
            self.shiftDown()
            self.heap.pop()   # Pop last element since it is added at first
            return mindata   # Return min data
    
    def getLeftChildIndex(self, parentIndex):
        return (2 * parentIndex) + 1
    
    def getRightChildIndex(self, parentIndex):
        return (2 * parentIndex) + 2
    
    def getParentIndex(self, childIndex):
        return (childIndex - 1) // 2
    
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size
    
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size
    
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0 and index != 0
    
    def leftChild(self, index):
        return self.heap[self.getLeftChildIndex(index)]
    
    def rightChild(self, index):
        return self.heap[self.getRightChildIndex(index)]
    
    def parent(self, index):
        return self.heap[self.getParentIndex(index)]
    
    # Swap two index elements
    def swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp
    
    # Shift up when adding an element
    def shiftUp(self):
        index = self.size - 1   # Get last index
        # While it has a parent and if index data is less than its parent swap it
        while(self.hasParent(index) and self.heap[index] < self.parent(index)):
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)   # Change index 
            
    def shiftDown(self):
        index = 0   # Top index
        while(self.hasLeftChild(index)):   # Since it is a complete binaty tree, we can traverse until there is left child
            # Assume smaller child indes as left child, and if right child exists change it to right child
            smallerChildIndex = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index):
                smallerChildIndex = self.getRightChildIndex(index)
            # Don't do anything if it is in the correc position
            if self.heap[index] < self.heap[smallerChildIndex]:
                break
            else:
                self.swap(index, smallerChildIndex)   # Swap data
            index = smallerChildIndex                 # Keep track of smaller index

if __name__ == '__main__':
    heap = BinaryHeap()
    heap.add([20,50,40,100,70,10])
    print(heap.remove())
    print(heap.heap)