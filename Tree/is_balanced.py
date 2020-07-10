# METHOD 1 - O(n^2)
class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def height(node):
    
    if node is None:
        return -1
    else:
        lt = height(node.left)
        rt = height(node.right)
    return 1+max(lt, rt)
    
def isBalanced(node): 
    
    if node is None: 
        return True
        
    ltree = height(node.left) 
    rtree = height(node.right) 
    
    if (abs(ltree - rtree) <= 1) and isBalanced( 
    node.left) is True and isBalanced(node.right) is True: 
        return True
    return False
 
# def insertLevelOrder(arr, root, i, n): 
 
#     if i < n: 
#         temp = Node(arr[i])  
#         root = temp  
#         root.left = insertLevelOrder(arr, root.left, 
#                                      2 * i + 1, n)  
#         root.right = insertLevelOrder(arr, root.right, 
#                                       2 * i + 2, n) 
#     return root             
            
            
# arr = list(map(int, input("Enter the numbers you want in tree:").split()))
# n = len(arr) 
# root = None
# root = insertLevelOrder(arr, root, 0, n)  
root = Node(1)
root.left = Node(2)
root.left.left = Node(2)
root.left.left.left = Node(2)
print(isBalanced(root))
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
# METHOD 2 - O(n)
class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def isBalanced(node): 
    
    if node is None: 
        return 0
        
    ltree = isBalanced(node.left) 
    if ltree == -1:
        return -1
    rtree = isBalanced(node.right)
    if rtree == -1:
        return -1
    
    if abs(ltree - rtree) > 1:
        return -1
    else:    
        return 1+max(ltree, rtree)
 
def insertLevelOrder(arr, root, i, n): 
 
    if i < n: 
        temp = Node(arr[i])  
        root = temp  
        root.left = insertLevelOrder(arr, root.left, 
                                     2 * i + 1, n)  
        root.right = insertLevelOrder(arr, root.right, 
                                      2 * i + 2, n) 
    return root             
            
            
arr = list(map(int, input("Enter the numbers you want in tree:").split()))
n = len(arr) 
root = None
root = insertLevelOrder(arr, root, 0, n)  
ans = isBalanced(root)
if ans !=-1:
    print("The tree is balanced and its height is:", ans)
else:
    print("The tree is not balanced")
# root = Node(1)
# root.left = Node(2)
# root.left.left = Node(2)
# root.left.left.left = Node(2)
