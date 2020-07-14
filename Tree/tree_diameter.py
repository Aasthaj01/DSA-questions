# finding diameter of binary tree, maximum number of nodes between 2 leaf nodes is considered as diameter

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def diameter(node):
    if node is None:
        return 0
        
    else:
        d1 = 1+height(node.left)+height(node.right)
        d2 = diameter(node.left)
        d3 = diameter(node.right)
        return max(d1, max(d2, d3))
        
def height(node) :   
    if node is None:
        return 0
    else:
        ltree = height(node.left)
        rtree = height(node.right)
        return 1+ max(ltree, rtree)
        
def height_opt(node, res): 
    if (node == None): 
        return 0
  
    ltree = height_opt(node.left, res)  
  
    rtree = height_opt(node.right, res)  
  
    res[0] = max(res[0], 1 + ltree + 
                             rtree)  
  
    return 1 + max(ltree, rtree) 
  
def diameter_opt(node): 
    if (node == None):  
        return 0
    res = [-999999999999]   
    height_of_tree = height_opt(node, res)  
    return res[0]   
             

root = Node(1)
root.left = Node(2)
root.right = Node(5)
root.right.right = Node(6)
root.right.left = Node(7)
root.right.left.left = Node(10)
root.right.right.right = Node(20)

print("Diameter of the tree is:")
print(diameter(root))

print("Diameter from optimized sol with O(n) time complexity is:")
print(diameter_opt(root))

               
