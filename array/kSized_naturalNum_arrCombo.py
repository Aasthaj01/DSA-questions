# data is temporary array, index is for data array and i for main array
#The program prints increasing sequences of length k from first n natural numbers

def print_combinations(arr, n, k):
    data = [0] * k 
    current_combinations(arr, n, k, 0, data, 0) 
    data.sort()
  
def current_combinations(arr, n, k, index, data, i):
    if (index == k): 
        for j in range(k): 
            data.sort()
            print(data[j], end = " ") 
        print() 
        return
    if (i >= n): 
        return
    data[index] = arr[i] 
    current_combinations(arr, n, k, index + 1,  
                    data, i + 1) 
    current_combinations(arr, n, k, index,  
                    data, i + 1) 



arr = []
n = int(input("Enter the number upto which you want to consider:"))
for i in range(1, n+1):
    arr.append(i)
# print(arr)    
k = int(input("Enter the length of subarray you want: "))
print_combinations(arr, n ,k)
