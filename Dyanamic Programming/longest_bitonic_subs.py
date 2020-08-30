# longest bitonic sequence is once in which the elements are firstincfreaing and then decreasing.
# sorted array is also considered as bitonic
    
def lis(arr, n):
    lis = [1 for i in range(n+1)] 
    for i in range(1 , n): 
        for j in range(0 , i): 
            if ((arr[i] > arr[j]) and (lis[i] < lis[j] +1)): 
                lis[i] = lis[j] + 1
    
    return lis

def lds(arr, n): 
  
    lds = [0] * n
    for i in range(n): 
        lds[i] = 1
    for i in range(1, n): 
        for j in range(i): 
            if (arr[i] < arr[j] and 
                lds[i] < lds[j] + 1): 
                lds[i] = lds[j] + 1
    
    return lds

def  is_bitonic(arr, n):
 
    a = lis(arr, n)  
    b = lds(arr, n)
    maximum = a[0] + b[0] - 1
    for i in range(1 , n): 
        maximum = max((a[i] + b[i]-1), maximum)  
    return maximum

    
arr = list(map(int, input().split()))    
n = len(arr)
print(is_bitonic(arr, n))
