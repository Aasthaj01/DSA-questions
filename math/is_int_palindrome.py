def isPalindrome(A):
        if str(A)==str(A)[::-1]:
            return True
        else:
            return False
            
A =int(input("enter the number to be checked:"))
print(isPalindrome(A))


    
    
    

