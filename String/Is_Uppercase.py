def str_upper(string):
    for i in range(0, len(string)):
        if string[i].istitle():
            return string[i]
    return 0

string = str(input("Enter the string which you want to check: "))

print("Does the string contains any upper case letter? ", str_upper(string))
