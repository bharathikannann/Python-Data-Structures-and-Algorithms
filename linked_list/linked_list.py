# Author: BHARATHI KANNAN N - Github: https://github.com/bharathikannann, linkedin: https://linkedin.com/in/bharathikannann 
# ## Linked List
# 
# - Linked list is a linear collection of data elements whose order is not given by their physical placement in memory. Instead, each element points to the next.
# - In its most basic form, each node contains: data, and a reference
# - This structure allows for efficient insertion or removal of elements from any position in the sequence during iteration.
# - Linked lists are among the simplest and most common data structures. They can be used to implement several other common abstract data types, including lists, stacks, queues, etc..,
# 
# ### Time Complexity:
# - Insertion: O(1)
#     - Insertion at front: O(1)
#     - Insertion in between: O(1)
#     - Insertion at End: O(n)
# - Deletion: O(1)
# - Indexing: O(n)
# - Searching: O(n)

#Structure of the node for our linked list
class Node():
    #Each node has its data and a pointer which points to the next data
    def __init__(self, data, next=None):
        self.data=data
        self.next=next
    
    # Setter and Getter Functions
    #To set data
    def setData(self, data):
        self.data = data
        
    #To det data
    def getData(self):
        return self.data
    
    #To set next
    def setNext(self, data):
        self.data = data
        
    #To get next
    def getNext(self):
        return self.next

