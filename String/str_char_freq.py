# printing the frequency of characters in a string

def freq_str(s):
    n = len(s)
    count = [0]*26
    for i in range(n):
        count[ord(s[i]) - ord('a')]+=1
    for i in range(26):
        if count[i]>0:
            print(count[i])
    
s = str(input())
freq_str(s)

#================================================
from collections import Counter
s = str(input())
print(Counter(s))

#=================================================
s = str(input())
ans = {}
for keys in s:
    ans[keys] = ans.get(keys,0)+1
    
print(ans)    
    
