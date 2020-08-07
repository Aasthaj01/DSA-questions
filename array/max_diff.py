# Maximum Difference problem is to find the maximum of arr[j] - arr[i] where j>i.

def max_diff(arr, n):
    diff = arr[1] -arr[0]
    for i in range(0, n):
        
        for j in range(1+i, n):
            if j>i :
                diff = max(diff, arr[j]- arr[i])
    print(diff)  
    
# efficient solution
def max_difference(arr, n):
    minval = arr[0]
    diff = arr[1] - arr[0]
    for j in range(1, n):
        diff = max(diff, arr[j] - minval)
        minval = min(arr[j], minval)
    return diff
arr = list(map(int, input("Enter the array elements:").split()))
n = len(arr)
max_diff(arr, n)
print(max_difference(arr, n))
