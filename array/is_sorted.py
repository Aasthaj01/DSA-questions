# The program will return true in both the cases i.e reversed sort or increasing sort

arr = list(map(int, input().split()))    
n = len(arr)
flag = 0
temp = arr[:] 
temp.sort()
rev = arr
rev.sort(reverse = True)
if (temp == arr) or (rev == arr): 
    flag = 1
else:
    flag = 0
       
       
if (flag): 
    print ("Yes, array is sorted")
else:
    print("Array is not sorted")

