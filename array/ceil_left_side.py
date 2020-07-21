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

def ceil_nlogn(arr, n):
  
    s = set() 
    for i in range(0, n):  
        it = [x for x in s if x >= arr[i]]  
        if len(it) == 0:  
            print("-1", end = " ")  
        else:                  
            print(min(it), end = " ")          
        s.add(arr[i])             
            
arr = list(map(int, input("Enter the array elements: ").split()))
n = len(arr)
print("O(n**2) solution is:")
ceil_left_side(arr, n)
print("\n O(nlogn) solution is:")
ceil_nlogn(arr, n)
    
