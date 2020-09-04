# selection sort
# The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning.
# The algorithm maintains two subarrays in a given array.
# 1) The subarray which is already sorted.
# 2) Remaining subarray which is unsorted.

def selection_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        minIndex = i
        for j in range(i+1, n):
            if arr[j]<arr[minIndex]:
                minIndex = j
        if minIndex!=i:    
            arr[i], arr[minIndex] = arr[minIndex], arr[i] 
    return arr
    
arr = list(map(int, input().split()))
print(selection_sort(arr))
