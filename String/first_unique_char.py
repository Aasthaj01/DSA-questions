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
#=========================================================================
# first unique character in string is one which occured only once in the string

def check_left_non_repeating(str1):
    try:
        return str1.index([x for x in list(dict.fromkeys(list(str1))) if str1.count(x) == 1][0])
    except:
        return -1
                
str1 = str(input())                
print(check_left_non_repeating(str1))
