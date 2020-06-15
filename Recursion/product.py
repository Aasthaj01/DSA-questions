# product of 2 numbers using recursion

def product(num1, num2):
    if num1<num2:
        return(product(num2, num1))
    elif num1>0 and num2>0: 
        return (num1 + product(num1, num2-1))
    else:
        return 0
    

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
print(product(num1, num2))
