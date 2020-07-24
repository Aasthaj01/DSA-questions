# There are 3 querie i.e push, pop, max of stack
# 1 x = push x
# 2 = delete 
# 3 = max of stack

class stack():
    def __init__(self):
        self.items = []
        self.result = []
        
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
    def max_element(self):
        self.result.append(max(self.items))
        return self.result
        # print(max(self.items))        


    
s =stack()
t = int(input())  
for i in range(0, t):
    q = list(map(int, input().split()))
    if q[0] == 1:
        s.push(q[1])
    if q[0] == 2:
        s.pop()
    elif q[0] == 3:
        ans = s.max_element()
for i in range(0, len(ans)):
    
    print(ans[i])     
    
#=================================================================================================
 items = [0]
 for i in range(int(input())):
     nums = list(map(int, input().split()))
     if nums[0] == 1:
         items.append(max(nums[1], items[-1]))
     elif nums[0] == 2:
         items.pop()
     else:
        print(items[-1])

