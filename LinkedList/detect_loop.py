# Detecting loop in a linked list using set
# Idea is simple: the very first node whose next is already visited (or hashed) is the last node.
# We can also use Floyd Cycle Detection algorithm to detect and remove the loop. 
# In the Floyd’s algo, the slow and fast pointers meet at a loop node. We can use this loop node to remove cycle.
# There are following two different ways of removing loop when Floyd’s algorithm is used for Loop detection.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end = "-->")
            curr = curr.next
            
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head =new_node
            return 
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def is_loop(self):
        s = set()
        temp = self.head 
        while (temp): 
            if (temp in s): 
                return True
            s.add(temp)
            temp = temp.next
        return False
         
llist = LinkedList()
arr = list(map(int, input("Enter the number you waant in your linked list:").split()))
for i in range(0, len(arr)):
    llist.insert_end(arr[i])
llist.head.next.next.next = llist.head  
if( llist.is_loop()): 
    print ("Loop found") 
else : 
    print ("No Loop ") 
#=================================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end = "-->")
            curr = curr.next
            
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head =new_node
            return 
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
# Using Floyd loop detection; fast pointer and slow pointer concept --> space is O(1)
    def detectLoop(self): 
        slow = self.head 
        fast= self.head 
        while(slow and fast and fast.next): 
            slow = slow.next
            fast = fast.next.next
            if slow == fast: 
                return True
        return False
            
llist = LinkedList()
arr = list(map(int, input("Enter the number you want in your linked list:").split()))
for i in range(0, len(arr)):
    llist.insert_end(arr[i])
llist.head.next.next.next = llist.head  
    
if(llist.detectLoop()): 
    print ("Loop found") 
else : 
    print ("No Loop ")  
        
