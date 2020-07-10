# Checks if sum of both child nodes is equal to root node, if yes then returns true

class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
def children_sum(node):
    if node is None:
        return True
    elif node.right is None or node.left is None:
        return True
    else:
        s = 0
        if node.left is not None:
            s+= node.left.value
        if node.right is not None:
            s+= node.right.value
        return s==node.value and children_sum(node.left) and children_sum(node.right)
        
def insertLevelOrder(arr, root, i, n): 
 
    if i < n: 
        temp = Node(arr[i])  
        root = temp  
  
        root.left = insertLevelOrder(arr, root.left, 
                                     2 * i + 1, n)  

        root.right = insertLevelOrder(arr, root.right, 
                                      2 * i + 2, n) 
    return root             
            
            
arr = list(map(int, input().split()))
n = len(arr) 
root = None
root = insertLevelOrder(arr, root, 0, n)  
       
print(children_sum(root))
