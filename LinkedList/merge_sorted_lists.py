class Node: 
    def __init__(self,data): 
          
        self.data = data 
        self.next = None
          
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

def mergeLists(head1, head2): 
    temp = None
    if head1 is None: 
        return head2
    if head2 is None: 
        return head1 
  
    
    if head1.data <= head2.data:
        temp = head1  
        temp.next = mergeLists(head1.next, head2)   
    else: 
        temp = head2  
        temp.next = mergeLists(head1, head2.next) 
    return temp    


llist1 = LinkedList()
arr1 = list(map(int, input("Enter the number you want in your linked list:").split()))
for i in range(0, len(arr1)):
    llist1.append(arr1[i])
llist2 = LinkedList()
arr2 = list(map(int, input("Enter the number you want in your linked list:").split()))
for i in range(0, len(arr2)):
    llist2.append(arr2[i])
llist3 = LinkedList()   
llist3.head = mergeLists(llist1.head, llist2.head)
llist3.print_list()
      
