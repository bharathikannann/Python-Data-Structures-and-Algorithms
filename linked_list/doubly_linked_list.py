# Author: BHARATHI KANNAN N - Github: https://github.com/bharathikannann, linkedin: https://linkedin.com/in/bharathikannann 
# 
# ## Doubly Linked List
# - A doubly linked list is a linked data structure that consists of a set of sequentially linked records called nodes. Each node contains three fields: two link fields (references to the previous and to the next node in the sequence of nodes) and one data field.
# - The two node links allow traversal of the list in either direction. 

#Structure of the node for our doubly linked list
class Node(object):
    #Each node has its data and two pointers which points to the next data and previous data
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList(object):
    # Head of the doubly linked list
    def __init__(self):
        self.head = None
    
    # ------------------------------------------------------------------------------------------
    # Inserting at first
    def insertAtFirst(self, data):
        newNode = Node(data)
        # If head is none then make new node as head
        if(self.head == None):
            self.head = newNode
        # Insert new node before head and change the head
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
    
    # ------------------------------------------------------------------------------------------
    # To print all the elements
    def show(self):
        if(self.head == None):
            return
        temp = self.head
        # traverse till end and print each data
        while(temp):
            print(temp.data, end="<->")
            temp = temp.next
        # Last node is none and printed here for convenience
        print("None")
    
    # ------------------------------------------------------------------------------------------
    # Insert node at last
    def insertAtLast(self, data):
        if(self.head == None):
            return
        temp = self.head
        # Traverse till prev of last node and attach at last
        while(temp.next):
            temp = temp.next
        newNode = Node(data)
        temp.next = newNode
        newNode.prev = temp
    
    # ------------------------------------------------------------------------------------------
    # Insert at a certain position
    def insertAtPosition(self, data, position):
        # If position is 1 then insert at start
        if(position == 1):
            return self.insertAtFirst(data)
        newNode = Node(data)
        temp = self.head
        # Traverse till before the position (-2 because we already start at position 1)
        for i in range(position - 2):
            # If next of temp is none then we have reached till end. So we cannot insert after None so return 
            if(temp.next == None):
                return 
            temp = temp.next
        # Insert new node betwwen temp and next of temp
        newNode.next = temp.next
        newNode.prev = temp
        # If next of temp is none we cannot change it prev
        if(temp.next is not None):
            temp.next.prev = newNode
        temp.next = newNode
    
    # ------------------------------------------------------------------------------------------    
    # Delete an element
    def delete(self, data):
        # If head is none return
        if(self.head == None):
            return
        # If head is the element to be deleted
        temp = self.head
        if(temp.data == data):
            # change head to next element
            self.head = temp.next
            temp = None
            return
        # Traverse till end
        while(temp):
            if(temp.data == data):
                break
            temp = temp.next
        # If temp is none then we have reached till end and no data is found
        if(temp == None):
            return
        # Connect prev node to next of temp
        temp.prev.next = temp.next
        # If next of temp is none the we cannot link it's prev to prev of temp
        if(temp.next):
            temp.next.prev = temp.prev
        # Disconnect temp
        temp.next = None
        temp.prev = None
    
    # ------------------------------------------------------------------------------------------    
    # Delete the entire doubly linked list
    def deleteList(self):
        self.head = None
    
    # ------------------------------------------------------------------------------------------    
    # Count of nodes in our doubly linked list
    def length(self):
        temp = self.head
        count = 0
        # Traverse each time and increment the count
        while(temp):
            count +=1
            temp = temp.next
        return count
    
    # ------------------------------------------------------------------------------------------
    # Print all the elements in reverse
    def reversePrint(self):
        if(self.head == None):
            return
        temp = self.head
        while(temp.next):
            temp = temp.next
        while(temp):
            print(temp.data,end="<->")
            temp = temp.prev
        print()

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insertAtFirst(10)
    dll.insertAtFirst(20)
    dll.insertAtLast(5)
    dll.insertAtLast(2)
    dll.insertAtPosition(15, 5)
    dll.show()
    print("Delete an element")
    dll.delete(15)
    dll.show()
    print("Length:" + str(dll.length()))
    print("Print in reverse")
    dll.reversePrint()
    '''
    Output
    20<->10<->5<->2<->15<->None
    Delete an element
    20<->10<->5<->2<->None
    Length:4
    Print in reverse
    2<->5<->10<->20<->
    '''