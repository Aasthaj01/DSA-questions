# The program will return true in both the cases i.e reversed sort or increasing sort

def is_sorted(arr, n):
    temp = [0]*n
    for i in range(n):
        temp[i] = arr[i]
    temp.sort()
    rev = temp
    rev.sort(reverse=True)    
    for i in range(n):
        if arr[i] == temp[i]:
            return True
        elif arr[i] ==  rev[i]:
            return True  
        else:
            return False 
            
arr = list(map(int, input().split()))    
n = len(arr)
print(is_sorted(arr, n))
