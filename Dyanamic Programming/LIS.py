# This program returns the length of longest increasing subsequence such that all elements of the subsequence are sorted in increasing order.


def lis(n, arr):
    # listt is the list containing subsequence
    listt = [1]*n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i]>arr[j] and listt[i]<listt[j]+1:
                listt[i] = listt[j]+1
    maximum = 0
    for i in range(0, n):
        maximum = max(maximum, listt[i])
    return maximum
    
    
n = int(input("Enter the length of array:"))
arr = list(map(int, input("Enter the array elements:").split()))
print("The longest increasing subsequence is:", lis(n, arr))
