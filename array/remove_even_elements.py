# Given an array of numbers, remove alternate numbers starting from second position from start.

def remove_alternates(arr, n):
    arr = [v for i, v in enumerate(arr) if i % 2 == 0] 
    print(arr)
    #for i in range(0, n, 2):
        #arr1.append(arr[i])
    #print(arr1)

arr = list(map(int, input().split()))
n = len(arr)
remove_alternates(arr, n)
