# optimal strategy for is game is when you pick first.
# you can either choose 1st or last element and then second player get to choose from remaining array.
# You need to win the game

def optimal_strategy(arr, n):
    sume, sumo = 0, 0
    for i in range(1, n, 2):
        sume+= arr[i]
    for i in range(0, n, 2):
        sumo+= arr[i] 
    if sume>sumo:
        return "pick even"
    elif sume<sumo:
        return "pick odd"
    elif sume == sumo:
        return "tie"
    # return max(sume, sumo)    

arr = list(map(int, input().split()))
n = len(arr)
print(optimal_strategy(arr, n))
