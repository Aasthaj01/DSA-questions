def grayTobin(n):
    mask = n
    while mask!=0:
        mask>>=1
        n^=mask
    return n
    
t = int(input())  
arr = []
for i in range(t):
    n = int(input())
    answer = grayTobin(n)
    arr.append(answer)
    
for i in range(len(arr)):
    print(arr[i])
