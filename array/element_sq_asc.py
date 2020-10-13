# Given a array of both positive and negative integers ‘arr[]’, sort square of the numbers of the array.

# O(n log n) solution
arr = list(map(int, input().split()))
n = len(arr)
for i in range(n):
	arr.append(arr[i]*arr[i])
del arr[:n]
arr.sort()
print(arr)
#=================================================================================
# O(n) solution
def sortSquares(arr, n): 
    left, right = 0, n - 1
    index = n - 1
    result = [0 for x in arr] 
  
    while index >= 0: 
  
        if abs(arr[left]) >= abs(arr[right]): 
            result[index] = arr[left] * arr[left] 
            left += 1
        else: 
            result[index] = arr[right] * arr[right] 
            right -= 1
        index -= 1
      
    for i in range(n):  
        arr[i] = result[i]
    return arr

    
arr = list(map(int, input().split()))
n = len(arr)
print(sortSquares(arr, n))


