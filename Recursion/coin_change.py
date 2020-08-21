# coin change problem, what are the possible number of ways to make summ by taking out coins from arr. There is infinite supply of coins
# Example: arr = [1, 2, 3]   summ = 4, OUTPUT=4

def coin_change(arr, n, summ):
    if summ == 0:
        return 1
    elif n == 0:
        return 0
    elif summ<0:
        return 0
        
    include=0
    exclude = coin_change(arr, n-1, summ)
    if arr[n-1]<=summ:
        include = coin_change(arr, n, summ-arr[n-1])
        
    return include+exclude
    
arr = list(map(int, input("Enter the coin array:").split()))    
n = len(arr)
summ = int(input("Enter the sum you want:"))
print(coin_change(arr, n, summ))
