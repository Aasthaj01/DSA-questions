# first unique character in string is one which occured only once in the string

from collections import Counter

def check_left_non_repeating(str1):
    ans = Counter(str1)
    if len(str1) == 0:
        return -1
    for i, c in enumerate(str1):
        if ans[c] == 1:
            return i
    return -1
                
str1 = str(input())                
print(check_left_non_repeating(str1))
