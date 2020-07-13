# Given inorder and preorder traversal of a tree, print postorder traversal of that tree

class Node: 
    def __init__(self, value): 
        self.value = value 
        self.left = None
        self.right = None
 
def buildTree(inOrder, preOrder, inStrt, inEnd): 
    if (inStrt > inEnd): 
        return None
    tNode = Node(preOrder[buildTree.preIndex]) 
    buildTree.preIndex += 1
    if inStrt == inEnd:
        return tNode 
   
    inIndex = search(inOrder, inStrt, inEnd, tNode.value) 
 
    tNode.left = buildTree(inOrder, preOrder, inStrt, inIndex-1) 
    tNode.right = buildTree(inOrder, preOrder, inIndex + 1, inEnd) 
    return tNode
    
def search(arr, start, end, data): 
    for i in range(start, end + 1): 
        if arr[i] == data: 
            return i 
  
def printPostorder(node): 
    if node is None: 
        return 
    printPostorder(node.left) 
    printPostorder(node.right)
    print(node.value)


inOrder = list(map(int, input("Enter inorder traversal of the tree:").split()))
preOrder = list(map(int, input("Enter preorder traversal of the tree:").split()))
buildTree.preIndex = 0
root = buildTree(inOrder, preOrder, 0, len(inOrder)-1) 
print("Postorder traversal of the constructed tree is:")
printPostorder(root) 
#------------------------------------------------------------------------------------------------------------------------------------

class TreeNode:
   def __init__(self, data, left = None, right = None):
      self.data = data
      self.left = left
      self.right = right
      
def print_tree(root):
   
   if root is not None:
      print_tree(root.left)
      print_tree(root.right)
      print(root.data, end = ' ')
      
class Solution(object):
   def buildTree(self, preorder, inorder):
       if inorder:
          root = TreeNode(preorder.pop(0))
          root_index = inorder.index(root.data)
          root.left = self.buildTree(preorder,inorder[:root_index])
          root.right = self.buildTree(preorder,inorder[root_index+1:])
          return root
      
ob1 = Solution()
preorder = list(map(int, input("Enter preorder traversal:").split()))
inorder = list(map(int, input("Enter inorder traversal:").split()))
print("The postorder traversal of the tree is:")
print_tree(ob1.buildTree(preorder, inorder))
   
