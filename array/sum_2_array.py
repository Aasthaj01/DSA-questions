from operator import add

n = int(input("Enter the size of array:"))
a = list(map(int, input("Enter the elements of array a:").split()))
b = list(map(int, input("Enter the elements of array b:").split()))
c = []
for i in range(0, n):
  c = list(map(add, a, b))
	
for i in range(0, len(a)):    
  print(c[i], end = " ")	

#----------------------------------------------METHOD 2-------------------------------------------------------------
  
n = int(input("Enter the size of array:"))
a = list(map(int, input("Enter the elements of array a:").split()))
b = list(map(int, input("Enter the elements of array b:").split()))
c = []
for i in range(0, n):
	c.append(a[i] + b[i])

print(str(c))
