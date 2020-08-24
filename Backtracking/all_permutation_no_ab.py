# Given a string, generate all permutations of it that do not contain ‘B’ after ‘A’, i.e., the string should not contain “AB” as a substring.

def find_permutations(string, i, n, res):
    
    if i == n:
        res.append(''.join(string))
        
    else: 
        for j in range(i, n):
            if issafe(string, i, n, j):
               
                string[i], string[j] = string[j], string[i]  
                find_permutations(string, i+1, n, res)
                string[i], string[j] = string[j], string[i]
    return res        


def  issafe(string, i, n, j):
    if j!=0 and (string[j-1] == 'A' or string[j-1] == 'a') and (string[i] == 'B' or string[i] == 'b'):
        return False
    if (n == j+1) and (string[i] == 'a' or string[i] == 'A') and (string[j] == 'b' or string[j] == 'B'): 
        return False
    return True    
                
s1 = str(input())
n = len(s1)
res = []
string = list(s1)
print(find_permutations(string, 0, n, res))
#=============================================================================================
def permute(st, l, r, res): 
    listt = []
    if (l == r): 
        res.append(''.join(st))    
    for i in range(l, r + 1): 
        st[l], st[i] = st[i], st[l] 
        permute(st, l + 1, r, res) 
        st[l], st[i] = st[i], st[l]
    for item in res:
        if 'ab' not in item:
            listt.append(item)
    return listt       
        
          
st = str(input())
res = [] 
print(permute(list(st), 0, len(st) - 1, res)) 

