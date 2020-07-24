class Queue(object):
    def __init__(self):
        self.items = []
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    def enqueue(self, item):
        self.items.insert(0, item)
    def is_empty(self):
        return len(self.items)==0
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
    def __len__(self):
        return self.size()
    def size(self):
        return len(self.items)
        
        
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class Binarytree(object):
    def __init__(self, root):
        self.root = Node(root)
    
    def print_tree(self, traversal_type):
        if traversal_type == "preorder" or traversal_type =="Preorder":
            return self.pre_order(b.root, " ")
        elif traversal_type == "Inorder" or  traversal_type == "inorder":
            return self.in_order(b.root, " ")
        elif traversal_type == "Postorder" or  traversal_type == "postorder":
            return self.in_order(b.root, " ")
        elif traversal_type == "levelorder" or traversal_type == "Level order" or traversal_type == "bst":
            return self.level_order(b.root)    
        else:
            print("traversal type"+ "- " +str(traversal_type)+" "+"is not supported")
            return False
    
    def in_order(self, start, traversal):
        if start:
            traversal = self.in_order(start.left, traversal)
            traversal +=(str(start.value) + "-->")
            traversal = self.in_order(start.right, traversal)
        return traversal    
            
    def pre_order(self,start, traversal):
        if start:
            traversal+= (str(start.value) + "-->")
            traversal = self.pre_order(start.left, traversal)
            traversal = self.pre_order(start.right, traversal)
        return traversal
        
    def post_order(self,start, traversal):
        if start:
            traversal = self.pre_order(start.left, traversal)
            traversal = self.pre_order(start.right, traversal)
            traversal+= (str(start.value) + "-->")
        return traversal 
        
    def level_order(self, start):
        if start is None:
            return 
        queue =Queue()
        queue.enqueue(start)
        traversal = ""
        while len(queue)>0:
            traversal+= str(queue.peek())+ "-->"
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right) 
        return traversal        
        
        
b = Binarytree(1)        
b.root.left = Node(2)
b.root.right = Node(3)
b.root.left.left = Node(10)
b.root.right.left = Node(20)
print(b.print_tree("Preorder"))
print(b.print_tree("Inorder"))
print(b.print_tree("postorder"))
print(b.print_tree("levelorder"))
#---------------------------------------------------------------------------------------------------------------------------------------------

class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
def printLevelOrder(node): 
    h = height(node) 
    for i in range(1, h+1): 
        printGivenLevel(node, i) 

def printGivenLevel(node , level): 
    if node is None: 
        return
    if level == 1: 
        print(node.value,end=" ") 
    elif level > 1 : 
        printGivenLevel(node.left , level-1) 
        printGivenLevel(node.right , level-1) 
  
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
def level_order(node):
    if node is None: 
        return
    queue = [] 
    queue.append(node)
    while(len(queue) > 0): 
        
        print (queue[0].value) 
        node = queue.pop(0) 
 
        if node.left is not None: 
            queue.append(node.left)
        if node.right is not None: 
            queue.append(node.right)
  
    
def height(node): 
    if node is None: 
        return 0 
    lheight = height(node.left) 
    rheight = height(node.right) 
    return 1+max(lheight, rheight)


root = Node(1)
root.left = Node(2)
root.left.left = Node(2)
root.left.left.left = Node(2)
ans = isBalanced(root)
if ans !=-1:
    print("The tree is balanced and its height is:", ans)
else:
    print("The tree is not balanced")
# method 2 - recursive 
print(level_order(root)) 
# method 3 - variation of method 1
printLevelOrder(root)
#==============================================================================================
#O(n)
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:        
    def levelOrder(self, root) :
        ans = []
        def traversal(level, node):
            if node is not None:
                if len(ans) <= level:
                    ans.append([node.val])
                else:
                    ans[level].append(node.val)

                traversal(level+1, node.left)
                traversal(level+1, node.right)

        traversal(0, root)

        return ans
    
  def level_order_insert(arr, root, i, n):
    if i<n:
        temp = Node(arr[i])
        root = temp 
        root.left = level_order_insert(arr, root.left, 2*i+1, n)
        root.right = level_order_insert(arr, root.right, 2*i+2, n)
    return root

s= Solution()
arr = list(map(int, input().split()))
n = len(arr)
root = None
root = level_order_insert(arr, root, 0, n)
print(s.levelOrder(root))
