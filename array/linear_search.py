# searches for the element in input array and returns its position if found

def element_search(arr, n, key):
    for i in range(n):
        if arr[i]==key:
            return i+1
    return -1
        
arr = list(map(int, input("Enter the array elements:").split())) 
n = len(arr)
key = int(input("Enter the element you want to search in the array:"))
index = element_search(arr, n, key)
if index != -1: 
    print ("element found at position: " + str(index))  
else: 
    print ("element not found") 
      
