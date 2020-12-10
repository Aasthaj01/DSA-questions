# the complexity mainly depends on pivot
# avg time complexity is nlogn and worst is n^2

# When last element is chosen as pivot
def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
 
 
arr = list(map(int, input().split()))
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print(arr[i], end = " ")
    
#=====================================================================================
# Method 2: pivot at the end

def quick_sort(arr):
    if len(arr)<1:
        return arr
    else:
        pivot = arr.pop()
        
        
    lower_arr = []
    higher_arr = []
    
    
    for item in arr:
        if item < pivot:
            lower_arr.append(item)
        else:
            higher_arr.append(item)
    return quick_sort(lower_arr)+[pivot]+quick_sort(higher_arr)        
    
    

arr = [5, 18, 1, 0, 3, 2, 14, 21]    
print(quick_sort(arr))
