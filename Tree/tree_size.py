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
#-------------------------------------------------------------------------------------------------------
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0

        def dfs(node):
            if not node: return 0

            left = node.left
            left_count = 1
            while left:
                left = left.left
                left_count += 1

            right = node.right
            right_count = 1
            while right:
                right = right.right
                right_count += 1

            if left_count == right_count:
                return (2**left_count) - 1
            else:
                left = dfs(node.left)
                right = dfs(node.right)

                return left + right + 1
        
        return dfs(root)
    

