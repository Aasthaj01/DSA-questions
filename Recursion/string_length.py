def string_length(str) : 
    if str == '': 
        return 0
    else : 
        return 1 + string_length(str[1:])  
      
str = input("Enter the string: ")
print (string_length(str)) 
