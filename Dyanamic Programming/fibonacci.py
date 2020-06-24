
#Recursion
def fib(num):
    if num <= 1:
      return num
    else:    
        return (fib(num-1) + fib(num-2))
        
        
# Top Down approach - fibonacci        
def fib_topDown(num):
    if num <= 1:
        arr[num] = num
        return arr[num]
        
    elif arr[num]!=-1:
        return arr[num]
        
    else: 
        arr[num] = fib(num-1) + fib(num-2)
    return (arr[num])    
    
num = int(input("Enter the number till which you want to find fib:"))
arr = [-1]*50
for i in range(0, num+1):
    print(fib_topDown(i))


