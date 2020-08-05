# left rotation of array by 1

def left_rotate(arr, n):
    
    temp = arr[0]
    for i in range(1, n):
        arr[i-1] = arr[i]
    arr[n-1] = temp
    return arr    


arr = list(map(int, input().split()))
n = len(arr)
ans =left_rotate(arr, n)
for i in range(len(ans)):
    print(ans[i], end = " ")
