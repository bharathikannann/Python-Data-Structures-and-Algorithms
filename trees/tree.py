# ### Trees
# A tree is a widely used abstract data type that simulates a hierarchical tree structure, with a `root` value and subtrees of `children` with a `parent` node, represented as a set of linked nodes.
# 
# A tree data structure can be defined recursively as a collection of nodes (starting at a root node), where each node is a data structure consisting of a value, together with a list of references to nodes (the "children"), with the constraints that no reference is duplicated, and none points to the root.
# 
# Applications of trees:
# - Manipulate hierarchical data.
# - Make information easy to search (see tree traversal).
# - Manipulate sorted lists of data.
# - As a workflow for compositing digital images for visual effects.
# - Router algorithms
# - Form of a multi-stage decision-making (see business chess).
# 
# #### Binary Tree
# - A tree is called binary tree if each node of the tree has zero, one or two children.
# - Empty tree is also a valid binary tree.
# 
# #### Types of binary trees:
# 1. `Full binary tree`: A Binary Tree is full if every node has 0 or 2 children. Following are examples of full binary tree.
# 2. `Complete binary tree`: A Binary Tree is complete Binary Tree if all levels are completely filled except possibly the last level and the last level has all keys as left as possible.
# 3. `Perfect Binary Tree`: A Binary tree is Perfect Binary Tree in which all internal nodes have two children and all leaves are at same level.
# 4. `Balanced Binary Tree`: A binary tree is balanced if height of the tree is O(Log n) where n is number of nodes. For Example, AVL tree maintain O(Log n) height by making sure that the difference between heights of left and right subtrees is 1. Red-Black trees maintain O(Log n) height by making sure that the number of Black nodes on every root to leaf paths are same and there are no adjacent red nodes. Balanced Binary Search trees are performance wise good as they provide O(log n) time for search, insert and delete.
# 5. `A degenerate (or pathological) tree`: A Tree where every internal node has one child. Such trees are performance-wise same as linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
        
    def preorder(self, root):
        if(root):
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
        
    def inorder(self, root):
        if(root):
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
            
    def postorder(self, root):
        if(root):
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")

if __name__ == '__main__':
    tree = Tree()
    tree.root = Node(10)
    tree.root.left = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(8)
    tree.root.right = Node(15)
    '''
        Tree Structure
                10
              /    \
            5        15
           / \
         2     8
    '''
    print("Preorder")
    tree.preorder(tree.root)
    print("\nInorder")
    tree.inorder(tree.root)
    print("\nPostorder")
    tree.postorder(tree.root)
    '''
    Output
    Preorder
    10 5 2 8 15 
    Inorder
    2 5 8 10 15 
    Postorder
    2 8 5 15 10 
    '''

