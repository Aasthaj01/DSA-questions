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
#-------------------------------------------------------------------------------------
#Printing longest palindromic subsequence

def longest_palindrome_subs(s, s2, m, n):
    dp = [[-1]*(n+1)]*(m+1)
    
    for i in range(0, m+1):
        dp[i][0] = 0
        for j in range(0, n+1):
            dp[0][j] = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            
           
            if s[i-1]==s2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
              
            else:
                
                dp[i][j] =  max(dp[i][j-1], dp[i-1][j])
     
    index = dp[m][n]  
  
    lcs = [""] * (index + 1) 
   
    i, j= m, n  
      
    while (i > 0 and j > 0) :  
        if (s[i - 1] == s2[j - 1]) : 
          
             
            lcs[index - 1] = s[i - 1] 
            i -= 1
            j -= 1
  
              
            index -= 1
        
        elif(dp[i - 1][j] > dp[i][j - 1]) : 
            i -= 1
              
        else : 
            j -= 1
      
    ans = "" 
      
    for x in range(len(lcs)) : 
        ans += lcs[x] 
      
    return ans 


s = str(input())    
m = len(s)
n = len(s)
s2 = "".join(s[::-1])
print(longest_palindrome_subs(s, s2, m, m))    
    
