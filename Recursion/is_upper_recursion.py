# to find the first occuring upper case in the input string

# --------Recursion-------
def recursive_uppercase(string, i):
    if string[i].isupper():
        return string[i]
    elif (string[i] == '\0') :
        return 0
    else:
        return recursive_uppercase(string, i+1)
        
            
string = str(input("Enter the string which you want to check: "))
print("Does the string contains any upper case letter? ", recursive_uppercase(string, 0))
