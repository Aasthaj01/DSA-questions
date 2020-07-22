# lower bound in c++ set uses red black tree internally
# in python set are unordered 

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

print("O(nlogn) solution is:")
ceil_nlogn(arr, n)
