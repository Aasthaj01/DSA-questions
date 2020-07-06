def binaryToGray(n):
    return n^(n>>1)
    
    
t = int(input())  
arr = []
for i in range(t):
    n = int(input())
    answer = binaryToGray(n)
    arr.append(answer)
    
for i in range(len(arr)):
    print(arr[i])
