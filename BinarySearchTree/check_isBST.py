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

    
#==========================================================================================================

class Node:  
    def __init__(self, value):  
        self.value = value
        self.left = None
        self.right = None
  
def isBST(root, l = None, r = None):  
    if (root == None) : 
        return True
  
    if (l != None and root.value <= l.value) : 
        return False
 
    if (r != None and root.value >= r.value) : 
        return False
  
    
    return (isBST(root.left, l, root) and 
        isBST(root.right, root, r))  
  
def level_order(arr, node, i, n):
    if i<n:
        temp  = Node(arr[i])
        node = temp
        node.left = level_order(arr, node.left, 2*i+1, n)
        node.right = level_order(arr, node.right, 2*i+2, n)
    return node
    
    
arr = list(map(int, input("Enter tree nodes:").split()))
n = len(arr)
root = None
root = level_order(arr, root, 0, n)
if (isBST(root,None,None)): 
    print("Is BST") 
else: 
    print("Not a BST") 
#=======================================================================================================
import sys

class Node(object):
    def __init__(self, val):
        self.right = None
        self.left = None
        self.val = val
        
def is_bst(root, prev):
    if root is None:
        return True
    if is_bst(root.left, prev) == False:
        return False
    if root.val<= prev:
        return False
    prev = root.val    
    return is_bst(root.right, prev)
    
def level_order_insert(arr, root, i, n):
    if i<n:
        temp = Node(arr[i])
        root = temp 
        root.left = level_order_insert(arr, root.left, 2*i+1, n)
        root.right = level_order_insert(arr, root.right, 2*i+2, n)
    return root


arr = list(map(int, input().split()))
n = len(arr)
root = None
root = level_order_insert(arr, root, 0, n)    
max_int = sys.maxsize    
prev = -max_int  


if is_bst(root, prev) == True:
    print("Tree is bst")
else:
    print("No, tree is not a bst")

