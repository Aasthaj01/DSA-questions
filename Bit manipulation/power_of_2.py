# To check if a number if power of 2 or not

def check_power2(c):
    result = 0
    if c[0] == '1':
        result = c.find('1', 1)
        if result>=1:
            print("Number is not a power of 2")
    else:
        print("Number is not a power of 2") 
        
  
    
n  = int(input("Enter the number: "))  
b = bin(n).replace("0b", "")
c = str(b)

if n>0:
    check_power2(c)
else:
    print("Number is not greater than 0")
    
#------------------------------------------------------------------------------------------------------
#   METHOD 2 
def check(n):
    if n==0:
        return False
    while n!=1:
        if n%2 !=0:
            return False
        n = n//2
    return True
    
n = int(input())    
print(check(n))

# ------------------------------------------------------------------------------------------------------
# METHOD 3 Brian algorithm

def count(n):
    result = 0
    while n>0:
        n = n & (n-1)
        result +=1
    return result 
    
n = int(input("Enter the number: "))
set_bits= count(n)
if set_bits>=1:
    print("number is not power of 2")
elif n>0:
    print("Number is power of 2")
