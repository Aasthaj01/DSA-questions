# recursive bubble sort

def bubble_sort(arr):
    # base case
    if len(arr) == 1:
        return arr
    else:
        for i in range(len(arr)):
            try:
                if arr[i]>arr[i+1]:
                    temp = arr[i]
                    arr[i] = arr[i+1]
                    arr[i+1] = temp
                    bubble_sort(arr)
            except IndexError: 
                pass
        return arr    
            
        
        
arr = list(map(int, input("Enter the elements:").split()))
print("The sorted array is:", bubble_sort(arr))
