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
