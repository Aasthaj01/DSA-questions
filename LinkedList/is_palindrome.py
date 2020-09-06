# Method 1, using stack

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

    def ispalindrome(self): 
        slow = self.head 
        stack = [] 
        
        ispalin = True
        while slow != None: 
            stack.append(slow.data) 

            slow = slow.next 
    
        while self.head != None: 

            i = stack.pop() 
            if self.head.data == i: 
                ispalin = True
            else: 
                ispalin = False
                break
            self.head = self.head.next 
        return ispalin 
 
llist = LinkedList()
arr = list(map(int, input("Enter the number you waant in your linked list:").split()))
for i in range(0, len(arr)):
    llist.append(arr[i])  

result = llist.ispalindrome() 
print("Is the lisked list a palindrome?", result) 
