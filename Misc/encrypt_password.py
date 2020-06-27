# Write a program that encrypts a password given as a string. Given below is the encryption process which is involved:
# Given a string s, let s[i] represents the ith character (0 based indexing is involved), Steps involved are:
# if s[i] is the lowercaseand next letter is uppercase, swap them and add a "*" after them, and move to i+2
#if s[i] is a number, replace it with a 0, place the original number at the start, and move to i+1
# else move to i+1
#stop if i is more then or equal to string length, otherwise, go to step 1
# EXAMPLE:  aAst3h4aj =   43Aa*st0h0aj


# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#-------------------------------------------------------------------------------------------------

def encryptPassword(s):
    
    listt = []
    for i in range(0, len(s)):
        
        if i<(len(s)-1) and s[i].islower() and s[i+1].isupper():
            listt.append(s[i+1])
            listt.append(s[i])
            listt.append("*")
        
        elif s[i].isnumeric():
            listt.insert(0, s[i])
            listt.append("0")
            
        else:
            if i>0 and s[i-1].islower() and s[i].isupper():
                continue
            listt.append(s[i])
        
    for i in range(0, len(listt)):
        print(listt[i], end="")




s = input()

encryptPassword(s)


