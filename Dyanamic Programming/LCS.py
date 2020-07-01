
# Memorization or top down approach to find longest common subsequence
    
def longest_sub(s1, s2, m, n):
    
    
    if (memo[m-1][n-1]!=-1):
        return memo[m-1][n-1]
    
    if m==0 or n==0:
        return 0
        
    
    if s1[m-1]==s2[n-1]:
        memo[m-1][n-1] = 1+longest_sub(s1, s2, m-1, n-1)
        return memo[m-1][n-1]
    
    else:
        memo[m-1][n-1] =  max(longest_sub(s1, s2, m, n-1), longest_sub(s1, s2, m-1, n))        
        return memo[m-1][n-1] 
    
    
s1 = str(input("Input string 1: "))
m = len(s1)

s2 = str(input("Input string 2: "))
n = len(s2)
memo = [[-1 for i in range(m+1)]for j in range(n+1)]


print(longest_sub(s1, s2, m, n))
#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Bottom up approach or tabulation method

def lcs(s1, s2, m, n):
    
    dp = [[-1]*(n+1)]*(m+1)
    
    for i in range(0, m+1):
        dp[i][0] = 0
        for j in range(0, n+1):
            dp[0][j] = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            
           
            if s1[i-1]==s2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
                # return 1+lcs(s1, s2, m-1, n-1)
            else:
                
                dp[i][j] =  max(dp[i][j-1], dp[i-1][j])
    return dp[m][n]    
        
s1 = str(input())
m = len(s1)
s2 = str(input())
n = len(s2)
print(lcs(s1, s2, m, n))





