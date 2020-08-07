# Stock buy sell problem in array
# In share market, one buys the stock on one day and sell it to make profit, find max profit
# Example ==> [10, 60, 2, 7, 55]  -->> (60-10) + (55-2) is the max profit

def sell_buy(price, start, end):
    if (end <= start): 
        return 0
    profit = 0
  
    for i in range(start, end, 1): 
        for j in range(i+1, end+1): 
            if (price[j] > price[i]): 
                curr_profit = price[j] - price[i] +\
                            sell_buy(price, start, i - 1)+\
                            sell_buy(price, j + 1, end) 
  
                
                profit = max(profit, curr_profit)
    return profit
    
def profit_shares(price, n):
    profit = 0
    for i in range(1, n):
        if price[i]> price[i-1]:
            profit+= price[i]-price[i-1]
    return profit        
            
price= list(map(int, input("Enter the shares prices i.e both purchased and selling:").split()))
n = len(price)
start = 0
end = n-1
print(profit_shares(price, n))
print(sell_buy(price, start, end))
