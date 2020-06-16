#generate and print all possible combinations of r elements in array
# Here, data is temporary array, index is for data array and i for main array

def print_combinations(arr, n, r):
    data = [0] * r 
    current_combinations(arr, n, r, 0, data, 0) 
  
def current_combinations(arr, n, r, index, data, i):
    if (index == r): 
        for j in range(r): 
            print(data[j], end = " ") 
        print() 
        return
    if (i >= n): 
        return
    data[index] = arr[i] 
    current_combinations(arr, n, r, index + 1,  
                    data, i + 1) 
    current_combinations(arr, n, r, index,  
                    data, i + 1) 



arr = list(map(int, input("Enter the array elements: ").split()))
n = len(arr)
r = int(input("Enter the length of subarray you want: "))
print_combinations(arr, n ,r)
