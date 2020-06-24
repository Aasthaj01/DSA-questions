
#Recursion--------------------------O(2^n)
def fib(num):
    if num <= 1:
      return num
    else:    
        return (fib(num-1) + fib(num-2))
  
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Bottom Down approach--------------O(n)  
def fibonacci_bottom_up(num):
  arr[0] = 0
  arr[1] = 1

  for i in range(2, num+1):
    arr[i] = arr[i-1] + arr[i-2]
  return arr[num]


num = int(input("Enter the number till which you want to find fib sequence:"))
arr = [-1]*50
for i in range(0, num+1):
    print(fibonacci_bottom_up(i))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Top Down approach----------------O(2n-1) i.e O(n)     
def fib_topDown(num, arr):
    if num <= 1:
        arr[num] = num
        return arr[num]
        
    elif arr[num]!=-1:
        return arr[num]
        
    else: 
        arr[num] = fib_topDown(num-1, arr) + fib_topDown(num-2, arr)
    return (arr[num])    
    
num = int(input("Enter the number till which you want to find fib sequence:"))
arr = [-1]*50
for i in range(0, num+1):
    print(fib_topDown(i, arr))


