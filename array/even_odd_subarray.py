# max sum of continuous subarray     

def max_alternating_subarray(arr, n):
    res = 1
    curr = 1
    for i in range(1, n):
        if (arr[i]%2 == 0 and arr[i-1]%2 !=0) or (arr[i-1]%2 == 0 and arr[i]%2 !=0):
            curr+=1
            res = max(res, curr)
        else:
            curr = 1
    return res  
    
    
def naive_sol(arr, n):
    res = 1
    for i in range(0, n):
        curr = 1
        for j in range(i+1, n):
            if (arr[j]%2 == 0 and arr[j-1]%2 !=0) or (arr[j-1]%2 == 0 and arr[j]%2 !=0):
                curr = curr+1
            else:
                break
        res = max(curr, res)
    return res
    
arr= list(map(int, input("Enter the numbers:").split()))
n = len(arr)
print(max_alternating_subarray(arr, n))
print(naive_sol(arr, n))
