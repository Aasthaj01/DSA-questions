# This program returns the length of longest increasing subsequence such that all elements of the subsequence are sorted in increasing order.

# nlogn implementation of longest increasing subsequence
def bin_search(listt, l, r, x):
    while (r>l):
        m = l+(r-l)//2
        if listt[m]>=x:
            r = m
        else:
            l = m+1
            
    return r
    
    
def lis(n, arr):
    listt = [0]*n
    length = 1
    listt[0] = arr[0]
    for i in range(1, n):
        if arr[i]>listt[length-1]:
            listt[length] = arr[i]
            length = length+1
        else:
            c = bin_search(listt, 0, length-1, arr[i])
            listt[c] = arr[i]
    return length
        
n = int(input("Enter the length of array:")) 
arr = list(map(int, input().split()))
print(lis(n, arr))
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
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
