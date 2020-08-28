# optimal strategy for is game is when you pick first.
# you can either choose 1st or last element and then second player get to choose from remaining array.
# You need to maximize the output
#===================================================================================================================
#recursive sol
def optimal_strategy(arr, i, j, summ):
    if i+1 == j:
        return max(arr[i], arr[j])
    return max((summ-optimal_strategy(arr, i+1, j, summ-arr[i])), (summ -optimal_strategy(arr, i, j-1, summ-arr[j])))

arr = list(map(int, input().split()))
n = len(arr)
summ = sum(arr)
print(optimal_strategy(arr, 0, n-1, summ))
#=====================================================================================================================
# recursive solution 2
# you can choose ith element or jth, we'll take max of arr[i]+min(optimal_strategy(arr, i+2, j), optimal_strategy(arr, i+1, j-1)) and similarly when we select last element
def optimal_strategy(arr, i, j):
    if i+1 == j:
        return max(arr[i], arr[j])
    return max(arr[i]+min(optimal_strategy(arr, i+2, j), optimal_strategy(arr, i+1, j-1))
               arr[i]+min(optimal_strategy(arr, i, j-2), optimal_strategy(arr, i+1, j-1)))

arr = list(map(int, input().split()))
n = len(arr)
print(optimal_strategy(arr, 0, n-1, summ))
