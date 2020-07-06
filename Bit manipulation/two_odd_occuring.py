# Find out 2 odd occuring elements from the input list

def two_odd(listt, n):
    result = 0
    res1 = 0
    res2 = 0
    for i in range(n):
        result = listt[i]^result
        sn = result & (~(result-1))
    for i in range(n):
        if sn&listt[i]!=0:
            res1 = res1^listt[i]
        else:
            res2 = res2^listt[i]
    return (res1, res2) 
    
listt = list(map(int, input().split()))
# arr = []
n = len(listt)
print(two_odd(listt, n))
