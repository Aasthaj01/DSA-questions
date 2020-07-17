# Let array be a. Running sum is a[0], a[0]+a[1], a[0]+a[1]+a[2]..........

arr = list(map(int, input("Enter the numbers in array:").split()))   
s = 0
listt = []
for i in range(len(arr)):
    s = s+arr[i]
    listt.append(s)
print(listt)    
    
