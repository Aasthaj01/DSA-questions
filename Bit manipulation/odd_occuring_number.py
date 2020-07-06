# Find the number occuring odd number of times in the array

#  METHOD 1 - Naive solution -O(n^2)
def odd_occuring(arr, n):
    for i in range(0, n):
        count = 0
        for j in range(0, n):
            if arr[j]==arr[i]:
                count+=1
                
        if (count%2)!=0:
            return arr[i]
            
            
arr = list(map(int, input("Enter the numbers for array:").split()))
n = len(arr)
print("Number in the list occuring odd number of times is:", odd(arr, n))

#---------------------------------------------------------------------------------------------------------------
# METHOD 2 - using XOR - O(n)

def odd(arr, n):
    result = 0
    for i in range(0, n):
        result = result^arr[i]
    return result        
    
    
arr = list(map(int, input("Enter the numbers for array:").split()))
n = len(arr)

print("Number in the list occuring odd number of times is:", odd(arr, n))
