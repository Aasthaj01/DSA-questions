# Finding max width. Maximum Width of Binary tree is the maximum number of nodes present in a level of the Tree.

class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
def max_width_tree(node):
    if node is None:
        return 
    queue = [] 
   
    queue.insert(0, node)
    res = 0
    while(len(queue) > 0):
        count = len(queue)
        res = max(res, count)
        while (count is not 0): 
            count = count-1
            curr = queue[-1]   
            queue.pop()
            
            if curr.left is not None: 
                queue.insert(0, curr.left)
            if curr.right is not None: 
                queue.insert(0, curr.right)
    return res 

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
  

root = Node(1)
root.left = Node(2)
root.left.left = Node(2)
root.left.left.left = Node(2)
print("Maximum heigt of the tree is:", max_width_tree(root))

