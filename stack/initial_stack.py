# Stack problems
# ------Reversing a stack ------ 
class stack():
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
    
    def is_empty(self):
        if self.items == []:
            return
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def display(self):
        for item in reversed(self.items):
            print(item)        
            
            
s = stack()  
num = int(input("How many numbers you want in the stack?"))
entries = list(map(int, input("Enter the numbers: ").split()))
# print(entries)
for item in entries:
    s.push(int(item))
 
print('The stack is:')
s.display()
