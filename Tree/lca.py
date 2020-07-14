# lca is lowest common ancestor 
# i.e if 2 nodes haves 2 common ancestors then the function will return that common ancestor which is on lower level than other.
# There can be 2 methods for the same: O(n) solution where tree is traversed 3 times and n+extra space time complexity
# Other approach is traversing tree once and looking for the node that is common for the input nodes  If root doesn’t match with any of the keys, we recur for left and right subtree. The node which has one key present in its left subtree and the other key present in right subtree is the LCA. If both keys lie in left subtree, then left subtree has LCA also, otherwise LCA lies in right subtree- O(h) time complexity solution

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def lowest_common_ancestor(node, n1, n2):
    if node is None:
        return   
    if node.value == n1 or node.value == n2:
        return node.value
    left_lca = lowest_common_ancestor(node.left, n1, n2)   
    right_lca =lowest_common_ancestor(node.right, n1, n2)
    
    if left_lca and right_lca:
        return node.value
    if left_lca is not None:
        return left_lca
    else:
        return right_lca
   
def construct_tree(arr, node, i, n):
    if i<n:
        temp = Node(arr[i])
        node = temp
        node.left = construct_tree(arr, node.left, 2*i+1, n)
        node.right = construct_tree(arr, node.right, 2*i+2, n)
    return node 
    


arr = list(map(int, input("Enter the nodes:").split()))
n = len(arr)
root = None
root = construct_tree(arr, root, 0, n)

t = int(input("Enter number of test cases:"))
arr = []
for i in range(0, t):
    n1, n2 = list(map(int, input().split()))
    ans = lowest_common_ancestor(root, n1, n2)
    arr.append(ans)

print(arr)
# -----------------------------------------------------------------------------------
# Method 2 - Naive solution

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findPath(node, path, k): 
  
    if node is None: 
        return False
 
    path.append(node.value) 
  
    if node.value == k : 
        return True
  
    if ((node.left != None and findPath(node.left, path, k)) or
            (rnode.right!= None and findPath(node.right, path, k))): 
        return True 
  
    path.pop() 
    return False
  
def findLCA(node, n1, n2): 
  
    path1 = [] 
    path2 = [] 
  
 
    if not findPath(node, path1, n1) or not findPath(node, path2, n2)): 
        return -1 
    i = 0 
    while(i < len(path1) and i < len(path2)): 
        if path1[i] != path2[i]: 
            break
        i += 1
    return path1[i-1]
    
def construct_tree(arr, node, i, n):
    if i<n:
        temp = Node(arr[i])
        node = temp
        node.left = construct_tree(arr, node.left, 2*i+1, n)
        node.right = construct_tree(arr, node.right, 2*i+2, n)
    return node 
    

arr = list(map(int, input("Enter the nodes:").split()))
n = len(arr)
root = None
root = construct_tree(arr, root, 0, n)

t = int(input("Enter number of test cases:"))
arr = []
for i in range(0, t):
    n1, n2 = list(map(int, input().split()))
    ans = findLCA(root,n1, n2)
    arr.append(ans)

print(arr)


               
