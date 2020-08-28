def longest_palindrome(s1, s2, m, n):
    dp = [[-1]*(n+1)]*(m+1)
    
    for i in range(0, m+1):
        dp[i][0] = 0
        for j in range(0, n+1):
            dp[0][j] = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            
           
            if s1[i-1]==s2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
              
            else:
                
                dp[i][j] =  max(dp[i][j-1], dp[i-1][j])
    return dp[m][n]  
        

s1 = str(input())
m = len(s1)
s2 = "".join(s1[::-1])
print(longest_palindrome(s1, s2, m, m))
