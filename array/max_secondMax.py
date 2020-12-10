# max and second max element of arr.
# Given an array arr[] of size n of positive integers which may have duplicates.
The task is to find the maximum and second maximum from the array, and both of them should be distinct, so If no second max exists, then the second max will be -1.

def largestAndSecondLargest(n, arr):
    max1 = -1
    max2 = -1
    arr=set(arr)
    if len(arr)<2:
        max1=max(arr)
    else:
        max1=max(arr)
        arr.remove(max1)
        max2=max(arr)
    return [max1, max2]
                
            
#Example: arr = [1000, 1000, 20, 10, 500]  
arr = list(map(int, input()).split()))
n = len(arr)
ans = largestAndSecondLargest(n, arr)
for i in range(len(ans)):
    print(ans[i], end = " ")
#====================================================================================================================

arr = [7, 2, 4, 10, 18]
n = len(arr)

maxnum = max(arr[0], arr[1])
minnum = min(arr[0], arr[1])
for i in range(2, n):
    if arr[i]>=maxnum:
        minnum = maxnum
        maxnum = arr[i]
    elif arr[i]>minnum or maxnum!= arr[i]:
        minnum = arr[i]
print(maxnum, minnum)

#=========================================================================================================================
arr = [7, 2, 4, 10, 18, 18]
listt = set(arr)
print(max(listt))
listt.remove(max(listt))
print(max(listt))
