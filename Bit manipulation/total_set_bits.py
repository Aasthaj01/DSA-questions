# Count the number of set bits i.e '1' in binary representation of the number
# METHOD 1

def count_one(c):
    
    if n>0:
        count = 0
        for i in reversed(range(len(c))):
            if c[i]=='1':
                count+=1
            else:
                continue
        
        return count
    else:
        print("Number is less than 0")

    
n = int(input("Enter the number: "))
b = bin(n).replace("0b", "")
c = str(b)
print("Number of set bits are:", count_one(c))

#---------------------------------------------------------------------------------------
# METHOD 2

def count(n):
    result = 0
    while n>0:
        result = result+(n&1)
        n>>=1
    return result
    
    
n = int(input("Enter the number: "))
print("Number of set bits are:", count(n))




