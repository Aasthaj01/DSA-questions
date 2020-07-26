# Find kth smallest element in bst

class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
    
        
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



def kthSmallest(root, k):
    def inorder(curr, arr): 
        if not curr:
            return
        inorder(curr.left, arr) 
        arr.append(curr.value) 
        inorder(curr.right, arr)
    arr = []
    inorder(root, arr)
    return arr[k-1]
    
    
arr = list(map(int, input("Enter nodes other than root node:").split()))
n = len(arr) 
a= int(input("Enter root node:"))
r = Node(a)
for i in range(0, n):
    insert(r, Node(arr[i]))
k = int(input("Enter the element to be searched:")) 
print(kthSmallest(r, k))
  

        

       
