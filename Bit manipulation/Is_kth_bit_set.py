# check kth bit of the number is set or not

# METHOD 1- Right shift operator
a = int(input("Enter the number:"))
k = int(input("Enter the position which you want to check:"))
n = a>>(k-1)

if n & 1 == 1:
    print("SET")
else:
    print("NOT SET")
    
#--------------------------------------------------------------------------------------------------------
#METHOD 2- Left shift operator

a, k = list(map(int, input("Enter the number and position which you want to check:").split()))
n = a>>(k-1)

if a&n != 0:
    print("SET")
else:
    print("NOT SET")
    
