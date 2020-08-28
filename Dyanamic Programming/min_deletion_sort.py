def bin_search(listt, l, r, x):
    while (r>l):
        m = l+(r-l)//2
        if listt[m]>=x:
            r = m
        else:
            l = m+1
            
    return r
    
    
def lis(n, arr):
    listt = [0]*n
    length = 1
    listt[0] = arr[0]
    for i in range(1, n):
        if arr[i]>listt[length-1]:
            listt[length] = arr[i]
            length = length+1
        else:
            c = bin_search(listt, 0, length-1, arr[i])
            listt[c] = arr[i]
    return length
        

arr = list(map(int, input().split()))
n =len(arr)
print(n - lis(n, arr))
