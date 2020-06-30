# Program finds the longest common subsequence out of the two input strings

def long_sub_print(s1, s2, m, n, T):
    
    
    if m==0 or n==0:
        return str()
        
    elif s1[m-1]==s2[n-1]:
        return long_sub_print(s1, s2, m-1, n-1, T)+ s1[m-1]
        
    elif T[m-1][n]>T[m][n-1]:
        return long_sub_print(s1, s2, m-1, n, T)
        
    else:
        return long_sub_print(s1, s2, m, n-1, T)
        
def longest_sub(s1, s2, m, n, ):
    
    
    if m==0 or n==0:
        return 0
        
    elif s1[m-1]==s2[n-1]:
        return 1+longest_sub(s1, s2, m-1, n-1)
        
    else:
        return max(longest_sub(s1, s2, m, n-1), longest_sub(s1, s2, m-1, n))        
        
s1 = str(input("Input string 1: "))
m = len(s1)

s2 = str(input("Input string 2: "))
n = len(s2)

T = [[0 for i in range(n+1)] for j in range(m+1)]
print(longest_sub(s1, s2, m, n))
print(long_sub_print(s1, s2, m, n, T))
