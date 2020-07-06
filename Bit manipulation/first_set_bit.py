# first occrence of set bit

def first_set(c):
    count =1
    if c == '0':
        return 0 
    else:
        for i in reversed(range(len(c))):
            if c[i]=='0':
                count+=1
                continue
            if c[i] =='1':
                return count
    
t = int(input())
arr =[]

for i in range(t):
    n = int(input())
    b = bin(n).replace("0b", "")
    c =str(b)
    ans = first_set(c)
    arr.append(ans)
for i in range(len(arr)):
        print(arr[i], end = " ")   
        
#-----------------------------------------------------------------------------------------------------------
#METHOD 2

def PositionRightmostSetbit(n): 
    position = 1
    m = 1
    
    while (not(n & m)) : 
  
        m = m << 1
        position += 1
      
    return position 
  
t = int(input())
arr =[]

for i in range(t):
    n = int(input())
    ans = PositionRightmostSetbit(n)
    arr.append(ans)
for i in range(len(arr)):
        print(arr[i], end = " ")  


#------------------------------------------------------------------------------------------------------------
#METHOD 3
import math

def first_set(n):
    if n == 0:
        return 0 
    else:    
        return math.log2(n&-n)+1
    
    
t = int(input())
arr =[]

for i in range(t):
    n = int(input())
    
    ans = first_set(n)
    arr.append(ans)
for i in range(len(arr)):
        print(arr[i], end = " ")    
    
    

    
    
