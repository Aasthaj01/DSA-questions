# The program gives number of ways in which change of a particular amount can be made if coins available are "coins"


def coin_change(coins, n, amount):
    arr = [0 for k in range(amount+1)]
    arr[0] = 1
    for i in range(0, n):
        for j in range(coins[i], amount+1):
            arr[j] = arr[j] + arr[j-coins[i]]
    return arr[amount]
    
coins = list(map(int, input("Enter the coins available:").split()))
n = len(coins)
amount = int(input("Enter the amount whose change is to be made:"))
print(coin_change(coins, n, amount))
