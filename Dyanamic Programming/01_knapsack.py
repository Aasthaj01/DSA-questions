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
