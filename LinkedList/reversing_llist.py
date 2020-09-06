class Node:
    def __init__(self, data):
        self.data = data
        self.next =None
        
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node= last_node.next
        last_node.next = new_node    
    def print_list(self):
        cur_node = self.head 
        while cur_node:
            print(cur_node.data, end = " --> ")
            cur_node = cur_node.next
    def reverse_list(self):
        cur_node = self.head
        prev = None
        while cur_node:
            nxt = cur_node.next
            cur_node.next = prev
            prev =cur_node
            cur_node = nxt
        self.head = prev 
    def recursive(self):
        def reverse_recursive(cur_node, prev):
            if not cur_node:
                return prev
            nxt = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = nxt
            return reverse_recursive(cur_node, prev)
        self.head = reverse_recursive(cur_node = self.head, prev = None)

llist = LinkedList()
arr = list(map(int, input("Enter the number you want in your linked list:").split()))
for i in range(0, len(arr)):
    llist.append(arr[i])    
llist.reverse_list()
llist.print_list()
# Method 2
llist.recursive()
llist.print_list()
