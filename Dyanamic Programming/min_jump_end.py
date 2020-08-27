# min jumps to reach the end
# if there is 0 in array then we return infinite

# RECURSIVE SOLUTION
import sys
def min_jump_end(arr, n):
    maxi = sys.maxsize
    sub_res = 0
    if n == 1:
        return 0
    for i in range(n-1):
        if (i+arr[i])>=n-1:
            sub_res = min_jump_end(arr, i+1)
            if sub_res!=maxi:
                maxi = min(sub_res+1, maxi)
    return maxi 
    
    
arr = list(map(int, input().split()))
n = len(arr)
print(min_jump_end(arr, n))
#=================================================================================================
