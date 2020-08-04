# Rotating the array by d elements clockwise

def print_array(arr, n):
    for i in range(n):
        print(arr[i], end = " ")
# rotation of array of length n by d elements


def array_rotation(arr, n, d):
    for i in range(0, d):
        temp = arr[0]
        for j in range(0, n-1): 
          arr[j] = arr[j+1] 
        arr[n-1] = temp 
    print_array(arr, n)    
    
    
no_of_testCases = int(input("Enter the no of test cases you want:"))
for i in range(no_of_testCases):
    listt = list(map(int, input("Enter size of array and size of rotation:").split()))
    n = listt[0]
    d = listt[1]
    
    arr = list(map(int, input("Enter array elements:").split()))
    print("array before rotation is")
    for i in range(n):
        print(arr[i], end = " ")
    print()
    print("The array after rotation is:")
    array_rotation(arr, n, d)
    print()
#======================================================================
#O(k)

def rotate_right(nums, k):
    for i in range(k):
        nums.insert(0, nums.pop(len(nums) - 1))
    return nums    
nums = list(map(int, input().split()))
n = len(nums)
k = int(input())
ans = rotate_right(nums, k)
print(nums)

     

