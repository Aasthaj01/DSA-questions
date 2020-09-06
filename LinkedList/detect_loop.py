# Detecting loop in a linked list using set

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
        
