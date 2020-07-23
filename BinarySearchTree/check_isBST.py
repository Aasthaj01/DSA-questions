#  check if tree is bst

class Node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
      

    
def isBST(root):
    return checkBST(root, -10001, 10001)

def checkBST(root, Min, Max):
    if not root:
        return True
    if root.data <= Min or root.data >= Max:
        return False
    return checkBST(root.left, Min, root.data) and checkBST(root.right, root.data, Max)
    
    
root = Node(4) 
root.left = Node(2) 
root.right = Node(5) 
root.left.left = Node(1) 
root.left.right = Node(3) 
  
if (isBST(root)): 
    print ("Given tree is BST")
else: 
    print("Not a BST")
    
