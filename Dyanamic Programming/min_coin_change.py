#Given a amount, if we want to make change for amount, and we have infinite supply of each of coins = { C1, C2, .. , Cm}, what is the minimum number of coins to make the change?
#---------------------------RECURSION---------------------------------------------------------------------------------------------------------------
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

#------------------------------------DYNAMIC PROGRAMMING------------------------------------------------------------------

import sys

def coins_needed(coins, n, amount): 
      
    # table[i] will be storing the minimum  
    # number of coins required for i value.  
    # So table[amount] will have result 
    table = [0 for i in range(amount + 1)] 
  
    # Base case (If given value amount is 0) 
    table[0] = 0
  
    # Initialize all table values as Infinite 
    for i in range(1, amount + 1): 
        table[i] = sys.maxsize 
  
    # Compute minimum coins required  
    # for all values from 1 to amount 
    for i in range(1, amount + 1): 
          
        # Go through all coins smaller than i 
        for j in range(n): 
            if (coins[j] <= i): 
                sub_res = table[i - coins[j]] 
                if (sub_res != sys.maxsize and 
                    sub_res + 1 < table[i]): 
                    table[i] = sub_res + 1
    return table[amount] 
  

if __name__ == "__main__": 
    coins = list(map(int, input().split()))    
    n=  len(coins)
    amount = int(input())
    print(coins_needed(coins, n, amount))
     
