# Ceiling on left side 
#  An array is given, for every element of the array find the ceiling on left side. If not found, print -1.
#  Example: 2, 8, 30, 15, 25, 12 ==> -1, -1, -1, 30, 30, 15


import sys
def ceil_left_side(arr, n):
    print(-1, end = " ")
    for i in range(1, n):
        diff = sys.maxsize
        for j in range(0, i):
            if arr[j]>=arr[i]:
                diff = min(diff, arr[j]-arr[i])
        if diff == sys.maxsize:
            print(-1, end = " ")
        else:
            print(arr[i]+diff, end = " ")

arr = list(map(int, input("Enter the array elements: ").split()))
n = len(arr)
ceil_left_side(arr, n)
    
