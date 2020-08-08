# Maximum circular subarray sum
# Example [5, -2, 3, 4] --> 12

def naive(arr, n):
    res = arr[0]
    for i in range(0, n):
        curr_sum = arr[i]
        curr_max = arr[i]
        for j in range(1, n):
            index = (i+j)%2
            curr_sum += arr[index]
            curr_max = max(curr_max, curr_sum)
        res= max(res, curr_max)
    return res   
    
def max_sum_subarray(arr, n):
    res = arr[0]
    summ = arr[0]
    for i in range(1, n):
        summ = max(summ+arr[i], arr[i])
        res = max(res, summ)
    return res    

def max_sum_circular_subarray(arr, n):
    total_sum = 0
    for i in range(1, n):
        total_sum +=arr[i]
        arr[i] = -arr[i]
    circular_sum =total_sum + max_sum_subarray(arr, n) 
    return circular_sum
    
def overall_max(arr, n):
    max_normal_sum = max_sum_subarray(arr, n)
    max_circular_sum = max_sum_circular_subarray(arr, n)
    if max_normal_sum<0:
        return max_normal_sum
    return max(max_normal_sum, max_circular_sum)
    
arr = list(map(int, input("Enter the array elements:").split()))
n = len(arr)
print(naive(arr, n))
print(overall_max(arr, n))
