# sum of digits of a number

def sum_of_digits(number):
    if number == 0:
        return 0
    else:
        return(number % 10 + sum_of_digits(int(number/10))) 
    
    
number = int(input("Enter the number:"))
print(sum_of_digits(number))
