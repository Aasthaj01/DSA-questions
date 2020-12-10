# Method 1
num = 201
count = 0
if num>1:
    for i in range(1, num+1):
        if num%i == 0:
            count +=1
    if count == 2:
        print("Yes, the number is prime")
    else:
        print("No, it is a non prime number")
#======================================================================================        
# Method 2        
def isPrime(n):
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    elif(n%2 == 0 or n%3 == 0):
        return False
        
    i = 5
    while(i*i<=n):
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True

print(isPrime(25))
