class Node:
    def __init__(self, data):
        self.data = data
        self.next =None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end = "-->")
            curr_node = curr_node.next 

    def append_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def append_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node =last_node.next
        last_node.next = new_node

    def insertNodeAtPosition(self, data, position):
        prev_node = self.head
        if position == 0:
            new_node = Node(data)
            new_node.next = self.head
            return new_node

        while prev_node is not None:
            new_node = Node(data)

            for _ in range(position-1):
                prev_node = prev_node.next

            new_node.next = prev_node.next
            prev_node.next = new_node
            return self.head
       
        
llist = LinkedList()
arr = list(map(int, input("Enter the number you waant in your linked list:").split()))
num = int(input("Enter the number you wish to insert in the beginning:"))
for i in range(0, len(arr)):
    llist.append_node(arr[i])
llist.append_beginning(num)   
position = int(input())
llist.insertNodeAtPosition(num, position)
llist.print_list()    
