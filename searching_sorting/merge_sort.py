# Merge sort i.e. divide and conquer algorithm
# efficient in solving big data sorting problems in nlogn time

def merge_sort(arr, first,  middle, last):
    n1 = middle - first + 1
    n2 = last- middle 
 
    L = [0] * (n1) 
    R = [0] * (n2) 
   
    for i in range(0 , n1): 
        L[i] = arr[first + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[middle + 1 + j] 

    i = j =0     # Initial index of first subarray  
    k = first     # Initial index of merged subarray 
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
 
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
    
def merge_sort_2(arr, first, last):
    if first<last:
        middle = (first+(first+last)) // 2
        merge_sort_2(arr, first, middle)
        merge_sort_2(arr, middle+1, last)
        merge_sort(arr, first, middle, last)
        

arr = list(map(int, input().split()))
n = len(arr)
merge_sort_2(arr, 0, n-1)
print ("Sorted array is:") 
for i in range(n): 
    print (arr[i], end = " ")
