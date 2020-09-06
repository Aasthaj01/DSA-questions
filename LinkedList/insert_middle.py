#method 1 - by using insert at a position (here, mid is the required position)
class Node:
    def __init__(self, data):
        self.data = data
        self.next =None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data, end = "-->")
            curr_node = curr_node.next

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node= last_node.next
        last_node.next = new_node

    def insert_beginning(self, data):
        new_node = Node(data) 
        new_node.next = self.head
        self.head = new_node

    def insert_at_pos(self, data, position):
        prev_node = self.head
        if position == 0:
            insert_beginning(data)
        while prev_node is not None:
            new_node = Node(data)
            for _ in range(position-1):
                prev_node = prev_node.next

            new_node.next = prev_node.next
            prev_node.next = new_node
            return self.head

llist = LinkedList()
arr = list(map(int, input("Enter the number you want in your linked list:").split()))
for i in range(0, len(arr)):
    llist.insert(arr[i])
num = int(input("Enter the number you wish to insert:"))    
mid = len(arr)//2    
llist.insert_at_pos(num, mid)    
llist.delete_node_at_pos(d)
llist.print_ll()
#===================================================================
#method 2 - using fast pointers
class Node : 
    def __init__(self, data): 
        self.data = data  
        self.next = None
          
class LinkedList:  
    def __init__(self): 
        self.head = None
     
    def insert_beginning(self, new_data):  
        new_node = Node(new_data)  
        new_node.next = self.head  
        self.head = new_node  
          
    def insertAtMid(self, x):
        if (self.head == None):  
            self.head = Node(x)  
  
        else:  
         
            newNode = Node(x)    
            slow = self.head 
            fast = self.head.next
  
            while (fast != None and 
                   fast.next != None):  
                  
                # move slow pointer to next node, move fast pointer two nodes  
                # at a time  
                slow = slow.next 
                fast = fast.next.next
  
            # insert the 'newNode' and  
            # adjust the required links  
            newNode.next = slow.next
            slow.next = newNode 
  
    
    def display(self): 
        curr_node = self.head  
        while (curr_node != None):  
            print(curr_node.data, end = "-->"), 
            curr_node = curr_node.next

ll = LinkedList() 
ll.insert_beginning(5)
ll.insert_beginning(4)
ll.insert_beginning(3)
print("Linked list before insertion: ")
ll.display()  
x = int(input("Enter the number which you want to insert:"))
ll.insertAtMid(x) 
print("\nLinked list after insertion: ")
ll.display() 

