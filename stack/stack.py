# Author: BHARATHI KANNAN N - Github: https://github.com/bharathikannann, linkedin: https://linkedin.com/in/bharathikannann 
# 
# ### Stack
# 
# A stack is an abstract data type that serves as a collection of elements, with two main principal operations:
# - Push, which adds an element to the collection, and
# - Pop, which removes the most recently added element.
# The order in which elements come off a stack gives rise to its alternative name, LIFO (last in, first out).
#Structure of the node for our linked list
class Node:
    #Each node has its data and a pointer which points to the next data
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
class Stack:
    # Initializing the head to None
    def __init__(self):
        self.head = None
    
    # Push one element to the top    
    def push(self, data):
        # Create a new node, link before head and make it as head
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    
    # Remove the top element
    def pop(self):
        # If head is none then no element is present
        if(self.head == None):
            print("Stack underflow")
            return
        # Get the head data and link head to the next node
        data = self.head.data
        self.head = self.head.next
        # return the data
        return data
    
    # Get the top node data
    def peek(self):
        # If head is none then no element is present
        if(self.head == None):
            print("Stack is empty")
        # Return head data
        return self.head.data
    
    # Print all data
    def show(self):
        # If head is none then no element is present
        if(self.head == None):
            print("No data")
            return
        # Traverse all node and print all data
        temp = self.head
        while(temp):
            print(temp.data, end="->")
            temp = temp.next
        # Print None at last for convenience
        print("None")
    
    # Stack empty or not
    def isEmpty(self):
        # If head empty return True else false
        return True if self.head == None else False
    
    # Length of the stack
    def length(self):
        temp = self.head
        count = 0
        # Traverse all nodes and for each traversal increment count
        while(temp):
            count +=1
            temp = temp.next
        return count

if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.show()
    print("Top data: " + str(s.peek()))
    popdata = s.pop()
    print("Popped data:" +str(popdata))
    s.show()
    print("Length: " + str(s.length()))
    print("Is empty: " + str(s.isEmpty()))
    print("Pop 2 times")
    s.pop()
    s.pop()
    s.show()
    print("Is empty: " + str(s.isEmpty()))
    '''
    Output
    30->20->10->None
    Top data: 30
    Popped data:30
    20->10->None
    Length: 2
    Is empty: False
    Pop 2 times
    No data
    Is empty: True
    '''

