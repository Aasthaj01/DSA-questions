from collections import deque
class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
    
    def tree_size(self, node):
        if node is None:
            return 0
        else:
            ltree = self.tree_size(node.left)
            rtree = self.tree_size(node.right)
        return 1+(ltree+rtree) 
        
# Method 2 - calculating size of the tree using stack
    def tsize(self):
        if self.root is None:
            return 0
        else:
            s =deque()
            s.append(self.root)
            size =1
            while s:
                node = s.pop()
                if node.left is not None:
                    size+=1
                    s.append(node.left)
                if node.right is not None:
                    size+=1
                    s.append(node.right)    
            return size        
                

            
b = BinaryTree(1)        
b.root.left = Node(2)
b.root.right = Node(3)
b.root.left.left = Node(10)
b.root.left.right = Node(20)
b.root.right.left = Node(30)

print(b.tree_size(b.root))
print(b.tsize())
