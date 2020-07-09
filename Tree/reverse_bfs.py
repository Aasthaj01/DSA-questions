# reverse level order traversal

class Queue(object):
    def __init__(self):
        self.items = []
    def is_empty(self):
        if self.items == []:
            return
    def enqueue(self, item):
        return self.items.insert(0, item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
    def __len__(self):
        return self.size()
    def size(self):
        return len(self.items)
        
class Stack(object):
    def __init__(self):
        self.items = []
    def is_empty(self):
        if self.items == []:
            return 
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def push(self, item):
        self.items.append(item)
    def display(self):
        for item in reversed(self.items):
            print(item)
    def size(self):
        return len(self.items)
    def __len__(self):
        return self.size()
            
class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
    def print_tree(self, traversal_type):
        if traversal_type == "reverse levelorder" or traversal_type == "reverse order" or traversal_type == "reverse bst":
            return self.reverse_level_order(b.root)    
        else:
            print("traversal type"+ "- " +str(traversal_type)+" "+"is not supported")
            return False
    def level_order(self, start):
        if start is None:
            return 
        q =Queue()
        q.enqueue(start)
        traversal = ""
        while len(q)>0:
            traversal+= str(q.peek())+ "-->"
            node = q.dequeue()
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right) 
        return traversal            
    def reverse_level_order(self, start):
        if start is None:
            return
        s = Stack()
        q = Queue()
        q.enqueue(start)
        traversal = ""
        while len(q)>0:
            node = q.dequeue()
            s.push(node)
            if node.right:
                q.enqueue(node.right)
            if node.left:
                q.enqueue(node.left)
                
        while len(s)>0:
            node = s.pop()
            traversal += str(node.value)+"-"
        return traversal

            

b = BinaryTree(1)        
b.root.left = Node(2)
b.root.right = Node(3)
b.root.left.left = Node(10)
b.root.right.left = Node(20)
print(b.print_tree("reverse order"))
#------------------------------------------------------------------------------------------------------------------------
#METHOD 2 - Using library

# reverse bfs traversal
from collections import deque
from queue import Queue

class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
    def print_tree(self, traversal_type):
        if traversal_type == "reverse levelorder" or traversal_type == "reverse order" or traversal_type == "reverse bst":
            return self.reverse_level_order(b.root)    
        else:
            print("traversal type"+ "- " +str(traversal_type)+" "+"is not supported")
            return False
    def level_order(self, start):
        if start is None:
            return 
        
        q =Queue(maxsize = 30)
        q.put(start)
        traversal = ""
        while q.qsize()>0:
            traversal+= str(q.first())+ "-->"
            node = q.get()
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        return traversal 
    
    def reverse_level_order(self, start):
        if start is None:
            return
        s = deque()
        q = Queue(maxsize = 30)
        q.put(start)
        traversal = ""
        while q.qsize()>0:
            node = q.get()
            s.append(node)
            if node.right:
                q.put(node.right)
            if node.left:
                q.put(node.left)
                
        while len(s)>0:
            node = s.pop()
            traversal += str(node.value)+"-"
        return traversal

            
b = BinaryTree(1)        
b.root.left = Node(2)
b.root.right = Node(3)
b.root.left.left = Node(10)
b.root.right.left = Node(20)
print(b.print_tree("reverse order"))
    


    

