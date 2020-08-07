# max sum of continuous subarray     

def max_sum_subarray(arr, n):
    res = arr[0]
    summ = arr[0]
    for i in range(1, n):
        summ = max(summ + arr[i], arr[i])
        res = max(summ, res)
    return res  
    
    
def naive_sol(arr, n):
    res = arr[0]
    for i in range(0, n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum = curr_sum+arr[j]
            res = max(curr_sum, res)
    return res
    
arr= list(map(int, input("Enter the numbers:").split()))
n = len(arr)
print(max_sum_subarray(arr, n))
print(naive_sol(arr, n))
