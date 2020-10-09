# Let T and S be two trees, find if S is a subtree of T or not. If yes, find the number of nodes of tree S.

class Node:  
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
  
 
def areIdentical(root1, root2): 
       
    if root1 is None and root2 is None: 
        return True
    if root1 is None or root2 is None: 
        return False
  
    return (root1.data == root2.data and 
            areIdentical(root1.left , root2.left)and
            areIdentical(root1.right, root2.right) 
            )  
 
def isSubtree(T, S): 
    
    if S is None: 
        return True
  
    if T is None: 
        return False
    if (areIdentical(T, S)): 
        return True
  
    return isSubtree(T.left, S) or isSubtree(T.right, S) 

def tree_size(node):
    if node is None:
            return 0
    else:
        ltree = tree_size(node.left)
        rtree = tree_size(node.right)
    return 1+(ltree+rtree) 


T = Node(26) 
T.right = Node(3) 
T.right.right  = Node(3) 
T.left = Node(10) 
T.left.left = Node(4) 
T.left.left.right = Node(30) 
T.left.right = Node(6)
S = Node(10) 
S.right = Node(6) 
S.left = Node(4) 
S.left.right = Node(30) 
  
if isSubtree(T, S): 
    print(tree_size(S))
else : 
    print("0")