class LinkedList(object):
    # Head of the linked list
    def __init__(self):
        self.head = None
    
    # ------------------------------------------------------------------------------------------    
    # Inserting the element at the start of the linked list
    # Steps
        # 1. Creating the new node with the data.
        # 2. Assigning the next of the new node to the head
        # 3. Changing the head to the newnode since it has been changed as the first element
        
    def insertAtFirst(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    
    # ------------------------------------------------------------------------------------------    
    # Printing all the elements of the linked list
    # Steps
        # 1. Creating a temporary variable and assigining it to the first element (head)
        # 2. Traversing and printing the data till the end untill it is null
        
    def show(self):
        if(self.head == None):
            print("No element present in the list")
            return
        temp = self.head
        while(temp):
            print(temp.data, end='->')
            temp=temp.next
        print()
       # print("NONE") (for understanding since last element is null)
    
    # ------------------------------------------------------------------------------------------
    # Inserting the data at a specific position. Here the indexing starts from 1
    # Steps
    # 1. If position is 1 then insert at first
    # 2. Else traverse to the previous node and change the next of new node to the next of temp node and
    # change the next of temp node to new node
    # In step 2 order matters, because if we change the next of tempnode first we loss the position.
    
    def insertAtPosition(self, data, position):
        newNode = Node(data)
        if (position == 1):
            self.insertAtFirst(data)
        else:
            temp = self.head
            for i in range(position-2):
                temp = temp.next
            newNode.next = temp.next
            temp.next = newNode
    
    # ------------------------------------------------------------------------------------------
    # Deleting the data at any position 
    # Steps
    # 1. If head is the data to be deleted and if is none return none and if it the element to be deleted
    # change the head to the next of head by using temp node
    # 2. Else traverse untill the element is found and while traversing keep track of pevious node
    # 3. check if temp is none it means the traversing the reached till the end and no element is found
    # 4. connect next of previous to next of temp by skipping the temp which is the element to be deleted
    def delete(self, data):
        if (self.head == None):
            return None
        temp = self.head
        if(temp.data == data):
            self.head = temp.next
            return
        else:
            while(temp):
                if(temp.data ==  data):
                    break
                prev = temp
                temp = temp.next
            
            if temp == None:
                return
            
            prev.next = temp.next
            return
    
    # ------------------------------------------------------------------------------------------    
    # Insert the data at last
    # Steps: 
    # 1. If no element is present just insert at first
    # 2. Else traverse till the last and connect the new node with the temp which is the last node
            
    def insertAtLast(self, data):
        if self.head == None:
            self.insertAtFirst(data)
            return
        newNode = Node(data)
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        temp.next = newNode
    
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
    # If a data exists in any node (Search method)
    #Steps: 
    # 1: If head is none then no element present and false
    # 2: Else traverse the list and find if any data is present in any node and at last return false
        
    def ifNodeExists(self, data):
        if (self.head == None):
            return False
        else:
            temp = self.head
            while(temp):
                if (temp.data == data):
                    return True
                temp = temp.next
            return False
    
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
    
    # ------------------------------------------------------------------------------------------    
    # Reverse the linked list
    # Here we need three variables prev, current, after
    def reverse(self):
        prev = None
        # Set current to head and traverse till end
        current = self.head
        # Ex: 1(head,current)->2->3->None
        while(current is not None):
            # change after to next of current. Ex: 1(head,current)->2(after)->3->None
            after = current.next
            # then change next to current to prev (here the link changes backwards direction for linked list).
            # Ex: None(prev)<-1(head,current) 2(after)->3->None
            current.next = prev
            # Now change the prev and current and do the same for next nodes.
            # Ex: None<-1(head,prev) 2(after,current)->3->None
            prev = current
            current = after
        # Finally you end up in None<-1(head)<-2<-3(prev)<-None(current,after), so change the head node to prev
        self.head = prev
    
    # ------------------------------------------------------------------------------------------
    # Same reverse function usinf recursion
    # Made two functionso that we don't need to use list.head in the main function
    def reverseRecursion(self):
        return self.reverseRecursionLL(self.head)
    
    # The reverse function using recursion
    def reverseRecursionLL(self, temp):
        # If the last node is reached make it as head and return
        if(temp.next == None):
            self.head = temp
            return
        self.reverseRecursionLL(temp.next)
        # Make new temp variable and make it as next  of temp
        # 1->2->3(temp)->None(temp2)
        temp2 = temp.next
        # 1->2->3(temp,head)->None(temp2)
        # None(temp2)->3(temp,head)
        temp2.next = temp
        # None(temp2)->3(head)->None
        temp.next = None
        # The value of temp changes in every recursion so we don't need to change the temp to the previous node
    
    # ------------------------------------------------------------------------------------------ 
    # Get the middle element
    def getMiddleElement(self, printelement=False):
        # Make two nodes slow and fast
        slow = self.head
        fast = self.head.next
        # Ex: 1(head,slow)->2(fast)->3->4->None
        # Here slow moves one step and fast moves two steps in a single iteration
        while(fast!=None and fast.next != None):
            # Ex: 1(head)->2(slow)->3->4(fast)->None
            slow = slow.next
            fast = fast.next.next
        # At last print the slow node data
        # If the length is even the middle element is (length/2)-1. Slow works for both even and odd.
        if (printelement):
            print("The middle element is: " + str(slow.data))
        return slow.data
    
    # ------------------------------------------------------------------------------------------
    # Does First half and second half match we can use the same concept as before
    def isFirstSecondHalfMatch(self):
        slow = self.head
        fast = self.head.next
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        
        # We can traverse from head and next of slow node and can check each data on both sides
        # Ex: 1(head,temp)->2(slow)->3->4->None
        temp = self.head        # Ex: 1(head,temp)->2->3(slow)->4->None
        slow = slow.next
        # If the length is odd we don't need to check the middle element
        while(slow):
            if(temp.data != slow.data):
                return False
            slow = slow.next
            temp = temp.next
        return True
    
    # ------------------------------------------------------------------------------------------
    # Return true if a linked list is palindrome
    # Ex: 1->2->2->1->None
    def isPalindrome(self):
        # Use stack to store all the fist half elements
        stack = []
        slow = self.head
        fast = self.head.next
        stack.append(slow.data)
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            stack.append(slow.data)
        # If fast is none then it is an off length linked list and we don't need to check middle element
        if(fast == None):
            stack.pop()
        # Traverse from next of slow and check each element from stack and slow
        # Pop of the stack gives first half if linkedlist in reverse
        slow = slow.next
        while(slow):
            if(slow.data != stack.pop()):
                return False
            slow = slow.next
        return True
    
    # ------------------------------------------------------------------------------------------
    # Deleting the entire linked list
    def deleteList(self):
        self.head = None
    
    # ------------------------------------------------------------------------------------------    
    # Delete an element if it's right node is grater than it
    # Example: I/P - 5->1->3->2->7-None
    # O/P - 5->3->None
    def deleteGreaterValuesOnRight(self):
        # Check if only 1 node is present or head is none
        if(self.head == None and self.head.next == None):
            return
        temp = self.head
        # Traverse and check if the next node is grater anf if it is then delete the current node
        while(temp.next != None):
            if(temp.data < temp.next.data):
                self.delete(temp.data)
            temp = temp.next
    
    # ------------------------------------------------------------------------------------------        
    # Swapping pairwise elements
    # Ex: 1->2->3->4->None - 2->1->4->3->none
    def pairwiseSwapElements(self):
        # If head is none or next of head is null return
        if(self.head == None and self.head.next == None):
            return
        temp = self.head
        while(temp != None and temp.next != None):
            # Normal swapping
            n = temp.data
            temp.data = temp.next.data
            temp.next.data = n
            temp = temp.next.next
    
    # ------------------------------------------------------------------------------------------        
    # Delete alternate nodes
    def deleteAlternateNodes(self):
        # If head is none or next of head is null return
        if(self.head == None and self.head.next == None):
            return
        temp = self.head
        # While traversing eachtime skip next node
        while(temp != None and temp.next != None):
            temp.next = temp.next.next
            temp = temp.next
    
    # ------------------------------------------------------------------------------------------        
    # Move last node to front
    def moveLastNodeToFront(self):
        if(self.head == None or self.head.next == None):
            return
        temp = self.head
        # Traverse to the second last element in the linkedlist
        while(temp.next.next is not None):
            temp = temp.next
        # Get last node data and insert at first
        val = temp.next.data
        temp.next = None
        self.insertAtFirst(val)
    
    # ------------------------------------------------------------------------------------------    
    # Get count of a data in linkedlist
    def getCountOfValue(self, n):
        if(self.head == None):
            return
        temp = self.head
        count=0
        while(temp):
            if(temp.data == n):
                count+=1
            temp=temp.next
        return count

# Execute only in main file
if __name__ == '__main__':
    LList = LinkedList()
    print("Insert at first")
    LList.insertAtFirst(10)
    LList.insertAtFirst(20)
    LList.show()
    print("Insert at position")
    LList.insertAtPosition(5,3)
    LList.show()
    print("Delete")
    LList.delete(50)
    LList.show()
    print("Insert at last")
    LList.insertAtLast(2)
    LList.insertAtLast(1)
    LList.delete(10)
    LList.show()
    print("If Node 20 Exists: " + str(LList.ifNodeExists(20)))
    print("Length: " + str(LList.length()))
    print("Rotate Clockwise")
    LList.rotateClockwise(2)
    LList.show()
    print("Rotate Anticlockwise")
    LList.rotateAntiClockwise(2)
    LList.show()
    print("Reverse")
    LList.reverse()
    LList.show()
    LList.reverseRecursion()
    LList.show()
    LList.getMiddleElement(printelement=True)
    LList.insertAtLast(1)
    LList.insertAtLast(2)
    LList.insertAtLast(5)
    LList.insertAtLast(20)
    LList.show()
    print("First and second half match")
    print(LList.isFirstSecondHalfMatch())
    print("Is Palindrome")
    print(LList.isPalindrome())
    LList.deleteGreaterValuesOnRight()
    LList.show()
    print("Pair wise swap elements")
    LList.pairwiseSwapElements()
    LList.show()
    print("Delete alterntive nodes")
    LList.deleteAlternateNodes()
    LList.show()
    print("Move last node to front")
    LList.moveLastNodeToFront()
    LList.show()
    print("Get count of value")
    LList.insertAtFirst(20)
    print(LList.getCountOfValue(20))
    print("Delete entire list")
    LList.deleteList()
    LList.show()
    '''
    Output
    Insert at first
    20->10->
    Insert at position
    20->10->5->
    Delete
    20->10->5->
    Insert at last
    20->5->2->1->
    If Node 20 Exists: True
    Length: 4
    Rotate Clockwise
    2->1->20->5->
    Rotate Anticlockwise
    20->5->2->1->
    Reverse
    1->2->5->20->
    20->5->2->1->
    The middle element is: 5
    20->5->2->1->1->2->5->20->
    First and second half match
    False
    Is Palindrome
    True
    20->1->2->5->20->
    Pair wise swap elements
    1->20->5->2->20->
    Delete alterntive nodes
    1->5->20->
    Move last node to front
    20->1->5->
    Get count of value
    2
    Delete entire list
    No element present in the list
    '''