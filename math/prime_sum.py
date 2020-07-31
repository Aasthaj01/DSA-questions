#Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.

def primesum(A):
        i = 2
        ans = list()
        while i <= A - i:
            
            if isprime(A - i):
                ans.append(i)
                ans.append(A - i)
                break
            i = nextprime(i)
        return ans
        
def isprime(k):
        
    flag = 1
    if k == 1:
        return 0
    if k == 2:
        return 1
    for i in range(2,int(k/2)):
        if k % i == 0:
            flag = 0
            break
    return flag

def nextprime(k):
    
    while True:
        k += 1
        if isprime(k):
            
            return k
            break  
        
A = int(input("Enter the number you want to check:"))
print(primesum(A))    
