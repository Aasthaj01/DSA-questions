#Given 2 strings of length m and n respectively, find min ways to edit 1 string and make it similar to other if operations are insert, delete, replace

def editDistance(s1, s2, m, n):
    if m==0:
        return n
    if n==0:
        return m
    if s1[m-1] == s2[n-1]:
        return editDistance(s1, s2, m-1, n-1)
    else:
        result = 1+min(editDistance(s1, s2, m-1, n), editDistance(s1, s2, m, n-1), editDistance(s1, s2, m-1, n-1)) 
    return result    
    
s1 = str(input())
m = len(s1)
s2 = str(input())
n = len(s2)
print(editDistance(s1, s2, m, n))
