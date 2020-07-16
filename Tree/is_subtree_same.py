#Given two binary trees, check if the first tree is subtree of the second one. Tree with root 1 is the one with other tree is to be compared. 
# O(nm) complexity


class Node(object):
    def __init__(self, val):
        self.left = None
        self.right =None
        self.val = val
        
def IsTreeSame(root1, root2):

    if root1 is None and root2 is None: 
        return True
    if root1 is None or root2 is None: 
        return False
  
    
    return (root1.val == root2.val and 
            IsTreeSame(root1.left , root2.left)and
            IsTreeSame(root1.right, root2.right) 
            )  
    
def subtree(t1, t2):
  
    if t2 is None: 
        return True
    if t1 is None: 
        return False
    if (IsTreeSame(t1, t2)): 
        return True
    return subtree(t1.left, t2) or subtree(t1.right, t2) 
  
     
    


root1 = Node(50) 
root1.right = Node(55) 
root1.right.right  = Node(60) 
root1.left = Node(10) 
root1.left.left = Node(4) 
root1.left.left.right = Node(30) 
root1.left.right = Node(6) 
  

root2 = Node(10) 
root2.right = Node(6) 
root2.left = Node(4) 
root2.left.right = Node(30) 
  
print(subtree(root1, root2)) 

