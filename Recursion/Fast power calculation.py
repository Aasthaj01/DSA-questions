def fastPower(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return fastPower(a * a, b/2)
    else:
        return a * fastPower(a, b-1)
        
num = int(input('Enter a number'))
pow = int(input('Enter power'))
print(fastPower(num, pow))
