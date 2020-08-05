# Minium of Sliding Window Maximum 
# Given an array and an integer K, find the maximum for each and every contiguous subarray of size k. Then find minimum of the maximum array

def printMax(arr, n, k): 
    listt = []
    max = 0
    
    for i in range(n - k + 1):
        
        max = arr[i] 
        for j in range(1, k): 
            if arr[i + j] > max: 
                max = arr[i + j]
            
        listt.append(max)        
    return listt        
  

arr = list(map(int, input("Enter the array numbers:").split())) 
n = len(arr) 
k = int(input("Enter the window size:"))
ans = printMax(arr, n, k)
print(ans)
print(min(ans))
