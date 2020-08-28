# in recursive solution
# you can choose ith element or jth, we'll take max of arr[i]+min(optimal_strategy(arr, i+2, j), optimal_strategy(arr, i+1, j-1)) and similarly when we select last element
def optimal_strategy(arr, n):
    dp = [[0 for i in range(n)] 
                for j in range(n)]
    for gap in range(n): 
        for j in range(gap, n): 
            i = j - gap 
            x = 0
            if((i + 2) <= j): 
                x = dp[i + 2][j] 
            y = 0
            if((i + 1) <= (j - 1)): 
                y = dp[i + 1][j - 1] 
            z = 0
            if(i <= (j - 2)): 
                z = dp[i][j - 2] 
            dp[i][j] = max(arr[i] + min(x, y), 
                              arr[j] + min(y, z)) 
    return dp[0][n - 1]              
    

arr = list(map(int, input().split()))
n = len(arr)
print(optimal_strategy(arr, n))
