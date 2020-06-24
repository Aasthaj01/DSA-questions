# Recursion - fibonacci

def fib(num):
    if num <= 1:
       return num
    else:    
        return (fib(num-1) + fib(num-2))
    
    
num = int(input("Enter the number till which you want to find fib:"))

for i in range(num):
       print(fib(i))
