#This algorithm detects loop and corrects it as well.

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
                self.removeLoop(slow) 
          
                # Return 1 to indicate that loop is found 
                return 1
          
        # Return 0 to indicate that there is no loop 
        return 0 

    def removeLoop(self, loop_node): 
        ptr1 = loop_node 
        ptr2 = loop_node 
          
        # Count the number of nodes in loop 
        k = 1 
        while(ptr1.next != ptr2): 
            ptr1 = ptr1.next
            k += 1
  
        # Fix one pointer to head 
        ptr1 = self.head 
        # And the other pointer to k nodes after head 
        ptr2 = self.head 
        for i in range(k): 
            ptr2 = ptr2.next
  
        # Move both pointers at the same place 
        # they will meet at loop starting node 
        while(ptr2 != ptr1): 
            ptr1 = ptr1.next
            ptr2 = ptr2.next
  
        # Get pointer to the last node 
        while(ptr2.next != ptr1): 
            ptr2 = ptr2.next
  
        # Set the next node of the loop ending node 
        # to fix the loop 
        ptr2.next = None  
            
            
llist = LinkedList()
arr = list(map(int, input("Enter the number you want in your linked list:").split()))
for i in range(0, len(arr)):
    llist.insert_end(arr[i])
llist.head.next.next.next = llist.head  

if(llist.detectLoop()): 
    print ("Loop found") 
else : 
    print ("No Loop ") 
llist.detectLoop()    
llist.print_list()
    
        
