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
