# creating basic linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next =None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def print_list(self):
        cur_node = self.head 
        while cur_node:
            print(cur_node.data, end = " --> ")
            cur_node = cur_node.next
    
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node= last_node.next
        last_node.next = new_node
        
llist = LinkedList()
arr = list(map(int, input("Enter the number you waant in your linked list:").split()))
for i in range(0, len(arr)):
    llist.append(arr[i])
llist.print_list()    
            
