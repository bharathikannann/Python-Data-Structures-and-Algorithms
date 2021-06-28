from queue import Queue

class Node:
    # Node has data and two childs (left and right)
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def __preorder(self, root):   # Private functions
        if(root):
            print(root.data,end=" ")
            self.__preorder(root.left)
            self.__preorder(root.right)
    
    def preorder(self):   # Helper functions
        if self.root == None:
            print("Empty tree")
            return self
        self.__preorder(self.root)
        print()
        return self   # For chaining methods

    def __inorder(self, root):
        if(root):
            self.__inorder(root.left)
            print(root.data,end=" ")
            self.__inorder(root.right)
            
    def inorder(self):
        if self.root is None:
            print("Empty tree")
            return self
        self.__inorder(self.root)
        print()

    def __postorder(self, root):
        if(root):
            self.__postorder(root.left)
            self.__postorder(root.right)
            print(root.data,end=" ")
            
    def postorder(self):
        if self.root == None:
            print("Empty tree")
            return self
        self.__postorder(self.root)
        print()

    # Insert the data in a BST
    def __insert(self, data):
        newNode = Node(data)
        if(self.root == None): # If no element in bst
            self.root = newNode
        else:
            temp = self.root
            while(True):   # While we don't get to a leaf
                if(data == temp.data): # If data is already present return, No duplicate is allowed
                    return
                if(data < temp.data): # Go left
                    if(temp.left is None): # When no left node
                        temp.left = newNode
                        break
                    else:                  
                        temp = temp.left   # Go left
                else:
                    if(temp.right is None): # When no right node
                        temp.right = newNode
                        break
                    else:                   
                        temp = temp.right   # Go right
    
    # For inserting list of values
    def insert(self, values):
        if isinstance(values, int): # Only one element is added
            return self.__insert(values)
        for value in values: # If list of values are added
            self.__insert(value)
        return self
    
    # Return true if an element exists
    def search(self, data):
        if self.root == None: # If root is none
            raise indexError("Tree is empty, please use another")
        else:
            temp = self.root
            # Traverse the tree untill the node is none or data is found
            while temp is not None and temp.data is not data:   # Short circuiting
                if data < temp.data:
                    temp = temp.left   # Go left 
                else:
                    temp = temp.right   # Go right
            if temp == None:   # Fully traversed and not found
                return False
            return True
        
    # Sum of all the values
    def __sum(self, root):
        if(root is None):
            return 0
        # Sum of current node and its child nodes
        return root.data + self.__sum(root.left) + self.__sum(root.right)
    
    def sum(self):
        return self.__sum(self.root)
    
    # Difference of even and odd nodes
    def __getDiffEvenOddRows(self, root):
        if root is None:
            return 0
        # Difference of current node and its child nodes
        # For even rows minus of minus becomes plus
        return root.data - self.__getDiffEvenOddRows(root.left) - self.__getDiffEvenOddRows(root.right)
    
    def getDiffEvenOddRows(self):
        return self.__getDiffEvenOddRows(self.root)
    
    # No of nodes in the tree
    def __noOfNodes(self, root):
        if root is None:
            return 0
        # 1 for the nodes + its child nodes
        return 1 + self.__noOfNodes(root.left) + self.__noOfNodes(root.right) 
    
    def noOfNodes(self):
        return self.__noOfNodes(self.root)
    
    def __noOfLeafNodes(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1   # A child node
        return self.__noOfLeafNodes(root.left) + self.__noOfLeafNodes(root.right)
        
    def noOfLeafNodes(self):
        return self.__noOfLeafNodes(self.root)
    
    def __height(self, root):
        if root is None:
            return -1  # -1 because height starts from 0
        return max(self.__height(root.left), self.__height(root.right)) + 1
    
    def height(self):
        return self.__height(self.root)
    
    # Print values by level, Root node is level 1
    def __levelOrderTraversal(self, root):
        if(root is None):
            return
        q = Queue() # Creating a queue
        q.put(root) # Put root node
        while(not q.empty()):
            node = q.get() # Get the node and put all of its child nodes
            print(node.data, end=' ')
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)
        print()
            
    def levelOrderTraversal(self):
        return self.__levelOrderTraversal(self.root)        
        
    # Print values only at a certain level
    def  __printAtGivenLevel(self, root, level):
        if root is None:
            return
        if level == 1:   # Level reaches
            print(root.data, end=' ')
        self.__printAtGivenLevel(root.left, level - 1) # Decrement level and go left
        self.__printAtGivenLevel(root.right, level - 1) # Decrement level and go right
        
    def printAtGivenLevel(self, level):
        self.__printAtGivenLevel(self.root, level)
        print()
        return self
    
    def __reverseLevelOrderTraversal(self, root):
        if root is None:
            return
        q = Queue()
        s = []   # Stack
        q.put(root)
        while(not q.empty()):
            node = q.get()
            s.append(node.data)
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)
        while(len(s) != 0):   # It stored all the elements in queue in reverse order
            print(s.pop(), end=' ')   # Pop and print
        print()
        
    def reverseLevelOrderTraversal(self):
        return self.__reverseLevelOrderTraversal(self.root)
    
    def __levelOrderTraversalLineByLine(self, root):
        if root == None:
            return
        q = Queue()
        q.put(root)
        while(not q.empty()):
            count = q.qsize()
            while(count > 0):   # Here count will have the no of elements in a level
                node = q.get()
                print(node.data, end=' ')
                if node.left is not None:
                    q.put(node.left)
                if node.right is not None:
                    q.put(node.right)
                count -= 1
            print()
        
    def levelOrderTraversalLineByLine(self):
        return self.__levelOrderTraversalLineByLine(self.root) 
    
    def __leftSideOfTree(self, root):
        if root is None: 
            return
        print(root.data, end=' ')
        self.__leftSideOfTree(root.left)   # Traverse until left side of tree is none
        
    def leftSideOfTree(self):
        self.__leftSideOfTree(self.root)
        print()
        return self
    
    def __rightSideOfTree(self, root):
        if root is None:
            return
        print(root.data, end=' ')
        self.__rightSideOfTree(root.right)   # traverse until right side of tree is none
        
    def rightSideOfTree(self):
        self.__rightSideOfTree(self.root)
        print()
        return
    
    def inorderUsingStack(self):
        if self.root == None:
            return
        s = []
        temp = self.root
        while(temp):
            s.append(temp)   # Append all the left side nodes
            temp = temp.left   # Go left
        while(len(s) > 0):   # Traverse until stack is empty
            node = s.pop()   # Get the node and print
            print(node.data, end=' ')
            if node.right is not None:   # Chack for right nodes
                temp2 = node.right   # Assign a new temp node 
                while(temp2):   # If it has left nodes we need to go to the end of its left most node
                    s.append(temp2)
                    temp2 = temp2.left
                '''
                Example for this while loop
                                 10
                                /  \
                              5     15
                            /  \
                           2    8     If we reached 8 we need to check all its left nodes
                               /      First 8 will be added and 6 is added so when we pop 6 comes before 8
                              6
                '''
        print()
                    
    def __mirrorTree(self, root):
        if root == None:
            return
        temp = root.left   # Normal swap with a temp node
        root.left = root.right
        root.right = temp
        self.__mirrorTree(root.left) # Swap for left side
        self.__mirrorTree(root.right) # Swap for right side
        
    def mirrorTree(self):
        return self.__mirrorTree(self.root)
    
    def __delete(self, root):
        if root is None:
            return None
        root.left = self.__delete(root.left)   # Delete all left side
        root.right = self.__delete(root.right)   # Delete the right side nodes
        root = None   # Delete the current node
        return root
    
    def delete(self):
        self.root = self.__delete(self.root)   # Change the root because it is a global variable
        
    def empty(self):
        return self.root is None   # If root is none
    
    def __isIdentical(self, node1, node2):
        if node1 == None and node2 == None:   # If both nodes are empty
            return True
        if node1 == None or node2 == None:   # If any one is different 0,1 or 1,0 here 1,1 is already checked
            return False
        # Check if both nodes data and all its left and right nodes are equal
        return node1.data == node2.data and self.__isIdentical(node1.left, node2.left) and self.__isIdentical(node1.right, node2.right)
    
    def isIdentical(self, bst1, bst2):
        return self.__isIdentical(bst1.root, bst2.root)
    
    def __getLevelOfNode(self, root, data, level):
        if root is None:   
            return 0
        if root.data is data:   # Return level if we found data
            return level
        l = level   # Temp level
        l = self.__getLevelOfNode(root.left, data, level + 1)
        if l != 0:   # If we found data in left side we can skip checking in right side
            return l
        l = self.__getLevelOfNode(root.right, data, level + 1)
        return l
    
    def getLevelOfNode(self, data):
        return self.__getLevelOfNode(self.root, data, 1)   # Start at level 1
    
    def __printLeaves(self, root):
        if root is not None:
            if root.left is None and root.right is None:   # If both child nodes are none
                print(root.data, end=' ')
            self.__printLeaves(root.left)
            self.__printLeaves(root.right)
            
    def printLeaves(self):
        self.__printLeaves(self.root)
        print()
        return self
    
    def levelWiseSum(self):
        if self.root is None:
            return
        q = Queue()
        q.put(self.root)
        level = 0
        while True:
            count = q.qsize()
            if count == 0:
                break
            lsum = 0   # initialize lsum
            level += 1
            while count:
                node = q.get()
                lsum += node.data   # Add node value to lsum
                if node.left is not None:
                    q.put(node.left)
                if node.right is not None:
                    q.put(node.right)
                count -= 1
            print("Level-" + str(level) + " sum is " + str(lsum))
        return self
    
    def __recursiveSearch(self, root, data):
        if root is None:
            return False
        if root.data == data:   # If found return true
            return True
        # Do the same for both left and right side. If found any one will return True so use or gate
        return self.__recursiveSearch(root.left, data) or self.__recursiveSearch(root.right, data)
    
    def recursiveSearch(self, data):
        return self.__recursiveSearch(self.root, data)
    
    def spiralOrder(self):
        if self.root is None:
            print("Tree is empty")
        s1 = []   # Initialize two stacks
        s2 = []
        s1.append(self.root)
        while(len(s1) != 0  or len(s2) != 0):   # Until both are empty
            while(len(s1) != 0):   # Until s1 is empty
                node = s1.pop()
                print(node.data, end=' ')
                if node.right is not None:
                    s2.append(node.right)   # First append right as we are spiraling
                if node.left is not None:
                    s2.append(node.left)
            print()
            while(len(s2) != 0):   # Until s2 is empty
                node = s2.pop()
                print(node.data, end=' ')
                if node.left is not None:
                    s1.append(node.left)
                if node.right is not None:
                    s1.append(node.right)

    def printBetweenTwoLevels(self, a, b):
        if self.root == None:
            return
        q = Queue()
        q.put(self.root)
        level = 1   # To keep track of level
        while(True):
            count = q.qsize()
            if count == 0 or level > b:   # If level gets greater than max level break
                break
            while(count > 0):
                node = q.get()
                if a <= level and level <= b:   # Print only inbetween the levels
                    print(node.data, end=' ')
                if node.left is not None:
                    q.put(node.left)
                if node.right is not None:
                    q.put(node.right)
                count -=1
            level += 1   # Increment level
            print()

    def maxWidth(self):
        if self.root == None:
            return
        q = Queue()
        q.put(self.root)
        w = 0
        while(True):
            count = q.qsize()
            if count == 0:
                break
            if count > w:   # If count is greater than prev width update it
                w = count
            while(count > 0):
                node = q.get()
                if node.left is not None:
                    q.put(node.left)
                if node.right is not None:
                    q.put(node.right)
                count -= 1
        return w
    
    def __ifMirrorTree(self, root1, root2):
        if root1 is None and root2 is None:   # If both root is none return true
            return True
        if root1 is None or root2 is None:   # If any one is different return false
            return False
        return root1.data == root2.data and  self.__ifMirrorTree(root1.left, root2.right) and self.__ifMirrorTree(root1.right, root2.left)
    
    def ifMirrorTree(self, n1, n2):
        return self.__ifMirrorTree(n1.root, n2.root)
    
    def __ifMirrorStructureTree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return self.__ifMirrorStructureTree(root1.left, root2.right) and self.__ifMirrorStructureTree(root1.right, root2.left)
    
    def ifMirrorStructureTree(self, n1, n2):
        return self.__ifMirrorStructureTree(n1.root, n2.root)
    
    def __ifSameStructureTree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return self.__ifMirrorStructureTree(root1.left, root2.left) and self.__ifMirrorStructureTree(root1.right, root2.right)
    
    def ifSameStructureTree(self, n1, n2):
        return self.__ifMirrorStructureTree(n1.root, n2.root)
    
    def __ifSameTree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return root1.data == root2.data and self.__ifMirrorStructureTree(root1.left, root2.left) and self.__ifMirrorStructureTree(root1.right, root2.right)
    
    def ifSameTree(self, n1, n2):
        return self.__ifMirrorStructureTree(n1.root, n2.root)
    
    def isFoldable(self):
        node = self.root
        if node == None:
            return True
        # If foldable the left and right of root should be mirror structure
        return self.__ifMirrorStructureTree(node.left, node.right)

