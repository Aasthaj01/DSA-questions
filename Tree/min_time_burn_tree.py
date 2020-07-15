We are given a binary tree and a leaf node, we need to find time to burn the Binary Tree if we burn the given leaf at 0-th second.


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value

    def set_left(self, other):
        self.left = other
        other.parent = self

    def set_right(self, other):
        self.right = other
        other.parent = self

def get_distance_to_furthest(node):
    visited = set()
    queue = [(node, 0)]
    max_d = 0
    while queue:
        node, d = queue.pop(0)

        if node in visited:
            continue
        visited.add(node)

        max_d = max(d, max_d)

        if node.left:
            queue.append((node.left, d + 1))
        if node.right:
            queue.append((node.right, d + 1))
        if node.parent:
            queue.append((node.parent, d + 1))

    return max_d

root = Node(1)
root.set_left(Node(1))
root.set_right(Node(1))
root.left.set_left(Node(1))
root.left.set_right(Node(1))
root.left.right.set_left(Node(1))
root.left.right.set_right(Node(1))
root.right.set_right(Node(1))
root.right.right.set_right(Node(1))
root.right.right.right.set_right(Node(1))
print(get_distance_to_furthest(root.left.right))


#---------------------------------------------------------------------------------------------------------------------------
class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        
def min_time_burn_tree(node, leaf, distance, result):
    if node is None:
        return 0
    if node.value==leaf:
        distance = 0
        return 1
    ldist = -1
    rdist = -1
    ltree = min_time_burn_tree(node.left, leaf, ldist, result)
    rtree = min_time_burn_tree(node.right, leaf, rdist, result)
    if ldist!=-1:
  
        distance =ldist+1;
        result =max(result,distance+rtree)
    if rdist!=-1:

        distance =rdist+1;
        result =max(result,distance+ltree)
  
    return 1+max(ltree, rtree)    
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
    
    
# root = Node(1)
# root.left = Node(2)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right = Node(3)
# root.right.left = Node(7)
# root.right.left.left = Node(8)
# root.right.left.left.right = Node(6)
leaf  = int(input("Enter the leaf node from which you want to burn:"))
distance = -1
result = 0
h = min_time_burn_tree(root, leaf, distance, result)

print(h)
