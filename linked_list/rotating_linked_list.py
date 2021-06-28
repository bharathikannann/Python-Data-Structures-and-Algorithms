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
    # Length of the LinkedList
    # Steps: 
    # 1. If head is none the length is 0 else traverse and for each traversal increment count by 1

    def length(self):
        count = 0
        if(self.head is None):
            return count
        else:
            temp = self.head
            while(temp is not None):
                count+=1
                temp = temp.next
            return count
    
    # ------------------------------------------------------------------------------------------
    # Clockwise in linkedlist 
    # Example: 1->2->3->4->5->None, n=2, Then: 4->-5>->1->2->3->None
    
    def rotateClockwise (self, n):
        # If head is null or only head is present or n is less than or equal to 0 no operation can be done
        if (self.head == None or self.head.next == None or n<=0):
            return
        # Get the length of the linkedlist
        length = self.length()
        # If n is greater than length then a whole rotation is done and nothing is changed is our list. 
        # So inorder to reduce operations we can get the remainder of n%length.
        # Example if length is 4 and n is 6 then a complete rotation is done and then it is done two times.
        # So we can get the remainder and do the operation
        n = n % length
        # If n == 0  no operation is done (whole rotation)
        if (n == 0):
            return
        
        # 1(start,temp1,head)->2->3->4->None
        start = self.head
        temp1 = self.head
        
        # 1(start,head)->2(temp1)->3->4->None
        for i in range(length - n - 1):
            temp1 = temp1.next
            
        # 1(start)->2(temp1)->3(head)->4->None
        # 1(start)->2(temp1)->3(head,temp2)->4->None
        self.head = temp1.next
        temp2 = temp1.next

        # 1(start)->2->None
        # 3(head,temp2)->4->None
        temp1.next = None
        
        # 1(start)->2->None
        # 3(head)->4(temp2)->None
        for i in range(n - 1):
            temp2 = temp2.next
        # 3(head)->4(temp2)->1(start)->2->None
        temp2.next = start
        
    # ------------------------------------------------------------------------------------------    
    # Rotate Anticlockwise
    # Example: 1->2->3->4->5->None, n=2, Then: 3->4->5->1->2->None
    # Steps are same as before only the last step changes and the range in for loop changes
    def rotateAntiClockwise(self, n):
        if (self.head == None or self.head.next == None or n<=0):
            return 
        start = self.head
        temp1 = self.head
        length = self.length()
        n = n % length
        if (n == 0):
            return
        for i in range(n -1):
            temp1 = temp1.next
        self.head = temp1.next
        temp2 = temp1.next
        temp1.next = None
        for i in range(length -n -1):
            temp2 = temp2.next
        temp2.next = start

if __name__ == "__main__":
    ll = LinkedList()
    ll.insertAtFirst(10)
    ll.insertAtFirst(20)
    ll.insertAtFirst(30)
    ll.insertAtFirst(40)
    ll.insertAtFirst(50)
    ll.show()
    print("Rotate Cockwise")
    ll.rotateClockwise(2)
    ll.show()
    print("Rotate Anticlockwise")
    ll.rotateAntiClockwise(2)
    ll.show()
    '''
    Output
    50->40->30->20->10->None
    Rotate Cockwise
    20->10->50->40->30->None
    Rotate Anticlockwise
    50->40->30->20->10->None
    '''