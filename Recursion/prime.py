# check whether a number is prime or not

def prime(number, i=2):
    if number<=0:
        return False
    else:
        if (number%i == 0):
            return False
        elif((i*i)>number):   
            return True
        else:
            return prime(number, i+1)
        
number = int(input("Enter the number you want to check:"))
print("Is the number prime?", prime(number))
