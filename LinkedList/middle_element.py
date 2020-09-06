# finding middle of linked list

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
            
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
            
        
    def find_mid(self):
        slow = self.head
        fast = self.head
        if self.head is not None: 
            while (fast is not None and fast.next is not None): 
                fast = fast.next.next
                slow = slow.next
            print("The middle element is:", slow.data) 
        
    def mid_element(self):
        A = [self.head]
        while A[-1].next:
            A.append(A[-1].next)
        middle = float(len(A))/2
        if middle % 2 != 0:
            return A[int(middle - .5)].data
        else:
            return (A[int(middle)].data, A[int(middle-1)].data)    
        
        
llist = LinkedList()
arr = list(map(int, input("Enter the number you want in your linked list:").split()))
for i in range(0, len(arr)):
    llist.insert(arr[i])
llist.find_mid()
print(llist.mid_element())
llist.print_list()    
