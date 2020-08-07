# leader of an array isone in which no element is greater than right of it
# example = 1, 10, 5, 6, 2 ==> 10 is leader

# naive solution
def find_leaders(arr, n):
    
    for i in range(0, n):
        flag = False
        for j in range(i+1, n):
            if arr[i]<=arr[j]:
                flag = True
                break
        if flag == False:
            print(arr[i], end =" ")

#=============================================================
# O(N) solution
def leader_arr(arr, n):
    
    max_from_right = arr[n-1]    
    print(max_from_right, end = " ")    
    for i in range( n-2, -1, -1):         
        if max_from_right <= arr[i]:         
            print(arr[i], end = " ")
            max_from_right = arr[i] 
          

arr = list(map(int, input("Enter the array elements:").split()))
n = len(arr)
find_leaders(arr, n)
leader_arr(arr, n)
