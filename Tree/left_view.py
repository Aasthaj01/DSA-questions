# Finding leftmost nodes in the tree

class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
    
    def leftView(self, node, height, maxlevel): 
      
        if node is None: 
            return

        if (maxlevel[0]< height): 
            print(node.value)
            maxlevel[0] = height 
      
        self.leftView(node.left, height + 1, maxlevel) 
        self.leftView(node.right, height + 1, maxlevel) 
  
  
    def left_tree(self, node): 
        maxlevel = [0]
        self.leftView(node, 1, maxlevel) 
  

b = BinaryTree(10)        
b.root.left = Node(20)
b.root.right = Node(30)
b.root.right.left = Node(40)
b.root.right.right = Node(50)

b.left_tree(b.root)         
        

