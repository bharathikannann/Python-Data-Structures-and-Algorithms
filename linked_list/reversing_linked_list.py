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

if __name__ == "__main__":
    ll = LinkedList()
    ll.insertAtFirst(10)
    ll.insertAtFirst(20)
    ll.insertAtFirst(30)
    ll.insertAtFirst(40)
    ll.insertAtFirst(50)
    ll.show()
    print("Reverse")
    ll.reverse()
    ll.show()
    print("Reverse using recursion")
    ll.reverseRecursion()
    ll.show()
    '''
    Output
    50->40->30->20->10->None
    Reverse
    10->20->30->40->50->None
    Reverse using recursion
    50->40->30->20->10->None
    '''