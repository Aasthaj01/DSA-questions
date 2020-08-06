# finds element in array by using binary search
# indexing starts form 0

def binarySearch(arr, low, high, key): 
  
    if (high < low): 
        return -1
    
    mid = (low + high)//2
  
    if (key == arr[int(mid)]): 
        return mid 
  
    if (key > arr[int(mid)]): 
        return binarySearch(arr, 
           (mid + 1), high, key) 
  
    return (binarySearch(arr, low, 
           (mid -1), key)) 
  

arr = list(map(int, input("Enter the nmbers in the array:").split()))
n = len(arr) 
key = int(input("Enter the number you want to search:"))
print("Index:", int(binarySearch(arr, 0, n, key) )) 
