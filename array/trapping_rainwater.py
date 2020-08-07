# Trapping Rain Water Problem

# O(n**2) solution
def trappping_water(arr, n):
    res = 0
    for i in range(1, n-1):
        lmax = arr[i]
        for j in range(0, i):
            lmax =max(lmax, arr[j])
        rmax = arr[i]
        for j in range(i+1, n):
            rmax =max(rmax, arr[j]) 
        res = res+(min(lmax, rmax) - arr[i])
        
    return res
    
# O(n) solution    
def trapping_efficient_sol(arr, n):
    res = 0
    lmax = [0]*n
    rmax = [0]*n
    
    lmax[0] = arr[0]
    for i in range(1, n):
        lmax[i]  = max(lmax[i-1], arr[i])
        
    rmax[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        rmax[i] = max(rmax[i+1], arr[i])
        
    for i in range(0, n):    
        res += min(lmax[i], rmax[i]) - arr[i] 
  
    return res 
    
    
arr= list(map(int, input("Enter the heights:").split()))
n = len(arr)
print(trappping_water(arr, n))
print(trapping_efficient_sol(arr, n))

