# recursive insertion sort

def insertionSort(arr,n):
   # base case
   if n<=1:
      return
   # Sort
   insertionSort(arr,n-1)
   last = arr[n-1]
   j = n-2
  
   while (j>=0 and arr[j]>last):
      arr[j+1] = arr[j]
      j = j-1
   arr[j+1]=last
   
   
   
n = int(input("How many elements you want in the array?"))
arr = list(map(int, input("Enter the elements:").split()))
insertionSort(arr, n)
print("Sorted array is:")
for i in range(n):
   print(arr[i],end=" ")

#==================================================================
# Method 2
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i-1
        while j>=0 and arr[j]>arr[j+1]:
            arr[j+1], arr[j] = arr[j], arr[j+1] 
            j-=1
            # break
    return arr
    
arr = list(map(int, input().split()))
print(insertion_sort(arr))
            

