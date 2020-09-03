# checking if 2 strings are anagram or not

s1 = str(input())
s2 = str(input())
ans = {}
res  ={}
for keys in s1:
    ans[keys] = ans.get(keys,0)+1
for keys in s2:
    res[keys] = res.get(keys,0)+1    
    
if ans == res:
    print("Same")
else:
    print("Not same")
    
