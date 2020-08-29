# bottom up approach O(n**2) sol

def lds(arr, n): 
  
    lds = [0] * n 
    maxi = 0
    for i in range(n): 
        lds[i] = 1
#   similar to largest sum subsequence where arr[i]>arr[j] and dp[i]<dp[j] +arr[i]
    for i in range(1, n): 
        for j in range(i): 
            if (arr[i] < arr[j] and 
                lds[i] < lds[j] + 1): 
                lds[i] = lds[j] + 1
    maxi= max(lds)
    return maxi
    
arr = list(map(int, input().split()))    
n = len(arr) 
print(lds(arr, n))
