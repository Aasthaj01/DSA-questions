# deletion of a node from llist

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
            
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert_node_after(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node= last_node.next
        last_node.next = new_node
        
# There can be 2 cases: node to be deleted is head, node to be deleted is in between
    def delete_node(self, key):
        cur_node = self.head
        if cur_node and cur_node.data==key:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        while cur_node and cur_node.data!=key:
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None
        
llist = LinkedList()
arr = list(map(int, input("Enter the number you want in your linked list:").split()))
for i in range(0, len(arr)):
    llist.append(arr[i])
llist.prepend(45)
llist.insert_node_after(llist.head.next.next, 22)
llist.delete_node(5)
llist.print_list()    
            
