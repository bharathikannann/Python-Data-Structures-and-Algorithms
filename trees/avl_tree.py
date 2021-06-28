from queue import Queue
# AVL Tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.height = 0   # Keeps track of height for each node
        self.left = None
        self.right = None
        
class AVLTree:
    # Threshold is commonly set to 1 by default
    def __init__(self, threshold = 1):
        self.root = None
        self.threshold = threshold
    
    def insert(self, items):
        if not items:   # If empty
            return None
        for i in range(len(items)):   # Add each element
            self.root = self.__insert(self.root, items[i], self.threshold)
    
    def __insert(self, root, data, threshold):
        if not root:
            return Node(data)
        elif data < root.data:
            root.left = self.__insert(root.left, data, threshold)
        else:
            root.right = self.__insert(root.right, data, threshold)
        
        # Get the height for root
        # H(r) = 1 + max(h[r.left], h[r.right])
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        
        # Get balance
        # For AVL trees, -1 <= balance <= 1 
        balance = self.get_balance(root)
        
        # If balance is greater than 1, then left side is heavy so we must rotate right
        if balance > threshold:
            if self.get_balance(root.left) >= 0:     # Node left correctly balanced
                root = self.rotate_right(root)
            else:
                root = self.rotate_left_right(root)  # For node left right heavy
        # If balance is less than 1, right side is heavy
        elif balance < -threshold:
            if self.get_balance(root.right) <= 0:
                root = self.rotate_left(root)
            else:
                root = self.rotate_right_left(root)   # For node right left heavy
    
        return root
    
    # Rotate right for left-heavy rebalance
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
        left_temp = root.left         # Keep track of left node
        root.left = left_temp.right   # Change node left
        left_temp.right = root        # Update left_temp right, now left_temp comes to root position
        
        # Update heights of rotated nodes
        # Order of updating height is important, height value comes form bottom root
        # If root is changes and comes below left_temp first root should be updated
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        left_temp.height = 1 + max(self.get_height(left_temp.left), self.get_height(left_temp.right))
        
        return left_temp
    
    # Rotate left for rigt-heavy rebalance
    '''
      z                                y
     /  \                            /   \ 
    T1   y     Left Rotate(z)       z      x
        /  \   - - - - - - - ->    / \    / \
       T2   x                     T1  T2 T3  T4
           / \
         T3  T4
    '''
    def rotate_left(self, root):
        right_temp = root.right
        root.right = right_temp.left
        right_temp.left = root
        
        # Update heights of rotated nodes
        # Order of updating height is important, height value comes form bottom root
        # If root is changes and comes below right_temp first root should be updated
        root.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        right_temp.height = 1 + max(self.get_height(right_temp.left), self.get_height(right_temp.right))
        
        return right_temp
    
    # For right node left heavy rebalance
    '''
         z                               z                           x
        / \                            /   \                        /  \ 
       y   T4  Left Rotate (y)        x    T4  Right Rotate(z)    y      z
      / \      - - - - - - - - ->    /  \      - - - - - - - ->  / \    / \
    T1   x                          y    T3                    T1  T2 T3  T4
        / \                        / \
      T2   T3                    T1   T2
    '''
    def rotate_left_right(self, root):
        root.left = self.rotate_left(root.left)
        return self.rotate_right(root)
    
    # For left node right heavy rebalance
    '''
       z                            z                            x
      / \                          / \                          /  \ 
    T1   y   Right Rotate (y)    T1   x      Left Rotate(z)   z      y
        / \  - - - - - - - - ->     /  \   - - - - - - - ->  / \    / \
       x   T4                      T2   y                  T1  T2  T3  T4
      / \                              /  \
    T2   T3                           T3   T4
    '''
    def rotate_right_left(self, root):
        root.right = self.rotate_right(root.right)
        return self.rotate_left(root)
        
    def get_height(self, root):
        if not root:
            return -1
        return root.height
    
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
    
    def preorder(self):
        self.__preorder(self.root)
        print()
    
    def __preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.__preorder(root.left)
            self.__preorder(root.right)
            
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

if __name__ == "__main__":
    avl = AVLTree()
    avl.insert([5,4,3,2,1])
    avl.preorder()
    avl.level_order_traversal()
    '''
    Output
    Preorder -> 4 2 1 3 5 
    Level Order Traversal -> 4 
                             2 5 
                             1 3 
    '''

#Comparison with tree
class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, items):
        if not items:
            return None
        for i in range(len(items)):
            self.root = self.__insert(self.root, items[i])
        
    def __insert(self, root, data):
        if not root:
            return Node(data)
        elif data < root.data:
            root.left = self.__insert(root.left, data)
        else:
            root.right = self.__insert(root.right, data)
        return root
        
        
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

if __name__ == "__main__":
    tree = Tree()
    tree.insert([5,4,3,2,1])
    tree.level_order_traversal()
    '''
    Output
    5 
    4 
    3 
    2 
    1 
    '''

