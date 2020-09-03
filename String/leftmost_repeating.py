# leftmost repeating character
#==========================================================
# Naive solution

def check_left_repeating(string):
    n = len(string)
    for i in range(n):
        for j in range(i+1, n):
            if string[i] == string[j]:
                return i, string[i]
                
                
string = str(input())                
print(check_left_repeating(string))
