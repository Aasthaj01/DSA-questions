# Start level order traversal by first traversing leaf nodes and then root

class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None 
        
def level_insert(arr, root, i, n):
    if i < n: 
        temp = Node(arr[i])  
        root = temp  
  
        root.left = insertLevelOrder(arr, root.left, 
                                     2 * i + 1, n)  

        root.right = insertLevelOrder(arr, root.right, 
                                      2 * i + 2, n) 
    return root   
    
def insert(root, node):
    if root is None: 
        root = node 
    else: 
        if root.value < node.value: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node)

def printLevelOrder(node):
      arr = []
      h = height(node) 
      for i in reversed(range(1, h+1)): 
          printGivenLevel(node, i, arr) 
      return arr
       
def height(node): 
    if node is None: 
        return 0 
    lheight = height(node.left) 
    rheight = height(node.right) 
    return 1+max(lheight, rheight)
    
def printGivenLevel(node , level, arr): 
    
    if node is None: 
        return
    if level == 1: 
        arr.append(node.value) 
    elif level > 1 : 
        printGivenLevel(node.left , level-1, arr) 
        printGivenLevel(node.right , level-1, arr)
        
        
arr = list(map(int, input("Enter nodes other than root node:").split()))
n = len(arr) 
a= int(input("Enter root node:"))
r = Node(a)
for i in range(0, n):
    insert(r, Node(arr[i]))   
ans = printLevelOrder(r)
print(ans)
