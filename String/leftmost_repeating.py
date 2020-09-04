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

#=======================================================
# leftmost repeating character
import sys

def check_left_repeating(string):
    arr = [0]*NO_OF_CHARS
    for i in range(NO_OF_CHARS): 
        arr[i] = -1
  
    res = sys.maxsize 
    for i in range(len(string)): 
        if (arr[ord(string[i])] == -1): 
            arr[ord(string[i])] = i 
        else: 
            res = min(res, arr[ord(string[i])]) 
  
    if res == sys.maxsize: 
        return -1
    else: 
        return res 
  
  
NO_OF_CHARS = 256
string = str(input())     
index = check_left_repeating(string) 
if (index == -1): 
    print("Either all characters are distinct or string is empty") 
else: 
    print("First Repeating character is",string[index]) 
                
                
               

