# converting binary tree to doubly linklist 

class Node:    
    def __init__(self,data):    
        self.data = data;    
        self.left = None;    
        self.right = None;    
            
class BinaryTreeToDLL:    
    def __init__(self):    
        #Represent the root of binary tree    
        self.root = None    
        #Represent the head and tail of the doubly linked list    
        self.head = None    
        self.tail = None   
            
   
    def convertbtToDLL(self, node):    
          
        if node is None:   
            return    
                
        #Convert left subtree to doubly linked list    
        self.convertbtToDLL(node.left);    
            
        #If list is empty, add node as head of the list    
        if(self.head == None):    
            #Both head and tail will point to node    
            self.head = self.tail = node;    
        #Otherwise, add node to the end of the list    
        else:    
            #node will be added after tail such that tail's right will point to node    
            self.tail.right = node   
            #node's left will point to tail    
            node.left = self.tail   
            #node will become new tail    
            self.tail = node   
                
        #Convert right subtree to doubly linked list    
        self.convertbtToDLL(node.right);    
        
       
    def display(self):    
         
        current = self.head    
        if(self.head == None):    
            print("List is empty!");    
            return;    
        print("Nodes of generated doubly linked list: ")    
        while(current != None):    
            print(current.data, end = " <--> ")    
            current = current.right    
            
           
bt = BinaryTreeToDLL()    
bt.root = Node(1)  
bt.root.left = Node(2)   
bt.root.right = Node(3)    
bt.root.left.left = Node(4)    
bt.root.left.right = Node(5)    
bt.root.right.left = Node(6)   
bt.root.right.right = Node(7)   
   
bt.convertbtToDLL(bt.root)   
bt.display()
