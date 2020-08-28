# recursive solution
# either we will include the item or not consider it
# base case will be when n becomes 0 when no item is to be considered or when weight limit becomes 0
def knapsack(val, weight, limit, n):
    
    if n == 0 or limit == 0:
        return 0
    elif weight[n-1]>limit:
        return knapsack(val, weight, limit, n-1)
    else:
        return max(knapsack(val, weight, limit, n-1), val[n-1] + knapsack(val, weight, limit-weight[n-1], n-1) ) 
               

val = list(map(int, input("Price of items:").split()))
weight = list(map(int, input("Weight of items:").split()))
n = len(val)
limit = int(input("Max weight:"))
print(knapsack(val, weight, limit, n))
#=======================================================================================
# dp solution
# either we will include the item or not consider it
# base case will be when n becomes 0 when no item is to be considered or when weight limit becomes 0
def knapsack(val, weight, limit, n):
    dp = [[0 for i in range(limit+1)]for i in range(n+1) ]
     
    for i in range(0, n+1):
        for j in range(0, limit+1):
            if i == 0 or limit == 0: 
                dp[i][limit] = 0
            elif weight[i-1] <= j: 
                dp[i][j] = max(val[i-1] + dp[i-1][j-weight[i-1]],  dp[i-1][j]) 
            else: 
                dp[i][j] = dp[i-1][j] 
  
    return dp[n][limit]     

   
               

val = list(map(int, input("Price of items:").split()))
weight = list(map(int, input("Weight of items:").split()))
n = len(val)
limit = int(input("Max weight:"))
print(knapsack(val, weight, limit, n))
