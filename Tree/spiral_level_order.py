# Using 2 stacks, we can print level order in spiral form.
# s1 stores right node first and then left of odd levels(if top level is 1)
# s2 stores left and then right child so that when item is popped, it gets printed in reverse order of original level
# O(n) time 
# method for spiral order traversal 


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def spiral_traversal_left(node):
    if node is None:
        return
    s1 = []
    s2 = []
    s1.append(node)
    while not len(s1) == 0 or  not len(s2) == 0:
        while not len(s1) == 0:
            temp = s1[-1]
            s1.pop()
            print(temp.value, end = " ")
            
            if temp.right:
                s2.append(temp.right)
            if temp.left:    
                s2.append(temp.left)
                
        while not len(s2) == 0:
            temp = s2[-1]
            s2.pop()
            print(temp.value, end = " ")
            
            if temp.left:    
                s1.append(temp.left)
            if temp.right:
                s1.append(temp.right)
                
def spiral_traversal_right(node):
    if node is None:
        return
    s1 = []
    s2 = []
    s1.append(node)
    while not len(s1) == 0 or  not len(s2) == 0:
        while not len(s1) == 0:
            temp = s1[-1]
            s1.pop()
            print(temp.value, end = " ")
            if temp.left:    
                s2.append(temp.left)
            if temp.right:
                s2.append(temp.right)
            
                
        while not len(s2) == 0:
            temp = s2[-1]
            s2.pop()
            print(temp.value, end = " ")
            if temp.right:
                s1.append(temp.right)
            if temp.left:    
                s1.append(temp.left)
    
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
print("The left spiral traversal of the tree is:")
spiral_traversal_left(root)
print("\nThe right spiral traversal of the tree is:")
spiral_traversal_right(root)
            
            

# root = Node(1)  
# root.left = Node(2)  
# root.right = Node(3)  
# root.left.left = Node(7)  
# root.left.right = Node(6)  
# root.right.left = Node(5)  
# root.right.right = Node(4)  
# print("Spiral Order traversal of binary tree is: ")
# spiral_level(root)                    

