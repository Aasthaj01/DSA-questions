def reverse_num(x):
    ans = int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1])
    return ans if -2**31 <= ans <= 2**31 -1 else 0
    
n = int(input("Enter the integer:")) 
print("Reversed number is:")
print(reverse_num(n))

#=============================================================================================

from collections import deque

def neg(n):
    if n<0:
        return -int(str(-n)[::-1])
def reverse_num(n):
    while n>0:
        lsb = n%10
        s.append(lsb)
        n = n//10
    print_num(s)
    
def print_num(s):
    
    for i in range(len(s)):
        print(s[i], end = "")
        
s =[]
n = int(input("Enter the integer:")) 
print("Reversed number is:")
if n<=0:
    print(neg(n))
else:
    reverse_num(n)
