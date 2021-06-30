# Red Black Trees
# The AVL trees are more balanced compared to Red-Black Trees,
# but they may cause more rotations during insertion and deletion. 
# So if your application involves frequent insertions and deletions, 
# then Red-Black trees should be preferred.
# Refer AVL Tree implementation to understand how rotation works
# ------------------------------------------------------------------------
# Rules of Red Black Trees
# 1) Every node has a colour either red or black.
# 2) The root of the tree is always black.
# 3) There are no two adjacent red nodes (A red node cannot have a red parent or red child).
# 4) Every path from a node (including root) to any of its descendants NULL nodes has the same number of black nodes.

from queue import Queue
# Red-Black Tree Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.colour = 'R'   # Default the new node colou
        self.parent = None  # Parent of the node, useful for rotations
 
class RedBlackTree:
    def __init__(self):
        self.root = None
        self.ll = False   # Left Rotate
        self.rr = False   # Right Rotate
        self.lr = False   # Left Right Rotate
        self.rl = False   # Right Left Rotate
    
    # Left Rotation
    '''
              z(root)                                       y (temp)
             /  \                                       /      \
            T1   y(temp)       Left Rotate(z)       z (root)      x
                /  \           - - - - - - - ->    / \            / \
       (t_left)T2   x                             T1  T2(t_left) T3 T4
                   / \                                
                 T3  T4
    '''
    def rotate_left(self, root):
        temp = root.right
        t_left = temp.left
        temp.left = root
        root.right = t_left
        root.parent = temp
        if t_left is not None:   # None doesn't have parent property, so check it
            t_left.parent = root
        return temp              # Return temp, which is the root now              
    
    # Right Rotation
    '''
                 z                                      y 
                / \                                   /   \
               y   T4      Right Rotate (z)          x      z
              / \          - - - - - - - - ->      /  \    /  \ 
             x   T3                               T1  T2  T3  T4
            / \
          T1   T2               
    '''
    def rotate_right(self, root):
        temp = root.left
        t_right = temp.right
        temp.right = root
        root.left = t_right
        root.parent = temp
        if t_right is not None:   # None doesn't have parent property, so check it
            t_right.parent = root   
        return temp               # Return temp, which is the root now
    
    # Insert helper function
    def __insert(self, root, data):
        f = False   # Keep track of two adjacent red nodes
        if root is None:
            return Node(data)
        elif data < root.data:
            root.left = self.__insert(root.left, data)
            root.left.parent = root
            if root != self.root:   # Check for two adjacent red nodes
                if root.colour == 'R' and root.left.colour == 'R':
                    f = True
        else:
            root.right = self.__insert(root.right, data)
            root.right.parent = root
            if root != self.root:   # Check for two adjacent red nodes
                if root.colour == 'R' and root.right.colour == 'R':
                    f = True
        
        # Left rotate
        if self.ll:
            root = self.rotate_left(root)
            root.colour = 'B'            # Always change root color to black, because it will come to the top in all case
            root.left.colour = 'R'       # Change left of root to red
            self.ll = False              # Since it has done, make it as false
        
        if self.rr:
            root = self.rotate_right(root)
            root.colour = 'B'
            root.right.colour = 'R'
            self.rr = False
        
        # First do right rotation for right child of root and then do left rotation for root
        if self.rl:
            root.right = self.rotate_right(root.right)
            root.right.parent = root      # Update root.right's parent since it is changed
            root = self.rotate_left(root) 
            root.colour = 'B'
            root.left.colour = 'R'
            self.rl == False
        
        # First do left rotation for left child of root and do right rotation for root
        if self.lr:
            root.left = self.rotate_left(root.left)
            root = self.rotate_right(root)
            root.left.parent = root
            root.colour = 'B'
            root.right.colour = 'R'
            self.lr = False
        
        # If law is broken (Two adjacent red nodes)
        # Here rotations are not done right in this traversal, 
        # we need to move to its parent node to perform rotations for the current node
        # So we update ll, rr, rl, rl for remembering rotations and we traverse up for doing rotations
        if f:
            if root.parent.right == root:   # Check if we are right side
                # Check if uncle of root is none or black
                if root.parent.left == None or root.parent.left.colour == 'B':
                    # Check if left node exists and have red color
                    if root.left is not None and root.left.colour == 'R':        
                        self.rl = True   # Do right rotation                                        
                    elif root.right is not None and root.right.colour == 'R':
                        self.ll = True   # Do left rotation
                else:   # If uncle is red
                    root.parent.left.colour = 'B'   # Change left of parent and root to black
                    root.colour = 'B'
                    if root.parent is not self.root:   # If parent is not top root change it to red, since top root cannot be red
                        root.parent.colour = 'R'
            else:   # If we are in left side, do as same we did before
                if root.parent.right == None or root.parent.right.colour == 'B':
                    if root.left is not None and root.left.colour == 'R':
                        self.rr = True
                    elif root.right is not None and root.right.colour == 'R':
                        self.lr = True
                else:
                    root.parent.right.colour = 'B'
                    root.colour = 'B'
                    if root.parent is not self.root:
                        root.parent.colour = 'R'
            f = False   # Make f false, since we did all operations for current traversal
        return root
    
    def insert(self, data):
        if self.root == None: 
            self.root = Node(data)
            self.root.colour = 'B'   # Root is always black
        else:  
            self.root = self.__insert(self.root, data)
    
    # For testing
    def level_order_traversal(self):
        if self.root is None:
            return
        q = Queue()
        q.put(self.root)
        while(not q.empty()):
            count = q.qsize()
            while(count > 0):
                node = q.get()
                print(node.data, end=" ")
                if node.left is not None:
                    q.put(node.left)
                if node.right is not None:
                    q.put(node.right)
                count -= 1
            print()
            
    def __preorder(self, root):
        if root:
            print(root.data, end=' ')
            self.__preorder(root.left)
            self.__preorder(root.right)
    
    def preorder(self):
        return self.__preorder(self.root)

if __name__ == "__main__":
    rbt = RedBlackTree()
    a = [10,20,30,40,50,60]
    for i in a:
        rbt.insert(i)
    print("Level Order Traversal") 
    rbt.level_order_traversal()
    print("Pre order")
    rbt.preorder()    
    '''
    Output
    Level Order Traversal
    20 
    10 40 
    30 50 
    60 
    Pre order
    20 10 40 30 50 60 
    '''