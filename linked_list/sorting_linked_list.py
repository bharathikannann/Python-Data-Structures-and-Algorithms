# ### Author: [BHARATHI KANNAN N](https://github.com/bharathikannann)
# 
# <big>Sorting in Linked lists</big><br>
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
    # Merge sort linked list
    def sort(self):
        self.head = self.mergeSort(self.head)
    
    # Divide the linked list 
    # To find middle element use slow and fast node
    # Then split until one node or none is present
    # Then merge
    def mergeSort(self, node):
        if(node == None or node.next == None):
            return node
        slow = node
        fast = node
        temp = node
        while(fast != None and fast.next != None):
            temp = slow
            slow = slow.next
            fast = fast.next.next
        temp.next = None
        left = self.mergeSort(node)
        right = self.mergeSort(slow)
        return self.merge(left, right)
    
    # Merge the lists
    def merge(self, a, b):
        result = None
        if(a == None):
            return b
        if(b == None):
            return a
        # If data of first node is small then append the merge list of b with remaining of a
        if(a.data <= b.data):
            result = a
            result.next = self.merge(a.next, b)
        else:
            result = b
            result.next = self.merge(a, b.next)
        # Return the sorted merged list 
        return result

if __name__ == "__main__":
    ll = LinkedList()
    ll.insertAtFirst(10)
    ll.insertAtFirst(20)
    ll.insertAtFirst(30)
    ll.insertAtFirst(40)
    ll.insertAtFirst(50)
    ll.show()
    ll.sort()
    ll.show()
    '''
    Output
    50->40->30->20->10->None
    10->20->30->40->50->None
    '''