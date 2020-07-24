class Node(object):
    def __init__(self, value):
        self.left = None
        self.right =None
        self.value = value
               
def height(node):
    if node is None:
        return -1
    else:
        ltree = height(node.left)
        rtree = height(node.right)
        return 1+max(ltree, rtree)  
        
def swap(root, k) :
    swap_nodes(root, 1, k)
    
def swap_nodes(root, level, k):
    if (root is None or (root.left is None and root.right is None)):
        return
    else:
        if ((level+1)%k) == 0:
            root.left, root.right = root.right, root.left
        swap_nodes(root.left, level+1, k)
        swap_nodes(root.right, level+1, k)
        
        
def insert_bst(root, node):
    if root is None:
        root = node
    else:
        if root.value<node.value:
            if root.right is None:
                root.right = node
            else:
                insert_bst(root.right, node)
        if root.value>node.value:
            if root.left is None:
                root.left = node
            else:
                insert_bst(root.left, node)        
    
def level_order_insert(arr, root, i, n):
    if i<n:
        temp = Node(arr[i])
        root = temp 
        root.left = level_order_insert(arr, root.left, 2*i+1, n)
        root.right = level_order_insert(arr, root.right, 2*i+2, n)
    return root
    
def inorder(node):
    if node is None:
        return -1
    inorder(node.left)
    print(node.value, end = " ")
    inorder(node.right)
    
    
arr = list(map(int, input("Insert array elements:").split()))   
n = len(arr)
root = Node(int(input("Enter root node:")))
k = int(input("Enter the level at which you want to swap nodes:"))

for i in range(n):
    insert_bst(root, Node(arr[i]))
inorder(root)

swap(root, k)
print("\ninorder traversal of tree after swapping is:")
inorder(root)
print("\nheight of tree is:")
print(height(root))