if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert([10,5,15,2,6,12,16])
    '''
                10
              /   \
            5       15
           / \     /   \ 
         2     6  12   16
    '''
    print("Inorder Traversal")
    bst.inorder()
    print(bst.search(5))
    print("Sum")
    print(bst.sum())
    print("Difference of Even and Odd Rows")
    print(bst.getDiffEvenOddRows())
    print("No of nodes")
    print(bst.noOfNodes())
    print("No of Leaf Nodes")
    print(bst.noOfLeafNodes())
    print("Height")
    print(bst.height())
    print("Level order traversal")
    bst.levelOrderTraversal()
    print("Print at given level")
    bst.printAtGivenLevel(2)
    print("Level order traversal in reverse")
    bst.reverseLevelOrderTraversal()
    print("Print level order travsesal line by line")
    bst.levelOrderTraversalLineByLine()
    print("Left side of tree")
    bst.leftSideOfTree()
    print("Right side of tree")
    bst.rightSideOfTree()
    print("Inorder using stack")
    bst.inorderUsingStack()
    print("Mirror Tree")
    bst.mirrorTree()
    bst.inorder()
    print("Empty or not")
    print(bst.empty())
    print("Are two binary search trees identical")
    bst2 = BinarySearchTree()
    bst2.insert([10,5,15,2,6,12,16])
    bst.mirrorTree()
    bst.inorder()
    bst2.inorder()
    print(bst.isIdentical(bst, bst2))
    print("Level of Node")
    print(bst.getLevelOfNode(4))
    print("Child Nodes")
    bst.printLeaves()
    print("level wise sum")
    bst.levelWiseSum()
    print("Recursive Search")
    print(bst.recursiveSearch(5))
    print("Spiral order")
    bst.spiralOrder()
    print("Values between two levels")
    bst.printBetweenTwoLevels(1,2)
    print("Max width")
    print(bst.maxWidth())
    print("Are two trees mirror structure without data")
    print(bst.ifMirrorStructureTree(bst, bst2))
    print("Are Two trees mirror with data")
    print(bst.ifMirrorTree(bst, bst2))
    print("Are Two trees same in structure without data")
    print(bst.ifSameStructureTree(bst, bst2))
    print("Are two trees same structure with data")
    print(bst.ifSameTree(bst, bst2))
    print("Is the tree foldable")
    print(bst.isFoldable())
    print("Delete entire tree")
    bst.delete()
    bst.inorder()
    '''
    Output
    Inorder Traversal
    2 5 6 10 12 15 16 
    True
    Sum
    66
    Difference of Even and Odd Rows
    26
    No of nodes
    7
    No of Leaf Nodes
    4
    Height
    2
    Level order traversal
    10 5 15 2 6 12 16 
    Print at given level
    5 15 
    Level order traversal in reverse
    16 12 6 2 15 5 10 
    Print level order travsesal line by line
    10 
    5 15 
    2 6 12 16 
    Left side of tree
    10 5 2 
    Right side of tree
    10 15 16 
    Inorder using stack
    2 5 6 10 12 15 16 
    Mirror Tree
    16 15 12 10 6 5 2 
    Empty or not
    False
    Are two binary search trees identical
    2 5 6 10 12 15 16 
    2 5 6 10 12 15 16 
    True
    Level of Node
    0
    Child Nodes
    2 6 12 16 
    level wise sum
    Level-1 sum is 10
    Level-2 sum is 20
    Level-3 sum is 36
    Recursive Search
    True
    Spiral order
    10 
    5 15 16 12 6 2 
    Values between two levels
    10 
    5 15 
    Max width
    4
    Are two trees mirror structure without data
    True
    Are Two trees mirror with data
    False
    Are Two trees same in structure without data
    True
    Are two trees same structure with data
    True
    Is the tree foldable
    True
    Delete entire tree
    Empty tree
    '''

