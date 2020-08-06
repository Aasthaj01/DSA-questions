#O(N**2)Complexity


def sort_arr(arr, n):
    for i in range(n):
        for j in range(i+1, n):
            temp = 0
            if arr[i]>arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr        
        
arr = [2, 5, 8, 1, 0]        
n = len(arr)
print(sort_arr(arr, n))
