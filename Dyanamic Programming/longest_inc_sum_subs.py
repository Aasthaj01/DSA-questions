# longest increasing sum subsequence -- related to lis (O(n^2))
def lsis(arr, n):
    maximum = 0
    dp = [0 for i in range(n)]
    for i in range(n):
        dp[i] = arr[i]
    for i in range(1, n):
        for j in range(i):
            if dp[i]<dp[j]+arr[i] and arr[i]>arr[j]:
                dp[i] = dp[j]+arr[i]
    maximum = max(dp) 
    return maximum           

arr = list(map(int, input().split()))
n = len(arr)
print(lsis(arr, n))
