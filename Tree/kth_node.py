# Finding maximum node in the tree

class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
    def node_k_dis(self, node, k):
        arr = []
        if node is None:
            return -1
        elif k == 0:
            return node.value
        else:
            
            ltree = self.node_k_dis(node.left, k-1)
            rtree = self.node_k_dis(node.right, k-1)
            arr.append(ltree)
            arr.append(rtree)
        return arr
        
        
b = BinaryTree(1)        
b.root.left = Node(2)
b.root.right = Node(3)
b.root.left.left = Node(10)
b.root.left.right = Node(20)
b.root.right.left = Node(30)
k = int(input("Enter the distance k: "))

print(b.node_k_dis(b.root, k))
