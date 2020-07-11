# depth first search tree traversals - inorder, preorder, postorder
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
        else:
            print("traversal type"+ " " +str(traversal_type)+" "+"is not supported")
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
        
        
b = Binarytree(1)        
b.root.left = Node(2)
b.root.right = Node(3)
b.root.left.left = Node(10)
b.root.right.left = Node(20)
print(b.print_tree("Preorder"))
print(b.print_tree("Inorder"))
print(b.print_tree("postorder"))
#-------------------------------------------------------------------------------------------------------------------------

class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    
def pre_order(node):
    if node is None:
        return 
    # root, left, right
    print(node.value, end = " ")
    pre_order(node.left)
    pre_order(node.right)
    
def post_order(node):
    if node is None:
        return 
    # left, right, root
    pre_order(node.left)
    pre_order(node.right) 
    print(node.value, end = " ")
    
def in_order(node):
    if node is None:
        return 
    # left, root, right
    pre_order(node.left)
    print(node.value, end = " ")
    pre_order(node.right) 
    
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
    
# def level(arr, node, i, n):
#     if i <n:
#         temp = Node(arr[i])
#         node = temp
         
#         node.left = level(arr, node.left, 2*i+1, n)
#         node.right = level(arr, node.right, 2*i+2, n)
#     return root    
        
# arr = list(map(int, input().split())) 
# n = len(arr)
# root = None
# root = level(arr, root, 0, n)

root = Node(1)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(2)
root.left.right =Node(5)
root.left.left.left = Node(2)
print("preorder traversal of tree is:") 
pre_order(root)
print("\npost order traversal of tree is:")
post_order(root)
print("\ninorder traversal of tree is:")
in_order(root)



