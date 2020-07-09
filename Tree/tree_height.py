# Find the height of the given tree using recursion

class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
    def height(self, node):
        if node is None:
            return -1
        else:
            ltree = self.height(node.left)
            rtree = self.height(node.right)
        return 1+max(ltree, rtree)
    

            
b = BinaryTree(1)        
b.root.left = Node(2)
b.root.right = Node(3)
b.root.left.left = Node(10)
b.root.left.right = Node(20)
b.root.right.left = Node(30)
print(b.height(b.root))
