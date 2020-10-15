# Given an array, return an array with odd numbers followed by the even numbers.
# Input  = {12, 34, 45, 9, 8, 90, 3}
# Output = {45, 9, 3, 12, 34, 8, 90}


def patterned_array(arr, n):
    for i in range(n):
        if arr[i]%2 != 0:
            arr.append(arr[i])
    for i in range(n):
        if arr[i]%2 == 0:
            arr.append(arr[i])
    del arr[:n]
    return arr
    
arr = list(map(int, input().split()))  
n = len(arr)
print(patterned_array(arr, n))
