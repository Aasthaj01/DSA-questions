#Given an array of size n, create a wave array 

def creating_wave(arr, n):
    arr.sort()
    for i in range(0, n-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
    
arr = list(map(int, input().split()))
n = len(arr)

ans = creating_wave(arr, n)
for i in range(n):
    print(ans[i], end = " ")
