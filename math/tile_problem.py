# Given a floor of size n x m and tiles of size 1 x m.
# The problem is to count the number of ways to tile the given floor using 1 x m tiles. 
# A tile can either be placed horizontally or vertically.
# Both n and m are positive integers and 2 < = m.


def countWays(n, m): 
    count =[0]*(n+2) 
    for i in range(1, n + 1): 
        if (i > m): 
            count[i] = count[i-1] + count[i-m]
        elif (i < m or i == 1):  
            count[i] = 1
        else: 
            count[i] = 2
            
    return count[n] 
  
  
n = int(input())
m = int(input())
print("Number of ways = ", countWays(n, m))
