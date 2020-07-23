#  create a binary search tree from given data

class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
# def bst_search(node, num):
#     if node is None:
#         return False

#     if num == node.value:
#         return True
#     if num <node.value:
#         return bst_search(node.left, num)
#     else:    
#         return bst_search(node.right, num) 
        
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
        
# def insertLevelOrder(arr, root, i, n): 
#     if i < n: 
#         temp = Node(arr[i])  
#         root = temp  
  
#         root.left = insertLevelOrder(arr, root.left, 
#                                      2 * i + 1, n)  

#         root.right = insertLevelOrder(arr, root.right, 
#                                       2 * i + 2, n) 
#     return root             
            
            
arr = list(map(int, input("Enter nodes other than root node:").split()))
n = len(arr) 
a= int(input("Enter root node:"))
r = Node(a)
for i in range(0, n):
    insert(r, Node(arr[i]))
inorder(r)   

# num = int(input("Enter the number to be searched:"))
# print(bst_search(r, num))
#=============================================================================================================================
class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
def insert(node, key):
    
    if node is None: 
        return Node(key)
    if key < node.value: 
        node.left = insert(node.left, key) 
    else: 
        node.right = insert(node.right, key) 
    return node

def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.value, end = " ") 
        inorder(root.right)

arr = list(map(int, input("Enter nodes other than root node:").split()))
n = len(arr) 
a= int(input("Enter root node:"))
r = Node(a)
for i in range(0, n):
    insert(r, arr[i])
inorder(r)   

#=============================================================================================================================
#Iterative approach where space complexity is o(1)
#  create a binary search tree from given data
class newNode:  
    
    def __init__(self, data):  
        self.key= data  
        self.left = None
        self.right = self.parent = None

def insert(root, key): 
  
    newnode = newNode(key)  
  
    x = root  
    # Pointer y maintains the trailing  
    # pointer of x  
    y = None
  
    while (x != None): 
        y = x  
        if (key < x.key): 
            x = x.left  
        else: 
            x = x.right  
      
    # If the root is None i.e the tree is  
    # empty. The new node is the root node  
    if (y == None): 
        y = newnode  
  
    # If the new key is less then the leaf node key  
    # Assign the new node to be its left child  
    elif (key < y.key): 
        y.left = newnode  
  
    # else assign the new node its  
    # right child  
    else: 
        y.right = newnode  
  
    # Returns the pointer where the  
    # new node is inserted  
    return y  
  
def Inorder(root) : 
  
    if (root == None) : 
        return
    else:  
        Inorder(root.left)  
        print( root.key, end = " " ) 
        Inorder(root.right) 
 
    """  
         50  
          / \  
        30   70  
        / \  / \  
       20 40 60 80 """
root = None
root = insert(root, 50)  
insert(root, 30)  
insert(root, 20)  
insert(root, 40)  
insert(root, 70)  
insert(root, 60)  
insert(root, 80)  
Inorder(root)
#==================================================================================================================
class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):
        if self.root == None:
            self.root = Node(val)

        root = self.root
        while True:
            if val > root.info:
                if root.right:
                    root = root.right
                else:
                    root.right = Node(val)
                    break
            elif val < root.info:
                if root.left:
                    root = root.left
                else:
                    root.left = Node(val)
                    break
            else:
                break

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
