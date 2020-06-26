#Given a amount, if we want to make change for amount, and we have infinite supply of each of coins = { C1, C2, .. , Cm}, what is the minimum number of coins to make the change?

import sys

def coins_needed(coins, amount, n):
    if amount==0:
        return 0
        
    ans = sys.maxsize
    for i in range(0, n):
        if amount-coins[i]>=0:
            small_ans = coins_needed(coins, amount-coins[i], n)  
            if (small_ans!=sys.maxsize) and ((small_ans + 1)< ans): 
                ans = small_ans+1
                # ans = min(ans, small_ans+1)
    return ans
    
    
coins = list(map(int, input("Enter the coins available:").split()))    
n=  len(coins)
amount = int(input("Enter the amount:"))
print(coins_needed(coins, amount, n))
