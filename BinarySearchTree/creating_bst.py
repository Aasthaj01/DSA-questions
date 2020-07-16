#  create a binary search tree from given data and searching a particular input node

class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
def bst_search(node, num):
    if node is None:
        return False

    if num == node.value:
        return True
    if num <node.value:
        return bst_search(node.left, num)
    else:    
        return bst_search(node.right, num) 
        
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
            
            
arr = list(map(int, input().split()))
n = len(arr) 
a= int(input("Enter nodes other than root node:"))
r = Node(a)
for i in range(0, n):
    insert(r, Node(arr[i]))
print(inorder(r))   

num = int(input("Enter the number to be searched:"))
print(bst_search(r, num))
