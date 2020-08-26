# counting inversions in array
# Inversion is possible if ith element is greater than jth where i is small than j
# example = [9, 6, 8, 4] ==>5
#==================================================================================================================
# Naive solution O(n**2) complexity
def array_inversion(arr, n):
    count = 0
    for i in range(n):
        for j in range(n):
            if i<j and arr[i]>arr[j]:
                count+=1
            continue
    return count    

arr = list(map(int, input("Enter the array elements:").split()))
n = len(arr)
print(array_inversion(arr, n))
#======================================================================================================================
