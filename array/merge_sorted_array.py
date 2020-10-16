#  Merge sorted arrays
def merge_sorted_array(arr1, arr2, n, m):
    arr3 = [None] * (n + m) 
    i = 0
    j = 0
    k = 0
    while i < n and j < m: 
        if arr1[i] < arr2[j]: 
            arr3[k] = arr1[i] 
            k = k + 1
            i = i + 1
        else: 
            arr3[k] = arr2[j] 
            k = k + 1
            j = j + 1
      
    while i < n: 
        arr3[k] = arr1[i]; 
        k = k + 1
        i = i + 1
 
    while j < m: 
        arr3[k] = arr2[j]; 
        k = k + 1
        j = j + 1
    print("Array after merging") 
    for i in range(n+m): 
        print(str(arr3[i]), end = " ") 
 
            


arr1 =list(map(int, input().split()))
n = len(arr1)
arr2 =list(map(int, input().split()))
m = len(arr2)
merge_sorted_array(arr1, arr2, n, m)
