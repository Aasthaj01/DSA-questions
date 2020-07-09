# Finding maximum node in the tree

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
                
    def tree_max_element(self, node):
        if node is None:
            return 0
        else:
            ans = node.value
            lans = self.tree_max_element(node.left)
            rans = self.tree_max_element(node.right)
            if lans>rans:
                ans = lans
            elif rans>lans:
                ans = rans
            return ans    
        
            
b = BinaryTree(1)        
b.root.left = Node(2)
b.root.right = Node(3)
b.root.left.left = Node(10)
b.root.left.right = Node(20)
b.root.right.left = Node(30)

print(b.tree_size(b.root))
print(b.tree_max_element(b.root))
