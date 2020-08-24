# if string s is given, find all the permutations of the string which is len(s)!

# METHOD 1
from itertools import permutations

def find_permutations(s1):
    permutation = [''.join(p)for p in permutations(s1)]
    return permutation

def fact(n):
    result  = 0
    if n==0:
        return 1
    else:
        return n*fact(n-1)

s1 = str(input())
n = len(s1)
total_perm = fact(n)
print("The total permutations will be:", total_perm)
print(find_permutations(s1))
#========================================================================================================================


def find_permutations(string, i, n, res):
    
    if i == n:
        res.append(''.join(string))
    else: 
        for j in range(i, n):
            string[i], string[j] = string[j], string[i]  
            find_permutations(string, i+1, n, res)
            string[i], string[j] = string[j], string[i]
    return res        
        
                
s1 = str(input())
res = []
n = len(s1)
string = list(s1)
print(find_permutations(string, 0, n, res))

