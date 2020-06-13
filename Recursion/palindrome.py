def str_palindrome(string):
    if len(string) < 1: 
        return True
    else:
        if s[0] == s[-1]: 
            return str_palindrome(s[1:-1]) 
        else: 
            return False
            
            
string = str(input("Enter string:"))
if(str_palindrome(string)==True): 
    print("Given String is a palindrome!")
else:
    print("Given String isn't a palindrome!")
