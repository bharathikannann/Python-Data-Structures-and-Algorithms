# ### Author: [BHARATHI KANNAN N](https://github.com/bharathikannann)
# 
# <big>Merging Two Sorted Linked lists</big><br>
# Merge sort algorithm
class Node():
    def __init__(self, data, next=None):
        self.data=data
        self.next=next
        
class LinkedList(object):
    def __init__(self):
        self.head = None
        
    def insertAtFirst(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def show(self):
        if(self.head == None):
            print("No element present in the list")
            return
        temp = self.head
        while(temp):
            print(temp.data, end='->')
            temp=temp.next
        print("None")
    # ------------------------------------------------------------------------------------------
    # Merge two sorted linked list
    def merge(self, l1, l2):
        l1.head = self.mergeSortedLinkedList(l1.head, l2.head)
    
    # ------------------------------------------------------------------------------------------
    def mergeSortedLinkedList(self, a, b):
        # Create a dummy start node and a temp node
        start = Node(10)
        temp = start
        while(True):
            # If any one of the list os none break
            if(a == None):
                temp.next = b
                break
            if(b == None):
                temp.next = a
                break
            # If a node's first data is small then assign it to next of temp and move to next of a 
            # Else do the same for b
            if(a.data <= b.data):
                temp.next = a
                a = a.next
            else:
                temp.next = b
                b = b.next
            temp = temp.next
        # Return next of start since firs element is a dummy value
        return start.next

if __name__ == "__main__":
    l1 = LinkedList()
    l2 = LinkedList()
    l1.insertAtFirst(3)
    l1.insertAtFirst(1)
    l2.insertAtFirst(4)
    l2.insertAtFirst(2)
    l1.show()
    l2.show()
    l1.merge(l1, l2)
    l1.show()
    '''
    Output
    1->3->None
    2->4->None
    1->2->3->4->None
    '''