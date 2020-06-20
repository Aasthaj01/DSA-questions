#You are given length of n sides, you need to answer whether it is possible to make n sided convex polygon with it.

#----------------------------------------------------------------------------------
def prob_solve(listt, N):
    sum = 0
    maxS = 0
    for i in range(0, N):
        sum += listt[i] 
        maxS = max(listt[i], maxS) 
  
    if ((sum-maxS)>maxS):
        print("YES")
    else:    
        print("NO")    

t = int(input())
for i in range(0, t):
    N = int(input())
    listt = list(map(int, input().split()))
    prob_solve(listt, N)
