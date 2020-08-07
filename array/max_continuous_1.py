# max consecutive 1s
# Given binary array, find count of maximum number of consecutive 1’s present in the array.
#Examples :
#Input  : arr[] = {1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1}
#Output : 4


def max_cons_1(arr, n):
    flag = 1
    count = 0
    res = 0
    for i in range(0, n):
        if arr[i] == flag:
            count = count+1
            res = max(res, count)
            
        if arr[i] > flag:
            count = 0
    return res            
           
arr= list(map(int, input("Enter the numbers:").split()))
n = len(arr)
print(max_cons_1(arr, n))
