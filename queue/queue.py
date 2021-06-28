# ### Author: [BHARATHI KANNAN N](https://github.com/bharathikannann)
# 
# ### Queue
# 
# A queue is a collection of entities that are maintained in a sequence and can be modified by the addition of entities at one end of the sequence and the removal of entities from the other end of the sequence.
# 
# The operation of adding an element to the rear of the queue is known as `enqueue`, and the operation of removing an element from the front is known as `dequeue`.

#Structure of the node for our linked list
class Node:
    #Each node has its data and a pointer which points to the next data
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
class Queue:
    # Front and rear node
    def __init__(self):
        self.front = self.rear = None
        # Size for our queue
        self.size = 0
        
    def enqueue(self, data):
        # Create new node
        newNode = Node(data)
        # If queue is empty 
        if(self.front == None):
            self.front = self.rear = newNode
            # Increment the size
            self.size += 1
            return
        # Insert at end (rear)
        self.rear.next = newNode
        self.rear = self.rear.next
        # Increment size
        self.size += 1
        
    def dequeue(self):
        # If queue is empty
        if(self.rear == None):
            print("Queue is empty")
            return
        # Change the front to its next node
        self.front = self.front.next
        # If front become none then there are no nodes present after dequeue, so make rear none
        if(self.front == None):
            self.rear = None
            # Decrement the size
        self.size -= 1

    # If a queue is empty or not
    def isEmpty(self):
        return self.front == None
    
    # Print all elements
    def show(self):
        if(self.front == None):
            return 
        temp = self.front
        while(temp):
            print(temp.data, end='->')
            temp = temp.next
        print("None")

if __name__ == '__main__':
    q = Queue()
    print("Enqueue")
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.enqueue(60)
    q.enqueue(70)
    q.enqueue(80)
    q.enqueue(90)
    q.enqueue(100)
    q.enqueue(110)
    q.show()
    print("Dequeue")
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.show()
    print("Size")
    print(q.size)
    '''
    Output
    Enqueue
    10->20->30->40->50->60->70->80->90->100->110->None
    Dequeue
    40->50->60->70->80->90->100->110->None
    Size
    8
    '''

