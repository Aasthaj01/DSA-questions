#Segregating 0s and 1s in an array

# Method 1:
def segregate0and1(arr, n) : 
      
    # Counts the no of zeros in arr 
    count = 0
    for i in range(0, n) : 
        if (arr[i] == 0) : 
            count = count + 1
    # Loop fills the arr with 0 until count 
    for i in range(0, count) : 
        arr[i] = 0
    # Loop fills remaining arr space with 1 
    for i in range(count, n) : 
        arr[i] = 1
       
def print_arr(arr , n) : 
    print( "Array after segregation is ",end = "") 
    for i in range(0, n) : 
        print(arr[i] , end = " ") 
        
        
arr = list(map(int, input().split()))
n = len(arr) 
segregate0and1(arr, n) 
print_arr(arr, n) 
#====================================================================================
Method 2: Using inbuilt sort function
def segregate0and1(arr, n) : 
    arr.sort()  
    return arr
       
arr = list(map(int, input().split()))
n = len(arr) 
print(segregate0and1(arr, n)) 

