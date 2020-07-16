# Deleting a node from bst - there can be 3 cases i.e when node to be deleted has no child, 1 child, 2 children. This can be done by finding inorder successor

class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.parent = None
        
def minValueNode(root): 
    current = root 
    while(current.left is not None): 
        current = current.left  
  
    return current  
  
def deleteNode(root, node): 
  
    if root is None: 
        return root  
  
 
    if node < root.value: 
        root.left = deleteNode(root.left, node) 
  
    elif(node > root.value): 
        root.right = deleteNode(root.right, node) 
  
   
    else: 
        if root.left is None : 
            temp = root.right  
            root = None 
            return temp  
              
        elif root.right is None : 
            temp = root.left  
            root = None
            return temp 
 
        temp = minValueNode(root.right) 
  
        root.value = temp.value 
  
        root.right = deleteNode(root.right , temp.value) 
  
  
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

def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.value, end = " ") 
        inorder(root.right)
        
def insertLevelOrder(arr, root, i, n): 
    if i < n: 
        temp = Node(arr[i])  
        root = temp  
  
        root.left = insertLevelOrder(arr, root.left, 
                                     2 * i + 1, n)  

        root.right = insertLevelOrder(arr, root.right, 
                                      2 * i + 2, n) 
    return root             
            
            
arr = list(map(int, input("Enter nodes other than root node:").split()))
n = len(arr) 
a= int(input("Enter root node:"))
r = Node(a)
for i in range(0, n):
    insert(r, Node(arr[i]))
print(inorder(r))
t = int(input("Enter number of test cases:"))

for i in range(0, t):
    
    deln = int(input("Enter the number to be deleted:"))
    result = deleteNode(r, deln)
  
    print("The tree traversal after deletion of node is:")
    print(inorder(result))
