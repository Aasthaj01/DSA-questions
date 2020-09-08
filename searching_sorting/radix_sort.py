def countingSort(arr, exp1): 
    n = len(arr)  
    output = [0] * (n)
    count = [0] * (100) 
   
    for i in range(0, n): 
        index = (arr[i]/exp1) 
        count[int((index)%10)] += 1
   
    for i in range(1,10): 
        count[i] += count[i-1] 

    i = n-1
    while i>=0: 
        index = (arr[i]/exp1) 
        output[ count[ int((index)%10) ] - 1] = arr[i] 
        count[int((index)%10)] -= 1
        i -= 1
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
    return arr    

def radix_sort(arr):
    max1 = max(arr)
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1/exp > 0:
        countingSort(arr,exp)
        exp *= 10

arr = list(map(int, input().split()))
radix_sort(arr)
for i in range(len(arr)):
    print(arr[i], end =" ")
