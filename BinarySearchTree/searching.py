#  input a binary search tree data and search for a given element

class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
def bst_search(node, num):
    if node is None:
        return False

    if num == node.value:
        return True
    if num <node.value:
        return bst_search(node.left, num)
    else:    
        return bst_search(node.right, num)  
        
def insertLevelOrder(arr, root, i, n): 
    if i < n: 
        temp = Node(arr[i])  
        root = temp  
  
        root.left = insertLevelOrder(arr, root.left, 
                                     2 * i + 1, n)  

        root.right = insertLevelOrder(arr, root.right, 
                                      2 * i + 2, n) 
    return root             
            
            
arr = list(map(int, input().split()))
n = len(arr) 
root = None
root = insertLevelOrder(arr, root, 0, n)  
num = int(input("Enter the number to be searched:"))
print(bst_search(root, num))
